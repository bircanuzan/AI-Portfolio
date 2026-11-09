import json
import unittest
from pathlib import Path
from src.candidate_agents import CANDIDATES
from src.eval_engine import (classify_exception, run_benchmark, run_case,
                             score_runs, validate_rubric)

ROOT = Path(__file__).resolve().parents[1]


class EvaluationHarnessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases = json.loads((ROOT / "evaluation_cases.json").read_text(encoding="utf-8"))
        cls.rubric = json.loads((ROOT / "rubric.json").read_text(encoding="utf-8"))
        cls.results = {r["candidate"]: r for r in run_benchmark(CANDIDATES, cls.cases, cls.rubric)}

    def test_reference_patch_passes_all_independent_cases(self):
        result = self.results["synthetic-reference-patch"]
        self.assertEqual(result["passed"], len(self.cases))
        self.assertEqual(result["score"], 100.0)

    def test_tax_order_regression_detected(self):
        result = self.results["synthetic-tax-before-discount-patch"]
        failures = {r["case_id"] for r in result["records"] if r["status"] != "pass"}
        self.assertEqual(failures, {"PR101-C02", "PR101-C03"})
        self.assertEqual(result["score"], 75.0)

    def test_rounding_regression_detected(self):
        result = self.results["synthetic-truncation-patch"]
        failures = {r["case_id"] for r in result["records"] if r["status"] != "pass"}
        self.assertEqual(failures, {"PR101-C04"})
        self.assertEqual(result["score"], 90.0)

    def test_mismatch_includes_expected_and_observed(self):
        record = next(r for r in self.results["synthetic-truncation-patch"]["records"]
                      if r["case_id"] == "PR101-C04")
        self.assertEqual(record["failure_type"], "functional-regression")
        self.assertEqual(record["expected"]["tax"], "0.02")
        self.assertEqual(record["observed"]["tax"], "0.01")

    def test_infrastructure_exception_needs_review(self):
        self.assertEqual(classify_exception(TimeoutError("runner failed")), "environment-or-infrastructure")
        self.assertEqual(classify_exception(OSError("filesystem unavailable")), "environment-or-infrastructure")
        self.assertEqual(classify_exception(ValueError("bad user input")), "candidate-runtime-error")

    def test_infrastructure_exception_is_not_scored_as_model_fault(self):
        def fails_environment(*_args):
            raise OSError("sandbox unavailable")
        record = run_case("synthetic-unavailable-runner", fails_environment, self.cases[0])
        self.assertEqual(record["status"], "error")
        self.assertEqual(record["failure_type"], "environment-or-infrastructure")

    def test_rubric_rejects_duplicate_case_ids(self):
        with self.assertRaises(ValueError):
            validate_rubric(self.rubric, self.cases + [self.cases[0]])

    def test_rubric_rejects_invalid_weights(self):
        invalid = dict(self.rubric)
        invalid["category_weights"] = dict(self.rubric["category_weights"])
        invalid["category_weights"]["happy_path"] = 30
        with self.assertRaises(ValueError):
            validate_rubric(invalid, self.cases)

    def test_scores_are_repeatable(self):
        again = {r["candidate"]: r for r in run_benchmark(CANDIDATES, self.cases, self.rubric)}
        self.assertEqual(again, self.results)

    def test_scoring_rejects_missing_category(self):
        with self.assertRaises(ValueError):
            score_runs(self.results["synthetic-reference-patch"]["records"][:1], self.rubric)


if __name__ == "__main__":
    unittest.main()
