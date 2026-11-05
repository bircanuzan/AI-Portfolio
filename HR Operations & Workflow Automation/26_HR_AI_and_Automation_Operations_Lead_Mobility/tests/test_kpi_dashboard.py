import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))
from kpi_dashboard import summarize

class KPIValidation(unittest.TestCase):
    def test_case_metrics(self):
        s=summarize()
        self.assertEqual(s["cases"],6)
        self.assertEqual(s["sla_attainment"],4/6)
        self.assertEqual(s["human_review_rate"],3/6)
        self.assertEqual(s["median_cycle_hours"],25.5)

if __name__=="__main__":unittest.main()
