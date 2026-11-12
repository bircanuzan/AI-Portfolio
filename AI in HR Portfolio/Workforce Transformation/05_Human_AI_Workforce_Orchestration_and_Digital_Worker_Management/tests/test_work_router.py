import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from work_router import route_request, evaluate

def request(**kwargs):
    r = dict(task="policy_faq", agent_status="PILOT", has_access=True,
             policy_current=True, sensitive=False)
    r.update(kwargs)
    return r

class OrchestrationTests(unittest.TestCase):
    def test_policy_route(self):
        self.assertEqual(route_request(request())["route"], "A-POL")
    def test_aggregates_route(self):
        self.assertEqual(route_request(request(task="aggregate_reporting"))["route"], "A-RPT")
    def test_termination_human(self):
        self.assertEqual(route_request(request(task="termination_decision"))["route"], "HUMAN_REVIEW")
    def test_sensitive_human(self):
        self.assertEqual(route_request(request(sensitive=True))["route"], "HUMAN_REVIEW")
    def test_shadow_human(self):
        self.assertEqual(route_request(request(agent_status="SHADOW"))["route"], "HUMAN_REVIEW")
    def test_missing_access_human(self):
        self.assertEqual(route_request(request(has_access=False))["route"], "HUMAN_REVIEW")
    def test_stale_source_human(self):
        self.assertEqual(route_request(request(policy_current=False))["route"], "HUMAN_REVIEW")
    def test_unknown_task_human(self):
        self.assertEqual(route_request(request(task="unknown"))["route"], "HUMAN_REVIEW")
    def test_never_executes(self):
        self.assertFalse(route_request(request())["executed"])
    def test_scenarios(self):
        rows, passed = evaluate()
        self.assertEqual(passed, len(rows))

if __name__ == "__main__":
    unittest.main()