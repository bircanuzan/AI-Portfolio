"""Project 11 quality gate tests on fictitious data only."""
import importlib.util
import sys
import unittest
from copy import deepcopy
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))
from trusted_workforce_metrics import read_source,metrics
SYN={
"employee_id":"SYN-000","department":"Demo","location":"Dubai","level":"L1",
"tenure_years":"1.0","performance_rating":"3","learning_hours":"10",
"primary_skill":"AI Literacy","skill_level":"3","internal_move_12m":"0",
"exit_12m":"1","hire_source":"Demo","time_to_fill_days":"20"
}
def fixture(n=12):
    return [dict(SYN,employee_id=f"SYN-{i:03d}") for i in range(n)]

class QualityGateTests(unittest.TestCase):
    def test_full_500_row_snapshot(self):
        m=metrics(read_source(ROOT/"synthetic_hr_data.csv"))
        self.assertEqual(m["kpis"]["workforce_record_count"],500)
        self.assertEqual(sum(r["records"] for r in m["department_metrics"]),500)
    def test_valid_sample(self):
        m=metrics(fixture())
        self.assertEqual(m["kpis"]["exit_flagged_count"],12)
        self.assertEqual(m["department_metrics"][0]["exit_flag_share_pct"],100.0)
    def test_duplicate_key_fails(self):
        x=fixture();x[1]["employee_id"]=x[0]["employee_id"]
        with self.assertRaises(ValueError):metrics(x)
    def test_invalid_exit_flag_fails(self):
        x=fixture();x[0]["exit_12m"]="2"
        with self.assertRaises(ValueError):metrics(x)
    def test_missing_field_fails(self):
        x=fixture();del x[0]["location"]
        with self.assertRaises(ValueError):metrics(x)
    def test_bad_skill_level_fails(self):
        x=fixture();x[0]["skill_level"]="6"
        with self.assertRaises(ValueError):metrics(x)
    def test_non_numeric_tenure_fails(self):
        x=fixture();x[0]["tenure_years"]="oops"
        with self.assertRaises(ValueError):metrics(x)
    def test_small_group_is_suppressed(self):
        x=fixture(9)
        self.assertEqual(metrics(x)["department_metrics"],[])
    def test_empty_source_fails(self):
        with self.assertRaises(ValueError):metrics([])
    def test_row_level_data_is_not_exported(self):
        m=metrics(fixture())
        self.assertNotIn("employee_id",str(m))
    def test_export_has_no_unverified_time_to_fill(self):
        self.assertNotIn("time_to_fill_days",str(metrics(fixture())))

if __name__=="__main__":unittest.main()
