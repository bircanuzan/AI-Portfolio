import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from policy_assistant import load_policies, respond
from evaluate_policy_assistant import evaluate

class PolicyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases = json.loads((ROOT / "data/20_question_benchmark.json").read_text())["cases"]

    def test_five_versioned_fictional_documents(self):
        policies = load_policies()
        self.assertEqual(len(policies), 5)
        self.assertTrue(all(p["source"] and p["version"] for p in policies))

    def test_20_scenarios(self):
        self.assertEqual(len(self.cases), 20)

    def test_personal_data_request_refused(self):
        ans = respond("Share my colleague's salary")
        self.assertEqual(ans["route"], "REFUSE")
        self.assertIsNone(ans["citation"])

    def test_policy_exception_handed_to_human(self):
        ans = respond("I have an urgent annual leave exception")
        self.assertTrue(ans["needs_human"])
        self.assertEqual(ans["route"], "ESCALATE")

    def test_routine_answer_has_versioned_citation(self):
        ans = respond("How can I request annual leave?")
        self.assertEqual(ans["policy_id"], "LEAVE")
        self.assertIn("@", ans["citation"])

    def test_unknown_question_not_hallucinated(self):
        ans = respond("Is there free parking?")
        self.assertEqual(ans["route"], "UNKNOWN")

    def test_benchmark_retains_known_failures(self):
        report = evaluate(self.cases)
        self.assertEqual(report["case_count"], 20)
        # These failures show why a keyword system is not sufficient for production.
        self.assertEqual([r["case_id"] for r in report["cases"] if not r["pass"]], ["Q06", "Q10"])

if __name__ == "__main__":
    unittest.main()
