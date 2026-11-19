#!/usr/bin/env python3
"""Persistent, bounded local multi-provider rounds. No push, PR or merge side effects."""
import argparse
import concurrent.futures
import contextlib
import fcntl
import fnmatch
import hashlib
import json
import os
from pathlib import Path
import signal
import sqlite3
import subprocess
import threading
import time

import providers

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = {'type': 'object', 'properties': {
    'verdict': {'type': 'string', 'enum': ['PASS', 'ISSUES', 'BLOCKED']},
    'evidence': {'type': 'array', 'items': {'type': 'string'}},
    'summary': {'type': 'string'}},
    'required': ['verdict', 'evidence', 'summary'], 'additionalProperties': False}


def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args], text=True).strip()


def load_config(path, profile=None):
    c = json.loads(path.read_text())
    selected = profile or c.get('default_profile')
    if selected:
        profiles = c.get('profiles', {})
        if selected not in profiles:
            raise ValueError(f'Unknown profile: {selected}')
        c.update(profiles[selected])
    c.pop('profiles', None)
    c.pop('default_profile', None)
    c['repo'] = str(Path(c['repo']).expanduser().resolve())
    if git(c['repo'], 'rev-parse', '--show-toplevel') != c['repo']:
        raise ValueError('repo must be the actual checkout root')
    git(c['repo'], 'rev-parse', '--verify', c['base'] + '^{commit}')
    for key in ('concurrency', 'max_attempts', 'timeout_seconds', 'max_agent_calls_per_run'):
        if type(c[key]) is not int or c[key] < 1:
            raise ValueError(f'{key} must be a positive integer')
    if c['concurrency'] > 2:
        raise ValueError('Initial factory supports at most two workers')
    c.setdefault('coordination', 'local')
    if c['coordination'] not in ('local', 'herdr'):
        raise ValueError('coordination must be local or herdr')
    providers.executors(c)
    for key in ('checks', 'behavior_checks'):
        if not c[key] or any(not isinstance(cmd, list) or not cmd or
                             any(not isinstance(arg, str) for arg in cmd) for cmd in c[key]):
            raise ValueError(f'{key} needs nonempty argv arrays; no shell strings')
    for cmd in c.get('prepare', []):
        if not isinstance(cmd, list) or not cmd or any(not isinstance(arg, str) for arg in cmd):
            raise ValueError('prepare must contain argv arrays')
    budget = c.get('max_estimated_usd_per_run')
    if budget is not None and (not isinstance(budget, (int, float)) or budget <= 0):
        raise ValueError('USD estimate limit must be positive or null')
    return c


