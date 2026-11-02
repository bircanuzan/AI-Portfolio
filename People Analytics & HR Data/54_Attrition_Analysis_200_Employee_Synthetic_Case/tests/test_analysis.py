import sys
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE / "src"))
from analyze_attrition import analyse, read_csv

class AttritionTests(unittest.TestCase):
    def test_200_distinct_synthetic_employees(self):
        rows = read_csv(BASE / "data" / "synthetic_employee_cohort.csv")
        self.assertEqual(len(rows), 200)
        self.assertEqual(len({r["employee_id"] for r in rows}), 200)
        self.assertTrue(all(r["cohort"] == "2026-Q3" for r in rows))

    def test_group_numerators_reconcile(self):
        result = analyse(read_csv(BASE / "data" / "synthetic_employee_cohort.csv"))
        self.assertEqual(sum(x["employees"] for x in result["department_breakdown"]), 200)
        self.assertEqual(sum(x["exits"] for x in result["department_breakdown"]), result["exits"])
        self.assertEqual(result["exit_rate_pct"], round(result["exits"] / 200 * 100, 1))

    def test_invalid_departure_is_rejected(self):
        row = dict(read_csv(BASE / "data" / "synthetic_employee_cohort.csv")[0])
        row["exited"] = "?"
        with self.assertRaises(ValueError):
            analyse([row])

    def test_duplicate_employee_is_rejected(self):
        row = read_csv(BASE / "data" / "synthetic_employee_cohort.csv")[0]
        with self.assertRaises(ValueError):
            analyse([row, row])

if __name__ == "__main__":
    unittest.main()
