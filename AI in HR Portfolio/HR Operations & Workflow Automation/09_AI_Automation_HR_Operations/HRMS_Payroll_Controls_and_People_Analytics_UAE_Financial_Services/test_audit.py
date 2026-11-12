"""Reproducible unittest cases; uses synthetic test fixtures only."""
import csv
import unittest
from pathlib import Path
from audit import audit


class PayrollControlTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with Path(__file__).with_name('sample_hrms_payroll.csv').open(newline='', encoding='utf-8') as h:
            cls.rows = list(csv.DictReader(h))

    def test_expected_sample_flags(self):
        result = audit(self.rows)
        self.assertEqual(result['rows_checked'], 7)
        self.assertEqual(result['unique_employee_ids'], 6)
        self.assertEqual(result['total_control_flags'], 6)

    def test_duplicate_and_eos(self):
        result = audit(self.rows)
        self.assertEqual(result['flags_by_control']['DUPLICATE_EMPLOYEE'], 2)
        self.assertEqual(result['flags_by_control']['EOS_REVIEW_PENDING'], 1)

    def test_clean_row_is_not_flagged(self):
        result = audit([self.rows[0]])
        self.assertEqual(result['total_control_flags'], 0)


if __name__ == '__main__':
    unittest.main()
