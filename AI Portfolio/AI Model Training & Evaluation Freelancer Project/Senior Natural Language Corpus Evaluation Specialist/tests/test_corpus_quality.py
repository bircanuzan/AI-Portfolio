import unittest
import importlib.util
from pathlib import Path
path=Path(__file__).resolve().parents[1]/"src"/"corpus_quality.py"
spec=importlib.util.spec_from_file_location("corpus",path)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class CorpusTests(unittest.TestCase):
    def test_unicode_duplicate(self):
        def r(id,text):return dict(id=id,text=text,language="en",domain="test",source="synthetic",annotation_a="A",annotation_b="A")
        result=m.audit([r("1","Café test"),r("2","Cafe\u0301   test")])
        self.assertEqual(result["duplicate_ids"],["2"])
    def test_agreement(self):
        self.assertEqual(m.kappa(["A","B"],["A","B"]),1.0)
    def test_empty(self):
        r=dict(id="x",text="",language="en",domain="test",source="synthetic",annotation_a="A",annotation_b="A")
        self.assertIn("x",m.audit([r])["empty_text_ids"])
if __name__=="__main__":unittest.main()
