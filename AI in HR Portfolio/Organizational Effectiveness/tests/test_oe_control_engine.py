"""Standard-library tests; synthetic data only."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from oe_control_engine import (
    load_case, validate_case, workforce_summary, reconcile_payroll,
    review_hiring_requests, evaluate_role, automation_impact, strategy_scorecard,
    build_report
)

class TestGroupOEControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.case = load_case()

    def test_fixture_integrity(self):
        self.assertEqual(validate_case(self.case), [])

    def test_positions_and_vacancies_are_separate(self):
        result = workforce_summary(self.case)
        self.assertEqual(result["total_approved_position_records"], 9)
        self.assertEqual(result["total_occupied"], 6)
        self.assertEqual(result["vacant_position_ids"], ["P03", "P06", "P08"])

    def test_entity_costs_and_budget_checks(self):
        results = workforce_summary(self.case)["entities"]
        corp = next(row for row in results if row["entity"] == "CORP")
        self.assertEqual(corp["annual_committed_position_run_rate_aed"], 2223000.0)
        self.assertFalse(any(row["control_breach"] for row in results))

    def test_payroll_difference_is_flagged_not_mutated(self):
        findings = reconcile_payroll(self.case)
        self.assertEqual(findings, [{"employee": "E02", "issue": "base_salary_difference", "annual_difference_aed": 5000}])

    def test_hiring_routes_no_auto_approval(self):
        rows = review_hiring_requests(self.case)
        mapping = {row["request"]: row["recommendation"] for row in rows}
        self.assertEqual(mapping, {
            "REQ-01": "RECOMMEND_FOR_APPROVAL", "REQ-02": "ESCALATE_HCC",
            "REQ-03": "ESCALATE_CPO", "REQ-04": "HOLD_LEGAL",
            "REQ-05": "HOLD_VENDOR", "REQ-06": "RECOMMEND_FOR_APPROVAL"
        })
        self.assertTrue(all(not row["automatic_approval"] for row in rows))

    def test_role_scoring_is_consistent(self):
        role = next(p for p in self.case["positions"] if p["id"] == "P02")
        self.assertEqual(evaluate_role(role["factors"], self.case["assumptions"]), {
            "points": 770, "illustrative_grade": "G7"
        })

    def test_high_impact_ai_excluded(self):
        rows = automation_impact(self.case)
        high = next(row for row in rows if row["activity"] == "ACT03")
        self.assertTrue(high["excluded_from_capacity_claim"])
        self.assertEqual(high["theoretical_hours_only"], 0.0)
        self.assertTrue(all(row["human_review_required"] for row in rows))

    def test_strategy_scorecard(self):
        self.assertEqual(strategy_scorecard(self.case), {
            "all": 4, "complete": 2, "at_risk": ["S03"]
        })

    def test_report_is_only_a_recommendation(self):
        result = build_report(self.case)
        self.assertTrue(result["synthetic"])
        self.assertTrue(result["action"].startswith("NONE"))

    def test_duplicate_employee_rejected(self):
        case = {**self.case, "employees": list(self.case["employees"]) + [dict(self.case["employees"][0])]}
        self.assertIn("duplicate_employee_id", validate_case(case))

    def test_invalid_job_factor_rejected(self):
        with self.assertRaises(ValueError):
            evaluate_role({"impact": 7, "complexity": 3, "expertise": 3, "leadership": 2},
                          self.case["assumptions"])

if __name__ == "__main__":
    unittest.main()
