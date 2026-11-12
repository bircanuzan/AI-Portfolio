import unittest
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from gold_oracle import plan

class PeopleOpsEvalsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows=plan()

    def get(self,dept,month):
        return next(r for r in self.rows if r["department"]==dept and r["month"]==month)

    def test_full_model(self):
        self.assertEqual(len(self.rows),24)

    def test_total_opening_fte(self):
        self.assertEqual(sum(x["opening_fte"] for x in self.rows if x["month"]=="2026-11"),17.5)

    def test_authorization(self):
        self.assertEqual(self.get("Operations","2027-01")["approved_hires"],0.0)

    def test_headcount_reconciles(self):
        for r in self.rows:
            self.assertEqual(r["opening_fte"]+r["approved_hires"]-r["approved_exits"],r["closing_fte"])

    def test_compensation_gold(self):
        nov=self.get("Operations","2026-11")
        self.assertEqual(nov["monthly_base_aed"],74750)
        self.assertEqual(nov["loaded_cost_aed"],91195)
        self.assertEqual(nov["budget_variance_aed"],-6195)

    def test_approved_exit(self):
        self.assertEqual(self.get("Operations","2026-12")["closing_fte"],5.5)

if __name__=="__main__":
    unittest.main()
