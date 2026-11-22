"""Offline unit tests for synthetic project-management evaluation harness."""
import unittest
from pathlib import Path

from evaluate_pm import (
    ROOT, load_cases, critical_path, compute_reference, compare_answer, run_evaluation
)


class ProjectManagementEvaluationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases = load_cases(ROOT / "data/cases.jsonl")
        cls.by_id = {x["id"]: x for x in cls.cases}

    def test_fixture_inventory(self):
        self.assertEqual(len(self.cases), 6)
        self.assertEqual(len(self.by_id), len(self.cases))

    def test_schedule_forward_pass(self):
        self.assertEqual(compute_reference(self.by_id["PM-001"]),
                         {"duration_days": 10, "critical_path": ["A", "B", "D"]})

    def test_earned_value_critical_numbers(self):
        ref = compute_reference(self.by_id["PM-002"])
        self.assertAlmostEqual(ref["cpi"], 0.8)
        self.assertAlmostEqual(ref["spi"], 48/54)
        self.assertAlmostEqual(ref["eac"], 125000)
        self.assertTrue(ref["over_budget"] and ref["behind_schedule"])

    def test_capacity_risk_and_scrum(self):
        self.assertEqual(compute_reference(self.by_id["PM-003"])["capacity_gap_hours"], 5)
        self.assertEqual(compute_reference(self.by_id["PM-004"])["aggregate_emv_aed"], 8000)
        self.assertEqual(compute_reference(self.by_id["PM-005"])["overcommitment_points"], 8)

    def test_no_unapproved_scope_change(self):
        ref = compute_reference(self.by_id["PM-006"])
        self.assertFalse(ref["approve_immediately"])
        self.assertFalse(ref["update_baseline_now"])
        self.assertTrue(ref["impact_assessment_required"])

    def test_expected_good_and_bad_fixture_detection(self):
        result = run_evaluation(self.cases)
        self.assertEqual(result["perfect_good_fixtures"], 6)
        self.assertEqual(result["flawed_fixtures_with_error_detected"], 6)

    def test_reject_cycles(self):
        with self.assertRaises(ValueError):
            critical_path([{"id":"A","duration_days":1,"depends_on":["B"]},
                           {"id":"B","duration_days":1,"depends_on":["A"]}])

    def test_boolean_not_accepted_as_numeric(self):
        check = compare_answer({"capacity_gap_hours": 1}, {"capacity_gap_hours": True})
        self.assertEqual(check["correct_fields"], 0)

    def test_reject_unexpected_field_in_schema(self):
        check = compare_answer({"capacity_gap_hours": 5},
                               {"capacity_gap_hours": 5,"unsupported":"extra"})
        self.assertTrue(check["field_checks"]["capacity_gap_hours"]["correct"])
        self.assertFalse(check["strict_schema"])


if __name__ == "__main__":
    unittest.main()
