import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from screening_audit import audit, screen

class ScreenAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tests = json.loads((ROOT / "data/paired_synthetic_candidate_tests.json").read_text())["conditions"]

    def test_16_paired_cases(self):
        self.assertEqual(len(self.tests), 16)

    def test_intentional_flaw_is_detected(self):
        result = audit(self.tests)
        self.assertGreater(result["unjustified_flawed_flips"], 0)

    def test_controlled_scorer_invariant_on_non_job_fields(self):
        result = audit(self.tests)
        self.assertEqual(result["unjustified_controlled_flips"], 0)

    def test_valid_work_sample_can_change_decision(self):
        pair = next(c for c in self.tests if c["id"] == "T14")
        self.assertNotEqual(screen(pair["baseline"], True)["decision"],
                            screen(pair["variation"], True)["decision"])

    def test_mandatory_licence_required(self):
        pair = next(c for c in self.tests if c["id"] == "T15")
        self.assertEqual(screen(pair["variation"], True)["decision"], "REVIEW")

if __name__ == "__main__":
    unittest.main()
