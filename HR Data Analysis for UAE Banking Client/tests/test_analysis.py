"""Authored regression tests of synthetic HR MIS calculations and control failures."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from analysis import CUTOFF, read_csv, summarise  # noqa: E402


class TestMonthEndMIS(unittest.TestCase):
    def setUp(self):
        self.employees = read_csv(ROOT / "data" / "employee_snapshot.csv")
        self.positions = read_csv(ROOT / "data" / "funded_positions.csv")
        self.reqs = read_csv(ROOT / "data" / "requisitions.csv")

    def report(self):
        return summarise(self.employees, self.positions, self.reqs, CUTOFF)

    def test_group_actual_fte_and_headcount(self):
        g = self.report()["group"]
        self.assertEqual(g["actual_headcount"], 8)
        self.assertEqual(g["actual_fte"], 8.0)
        self.assertEqual(g["funded_fte"], 12.0)
        self.assertEqual(g["vacancy_fte"], 4.0)

    def test_group_people_cost_bridge(self):
        g = self.report()["group"]
        self.assertEqual(g["annualized_actual_cost_aed"], 2095000.0)
        self.assertEqual(g["annual_budget_aed"], 3430000.0)
        self.assertEqual(g["cost_variance_aed"], -1335000.0)

    def test_illustrative_emirati_gap(self):
        d = {x["division"]: x for x in self.report()["divisions"]}
        self.assertEqual(d["Finance"]["illustrative_target_gap_fte"], 0)
        self.assertEqual(d["Technology"]["illustrative_target_gap_fte"], 1)
        self.assertEqual(d["Retail"]["illustrative_target_gap_fte"], 1)
        self.assertEqual(self.report()["group"]["emirati_fte_share_pct"], 37.5)

    def test_pending_requisitions_not_treated_as_approved(self):
        g = self.report()["group"]
        self.assertEqual(g["approved_requisitions_fte"], 2.0)
        self.assertEqual(g["pending_requisitions_fte"], 3.0)
        self.assertEqual(g["scenario_fte_after_approved_hires"], 10.0)

    def test_duplicate_employee_rejected(self):
        self.employees.append(dict(self.employees[0]))
        with self.assertRaisesRegex(ValueError, "duplicate"):
            self.report()

    def test_unmapped_division_rejected(self):
        self.employees[0]["division"] = "UnmappedUnit"
        with self.assertRaisesRegex(ValueError, "unmapped division"):
            self.report()

    def test_inconsistent_cutoff_rejected(self):
        self.positions[0]["as_of"] = "2026-09-30"
        with self.assertRaisesRegex(ValueError, "inconsistent reporting cutoff"):
            self.report()

    def test_unapproved_funded_positions_rejected(self):
        self.positions[0]["approval_status"] = "Pending"
        with self.assertRaisesRegex(ValueError, "unapproved allocation"):
            self.report()

    def test_invalid_fte_rejected(self):
        self.employees[0]["fte"] = "-0.5"
        with self.assertRaisesRegex(ValueError, "negative"):
            self.report()


if __name__ == "__main__":
    unittest.main()
