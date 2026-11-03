import importlib.util
from pathlib import Path
import unittest

PATH = Path(__file__).resolve().parents[1] / "src" / "tool_portfolio.py"
SPEC = importlib.util.spec_from_file_location("tool_portfolio", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

class PortfolioTests(unittest.TestCase):
    def test_inventory_loads_and_spend_is_nonzero(self):
        report = MODULE.audit()
        self.assertEqual(len(report["tools"]), 5)
        self.assertGreater(report["annual_paid_license_run_rate_usd"], 0)

    def test_unused_seats_are_not_called_savings(self):
        report = MODULE.audit()
        self.assertGreater(report["potential_seat_exposure_usd"], 0)
        self.assertTrue(all(x["verified_savings_usd"] == 0 for x in report["tools"]))

    def test_data_approval_flag(self):
        tool = next(x for x in MODULE.audit()["tools"] if x["tool_id"] == "AI-ASSIST-A")
        self.assertIn("REVIEW_DATA_APPROVAL", tool["review_flags"])

    def test_bad_data_rejected(self):
        r = {"tool_id": "X", "product_family": "test", "paid_seats": "3",
             "active_seats": "4", "monthly_cost_per_seat_usd": "10",
             "sensitive_data_approved": "true", "security_owner_present": "true",
             "months_until_renewal": "8"}
        with self.assertRaises(ValueError):
            MODULE.evaluate(r)

if __name__ == "__main__":
    unittest.main()
