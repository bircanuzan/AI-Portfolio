"""Stdlib unit tests for role inventory quality controls."""
import importlib.util
from pathlib import Path
import unittest

SOURCE=Path(__file__).resolve().parents[1]/"src"/"validate_roles.py"
spec=importlib.util.spec_from_file_location("validate_roles", SOURCE)
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class RoleInventoryTests(unittest.TestCase):
    def row(self, **kwargs):
        r={"position_id":"P001","market":"Market A","business_unit":"Ground Operations",
           "current_title":"Station Operations Manager","manager_position_id":"",
           "job_family":"Ground Operations","job_subfamily":"Station Operations",
           "track_level":"M1","global_job_code":"OPS-STATION-M1",
           "local_grade":"A-G6","role_profile_version":"1.0","review_status":"pending_calibration"}
        r.update(kwargs)
        return r

    def test_valid_row(self):
        self.assertEqual(module.validate([self.row()]),[])

    def test_duplicate_position(self):
        codes=[f["code"] for f in module.validate([self.row(), self.row()])]
        self.assertIn("duplicate_position",codes)

    def test_bad_family_relation(self):
        codes=[f["code"] for f in module.validate([self.row(job_subfamily="Data Analytics")])]
        self.assertIn("invalid_family_subfamily",codes)

    def test_bad_level(self):
        codes=[f["code"] for f in module.validate([self.row(track_level="CEO")])]
        self.assertIn("invalid_track_level",codes)

    def test_missing_reporting_reference(self):
        codes=[f["code"] for f in module.validate([self.row(manager_position_id="P404")])]
        self.assertIn("missing_manager_position",codes)

    def test_no_grade_means_incomplete_data(self):
        issues=module.validate([self.row(local_grade="")])
        self.assertTrue(any(x["code"]=="missing_required" for x in issues))

if __name__=="__main__":
    unittest.main()
