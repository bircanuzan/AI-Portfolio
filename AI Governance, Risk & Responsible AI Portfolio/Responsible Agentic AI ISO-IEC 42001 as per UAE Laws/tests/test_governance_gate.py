import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from governance_gate import evaluate, run_suite


class GovernanceGateTests(unittest.TestCase):
    def test_authored_scenarios(self):
        scenarios = json.loads((ROOT / 'data' / 'synthetic_scenarios.json').read_text())
        result = run_suite(scenarios)
        self.assertEqual(result['total'], 12)
        self.assertEqual(result['failed'], 0, result['results'])

    def test_prompt_injection_overrides_approval(self):
        self.assertEqual(evaluate({'tool': 'send_candidate_message', 'prompt_injection': True, 'human_approval': True})['decision'], 'DENY')

    def test_personal_data_requires_recorded_basis(self):
        self.assertEqual(evaluate({'tool': 'draft_candidate_message', 'personal_data': True})['decision'], 'DENY')

    def test_unapproved_tool_denied(self):
        self.assertEqual(evaluate({'tool': 'shell_exec'})['decision'], 'DENY')

    def test_high_impact_action_never_autonomously_allowed(self):
        self.assertEqual(evaluate({'tool': 'rank_candidates', 'human_approval': True})['decision'], 'ESCALATE_HUMAN')

    def test_export_with_safeguards_still_escalated(self):
        self.assertEqual(evaluate({'tool': 'export_candidate_data', 'data_export': True, 'transfer_safeguards_approved': True})['decision'], 'ESCALATE_HUMAN')

    def test_denial_overrides_escalation(self):
        self.assertEqual(evaluate({'tool': 'rank_candidates', 'personal_data': True})['decision'], 'DENY')

    def test_source_freshness_required(self):
        self.assertEqual(evaluate({'tool': 'answer_hr_policy'})['decision'], 'ESCALATE_HUMAN')

    def test_allow_does_not_mean_external_execution(self):
        result = evaluate({'tool': 'answer_hr_policy', 'source_verified': True})
        self.assertEqual(result['decision'], 'ALLOW_DEMO_ONLY')
        self.assertEqual(result['evidence_status'], 'LOCAL_DETERMINISTIC_SIMULATION')


if __name__ == '__main__':
    unittest.main()
