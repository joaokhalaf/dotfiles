"""CLI adapters. Prompts, queue and verification are provider independent."""
from dataclasses import dataclass
import json
from pathlib import Path
import re
import shutil
import subprocess

PROVIDERS = ('codex', 'claude', 'opencode')


@dataclass
class Invocation:
    argv: list[str]
    report: Path | None = None
    schema: dict | None = None

    def prompt(self, text):
        if self.schema is None:
            return text
        return (text + '\n\nEnd with a final message that is only a JSON object, no prose or code fence, '
                'matching this JSON Schema:\n' + json.dumps(self.schema))


def validate_executor(spec):
    if not isinstance(spec, dict) or spec.get('provider') not in PROVIDERS:
        raise ValueError('Executor provider must be one of: ' + ', '.join(PROVIDERS))
    model = spec.get('model')
    if model is not None and (not isinstance(model, str) or not model.strip()):
        raise ValueError('Executor model must be a nonempty string or null (inherit CLI default)')
    if spec.get('focus') is not None and not isinstance(spec['focus'], str):
        raise ValueError('Reviewer focus must be text')


def executors(config):
    # Read old configs without forcing an immediate migration.
    author = config.get('executor', {'provider': 'claude', 'model': config.get('author_model')})
    reviewers = config.get('reviewers', [{'provider': 'claude', 'model': model}
                                       for model in config.get('review_models', [])])
    validate_executor(author)
    if not isinstance(reviewers, list) or len(reviewers) < 2:
        raise ValueError('Configure at least two independent reviewer sessions')
    for reviewer in reviewers:
        validate_executor(reviewer)
    return author, reviewers


def authenticated(provider):
    if provider == 'codex':
        result = subprocess.run(['codex', 'login', 'status'], text=True, capture_output=True)
        return result.returncode == 0
    if provider == 'claude':
        result = subprocess.run(['claude', 'auth', 'status', '--json'], text=True, capture_output=True)
        return result.returncode == 0 and json.loads(result.stdout).get('loggedIn', False)
    if provider == 'opencode':
        return shutil.which('opencode') is not None and subprocess.run(
            ['opencode', '--version'], capture_output=True).returncode == 0
    raise ValueError(f'Unknown provider: {provider}')


def build(spec, log, schema, readonly=False):
    validate_executor(spec)
    if spec['provider'] == 'codex':
        schema_path = log.with_suffix('.schema.json')
        schema_path.write_text(json.dumps(schema))
        report_path = log.with_suffix('.report.json')
        # Remove a stale report before any new invocation; never accept an earlier result.
        report_path.unlink(missing_ok=True)
        argv = ['codex', 'exec', '--json', '--color', 'never',
                '--sandbox', 'read-only' if readonly else 'workspace-write',
                '--output-schema', str(schema_path), '--output-last-message', str(report_path)]
        if spec.get('model'):
            argv += ['--model', spec['model']]
        return Invocation(argv + ['-'], report_path)
    if spec['provider'] == 'opencode':
        argv = ['opencode', 'run', '--format', 'json', '--archived',
                '--agent', 'plan' if readonly else 'build']
        if spec.get('model'):
            argv += ['--model', spec['model']]
        return Invocation(argv, schema=schema)
    argv = ['claude', '-p', '--output-format', 'json',
            '--permission-prompts', 'none', '--json-schema', json.dumps(schema)]
    if spec.get('model'):
        argv += ['--model', spec['model']]
    # Existing Claude permissions apply; no fabricated readonly tool policy or bypass.
    return Invocation(argv)


def last_json_object(text):
    text = re.sub(r'^```(?:json)?\s*|\s*```$', '', text.strip())
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start = text.rfind('\n{')
        return json.loads(text[start + 1:]) if start >= 0 else None


def parse_opencode(log):
    events = []
    for line in log.read_text().splitlines():
        try:
            value = json.loads(line)
            if isinstance(value, dict):
                events.append(value)
        except json.JSONDecodeError:
            pass
    if any(event.get('type') == 'error' for event in events):
        raise RuntimeError(f'OpenCode reported an error: {log}')
    texts = [event['part'].get('text', '') for event in events
             if event.get('type') == 'text' and isinstance(event.get('part'), dict)]
    finished = [event for event in events if event.get('type') == 'step_finish']
    if not texts or not finished:
        raise RuntimeError(f'OpenCode did not finish with a text report: {log}')
    tokens = finished[-1].get('part', {}).get('tokens')
    return last_json_object(texts[-1]), {
        'estimated_usd': None, 'usage': tokens, 'session_id': events[0].get('sessionID')}


def parse(spec, invocation, log):
    if spec['provider'] == 'opencode':
        return parse_opencode(log)
    if spec['provider'] == 'claude':
        value = json.loads(log.read_text())
        if value.get('is_error'):
            raise RuntimeError(f'Claude reported an error: {log}')
        return value.get('structured_output'), {
            'estimated_usd': value.get('total_cost_usd'), 'usage': value.get('usage'),
            'session_id': value.get('session_id')}
    events = []
    for line in log.read_text().splitlines():
        try:
            value = json.loads(line)
            if isinstance(value, dict):
                events.append(value)
        except json.JSONDecodeError:
            pass  # stderr messages remain in the raw log; they are not results.
    if any(event.get('type') in ('turn.failed', 'error') for event in events):
        raise RuntimeError(f'Codex reported a failed turn: {log}')
    completed = [event for event in events if event.get('type') == 'turn.completed']
    if not completed or invocation.report is None or not invocation.report.is_file():
        raise RuntimeError(f'Codex did not complete with a structured report: {log}')
    started = next((event for event in events if event.get('type') == 'thread.started'), {})
    return json.loads(invocation.report.read_text()), {
        'estimated_usd': None, 'usage': completed[-1].get('usage'),
        'session_id': started.get('thread_id')}


def require_pass(report, log):
    if isinstance(report, dict) and report.get('verdict') in ('BLOCKED', 'ISSUES'):
        summary = report.get('summary')
        detail = summary.strip() if isinstance(summary, str) and summary.strip() else 'No summary provided'
        raise RuntimeError(f"{report['verdict']}: {detail}; report/log: {log}")
    if (not isinstance(report, dict) or report.get('verdict') != 'PASS'
            or not isinstance(report.get('summary'), str)
            or not isinstance(report.get('evidence'), list) or not report['evidence']
            or any(not isinstance(item, str) or not item.strip() for item in report['evidence'])):
        raise RuntimeError(f'Invalid or incomplete structured agent report: {log}')
    return report
