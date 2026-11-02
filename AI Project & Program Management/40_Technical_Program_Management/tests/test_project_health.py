"""Unit tests for the synthetic TPM dashboard."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from project_health import calculate, records


class ProjectHealthTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = [records(name) for name in
                    ("milestones.csv", "raid_register.csv", "feature_requests.csv", "capacity_plan.csv")]

    def test_october_29_portfolio(self):
        report = calculate("2026-10-29", *self.data)
        totals = report["portfolio"]
        self.assertEqual(totals["milestones_total"], 13)
        self.assertEqual(totals["completed"], 6)
        self.assertEqual(totals["completed_on_time"], 4)
        self.assertEqual(totals["on_time_completion_pct"], 66.7)
        self.assertEqual(totals["overdue_open"], 2)
        self.assertEqual(totals["open_p1_count"], 1)
        self.assertEqual(totals["blocked_feature_count"], 1)
        self.assertEqual(totals["capacity_gap_hours_per_week"], 24)

    def test_explainable_rag(self):
        report = calculate("2026-10-29", *self.data)
        atlas = report["clients"]["Atlas Bank"]
        beacon = report["clients"]["Beacon FinTech"]
        self.assertEqual(atlas["rag"], "Amber")
        self.assertEqual(beacon["rag"], "Red")
        self.assertEqual(atlas["overdue_open_ids"], ["A04"])
        self.assertEqual(beacon["open_p1_ids"], ["I01"])

    def test_early_date_does_not_treat_future_done_as_completed(self):
        report = calculate("2026-10-01", *self.data)
        self.assertEqual(report["portfolio"]["completed"], 0)
        self.assertIsNone(report["portfolio"]["on_time_completion_pct"])
        self.assertEqual(report["portfolio"]["capacity_gap_hours_per_week"], 0)


if __name__ == "__main__":
    unittest.main()
