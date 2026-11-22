import json
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from automation_demo import route, summary

DATA = Path(__file__).resolve().parents[1] / "data" / "synthetic_requests.json"

class WorkflowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = json.loads(DATA.read_text(encoding="utf-8"))
        cls.decisions = route(cls.rows)

    def test_expected_synthetic_dispositions(self):
        self.assertEqual(summary(self.decisions)["draft_ready"], 4)
        self.assertEqual(summary(self.decisions)["human_review"], 3)
        self.assertEqual(summary(self.decisions)["blocked"], 1)

    def test_no_external_actions(self):
        self.assertEqual(summary(self.decisions)["external_actions_executed"], 0)

    def test_sensitive_export_blocked(self):
        self.assertEqual(self.decisions[5]["status"], "blocked")

    def test_human_review_for_hr_and_finance(self):
        self.assertEqual(self.decisions[2]["status"], "human_review")
        self.assertEqual(self.decisions[3]["status"], "human_review")

    def test_duplicate_detection(self):
        rows = [{"request_id": "x", "department": "support", "request": "Help"},
                {"request_id": "x", "department": "support", "request": "Help"}]
        self.assertEqual(route(rows)[1]["status"], "invalid_input")

    def test_missing_fields(self):
        self.assertEqual(route([{"department": "operations"}])[0]["status"], "invalid_input")

    def test_drafts_never_execute(self):
        for record in self.decisions:
            if record["status"] != "draft_ready":
                self.assertIsNone(record["draft"])

if __name__ == "__main__":
    unittest.main()
