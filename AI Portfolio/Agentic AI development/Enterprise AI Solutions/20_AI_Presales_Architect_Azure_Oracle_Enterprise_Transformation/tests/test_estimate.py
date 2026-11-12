import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from estimate import estimate
class EstimateTests(unittest.TestCase):
    def test_total_math(self):
        x=estimate({"architect":(2,1000)},0.15)
        self.assertEqual(x["total_aed"],2300)
    def test_reject_invalid(self):
        with self.assertRaises(ValueError): estimate({"x":(-1,1000)})
    def test_zero(self):
        self.assertEqual(estimate({"x":(0,10)},0)["total_aed"],0)
if __name__=="__main__":unittest.main()
