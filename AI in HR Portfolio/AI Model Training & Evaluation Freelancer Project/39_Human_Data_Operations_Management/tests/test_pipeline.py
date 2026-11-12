import sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))
from pipeline import audit, cohen_kappa, rows, validate

class DataOpsTests(unittest.TestCase):
    def setUp(self):
        self.cases=rows(ROOT/"data"/"cases.csv")
        self.reviews=rows(ROOT/"data"/"reviews.csv")
    def test_48_unique_complete_cases(self):
        self.assertEqual(len(self.cases),48)
        self.assertFalse(validate(self.cases,self.reviews))
    def test_dataset_quality_hold(self):
        result=audit(self.cases,self.reviews)
        self.assertEqual(result["decision"],"HOLD")
        self.assertGreater(len(result["adjudication_queue"]),0)
    def test_perfect_kappa(self):
        self.assertEqual(cohen_kappa(["payroll","mobility"],["payroll","mobility"]),1.0)
    def test_duplicate_rejected(self):
        self.assertTrue(any("duplicate" in x for x in validate(self.cases+[self.cases[0]],self.reviews)))
    def test_unmatched_review_rejected(self):
        self.assertTrue(any("Unmatched" in x for x in validate(self.cases,self.reviews[:-1])))
    def test_invalid_label_rejected(self):
        bad=[dict(x) for x in self.reviews]
        bad[0]["annotator_b"]="unknown"
        self.assertTrue(any("invalid" in x for x in validate(self.cases,bad)))
if __name__=="__main__": unittest.main()
