"""TA capacity arithmetic validation, fictional requisitions only."""
import sys,unittest
from pathlib import Path
from copy import deepcopy
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))
from recruitment_capacity import read,evaluate
SOURCE=ROOT/"data"/"synthetic_recruitment_capacity.csv"
class CapacityTests(unittest.TestCase):
    def test_six_requisitions(self):
        self.assertEqual(evaluate(read(SOURCE))["requisitions"],6)
    def test_no_hiring_decision(self):
        x=evaluate(read(SOURCE))
        self.assertFalse(x["automated_hiring"])
        self.assertTrue(all(not r["candidate_quality_or_hire_prediction"] for r in x["records"]))
    def test_gap_math(self):
        for r in evaluate(read(SOURCE))["records"]:
            self.assertEqual(r["review_hour_gap"],round(max(0,r["review_workload_hours"]-r["available_hours"]),2))
    def test_some_bottlenecks_found(self):
        self.assertGreater(evaluate(read(SOURCE))["review_capacity_gap_hours"],0)
    def test_duplicate_id_fails(self):
        x=read(SOURCE);x.append(deepcopy(x[0]))
        with self.assertRaises(ValueError):evaluate(x)
    def test_bad_negative_queue(self):
        x=read(SOURCE);x[0]["fictional_review_queue"]="-1"
        with self.assertRaises(ValueError):evaluate(x)
    def test_bad_fractional_demand(self):
        x=read(SOURCE);x[0]["hiring_demand"]="1.5"
        with self.assertRaises(ValueError):evaluate(x)
    def test_missing_market(self):
        x=read(SOURCE);del x[0]["market"]
        with self.assertRaises(ValueError):evaluate(x)
    def test_unbounded_review_time(self):
        x=read(SOURCE);x[0]["review_hours_per_profile"]="100"
        with self.assertRaises(ValueError):evaluate(x)
    def test_empty_source_fails(self):
        with self.assertRaises(ValueError):evaluate([])
if __name__=="__main__":unittest.main()
