import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from evaluate import evaluate, score_one

GOOD={"task_id":"B01", "structure":"4","evidence":"4","quantitative":"4","craft":"4","implementation":"4","governance":"4", "critical_defects":"", "rationale":"Illustrative"}
class TestEvaluate(unittest.TestCase):
    def test_perfect(self):
        self.assertEqual(score_one(GOOD)["final_score"],100)
        self.assertEqual(score_one(GOOD)["status"],"EXEMPLAR_REVIEW")
    def test_critical_cap(self):
        r=score_one({**GOOD,"critical_defects":"material_formula_error"})
        self.assertEqual(r["final_score"],49)
        self.assertEqual(r["status"],"FAIL")
    def test_grade_out_of_bounds(self):
        with self.assertRaises(ValueError):score_one({**GOOD,"structure":"5"})
    def test_unknown_defect(self):
        with self.assertRaises(ValueError):score_one({**GOOD,"critical_defects":"nonsense"})
    def test_unknown_task(self):
        with self.assertRaises(ValueError):evaluate([GOOD],[{"task_id":"B03"}])
    def test_duplicates(self):
        with self.assertRaises(ValueError):evaluate([GOOD,GOOD],[{"task_id":"B01"}])
if __name__=="__main__": unittest.main()

