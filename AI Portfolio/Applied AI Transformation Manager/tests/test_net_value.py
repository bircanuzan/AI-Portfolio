import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from net_value import load,calculate,parse,report,GATES

class NetValueTests(unittest.TestCase):
    def setUp(self):
        self.r=load()[0]
    def test_three_cohorts_six_scenarios(self):
        self.assertEqual(len(report()["cases"]),6)
    def test_review_rework_and_exception_subtracted(self):
        x=calculate(self.r)
        net=x["baseline_human_hours_hypothesis"]-x["future_human_execution_hours_hypothesis"]-x["review_hours_hypothesis"]-x["rework_hours_hypothesis"]-x["exception_hours_hypothesis"]-x["oversight_hours_hypothesis"]
        self.assertAlmostEqual(x["net_capacity_hours_hypothesis"],net,places=1)
    def test_conservative_lower_net(self):
        self.assertLess(calculate(self.r,"conservative")["net_capacity_hours_hypothesis"],calculate(self.r)["net_capacity_hours_hypothesis"])
    def test_negative_net_capacity_allowed(self):
        r=self.r.copy()
        r.update(task_success_share=0.0,review_minutes_per_attempt=20.0,oversight_hours_month=500.0)
        self.assertLess(calculate(r)["net_capacity_hours_hypothesis"],0)
    def test_failures_require_full_human_task_effort(self):
        r=self.r.copy()
        r["task_success_share"]=0.0
        x=calculate(r)
        self.assertAlmostEqual(x["baseline_human_hours_hypothesis"],x["future_human_execution_hours_hypothesis"],places=1)
    def test_invalid_population_rejected(self):
        data={k:(str(v).lower() if k in GATES else str(v)) for k,v in self.r.items()}
        data["activated_engineers"]=str(self.r["eligible_engineers"]+1)
        with self.assertRaises(ValueError):parse(data)
    def test_invalid_probability_rejected(self):
        data={k:(str(v).lower() if k in GATES else str(v)) for k,v in self.r.items()}
        data["task_success_share"]="1.2"
        with self.assertRaises(ValueError):parse(data)
    def test_unverified_data_blocks_release(self):
        x=calculate(self.r)
        self.assertEqual(x["release_state"],"HOLD_UNVERIFIED_EVIDENCE")
        self.assertIn("baseline_measured",x["missing_evidence"])
    def test_approvals_only_propose_human_review(self):
        r=self.r.copy()
        for k in GATES:r[k]=True
        x=calculate(r)
        self.assertEqual(x["release_state"],"HUMAN_REVIEW_REQUIRED")
        self.assertIsNone(x["actual_roi"])
        self.assertIsNone(x["actual_cash_savings_usd"])
        self.assertFalse(x["headcount_reduction_authorized"])
if __name__=="__main__":unittest.main()
