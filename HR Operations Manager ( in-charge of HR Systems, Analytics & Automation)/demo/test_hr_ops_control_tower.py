"""Unit tests for synthetic payroll control decisions."""
import csv
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from hr_ops_control_tower import audit  # noqa: E402

def read(name):
    with (HERE / name).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

class ControlTests(unittest.TestCase):
    def setUp(self):
        self.employees = read("employees.csv")
        self.payroll = read("payroll_batch.csv")

    def test_fixture_flags_and_hold(self):
        r = audit(self.employees, self.payroll)
        self.assertEqual(r["payroll_rows"], 4)
        self.assertEqual(r["release_gate"], "HOLD_FOR_REVIEW")
        self.assertEqual(r["flags_by_code"]["AMOUNT_VARIANCE"], 1)
        self.assertEqual(r["flags_by_code"]["MISSING_APPROVAL"], 1)
        self.assertEqual(r["flags_by_code"]["EXITED_EMPLOYEE"], 1)
        self.assertEqual(r["flags_by_code"]["EOS_REVIEW_PENDING"], 1)
        self.assertEqual(r["flags_by_code"]["MISSING_BANK_REFERENCE"], 1)
        self.assertEqual(r["flags_by_code"]["WPS_APPLICABILITY_REVIEW"], 1)

    def test_clean_payroll_still_needs_human_review(self):
        r = audit([self.employees[0]], [self.payroll[0]])
        self.assertEqual(r["total_flags"], 0)
        self.assertEqual(r["release_gate"], "HUMAN_REVIEW_REQUIRED")

    def test_duplicate_payroll_is_blocked(self):
        r = audit(self.employees, [self.payroll[0], self.payroll[0]])
        self.assertEqual(r["flags_by_code"]["DUPLICATE_PAYROLL_ROW"], 2)

    def test_duplicate_master_is_blocked(self):
        r = audit([self.employees[0], self.employees[0]], [self.payroll[0]])
        self.assertEqual(r["flags_by_code"]["DUPLICATE_EMPLOYEE_MASTER"], 1)
        self.assertTrue(next(f["is_blocking"] for f in r["flags"] if f["code"] == "DUPLICATE_EMPLOYEE_MASTER"))

    def test_unknown_employee_is_blocked(self):
        p = dict(self.payroll[0], employee_id="NOT-IN-HRMS")
        r = audit(self.employees, [p])
        self.assertEqual(r["flags_by_code"]["UNKNOWN_EMPLOYEE"], 1)

    def test_invalid_amount_is_blocked(self):
        p = dict(self.payroll[0], proposed_net_aed="not-a-number")
        r = audit(self.employees, [p])
        self.assertEqual(r["flags_by_code"]["INVALID_AMOUNT"], 1)

if __name__ == "__main__":
    unittest.main()
