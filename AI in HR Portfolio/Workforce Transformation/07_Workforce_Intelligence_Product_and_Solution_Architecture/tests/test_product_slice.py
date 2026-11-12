import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from product_slice import triage, backlog_card, run

def case(**updates):
    x = dict(id="U1", title="Aggregate reporting", business_owner="HR",
             value=4, readiness=4, effort=2, risk="low", impact_on_employment=False)
    x.update(updates)
    return x

class ProductTests(unittest.TestCase):
    def test_eligible_is_discussion_only(self):
        self.assertEqual(triage(case())["decision"], "DISCUSS")
    def test_high_risk_held(self):
        self.assertEqual(triage(case(risk="high"))["decision"], "HOLD")
    def test_employment_action_held(self):
        self.assertEqual(triage(case(impact_on_employment=True))["decision"], "HOLD")
    def test_unknown_employment_impact_defaults_to_hold(self):
        c = case()
        del c["impact_on_employment"]
        self.assertEqual(triage(c)["decision"], "HOLD")
    def test_incomplete_held(self):
        self.assertEqual(triage({"id": "bad"})["decision"], "HOLD")
    def test_invalid_scale_held(self):
        self.assertEqual(triage(case(value=8))["reason"], "INVALID_INPUT")
    def test_backlog_requires_control_gates(self):
        self.assertEqual(len(backlog_card(case())["definition_of_done"]), 5)
    def test_never_executes(self):
        self.assertFalse(triage(case())["action_executed"])
        self.assertTrue(triage(case())["human_approval_required"])
    def test_dataset(self):
        self.assertEqual(len(run()), 4)

if __name__ == "__main__":
    unittest.main()