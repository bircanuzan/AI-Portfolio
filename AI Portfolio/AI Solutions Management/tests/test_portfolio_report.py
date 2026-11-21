"""No-dependencies tests for the synthetic portfolio report."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from portfolio_report import build_report, read_csv  # noqa: E402


class PortfolioReportTests(unittest.TestCase):
    def setUp(self):
        self.registry = read_csv(ROOT / "data" / "ai_tool_register_synthetic.csv")
        self.usage = read_csv(ROOT / "data" / "monthly_usage_synthetic.csv")

    def test_expected_synthetic_totals(self):
        report = build_report(self.registry, self.usage)
        for expected in ["**97**", "**63**", "**64.9%**", "$3,430.00",
                         "$4,081.50", "$651.50", "**19.0%**"]:
            self.assertIn(expected, report)
        self.assertIn("DPO", report)  # Telnyx example is pending DPO review

    def test_rejects_unknown_tool(self):
        records = [dict(self.usage[0], tool_id="AI-UNKNOWN")]
        with self.assertRaises(ValueError):
            build_report(self.registry, records)

    def test_rejects_overallocated_seats(self):
        records = [dict(self.usage[0], active_users="41")]
        with self.assertRaises(ValueError):
            build_report(self.registry, records)

    def test_rejects_duplicate_tool_id(self):
        with self.assertRaises(ValueError):
            build_report(self.registry + [dict(self.registry[0])], self.usage)


if __name__ == "__main__":
    unittest.main()
