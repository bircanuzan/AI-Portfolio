import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from financial_model import calculate, scenarios

ASSUMPTIONS = {
    "horizon_years": 3, "upfront_investment": 300000,
    "annual_gross_benefit_base": 220000, "annual_operating_cost_base": 50000,
    "discount_rate": 0.10, "adoption_factors": [0.75, 1, 1.25],
    "cost_factors": [0.9, 1, 1.2]
}
class TestFinancialModel(unittest.TestCase):
    def test_base_cash_flow(self):
        c=calculate(ASSUMPTIONS)
        self.assertEqual(c["cash_flows"], [-300000,170000,170000,170000])
        self.assertAlmostEqual(c["npv"], -300000+sum(170000/(1.1**t) for t in (1,2,3)), places=2)
        self.assertAlmostEqual(c["simple_payback_years"], 300000/170000, places=3)
    def test_scenario_downside(self):
        self.assertLess(calculate(ASSUMPTIONS,0.75,1.2)["npv"],calculate(ASSUMPTIONS)["npv"])
    def test_sensitivity_count(self):
        self.assertEqual(len(scenarios(ASSUMPTIONS)),9)
    def test_no_positive_net_payback(self):
        self.assertIsNone(calculate(ASSUMPTIONS,0,1)["simple_payback_years"])
    def test_invalid_input(self):
        with self.assertRaises(ValueError): calculate(ASSUMPTIONS, -0.1, 1)
if __name__=="__main__": unittest.main()

