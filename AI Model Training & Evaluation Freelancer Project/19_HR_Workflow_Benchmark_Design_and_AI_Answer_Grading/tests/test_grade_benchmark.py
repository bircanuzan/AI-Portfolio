"""Deterministic unit tests for hypothetical HR task, rubric and ambiguity gates."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from grade_benchmark import UngradeableCase, grade, quality_gate

class BenchmarkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.case = json.loads((ROOT / "data/benchmark_case.json").read_text(encoding="utf-8"))
        cls.samples = json.loads((ROOT / "data/sample_answers.json").read_text(encoding="utf-8"))

    def test_quality_gate_passes_original(self):
        self.assertTrue(quality_gate(self.case))

    def test_gold_calculation_matches_policy(self):
        a = self.case["documents"]["A"]
        b = self.case["documents"]["B"]
        expected = a["monthly_base_aed"] * b["last_worked_day"] / a["proration_denominator"]
        self.assertEqual(expected, 12000)
        self.assertEqual(self.case["documents"]["C"]["draft_base_aed"] - expected, 6000)

    def test_score_examples(self):
        for sample in self.samples:
            with self.subTest(sample=sample["sample_id"]):
                result = grade(self.case, sample["answer"])
                self.assertEqual(result["total"], sample["expected_score"])
                self.assertEqual(result["maximum"], 10)

    def test_missing_policy_not_gradeable(self):
        data = copy.deepcopy(self.case)
        del data["documents"]["A"]
        with self.assertRaises(UngradeableCase):
            quality_gate(data)

    def test_conflicting_exit_dates_not_gradeable(self):
        data = copy.deepcopy(self.case)
        data["documents"]["D"]["last_worked_day"] = 21
        with self.assertRaises(UngradeableCase):
            quality_gate(data)

    def test_missing_allowance_register_not_gradeable(self):
        data = copy.deepcopy(self.case)
        data["documents"]["E"]["allowance_status"] = None
        with self.assertRaises(UngradeableCase):
            quality_gate(data)

    def test_external_legal_inference_not_gradeable(self):
        data = copy.deepcopy(self.case)
        data["requires_external_legal_interpretation"] = True
        with self.assertRaises(UngradeableCase):
            quality_gate(data)

    def test_not_biased_to_output_prose(self):
        answer = copy.deepcopy(self.case["gold_answer"])
        answer["approved_base_aed"] = 99999
        self.assertEqual(grade(self.case, answer)["total"], 8)

if __name__ == "__main__":
    unittest.main()
