import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from people_kpis import load_rows, calculate, ratio
ROOT=Path(__file__).resolve().parents[1]

class KPITests(unittest.TestCase):
    def test_reconciliation_and_coverage(self):
        rows=load_rows(ROOT/"data/synthetic_workforce.csv")
        self.assertEqual(len(rows),4)
        self.assertAlmostEqual(calculate(rows[0])["attrition_rate"],5/102.5)
        self.assertAlmostEqual(calculate(rows[0])["learning_reach"],70/105)
    def test_zero_denominator(self):
        self.assertEqual(ratio(0,0),0)
    def test_vacancy_proxy(self):
        row=load_rows(ROOT/"data/synthetic_workforce.csv")[0]
        self.assertAlmostEqual(calculate(row)["vacancy_pressure_proxy"],9/114)
if __name__=="__main__":
    unittest.main()
