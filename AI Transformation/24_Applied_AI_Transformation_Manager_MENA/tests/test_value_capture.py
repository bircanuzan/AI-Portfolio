import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from value_capture import load_accounts,model
ROOT=Path(__file__).resolve().parents[1]
class ValueTests(unittest.TestCase):
    def test_cohorts(self):
        accounts=load_accounts(ROOT/"data/synthetic_accounts.csv")
        self.assertEqual(len(accounts),3)
        self.assertEqual(sum(x["eligible_engineers"] for x in accounts),3500)
        self.assertEqual(sum(x["activated_engineers"] for x in accounts),1205)
    def test_capacity_formula_and_scope(self):
        a=load_accounts(ROOT/"data/synthetic_accounts.csv")[0]
        report=model(a)
        self.assertAlmostEqual(report["activation_rate"],.4)
        self.assertGreater(report["risk_adjusted_capacity_hours_hypothesis"],0)
        self.assertIn("None",report["realized_savings_claim"])
    def test_bad_cohort(self):
        x=dict(load_accounts(ROOT/"data/synthetic_accounts.csv")[0])
        x["activated_engineers"]=2000
        with self.assertRaises(ValueError):
            model(x)
if __name__=="__main__":unittest.main()
