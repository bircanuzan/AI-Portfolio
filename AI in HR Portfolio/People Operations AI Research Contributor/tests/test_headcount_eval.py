"""Regression tests for the independent People Operations AI Research Contributor case."""
import sys
import unittest
from copy import deepcopy
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from headcount_eval import load, reference, grade

class PeopleOperationsTests(unittest.TestCase):
    def setUp(self):
        self.source=load()
        self.ref=reference(self.source)

    def test_expected_role_and_department_rows(self):
        self.assertEqual(len(self.ref["rows"]),18)
        self.assertEqual(len(self.ref["summary"]),9)

    def test_reference_passes_all_numeric_rubrics(self):
        result=grade(self.ref)
        self.assertEqual(result["status"],"PASS_NUMERIC_REFERENCE")
        self.assertEqual(result["automated_yes"],9)
        self.assertEqual(result["workbook_review_pending"],3)

    def test_hc_roll_forward(self):
        previous={}
        for row in self.ref["rows"]:
            rid=row["role_id"]
            if rid in previous:
                self.assertEqual(row["opening_hc"],previous[rid])
            previous[rid]=row["closing_hc"]

    def test_salary_tampering_is_detected(self):
        attempt=deepcopy(self.ref)
        attempt["rows"][0]["salary_aed"]="99999.00"
        outcomes={x["id"]:x["result"] for x in grade(attempt)["criteria"]}
        self.assertEqual(outcomes["POP-06"],"NO")

    def test_wrong_loaded_compensation_detected(self):
        attempt=deepcopy(self.ref)
        attempt["rows"][1]["loaded_cost_aed"]="0.00"
        outcomes={x["id"]:x["result"] for x in grade(attempt)["criteria"]}
        self.assertEqual(outcomes["POP-07"],"NO")

    def test_wrong_budget_variance_detected(self):
        attempt=deepcopy(self.ref)
        attempt["summary"][1]["budget_minus_cost_aed"]="999.00"
        self.assertEqual(grade(attempt)["status"],"FAIL_NUMERIC_REFERENCE")

    def test_missing_role_month_detected(self):
        attempt=deepcopy(self.ref)
        attempt["rows"].pop()
        self.assertEqual(grade(attempt)["criteria"][0]["result"],"NO")

    def test_duplicate_role_month_detected(self):
        attempt=deepcopy(self.ref)
        attempt["rows"].append(deepcopy(attempt["rows"][0]))
        self.assertEqual(grade(attempt)["criteria"][0]["result"],"NO")

    def test_negative_headcount_rejected_at_source(self):
        data=deepcopy(self.source)
        data["movements"][0][3]=100
        with self.assertRaises(ValueError):
            reference(data)

    def test_salary_band_violation_rejected(self):
        data=deepcopy(self.source)
        data["roles"][0]["salary"]="99999"
        with self.assertRaises(ValueError):
            reference(data)

    def test_duplicate_movement_rejected(self):
        data=deepcopy(self.source)
        data["movements"].append(deepcopy(data["movements"][0]))
        with self.assertRaises(ValueError):
            reference(data)

    def test_invalid_benefit_pct_rejected(self):
        data=deepcopy(self.source)
        data["benefits_load"]="1.2"
        with self.assertRaises(ValueError):
            reference(data)

    def test_rollup_reconciles_to_role_rows(self):
        for summary in self.ref["summary"]:
            detail=[r for r in self.ref["rows"]
                    if r["month"]==summary["month"]
                    and r["department"]==summary["department"]]
            self.assertEqual(summary["closing_hc"],sum(r["closing_hc"] for r in detail))

    def test_negative_variance_visible(self):
        self.assertTrue(any(
            x["budget_minus_cost_aed"].startswith("-") for x in self.ref["summary"]
        ))

    def test_no_live_model_or_real_hr_writes(self):
        self.assertFalse(self.ref["live_model_used"])
        self.assertEqual(self.ref["actual_employment_writes"],0)
        self.assertFalse(grade(self.ref)["live_model_graded"])

if __name__=="__main__":
    unittest.main()