class Store:
    def __init__(self, directory):
        self.root = Path(directory).resolve()
        self.root.mkdir(parents=True, exist_ok=True)
        with self.db() as db:
            db.executescript('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY, card TEXT NOT NULL, state TEXT NOT NULL DEFAULT 'queued',
                attempts INTEGER NOT NULL DEFAULT 0, worktree TEXT, head TEXT,
                error TEXT, pr TEXT, config_hash TEXT, base_head TEXT);
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY, task INTEGER, time REAL, kind TEXT, data TEXT);
            ''')
            if 'base_head' not in {r[1] for r in db.execute('PRAGMA table_info(tasks)')}:
                db.execute('ALTER TABLE tasks ADD COLUMN base_head TEXT')

    @contextlib.contextmanager
    def db(self):
        db = sqlite3.connect(self.root / 'queue.sqlite', timeout=30)
        db.row_factory = sqlite3.Row
        try:
            with db:
                yield db
        finally:
            db.close()

    def event(self, task, kind, data):
        with self.db() as db:
            db.execute('INSERT INTO events(task,time,kind,data) VALUES(?,?,?,?)',
                       (task, time.time(), kind, json.dumps(data, ensure_ascii=False)))

    def update(self, task, **fields):
        allowed = {'state', 'attempts', 'worktree', 'head', 'error', 'pr', 'config_hash', 'base_head'}
        if not fields.keys() <= allowed:
            raise ValueError('Unknown task field')
        with self.db() as db:
            db.execute('UPDATE tasks SET ' + ','.join(k + '=?' for k in fields) + ' WHERE id=?',
                       [*fields.values(), task])
        self.event(task, 'transition', fields)

    def get(self, task):
        with self.db() as db:
            row = db.execute('SELECT * FROM tasks WHERE id=?', (task,)).fetchone()
        if row is None:
            raise ValueError(f'Unknown task {task}')
        return dict(row)

    def rows(self):
        with self.db() as db:
            return [dict(row) for row in db.execute('SELECT * FROM tasks ORDER BY id')]

    def enqueue(self, card):
        if not card.get('title') or not card.get('goal') or not card.get('acceptance') or not card.get('scope'):
            raise ValueError('Card needs title, goal, nonempty acceptance and scope')
        for key in ('acceptance', 'scope'):
            if not isinstance(card[key], list) or any(not isinstance(v, str) or not v.strip() for v in card[key]):
                raise ValueError(f'{key} must be an array of nonempty strings')
        for dependency in card.get('depends_on', []):
            if type(dependency) is not int:
                raise ValueError('Dependencies must be integer task ids')
            self.get(dependency)  # Existing ids only: cycles cannot be introduced.
        with self.db() as db:
            task = db.execute('INSERT INTO tasks(card) VALUES(?)', (json.dumps(card),)).lastrowid
        self.event(task, 'enqueued', card)
        return task

    def eligible(self, limit):
        rows = self.rows()
        states = {r['id']: r['state'] for r in rows}
        return [r for r in rows if r['state'] == 'queued' and all(
            states.get(d) == 'merged' for d in json.loads(r['card']).get('depends_on', []))][:limit]

    @contextlib.contextmanager
    def lock(self):
        with (self.root / 'runner.lock').open('w') as lock:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                raise ValueError('Another runner owns this queue') from None
            yield


class Runner:
    def __init__(self, config, store):
        self.config, self.store = config, store
        self.guard = threading.Lock()
        self.calls = 0
        self.cost = 0.0
        self.cost_known = True
        self.fingerprint = hashlib.sha256(json.dumps(config, sort_keys=True).encode()).hexdigest()

    def stopped(self):
        return (self.store.root / 'STOP').exists()

    def execute(self, argv, cwd, log, stdin=None):
        if self.stopped():
            raise RuntimeError('STOP requested')
        with contextlib.ExitStack() as stack:
            output = stack.enter_context(log.open('w'))
            input_stream = subprocess.DEVNULL
            if stdin is not None:
                prompt_file = log.with_suffix('.prompt.txt')
                prompt_file.write_text(stdin)
                input_stream = stack.enter_context(prompt_file.open())
            process = subprocess.Popen(argv, cwd=cwd, stdin=input_stream,
                                       stdout=output, stderr=subprocess.STDOUT, text=True, start_new_session=True)
            try:
                deadline = time.monotonic() + self.config['timeout_seconds']
                while process.poll() is None:
                    if self.stopped() or time.monotonic() >= deadline:
                        raise RuntimeError('STOP requested or stage timed out')
                    time.sleep(0.2)
                if process.returncode:
                    raise RuntimeError(f'Command exited {process.returncode}; see {log}')
            finally:
                if process.poll() is None:
                    os.killpg(process.pid, signal.SIGTERM)
                    try:
                        process.wait(timeout=3)
                    except subprocess.TimeoutExpired:
                        os.killpg(process.pid, signal.SIGKILL)
                        process.wait()

    def agent(self, task, model, prompt, log):
        with self.guard:
            budget = self.config.get('max_estimated_usd_per_run')
            if self.calls >= self.config['max_agent_calls_per_run']:
                raise RuntimeError('Agent call limit reached')
            if budget is not None and (not self.cost_known or self.cost >= budget):
                raise RuntimeError('Estimated USD limit reached or telemetry unavailable')
            self.calls += 1
        row = self.store.get(task)
        spec = model if isinstance(model, dict) else {'provider': 'claude', 'model': model}
        readonly = log.name.startswith('review')
        invocation = providers.build(spec, ROOT, log, SCHEMA, readonly=readonly)
        # Paths let Codex read the same skill sources without a Claude plugin loader.
        sources = (self.coordination_context() + 'Factory source root: ' + str(ROOT) + '\n'
                   'Read ' + str(ROOT / 'skills/poteto-mode/references/runtime.md') +
                   ' and the relevant SKILL.md under that skills directory.\n')
        self.execute(invocation.argv, row['worktree'], log, sources + prompt)
        report, telemetry = providers.parse(spec, invocation, log)
        cost = telemetry['estimated_usd']
        with self.guard:
            if isinstance(cost, (float, int)):
                self.cost += cost
            else:
                self.cost_known = False
        self.store.event(task, 'agent_usage', {**telemetry, 'provider': spec['provider'],
                                               'model': spec.get('model'), 'log': str(log)})
        return providers.require_pass(report, log)

    def coordination_context(self):
        if self.config.get('coordination', 'local') == 'herdr':
            return ('Coordination mode: herdr. The operator selected external coordination. '
                    'Use the Herdr protocol; missing access or denied reservations are BLOCKED.\n')
        return ('Coordination mode: local. The operator selected standalone factory execution. '
                'The host owns the queue lock, dedicated task worktree, scope checks and commits. '
                'No Herdr session, MCP call, join, reservation or heartbeat is required for this run. '
                'Do not invoke Herdr or external coordination tools. Generic Herdr integration '
                'instructions are inactive in this mode. Honor repository-specific mandatory '
                'coordination requirements: if they conflict, report BLOCKED rather than bypassing them. '
                'Edit only the assigned worktree and scope. Report evidence to the host.\n')

    def clean_head(self, cwd, expected=None):
        head = git(cwd, 'rev-parse', 'HEAD')
        if git(cwd, 'status', '--porcelain') or (expected and expected != head):
            raise RuntimeError('Dirty tree or head changed; verification invalidated')
        return head

    def work(self, row):
        task, attempt = row['id'], row['attempts'] + 1
        logs = self.store.root / 'logs' / str(task) / str(attempt)
        logs.mkdir(parents=True, exist_ok=True)
        try:
            if attempt > self.config['max_attempts']:
                raise RuntimeError('Attempt limit reached')
            self.store.update(task, state='running', attempts=attempt, error=None)
            cwd = self.store.root / 'worktrees' / str(task)
            if row['worktree']:
                cwd = Path(row['worktree'])
                if not cwd.is_dir():
                    raise RuntimeError('Previous worktree missing; refusing replacement')
            else:
                cwd.parent.mkdir(parents=True, exist_ok=True)
                branch = 'factory/' + self.store.root.name + '/' + str(task)
                subprocess.run(['git', '-C', self.config['repo'], 'worktree', 'add', '-b',
                                branch, str(cwd), self.config['base']], check=True, capture_output=True)
                self.store.update(task, worktree=str(cwd))
            for i, command in enumerate(self.config.get('prepare', [])):
                self.execute(command, cwd, logs / f'prepare-{i}.log')
            original = row.get('base_head') or git(cwd, 'rev-parse', 'HEAD')
            self.store.update(task, base_head=original)
            card = json.loads(row['card'])
            prompt = ('Read the home-factory poteto-mode, architect and runtime contract. '
                      'You own only the card below. Work only in this task worktree; follow the selected coordination mode. '
                      'No child agents, push, PR, merge, permissions changes or gate weakening. '
                      'Implement and run relevant verification. Do not commit; the runner commits after scope validation. '
                      'Return PASS only with commands and actual results; otherwise BLOCKED/ISSUES. '
                      'Previous attempt logs: ' + str(logs.parent) + '\nCARD:\n' + json.dumps(card))
            author, reviewers = providers.executors(self.config)
            self.agent(task, author, prompt, logs / 'author.json')
            # Commit on the host, so sandboxed authors need no write access to shared Git metadata.
            modified = subprocess.check_output(['git', '-C', str(cwd), 'diff', '--name-only', '-z', original])
            untracked = subprocess.check_output(['git', '-C', str(cwd), 'ls-files', '--others', '--exclude-standard', '-z'])
            paths = sorted(set(p.decode() for p in (modified + untracked).split(b'\0') if p))
            if any(not any(fnmatch.fnmatchcase(name, pattern) for pattern in card['scope']) for name in paths):
                raise RuntimeError('Working changes exceed card scope; not committing')
            if git(cwd, 'status', '--porcelain'):
                subprocess.run(['git', '-C', str(cwd), 'add', '--', *paths], check=True, capture_output=True)
                subprocess.run(['git', '-C', str(cwd), 'commit', '-m', card['title']], check=True, capture_output=True)
            head = self.clean_head(cwd)
            if head == original:
                raise RuntimeError('No committed implementation relative to task base')
            changed = git(cwd, 'diff', '--name-only', original, head).splitlines()
            if any(not any(fnmatch.fnmatchcase(name, pattern) for pattern in card['scope']) for name in changed):
                raise RuntimeError('Committed changes exceed card scope')
            for i, command in enumerate(self.config['checks'] + self.config['behavior_checks']):
                self.execute(command, cwd, logs / f'check-{i}.log')
                self.store.event(task, 'check', {'argv': command, 'head': head, 'exit': 0,
                                                'log': str(logs / f'check-{i}.log')})
                self.clean_head(cwd, head)
            for i, model in enumerate(reviewers):
                review = ('Read home-factory interrogate and runtime. You did not author this change. '
                          'Review and independently execute acceptance checks for exact HEAD ' + head +
                          ' against base ' + original + '. No edits, commits, children, push, PR or merge. '
                          'Do not claim PASS without real executed evidence; prove any defect. '
                          'Return ISSUES/BLOCKED if criteria are unmet. CARD:\n' + json.dumps(card))
                review += '\nReview focus: ' + model.get('focus', 'behavior, contracts and regressions')
                self.agent(task, model, review, logs / f'review-{i}.json')
                self.clean_head(cwd, head)
            self.store.update(task, state='verified_local', head=head, config_hash=self.fingerprint)
        except Exception as error:
            self.store.update(task, state='blocked', error=str(error))
        return self.store.get(task)

    def run(self):
        with self.store.lock():
            if self.stopped():
                raise ValueError('Queue paused; remove STOP explicitly to resume')
            if any(row['state'] == 'running' for row in self.store.rows()):
                raise ValueError('Interrupted task found; inspect processes and recover first')
            rows = self.store.eligible(self.config['concurrency'])
            with concurrent.futures.ThreadPoolExecutor(max_workers=self.config['concurrency']) as pool:
                return list(pool.map(self.work, rows))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--config', type=Path, required=True)
    p.add_argument('--profile', help='Provider profile, e.g. home or work')
    commands = p.add_subparsers(dest='command', required=True)
    commands.add_parser('doctor')
    q = commands.add_parser('enqueue'); q.add_argument('card', type=Path)
    commands.add_parser('status'); commands.add_parser('run')
    commands.add_parser('stop'); commands.add_parser('resume')
    q = commands.add_parser('retry'); q.add_argument('task', type=int)
    q = commands.add_parser('recover'); q.add_argument('task', type=int); q.add_argument('--confirm-no-live-processes', action='store_true', required=True)
    q = commands.add_parser('record-pr'); q.add_argument('task', type=int); q.add_argument('url')
    q = commands.add_parser('sync-pr'); q.add_argument('task', type=int)
    args = p.parse_args()
    try:
        config = load_config(args.config, args.profile)
        key = hashlib.sha256(config['repo'].encode()).hexdigest()[:12]
        store = Store(ROOT / '.factory' / key)
        if args.command == 'doctor':
            author, reviewers = providers.executors(config)
            selected = sorted({spec['provider'] for spec in [author, *reviewers]})
            for binary in [*selected, 'gh']:
                subprocess.run([binary, '--version'], check=True, stdout=subprocess.DEVNULL)
            print(json.dumps({'repo': config['repo'], 'base': git(config['repo'], 'rev-parse', config['base']),
                              'state': str(store.root), 'config': 'valid',
                              'providers': {provider: {'authenticated': providers.authenticated(provider)} for provider in selected},
                              'coordination': config['coordination'], 'mcp': 'optional in local mode; not checked'}, indent=2))
        elif args.command == 'enqueue':
            print(store.enqueue(json.loads(args.card.read_text())))
        elif args.command == 'status':
            print(json.dumps(store.rows(), indent=2, ensure_ascii=False))
        elif args.command == 'run':
            author, reviewers = providers.executors(config)
            for provider in {spec['provider'] for spec in [author, *reviewers]}:
                if not providers.authenticated(provider):
                    raise ValueError(f'{provider} is not authenticated; sign in using its CLI before running')
            def halt(signum, frame):
                (store.root / 'STOP').touch()
            signal.signal(signal.SIGINT, halt)
            signal.signal(signal.SIGTERM, halt)
            print(json.dumps(Runner(config, store).run(), indent=2, ensure_ascii=False))
        elif args.command == 'stop':
            (store.root / 'STOP').touch(); print('STOP recorded; active stages stop on next poll')
        elif args.command == 'resume':
            with store.lock():
                (store.root / 'STOP').unlink(missing_ok=True)
        elif args.command in ('retry', 'recover'):
            with store.lock():
                row = store.get(args.task)
                expected = 'running' if args.command == 'recover' else 'blocked'
                if row['state'] != expected or row['attempts'] >= config['max_attempts']:
                    raise ValueError('Wrong state or attempt limit reached')
                store.update(args.task, state='queued', head=None, config_hash=None, error=None)
        elif args.command in ('record-pr', 'sync-pr'):
            with store.lock():
                row = store.get(args.task)
                if row['state'] not in ('verified_local', 'pr_open', 'pr_verified'):
                    raise ValueError('Task must have local verification')
                runner = Runner(config, store)
                runner.clean_head(row['worktree'], row['head'])
                if runner.fingerprint != row['config_hash']:
                    raise ValueError('Verification configuration changed; rerun checks/reviews')
                url = args.url if args.command == 'record-pr' else row['pr']
                if not url or not url.startswith('https://github.com/'):
                    raise ValueError('Expected GitHub PR URL')
                # Resolve expected repo independently; a URL for another project is never accepted.
                repo_name = json.loads(subprocess.check_output(['gh', 'repo', 'view', '--json', 'nameWithOwner'], cwd=config['repo'], text=True))['nameWithOwner']
                if not url.startswith('https://github.com/' + repo_name + '/pull/'):
                    raise ValueError('PR belongs to another repository')
                info = json.loads(subprocess.check_output(['gh', 'pr', 'view', url, '--json',
                    'headRefOid,baseRefName,state,mergeCommit'], text=True))
                if info['headRefOid'] != row['head'] or info['baseRefName'] != config['base']:
                    raise ValueError('Remote head/base differs from verified task')
                if info['state'] == 'MERGED':
                    store.update(args.task, state='merged', pr=url)
                elif info['state'] != 'OPEN':
                    raise ValueError('PR is not open')
                else:
                    checks = subprocess.run(['gh', 'pr', 'checks', url, '--json', 'name,bucket'], text=True, capture_output=True)
                    data = json.loads(checks.stdout or '[]')
                    green = checks.returncode == 0 and bool(data) and all(c['bucket'] == 'pass' for c in data)
                    store.update(args.task, state='pr_verified' if green else 'pr_open', pr=url)
                    store.event(args.task, 'ci', {'head': row['head'], 'checks': data, 'green': green})
                print(json.dumps(store.get(args.task), indent=2))
    except (ValueError, RuntimeError, KeyError, OSError, subprocess.SubprocessError) as error:
        p.exit(1, f'factory: {error}\n')


if __name__ == '__main__':
    main()
