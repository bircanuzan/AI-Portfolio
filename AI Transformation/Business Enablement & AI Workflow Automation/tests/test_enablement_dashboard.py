import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from enablement_dashboard import report

def sample(cid="A",status="complete",validated="true",approved="true",before="60",after="30"):
    return dict(campaign_id=cid,status=status,validated=validated,approved=approved,
                minutes_before=before,minutes_after=after)

class EnablementTests(unittest.TestCase):
    def test_basic_kpis(self):
        r=report([sample(),sample("B","pending","false","false","60","60")])
        self.assertEqual(r["completed_count"],1)
        self.assertEqual(r["completion_rate"],0.5)
        self.assertEqual(r["illustrative_completed_time_difference_minutes"],30)
    def test_duplicates(self):
        with self.assertRaises(ValueError):report([sample(),sample()])
    def test_unknown_status(self):
        with self.assertRaises(ValueError):report([sample(status="launched")])
    def test_empty(self):
        with self.assertRaises(ValueError):report([])
if __name__=="__main__":unittest.main()
