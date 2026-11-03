"""CHRO and CAIO scenario model: negative-control economics and no fabricated savings."""
import json,sys,unittest
from copy import deepcopy
from pathlib import Path
HERE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(HERE/"src"))
from executive_value_options import evaluate
CASE=json.loads((HERE/"data/synthetic_executive_options.json").read_text())
class ExecutiveInvestmentTests(unittest.TestCase):
    def test_three_distinct_options(self):
        output=evaluate(CASE)
        self.assertEqual(len(output["options"]),3)
    def test_baseline_has_zero_cost_and_zero_capacity(self):
        o=evaluate(CASE)["options"][0]
        self.assertEqual(o["net_capacity_change_hours"],0)
        self.assertEqual(o["first_year_capacity_value_less_costs_aed"],0)
    def test_manual_oversight_is_subtracted(self):
        o=evaluate(CASE)["options"][1]
        self.assertLess(o["net_capacity_change_hours"],o["gross_time_freed_hours"])
    def test_ai_option_not_automatically_best(self):
        o=evaluate(CASE)["options"]
        self.assertLess(o[2]["first_year_capacity_value_less_costs_aed"],o[1]["first_year_capacity_value_less_costs_aed"])
    def test_no_cash_saving_assumption(self):
        self.assertTrue(all(o["actual_cash_savings_aed"] is None for o in evaluate(CASE)["options"]))
    def test_all_options_hold_funding(self):
        self.assertTrue(all(o["production_funding_approved"] is False for o in evaluate(CASE)["options"]))
    def test_disallows_unknown_provenance(self):
        c=deepcopy(CASE);c["classification"]="CLIENT_IMPLEMENTED"
        with self.assertRaises(ValueError):evaluate(c)
    def test_disallows_adoption_beyond_one(self):
        c=deepcopy(CASE);c["options"][2]["eligible_adoption_fraction"]=1.3
        with self.assertRaises(ValueError):evaluate(c)
    def test_rejects_duplicate_option(self):
        c=deepcopy(CASE);c["options"][1]["id"]="baseline"
        with self.assertRaises(ValueError):evaluate(c)
    def test_disallows_negative_cost(self):
        c=deepcopy(CASE);c["options"][0]["annual_license_cost_aed"]=-1000
        with self.assertRaises(ValueError):evaluate(c)
    def test_rejects_boolean_numeric(self):
        c=deepcopy(CASE);c["minutes_per_requisition_baseline"]=True
        with self.assertRaises(ValueError):evaluate(c)
    def test_no_auto_ai_release(self):
        self.assertEqual(evaluate(CASE)["vendor_or_ai_release"],"HOLD")
if __name__=="__main__":unittest.main()
