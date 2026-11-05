"""Local unit tests of synthetic staging controls only."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from validate_changes import validate_event


def valid_event():
    return dict(event_id="EVT-100", worker_id="W-100", event_type="TRANSFER",
                effective_date="2026-11-03", subsidiary="SUB-A", cost_center="CC-100",
                approved_by="HR-MGR-1", finance_reference_valid=True)


class StagingControlTests(unittest.TestCase):
    def test_accept_valid(self):
        self.assertEqual(validate_event(valid_event(), set()), (True, "ACCEPTED_FOR_STAGING_ONLY"))

    def test_missing_hr_approval(self):
        e = valid_event(); e["approved_by"] = ""
        self.assertEqual(validate_event(e)[1], "MISSING_HR_APPROVAL")

    def test_invalid_finance_cost_center(self):
        e = valid_event(); e["cost_center"] = "CC-999"
        self.assertEqual(validate_event(e)[1], "INVALID_FINANCE_COST_CENTER")

    def test_finance_reference_not_approved(self):
        e = valid_event(); e["finance_reference_valid"] = False
        self.assertEqual(validate_event(e)[1], "FINANCE_REFERENCE_NOT_APPROVED")

    def test_duplicate_event(self):
        seen = set()
        self.assertTrue(validate_event(valid_event(), seen)[0])
        self.assertEqual(validate_event(valid_event(), seen)[1], "DUPLICATE_EVENT")

    def test_bad_date(self):
        e = valid_event(); e["effective_date"] = "2026-99-99"
        self.assertEqual(validate_event(e)[1], "INVALID_EFFECTIVE_DATE")

    def test_invalid_event_type(self):
        e = valid_event(); e["event_type"] = "PROMOTION_UNKNOWN"
        self.assertEqual(validate_event(e)[1], "UNSUPPORTED_EVENT")

    def test_unknown_subsidiary(self):
        e = valid_event(); e["subsidiary"] = "SUB-UNKNOWN"
        self.assertEqual(validate_event(e)[1], "UNKNOWN_SUBSIDIARY")

    def test_missing_worker_id(self):
        e = valid_event(); e["worker_id"] = ""
        self.assertEqual(validate_event(e)[1], "MISSING_REQUIRED_FIELD")

    def test_termination_does_not_require_cost_center(self):
        e = valid_event(); e["event_type"] = "TERMINATION"
        del e["cost_center"]
        self.assertTrue(validate_event(e)[0])


if __name__ == "__main__":
    unittest.main()
