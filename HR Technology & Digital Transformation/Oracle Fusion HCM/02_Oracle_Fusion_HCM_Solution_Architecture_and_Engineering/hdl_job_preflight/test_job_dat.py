"""Offline HDL formatting tests (not a tenant test)."""
import sys,unittest
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from check_job_dat import check
src=(HERE/"Job.dat").read_text()
class HDLTests(unittest.TestCase):
    def assert_bad(self,x,reason):
        r=check(x)
        self.assertFalse(r["structure_pass"])
        self.assertTrue(any(reason in e for e in r["errors"]),r["errors"])
    def test_valid_synthetic_job_dat(self):
        r=check(src)
        self.assertTrue(r["structure_pass"],r["errors"])
        self.assertEqual(r["checked"],2)
        self.assertFalse(r["oracle_import_performed"])
    def test_merge_before_metadata(self):
        self.assert_bad(src.splitlines()[1],"METADATA_FIRST")
    def test_bad_date(self):
        self.assert_bad(src.replace("2026/11/03","2026/99/03"),"INVALID_DATE")
    def test_duplicate_source_key(self):
        self.assert_bad(src+src.splitlines()[1]+"\n","DUPLICATE_SOURCE_KEY")
    def test_duplicate_metadata(self):
        self.assert_bad(src.splitlines()[0]+"\n"+src,"DUPLICATE_METADATA")
    def test_missing_key_column(self):
        self.assert_bad(src.replace("|SourceSystemId","",1),"MISSING_FIELDS")
    def test_bad_record_width(self):
        self.assert_bad(src.replace("|Synthetic HR Analyst","",1),"FIELD_COUNT")
    def test_wrong_discriminator(self):
        self.assert_bad(src.replace("MERGE|Job|","MERGE|Worker|",1),"NOT_JOB")
    def test_short_row(self):
        self.assert_bad(src+"MERGE|Job\n","SHORT_LINE")
    def test_blank_required(self):
        self.assert_bad(src.replace("SYN-JOB-001","",1),"BLANK_REQUIRED")
if __name__=="__main__":unittest.main()
