"""Synthetic HRIS unit tests: no external dependencies."""
import csv
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from validate_hcm import validate

class QualityChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with (HERE / "source_employees.csv").open(encoding="utf-8", newline="") as stream:
            cls.rows = list(csv.DictReader(stream))

    def test_fixture_is_held(self):
        x = validate(self.rows)
        self.assertEqual(x["record_count"], 6)
        self.assertEqual(x["release_status"], "HOLD_FOR_HUMAN_REVIEW")
        self.assertGreaterEqual(x["flag_count"], 6)

    def test_duplicate_is_flagged(self):
        self.assertEqual(sum(f["code"] == "DUPLICATE_EMPLOYEE_ENTITY_KEY" for f in validate(self.rows)["flags"]), 2)

    def test_invalid_date_is_flagged(self):
        self.assertTrue(any(f["code"] == "INVALID_EFFECTIVE_DATE" for f in validate(self.rows)["flags"]))

    def test_unapproved_pay_change_is_flagged(self):
        self.assertTrue(any(f["code"] == "UNAPPROVED_PAY_CHANGE" for f in validate(self.rows)["flags"]))

    def test_clean_row_is_still_human_signoff(self):
        x = validate([self.rows[0]])
        self.assertEqual(x["flag_count"], 0)
        self.assertEqual(x["release_status"], "READY_FOR_HUMAN_SIGNOFF")

if __name__ == "__main__":
    unittest.main()
