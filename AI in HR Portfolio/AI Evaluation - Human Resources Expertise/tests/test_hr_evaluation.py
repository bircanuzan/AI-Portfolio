import unittest
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1] / "src"))
from hr_evaluation import load_data,evaluate,report

class HREvaluationTests(unittest.TestCase):
    def setUp(self):
        self.cases=load_data()["cases"]
        self.by_id={c["id"]:c for c in self.cases}
    def test_all_reference_outcomes(self):
        x=report()
        self.assertEqual(x["case_count"],8)
        self.assertEqual(x["reference_match_count"],8)
    def test_recruitment_human_review(self):
        x=evaluate(self.by_id["TA-002"])
        self.assertEqual(x["status"],"CRITICAL_FAIL")
        self.assertFalse(x["authorizes_consequential_action"])
    def test_compensation_requires_approval(self):
        self.assertEqual(evaluate(self.by_id["TR-001"])["status"],"CRITICAL_FAIL")
    def test_employment_relations_escalation(self):
        x=evaluate(self.by_id["ER-001"])
        self.assertEqual(x["status"],"CRITICAL_FAIL")
        self.assertGreaterEqual(len(x["findings"]),2)
    def test_unsupported_evidence_flag(self):
        self.assertEqual(evaluate(self.by_id["TM-001"])["status"],"MAJOR_FAIL")
    def test_protected_traits_flagged(self):
        self.assertEqual(evaluate(self.by_id["EB-001"])["status"],"CRITICAL_FAIL")
    def test_private_data_flagged(self):
        self.assertEqual(evaluate(self.by_id["HO-001"])["status"],"CRITICAL_FAIL")
    def test_safe_advisory_allowed_without_auto_write(self):
        self.assertEqual(evaluate(self.by_id["OD-001"])["status"],"PASS")
    def test_malformed_model_output_rejected(self):
        case=dict(self.by_id["TA-001"])
        case["model_output"]={"action":"recommend_interview"}
        with self.assertRaises(ValueError):evaluate(case)
    def test_references_have_case_ids(self):
        self.assertEqual(len({c["id"] for c in self.cases}),len(self.cases))
if __name__=="__main__":unittest.main()
