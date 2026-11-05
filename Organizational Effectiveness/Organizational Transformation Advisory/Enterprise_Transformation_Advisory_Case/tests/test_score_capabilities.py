"""Standard-library tests for the transparent capability triage engine."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from score_capabilities import score_rows, DEFAULT_INPUT
import csv


def record(**overrides):
    base = dict(capability_id="C01", domain="Organization", capability="Decision rights",
                owner="COO", current="2.0", target="4.0", criticality="5",
                impacted_roles="90", sample_size="12", evidence_confidence="medium")
    base.update(overrides)
    return base


class CapabilityScoringTests(unittest.TestCase):
    def test_computes_priority_and_band(self):
        x = score_rows([record()])[0]
        self.assertEqual(x["gap"], "2.00")
        self.assertEqual(x["priority_score"], "10.00")
        self.assertEqual(x["priority_band"], "HIGH")
        self.assertEqual(x["evidence_gate"], "SCREENED")

    def test_low_confidence_or_weak_sample_requires_revalidation(self):
        self.assertEqual(score_rows([record(evidence_confidence="low")])[0]["evidence_gate"], "REVALIDATE")
        self.assertEqual(score_rows([record(sample_size="9")])[0]["evidence_gate"], "REVALIDATE")

    def test_rejects_out_of_range_and_duplicate_ids(self):
        with self.assertRaises(ValueError):
            score_rows([record(current="5.5")])
        with self.assertRaises(ValueError):
            score_rows([record(), record()])
        with self.assertRaises(ValueError):
            score_rows([record(evidence_confidence="uncertain")])

    def test_prioritizes_higher_gap_before_population(self):
        rows = [record(capability_id="C01", current="3", impacted_roles="600"),
                record(capability_id="C02", current="1", impacted_roles="20")]
        self.assertEqual([r["capability_id"] for r in score_rows(rows)], ["C02", "C01"])

    def test_bundled_fixture_is_valid(self):
        with DEFAULT_INPUT.open(newline="", encoding="utf-8") as stream:
            ranked = score_rows(list(csv.DictReader(stream)))
        self.assertEqual(len(ranked), 8)
        self.assertEqual(ranked[0]["capability_id"], "C06")


if __name__ == "__main__":
    unittest.main()
