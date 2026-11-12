"""Reproducibility and governance checks for fictional portfolio."""
import importlib.util
from pathlib import Path
import unittest

FILE = Path(__file__).resolve().parents[1] / "src" / "portfolio_quality.py"
SPEC = importlib.util.spec_from_file_location("portfolio_quality", FILE)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class PortfolioCaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.metrics = MOD.evaluate()

    def test_pipeline_dispositions(self):
        m = self.metrics
        self.assertEqual(m["demand_count"], 6)
        self.assertEqual(m["disposition"],
                         {"Approved": 3, "Deferred": 1, "Rejected": 1, "Pending": 1})

    def test_separate_cost_from_funding(self):
        m = self.metrics
        self.assertEqual(m["funding_total"], 380000)
        self.assertEqual(m["forecast_total"], 415000)
        self.assertEqual(m["funding_shortfalls"]["PRJ-002"], 55000)

    def test_approval_gap_escalated(self):
        self.assertIn("DMD-004", self.metrics["ungated_conversions"])
        self.assertIn("PRJ-002", self.metrics["finance_unapproved"])

    def test_governance_gates(self):
        self.assertEqual(self.metrics["release_gate"], "HOLD_FOR_REVIEW")
        self.assertIn("PRJ-002", self.metrics["overdue_milestones"])
        self.assertEqual(len(self.metrics["open_high_raid"]), 2)

    def test_product_conversion_and_benefits(self):
        self.assertEqual(self.metrics["product_count"], 1)
        self.assertEqual(self.metrics["orphan_conversions"], [])
        self.assertEqual(self.metrics["verified_realised_benefits"], 0)

    def test_board_report_contains_issue(self):
        narrative = MOD.report(self.metrics)
        self.assertIn("DMD-004", narrative)
        self.assertIn("AED 415,000", narrative)


if __name__ == "__main__":
    unittest.main()
