import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import providers
import factory


class ProviderTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.log = self.root / 'review-0.json'
        self.report = {'verdict': 'PASS', 'summary': 'Verified', 'evidence': ['ran behavior test: passed']}

    def tearDown(self):
        self.temp.cleanup()

    def test_codex_inherits_default_and_isolates_reviewer(self):
        call = providers.build({'provider': 'codex', 'model': None}, self.root, self.log, factory.SCHEMA, readonly=True)
        self.assertNotIn('--model', call.argv)
        self.assertEqual(call.argv[call.argv.index('--sandbox') + 1], 'read-only')
        self.assertNotIn('--plugin-dir', call.argv)
        self.assertEqual(json.loads(self.log.with_suffix('.schema.json').read_text()), factory.SCHEMA)

    def test_codex_workspace_write_author_and_explicit_model(self):
        call = providers.build({'provider': 'codex', 'model': 'chosen-model'}, self.root, self.log, factory.SCHEMA)
        self.assertIn('workspace-write', call.argv)
        self.assertEqual(call.argv[call.argv.index('--model') + 1], 'chosen-model')
        self.assertFalse(any('bypass' in arg for arg in call.argv))

    def test_codex_jsonl_and_tokens_normalized(self):
        spec = {'provider': 'codex'}
        call = providers.build(spec, self.root, self.log, factory.SCHEMA)
        call.report.write_text(json.dumps(self.report))
        self.log.write_text('warning on stderr\n' + json.dumps({'type': 'thread.started', 'thread_id': 'fixture'}) + '\n' + json.dumps({'type': 'turn.completed', 'usage': {'input_tokens': 12, 'output_tokens': 5}}))
        report, usage = providers.parse(spec, call, self.log)
        self.assertEqual(providers.require_pass(report, self.log), self.report)
        self.assertEqual(usage['session_id'], 'fixture')
        self.assertEqual(usage['usage']['output_tokens'], 5)
        self.assertIsNone(usage['estimated_usd'])

    def test_codex_failed_turn_never_reuses_success_report(self):
        spec = {'provider': 'codex'}
        call = providers.build(spec, self.root, self.log, factory.SCHEMA)
        call.report.write_text(json.dumps(self.report))
        self.log.write_text('{"type":"turn.failed"}\n{"type":"turn.completed"}')
        with self.assertRaises(RuntimeError):
            providers.parse(spec, call, self.log)

    def test_codex_missing_completion_blocks(self):
        spec = {'provider': 'codex'}
        call = providers.build(spec, self.root, self.log, factory.SCHEMA)
        call.report.write_text(json.dumps(self.report))
        self.log.write_text('{"type":"thread.started"}')
        with self.assertRaises(RuntimeError):
            providers.parse(spec, call, self.log)

    def test_stale_codex_report_removed(self):
        self.log.with_suffix('.report.json').write_text('stale')
        call = providers.build({'provider': 'codex'}, self.root, self.log, factory.SCHEMA)
        self.assertFalse(call.report.exists())

    def test_claude_format_and_usage_normalized(self):
        spec = {'provider': 'claude', 'model': 'sonnet'}
        call = providers.build(spec, self.root, self.log, factory.SCHEMA)
        self.assertIn('--plugin-dir', call.argv)
        self.assertIn('sonnet', call.argv)
        self.assertNotIn('--sandbox', call.argv)
        self.log.write_text(json.dumps({'structured_output': self.report, 'total_cost_usd': 0.1, 'usage': {'input_tokens': 8}}))
        report, usage = providers.parse(spec, call, self.log)
        self.assertEqual(providers.require_pass(report, self.log), self.report)
        self.assertEqual(usage['estimated_usd'], 0.1)

    def test_invalid_evidence_never_passes(self):
        for evidence in ([], 'passed', [None], ['']):
            with self.assertRaises(RuntimeError):
                providers.require_pass({**self.report, 'evidence': evidence}, self.log)

    def test_blocked_report_surfaces_actual_cause(self):
        report = {'verdict': 'BLOCKED', 'summary': 'Coordination permission denied', 'evidence': ['join failed']}
        with self.assertRaisesRegex(RuntimeError, 'BLOCKED: Coordination permission denied'):
            providers.require_pass(report, self.log)

    def test_issues_report_is_not_a_format_failure(self):
        with self.assertRaisesRegex(RuntimeError, 'ISSUES: Invalid input accepted'):
            providers.require_pass({'verdict': 'ISSUES', 'summary': 'Invalid input accepted'}, self.log)

    def test_provider_unavailable_does_not_fallback(self):
        with self.assertRaises(ValueError):
            providers.build({'provider': 'unknown'}, self.root, self.log, factory.SCHEMA)

    def test_profile_switch_keeps_checks(self):
        config_path = self.root / 'config.json'
        example = Path(__file__).resolve().parents[1] / 'factory.example.json'
        c = json.loads(example.read_text())
        c.update(repo=str(self.root), base='main', checks=[['true']], behavior_checks=[['true']])
        config_path.write_text(json.dumps(c))
        with patch.object(factory, 'git', side_effect=lambda repo, *args: str(self.root) if args[-1] == '--show-toplevel' else 'fixture-sha'):
            home = factory.load_config(config_path)
            work = factory.load_config(config_path, 'work')
        self.assertEqual(home['executor']['provider'], 'codex')
        self.assertEqual(work['executor']['provider'], 'claude')
        self.assertEqual(home['checks'], work['checks'])
        self.assertEqual(home['repo'], work['repo'])
        self.assertNotEqual(home, work)


if __name__ == '__main__':
    unittest.main()
