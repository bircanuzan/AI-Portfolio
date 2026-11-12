"""Unit and regression tests for evaluator attribution rules."""
import unittest
from triage import classify, run


def case(oracle, grader, environment=True):
    return {"case_id": "X", "oracle_pass": oracle,
            "grader_pass": grader, "environment_ok": environment}


class FailureTriageTests(unittest.TestCase):
    def test_verified_pass(self):
        self.assertEqual(classify(case(True, True)), "verified_pass")

    def test_candidate_failure(self):
        self.assertEqual(classify(case(False, False)), "genuine_candidate_failure")

    def test_grader_false_positive(self):
        self.assertEqual(classify(case(False, True)), "grader_false_positive")

    def test_grader_false_negative(self):
        self.assertEqual(classify(case(True, False)), "grader_false_negative")

    def test_environment_precedence(self):
        self.assertEqual(classify(case(True, True, False)), "environment_invalid")

    def test_nonboolean_rejected(self):
        sample = case(True, True)
        sample["oracle_pass"] = 1
        with self.assertRaises(TypeError):
            classify(sample)

    def test_duplicate_cases_rejected(self):
        cases = [case(True, True), case(False, False)]
        with self.assertRaises(ValueError):
            run(cases)


if __name__ == "__main__":
    unittest.main()
