import importlib.util
from pathlib import Path
import unittest

PATH = Path(__file__).resolve().parents[1] / "src" / "workforce_capacity.py"
SPEC = importlib.util.spec_from_file_location("workforce_capacity", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

class WorkforceModelTests(unittest.TestCase):
    def setUp(self):
        self.row = {
            "team": "Test", "monthly_cases": "120", "minutes_per_case": "30",
            "current_fte": "1", "paid_hours_per_fte": "160",
            "productive_fraction": "0.75", "eligible_case_share": "0.5",
            "assistance_success_rate": "1", "human_review_minutes_per_eligible_case": "5",
            "variability_buffer": "1.1"
        }

    def test_synthetic_rows_load(self):
        self.assertEqual(len(MODULE.load()), 3)

    def test_human_review_is_counted(self):
        result = MODULE.model(self.row)
        self.assertEqual(result["baseline_hours"], 60)
        self.assertEqual(result["assisted_human_hours"], 35)
        self.assertEqual(result["decision"], "HUMAN_VALIDATION_REQUIRED")

    def test_no_ai_eligibility_means_no_ai_savings(self):
        self.row["eligible_case_share"] = "0"
        result = MODULE.model(self.row)
        self.assertEqual(result["assisted_human_hours"], result["baseline_hours"])

    def test_rejects_impossible_fraction(self):
        self.row["eligible_case_share"] = "1.2"
        with self.assertRaises(ValueError):
            MODULE.model(self.row)

if __name__ == "__main__":
    unittest.main()
