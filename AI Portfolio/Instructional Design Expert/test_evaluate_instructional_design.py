"""Run with python -m unittest -v test_evaluate_instructional_design.py"""
import tempfile
import unittest
import json
from pathlib import Path
from evaluate_instructional_design import ROOT, FIELDS, read_cases, score_response, audit


class EvaluationHarnessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases = read_cases(ROOT/"data/evaluation_cases.jsonl")

    def test_cases_and_categories(self):
        self.assertEqual(len(self.cases), 8)
        self.assertEqual(len({c["domain"] for c in self.cases}), 8)

    def test_reference_and_authored_good_answers(self):
        for case in self.cases:
            with self.subTest(case=case["id"]):
                result = score_response(case["reference"], case["good_answer"])
                self.assertTrue(result["schema_valid"])
                self.assertEqual(result["field_accuracy"], 1)

    def test_all_deliberate_errors_detected(self):
        r = audit(self.cases)
        self.assertEqual(r["correct_fixture_passed"], 8)
        self.assertEqual(r["deliberate_errors_detected"], 8)

    def test_boolean_schema_does_not_accept_integer(self):
        a = {f: True for f in FIELDS}
        b = dict(a)
        b["objective_aligned"] = 1
        result = score_response(a, b)
        self.assertFalse(result["schema_valid"])
        self.assertIn("objective_aligned", result["field_errors"])

    def test_unknown_fields_invalid(self):
        a = {f: False for f in FIELDS}
        b = dict(a, unknown_key=False)
        self.assertFalse(score_response(a, b)["schema_valid"])

    def test_duplicate_case_rejected(self):
        duplicate = [dict(self.cases[0]), dict(self.cases[0])]
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)/"dup.jsonl"
            p.write_text("\n".join(json.dumps(x) for x in duplicate), encoding="utf-8")
            with self.assertRaises(ValueError):
                read_cases(p)


if __name__ == "__main__":
    unittest.main()
