import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from analytics_pipeline import analyse
DATA=Path(__file__).resolve().parents[1]/"data"/"synthetic_esim_orders.csv"

class SyntheticAnalyticsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=analyse(DATA)
    def test_quality_rules(self):
        self.assertEqual(self.data["kpis"]["input_rows"],9)
        self.assertEqual(self.data["kpis"]["accepted_orders"],6)
        self.assertEqual(self.data["kpis"]["quarantined_rows"],3)
    def test_financial_totals(self):
        k=self.data["kpis"]
        self.assertEqual(k["revenue_usd"],"195.00")
        self.assertEqual(k["cost_usd"],"82.00")
        self.assertEqual(k["gross_profit_usd"],"113.00")
        self.assertEqual(k["avg_order_value_usd"],"32.50")
        self.assertAlmostEqual(k["gross_margin_pct"],57.95)
    def test_segment_reconciliation(self):
        from decimal import Decimal
        for rows in self.data["segments"].values():
            self.assertEqual(sum(Decimal(r["revenue_usd"]) for r in rows),Decimal("195.00"))
            self.assertEqual(sum(r["orders"] for r in rows),6)

if __name__=="__main__": unittest.main()
