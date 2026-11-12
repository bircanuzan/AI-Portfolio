"""Independent assertions for PR-202 fixture and regression quality."""
import unittest
from benchmark import run, CASES
from config_parser import parse_config


class ParserTests(unittest.TestCase):
    def test_embedded_equals_preserved(self):
        self.assertEqual(parse_config("TOKEN=a=b=c"), {"TOKEN": "a=b=c"})

    def test_whole_line_comments(self):
        self.assertEqual(parse_config("# ignored\n\nFLAG=true"), {"FLAG": "true"})

    def test_duplicate_rejected(self):
        with self.assertRaises(ValueError):
            parse_config("A=1\nA=2")

    def test_invalid_key_rejected(self):
        with self.assertRaises(ValueError):
            parse_config("bad-key=1")

    def test_invalid_type_rejected(self):
        with self.assertRaises(TypeError):
            parse_config(None)

    def test_benchmark_reference_and_mutants(self):
        found = {r["candidate"]: r for r in run()["results"]}
        self.assertEqual(found["reference"]["passed"], len(CASES))
        self.assertLess(found["duplicate-key-defect"]["passed"], len(CASES))
        self.assertLess(found["value-truncation-defect"]["passed"], len(CASES))
        self.assertIn("B05", {f["case_id"] for f in found["duplicate-key-defect"]["failures"]})
        self.assertIn("B08", {f["case_id"] for f in found["value-truncation-defect"]["failures"]})


if __name__ == "__main__":
    unittest.main()
