"""Local-only regression tests for synthetic AI-agent operations."""
import unittest
from .agent_ops_eval import classify, evaluate

BASE = {"event_id": "one", "requires_approval": True,
        "approved": True, "policy_ok": True, "output_checked": True}

class AgentOpsTests(unittest.TestCase):
    def test_authorized_release(self):
        self.assertEqual(classify(BASE), "PASS")

    def test_unapproved_action_held(self):
        self.assertEqual(classify({**BASE, "approved": False}), "HOLD")

    def test_policy_breach_escalates_even_when_approved(self):
        self.assertEqual(classify({**BASE, "policy_ok": False}), "ESCALATE")

    def test_unchecked_output_requires_review(self):
        self.assertEqual(classify({**BASE, "output_checked": False}), "REVIEW")

    def test_duplicate_rejected(self):
        with self.assertRaisesRegex(ValueError, "duplicate"):
            evaluate([BASE, BASE])

    def test_invalid_flag_fails_closed(self):
        with self.assertRaises(ValueError):
            classify({**BASE, "approved": "yes"})

    def test_summary(self):
        events = [BASE, {**BASE, "event_id": "two", "approved": False}]
        self.assertEqual(evaluate(events)["counts"], {"PASS": 1, "HOLD": 1})
        self.assertEqual(evaluate(events)["pass_rate"], 0.5)

if __name__ == "__main__":
    unittest.main()
