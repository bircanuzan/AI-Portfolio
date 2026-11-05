import copy
import sys
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from audit_annotations import audit, rows, DataQualityError

class AnnotationAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = rows("source_requests.csv")
        cls.a = rows("annotations.csv")
        cls.g = rows("adjudicated_gold.csv")

    def test_designed_hold_case(self):
        x = audit(self.s, self.a, self.g)
        self.assertEqual(x["source_items"], 18)
        self.assertEqual(x["annotations"], 36)
        self.assertEqual(x["disagreements"], 5)
        self.assertAlmostEqual(x["observed_agreement"], 13/18, places=4)
        self.assertEqual(x["release_recommendation"], "hold_for_recalibration")
        self.assertEqual(x["annotator_gold_accuracy"]["A"], 1.0)

    def test_bad_label_rejected(self):
        a = copy.deepcopy(self.a)
        a[0]["label"] = "uncategorised"
        with self.assertRaises(DataQualityError): audit(self.s, a, self.g)

    def test_duplicate_rejected(self):
        with self.assertRaises(DataQualityError): audit(self.s, self.a + [self.a[0]], self.g)

    def test_missing_pair_rejected(self):
        with self.assertRaises(DataQualityError): audit(self.s, self.a[:-1], self.g)

    def test_bad_source_rejected(self):
        s = copy.deepcopy(self.s)
        s[0]["case_id"] = s[1]["case_id"]
        with self.assertRaises(DataQualityError): audit(s, self.a, self.g)

    def test_missing_gold_rejected(self):
        with self.assertRaises(DataQualityError): audit(self.s, self.a, self.g[:-1])

if __name__ == "__main__":
    unittest.main()
