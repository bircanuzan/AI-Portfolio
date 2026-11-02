"""Unit tests for simulated source, citation and release-gate logic."""
import importlib.util
from pathlib import Path
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "src" / "assurance_dashboard.py"
SPEC = importlib.util.spec_from_file_location("assurance_dashboard", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class AssuranceTests(unittest.TestCase):
    def test_fixture_count(self):
        tests, summary = MODULE.evaluate()
        self.assertEqual(len(tests), 6)
        self.assertEqual(summary["total"], 6)

    def test_policy_drift_detected(self):
        tests, _ = MODULE.evaluate()
        stale = next(x for x in tests if x["id"] == "T-001")
        self.assertFalse(stale["fresh"])
        self.assertFalse(stale["pass"])

    def test_correct_answer_without_citation_fails(self):
        tests, _ = MODULE.evaluate()
        missing_evidence = next(x for x in tests if x["id"] == "T-002")
        self.assertTrue(missing_evidence["answer"])
        self.assertFalse(missing_evidence["evidence"])
        self.assertFalse(missing_evidence["pass"])

    def test_release_gate_holds_critical_exceptions(self):
        _, summary = MODULE.evaluate()
        self.assertEqual(summary["critical_failures"], 2)
        self.assertEqual(summary["decision"], "HOLD")

    def test_expected_metrics(self):
        _, summary = MODULE.evaluate()
        self.assertEqual(summary["fresh"], 5)
        self.assertEqual(summary["evidence"], 3)
        self.assertEqual(summary["citation_present"], 4)
        self.assertEqual(summary["correct"], 4)
        self.assertEqual(summary["passed"], 3)


if __name__ == "__main__":
    unittest.main()
