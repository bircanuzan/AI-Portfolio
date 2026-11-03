"""Time-aware backtest and scenario constraints on invented aggregate monthly data."""
import sys,unittest
from copy import deepcopy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))
from workforce_scenario_forecast import read_source,validate,backtest,predict_exits,project,report
rows=read_source(ROOT/"data"/"synthetic_monthly_workforce.csv")
class ForecastTests(unittest.TestCase):
    def test_source_has_24_chronological_months(self):
        self.assertTrue(validate(rows))
        self.assertEqual(len(rows),24)
    def test_all_balances_reconcile(self):
        for r in rows:self.assertEqual(r["end_headcount"],r["start_headcount"]+r["hires"]-r["exits"])
    def test_duplicate_or_missing_month_fails(self):
        x=deepcopy(rows);x[5]["month"]=x[4]["month"]
        with self.assertRaises(ValueError):validate(x)
    def test_wrong_opening_balance_fails(self):
        x=deepcopy(rows);x[5]["start_headcount"]+=1
        with self.assertRaises(ValueError):validate(x)
    def test_negative_exits_fail(self):
        x=deepcopy(rows);x[0]["exits"]=-1
        with self.assertRaises(ValueError):validate(x)
    def test_short_training_history_fails(self):
        with self.assertRaises(ValueError):backtest(rows[:8])
    def test_rolling_origin_has_finite_errors(self):
        score=backtest(rows)
        self.assertEqual(len(score),2)
        self.assertTrue(all(s["mae_exits"]>=0 for s in score))
    def test_known_constant_history_forecasts_constant(self):
        self.assertEqual(predict_exits([5,5,5,5],"mean3"),5)
        self.assertEqual(predict_exits([5,5,5,5],"last"),5)
    def test_unknown_method_fails(self):
        with self.assertRaises(ValueError):predict_exits([5,6],"unknown")
    def test_projection_balances(self):
        _,s=project(rows,backtest(rows)[0]["method"])
        for scenario in s:
            for m in scenario["months"]:
                self.assertEqual(m["end_headcount"],m["start_headcount"]+m["planned_hires"]-m["assumed_exits"])
                self.assertGreaterEqual(m["end_headcount"],0)
    def test_retention_scenario_no_worse_than_stress(self):
        _,s=project(rows,backtest(rows)[0]["method"])
        by={x["name"]:x for x in s}
        self.assertGreaterEqual(by["retention_hypothesis"]["final_headcount"],by["stress"]["final_headcount"])
    def test_no_individual_attrition_risk_export(self):
        output=str(report(rows))
        self.assertNotIn("employee_id",output)
        self.assertNotIn("individual_risk",output)
    def test_invalid_scenario_params_rejected(self):
        with self.assertRaises(ValueError):project(rows,"last",capacity_factor=1.2)
    def test_report_is_expressly_synthetic(self):
        x=report(rows)
        self.assertIn("invented",x["disclosure"])
        self.assertTrue(x["distinct_from_200_employee_quarterly_cohort"])
if __name__=="__main__":unittest.main()
