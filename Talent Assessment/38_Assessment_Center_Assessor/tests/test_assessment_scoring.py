"""Scoring, evidence, calibration and dataset-integrity tests."""
import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from score_assessment import AssessmentDataError, assess, read_csv


class AssessorPracticeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.observations = read_csv("assessor_observations.csv")
        cls.finals = read_csv("adjudicated_ratings.csv")

    def test_expected_evidence_structure(self):
        summary = assess(self.observations, self.finals)
        self.assertEqual(summary["observed_items"], 12)
        self.assertEqual(summary["independent_ratings"], 24)
        self.assertEqual(summary["disagreement_evidence_ids"], ["E06", "E12"])

    def test_calibration_and_overall(self):
        result = assess(self.observations, self.finals)
        self.assertAlmostEqual(result["exact_agreement"], 10/12, places=4)
        self.assertAlmostEqual(result["cohens_kappa"], 0.6923, places=4)
        self.assertEqual(result["descriptive_overall_mean"], 3.17)
        self.assertEqual(result["lowest_scoring_competency"], "decision_making")

    def test_competency_mean(self):
        result = assess(self.observations, self.finals)
        self.assertEqual(result["integrated_competency_scores"]["analytical_thinking"], 3.67)
        self.assertEqual(result["integrated_competency_scores"]["stakeholder_management"], 3.0)
        self.assertEqual(result["integrated_competency_scores"]["decision_making"], 2.67)
        self.assertEqual(result["integrated_competency_scores"]["coaching_development"], 3.33)

    def test_reject_invalid_rating(self):
        bad = copy.deepcopy(self.observations)
        bad[0]["rating"] = "8"
        with self.assertRaises(AssessmentDataError):
            assess(bad, self.finals)

    def test_reject_missing_independent_rating(self):
        with self.assertRaises(AssessmentDataError):
            assess(self.observations[:-1], self.finals)

    def test_reject_duplicate(self):
        with self.assertRaises(AssessmentDataError):
            assess(self.observations + [self.observations[0]], self.finals)

    def test_reject_changed_evidence_metadata(self):
        bad = copy.deepcopy(self.observations)
        bad[1]["competency"] = "decision_making"
        with self.assertRaises(AssessmentDataError):
            assess(bad, self.finals)

    def test_reject_unreviewed_integrated_rating(self):
        incomplete = copy.deepcopy(self.finals)
        incomplete[0]["adjudication_rationale"] = ""
        with self.assertRaises(AssessmentDataError):
            assess(self.observations, incomplete)

    def test_reject_missing_adjudication(self):
        with self.assertRaises(AssessmentDataError):
            assess(self.observations, self.finals[:-1])


if __name__ == "__main__":
    unittest.main()
