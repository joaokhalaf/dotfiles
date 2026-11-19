import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('factory', Path(__file__).resolve().parents[1] / 'scripts/factory.py')
f = importlib.util.module_from_spec(spec)
spec.loader.exec_module(f)


class FakeRunner(f.Runner):
    """Replace paid model calls only; use real Git, worktrees, checks and queue."""
    def agent(self, task, model, prompt, log):
        cwd = Path(self.store.get(task)['worktree'])
        if log.name == 'author.json':
            (cwd / 'result.txt').write_text('accepted\n')
            subprocess.run(['git', '-C', str(cwd), 'add', 'result.txt'], check=True)
            subprocess.run(['git', '-C', str(cwd), 'commit', '-qm', 'Implement card'], check=True)
        log.write_text(json.dumps({'verdict': 'PASS', 'evidence': ['fixture check']}))
        return {'verdict': 'PASS', 'evidence': ['fixture check']}


class FactoryTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.repo = self.root / 'repo'
        subprocess.run(['git', 'init', '-q', '-b', 'main', str(self.repo)], check=True)
        for key, value in [('user.name', 'Test'), ('user.email', 'test@example.invalid')]:
            subprocess.run(['git', '-C', str(self.repo), 'config', key, value], check=True)
        (self.repo / 'base.txt').write_text('base')
        subprocess.run(['git', '-C', str(self.repo), 'add', '.'], check=True)
        subprocess.run(['git', '-C', str(self.repo), 'commit', '-qm', 'Initial'], check=True)
        self.config = {'repo': str(self.repo), 'base': 'main', 'concurrency': 2,
                       'max_attempts': 2, 'timeout_seconds': 5, 'max_agent_calls_per_run': 6,
                       'max_estimated_usd_per_run': None, 'author_model': 'sonnet',
                       'review_models': ['sonnet', 'opus'],
                       'checks': [['python3', '-c', 'print("check passed")']],
                       'behavior_checks': [['python3', '-c', 'from pathlib import Path; assert Path("result.txt").read_text()=="accepted\\n"']]}
        self.store = f.Store(self.root / 'state')
        self.card = {'title': 'Fixture', 'goal': 'Create result',
                     'acceptance': ['result is accepted'], 'scope': ['result.txt']}

    def tearDown(self):
        self.temp.cleanup()

    def test_real_worktrees_and_verified_heads(self):
        for _ in range(2):
            self.store.enqueue(self.card)
        rows = FakeRunner(self.config, self.store).run()
        self.assertEqual([r['state'] for r in rows], ['verified_local'] * 2)
        self.assertNotEqual(rows[0]['worktree'], rows[1]['worktree'])
        for row in rows:
            self.assertEqual(f.git(row['worktree'], 'rev-parse', 'HEAD'), row['head'])
        self.assertFalse((self.repo / 'result.txt').exists())
        self.assertEqual(FakeRunner(self.config, self.store).run(), [])

    def test_failed_check_blocks_and_preserves_worktree(self):
        self.store.enqueue(self.card)
        self.config['checks'] = [['python3', '-c', 'raise SystemExit(3)']]
        row = FakeRunner(self.config, self.store).run()[0]
        self.assertEqual(row['state'], 'blocked')
        self.assertTrue(Path(row['worktree']).is_dir())
        self.assertIsNone(row['head'])

    def test_missing_reviewer_evidence_blocks(self):
        class BrokenReviewer(FakeRunner):
            def agent(self, task, model, prompt, log):
                if log.name.startswith('review'):
                    raise RuntimeError('Reviewer unavailable')
                return super().agent(task, model, prompt, log)
        self.store.enqueue(self.card)
        self.assertEqual(BrokenReviewer(self.config, self.store).run()[0]['state'], 'blocked')

    def test_head_change_invalidates_review(self):
        class MutatingReviewer(FakeRunner):
            def agent(self, task, model, prompt, log):
                value = super().agent(task, model, prompt, log)
                if log.name.startswith('review'):
                    (Path(self.store.get(task)['worktree']) / 'result.txt').write_text('changed')
                return value
        self.store.enqueue(self.card)
        self.assertEqual(MutatingReviewer(self.config, self.store).run()[0]['state'], 'blocked')

    def test_dependencies_wait_for_merge(self):
        parent = self.store.enqueue(self.card)
        child = self.store.enqueue({**self.card, 'depends_on': [parent]})
        self.assertEqual([r['id'] for r in self.store.eligible(2)], [parent])
        self.store.update(parent, state='verified_local')
        self.assertEqual(self.store.eligible(2), [])
        self.store.update(parent, state='merged')
        self.assertEqual([r['id'] for r in self.store.eligible(2)], [child])

    def test_unknown_dependency_rejected(self):
        with self.assertRaises(ValueError):
            self.store.enqueue({**self.card, 'depends_on': [999]})

    def test_queue_lock(self):
        with self.store.lock():
            with self.assertRaises(ValueError):
                with self.store.lock():
                    pass

    def test_stop_and_interruption_block_launch(self):
        task = self.store.enqueue(self.card)
        (self.store.root / 'STOP').touch()
        with self.assertRaises(ValueError):
            FakeRunner(self.config, self.store).run()
        (self.store.root / 'STOP').unlink()
        self.store.update(task, state='running')
        with self.assertRaises(ValueError):
            FakeRunner(self.config, self.store).run()

    def test_configuration_requires_real_checks(self):
        path = self.root / 'config.json'
        self.config['behavior_checks'] = []
        path.write_text(json.dumps(self.config))
        with self.assertRaises(ValueError):
            f.load_config(path)
        self.config['behavior_checks'] = [['true']]
        self.config['checks'] = ['npm test']
        path.write_text(json.dumps(self.config))
        with self.assertRaises(ValueError):
            f.load_config(path)

    def test_timeout_terminates_stage(self):
        self.config['timeout_seconds'] = 0.1
        with self.assertRaises(RuntimeError):
            FakeRunner(self.config, self.store).execute(['python3', '-c', 'import time; time.sleep(10)'], self.repo, self.root / 'timeout.log')

    def test_agent_call_cap_is_enforced_before_launch(self):
        task = self.store.enqueue(self.card)
        self.store.update(task, worktree=str(self.repo))
        runner = f.Runner(self.config, self.store)
        runner.calls = 6
        with self.assertRaisesRegex(RuntimeError, 'call limit'):
            runner.agent(task, 'sonnet', 'not sent', self.root / 'unused.json')
        self.assertFalse((self.root / 'unused.json').exists())

    def test_retry_can_reverify_same_commit(self):
        task = self.store.enqueue(self.card)
        self.config['checks'] = [['python3', '-c', 'raise SystemExit(1)']]
        first = FakeRunner(self.config, self.store).run()[0]
        self.assertEqual(first['state'], 'blocked')
        self.store.update(task, state='queued')
        self.config['checks'] = [['true']]
        class VerifyExisting(FakeRunner):
            def agent(self, task, model, prompt, log):
                if log.name == 'author.json':
                    return {'verdict': 'PASS', 'evidence': ['prior committed work']}
                return super().agent(task, model, prompt, log)
        self.assertEqual(VerifyExisting(self.config, self.store).run()[0]['state'], 'verified_local')

    def test_out_of_scope_diff_blocks(self):
        self.store.enqueue({**self.card, 'scope': ['other.txt']})
        self.assertEqual(FakeRunner(self.config, self.store).run()[0]['state'], 'blocked')

    def test_prepare_runs_before_author(self):
        marker = self.root / 'prepared'
        self.config['prepare'] = [['python3', '-c', f'from pathlib import Path; Path({str(marker)!r}).touch()']]
        self.store.enqueue(self.card)
        class PreparedRunner(FakeRunner):
            def agent(inner, *args, **kwargs):
                self.assertTrue(marker.exists())
                return super().agent(*args, **kwargs)
        self.assertEqual(PreparedRunner(self.config, self.store).run()[0]['state'], 'verified_local')

    def test_failed_prepare_does_not_launch_author(self):
        self.config['prepare'] = [['python3', '-c', 'raise SystemExit(7)']]
        self.store.enqueue(self.card)
        row = FakeRunner(self.config, self.store).run()[0]
        self.assertEqual(row['state'], 'blocked')
        self.assertFalse((self.store.root / 'logs/1/1/author.json').exists())

    def test_missing_auth_does_not_consume_attempt(self):
        config_path = self.root / 'config.json'
        config_path.write_text(json.dumps(self.config))
        with patch.object(f, 'ROOT', self.root), patch('sys.argv', ['factory', '--config', str(config_path), 'run']), patch.object(f.providers, 'authenticated', return_value=False):
            with self.assertRaises(SystemExit) as error:
                f.main()
            self.assertEqual(error.exception.code, 1)
        self.assertEqual(list((self.root / '.factory').glob('*/worktrees')), [])

    def test_host_commits_uncommitted_author_changes(self):
        self.store.enqueue(self.card)
        class UncommittedAuthor(FakeRunner):
            def agent(inner, task, model, prompt, log):
                if log.name == 'author.json':
                    (Path(inner.store.get(task)['worktree']) / 'result.txt').write_text('accepted\n')
                    return {'verdict': 'PASS', 'evidence': ['fixture']}
                return super().agent(task, model, prompt, log)
        row = UncommittedAuthor(self.config, self.store).run()[0]
        self.assertEqual(row['state'], 'verified_local')
        self.assertEqual(f.git(row['worktree'], 'log', '-1', '--format=%s'), self.card['title'])

    def test_standalone_round_without_any_mcp(self):
        config = {**self.config, 'coordination': 'local',
                  'executor': {'provider': 'codex'},
                  'reviewers': [{'provider': 'codex', 'focus': 'contracts'},
                                {'provider': 'codex', 'focus': 'regressions'}]}
        outer = self
        class StandaloneRunner(f.Runner):
            def execute(inner, argv, cwd, log, stdin=None):
                if argv[0] != 'codex':
                    return super().execute(argv, cwd, log, stdin)
                outer.assertIn('Coordination mode: local', stdin)
                outer.assertIn('No Herdr session, MCP call', stdin)
                outer.assertNotIn('use Herdr coordination', stdin)
                if not log.name.startswith('review'):
                    (Path(cwd) / 'result.txt').write_text('accepted\n')
                report = Path(argv[argv.index('--output-last-message') + 1])
                report.write_text(json.dumps({'verdict': 'PASS', 'summary': 'Fixture ran without MCP',
                                              'evidence': ['result contract passed']}))
                log.write_text('{"type":"turn.completed","usage":{"input_tokens":1}}')
        for _ in range(2):
            self.store.enqueue(self.card)
        rows = StandaloneRunner(config, self.store).run()
        self.assertEqual([row['state'] for row in rows], ['verified_local', 'verified_local'])

    def test_herdr_requires_explicit_coordination_mode(self):
        local = f.Runner(self.config, self.store).coordination_context()
        external = f.Runner({**self.config, 'coordination': 'herdr'}, self.store).coordination_context()
        self.assertIn('Coordination mode: local', local)
        self.assertIn('missing access or denied reservations are BLOCKED', external)
        self.assertNotEqual(local, external)

    def test_state_survives_new_store(self):
        task = self.store.enqueue(self.card)
        self.store.update(task, state='blocked', attempts=1, error='fixture')
        self.assertEqual(f.Store(self.store.root).get(task)['attempts'], 1)


if __name__ == '__main__':
    unittest.main()
