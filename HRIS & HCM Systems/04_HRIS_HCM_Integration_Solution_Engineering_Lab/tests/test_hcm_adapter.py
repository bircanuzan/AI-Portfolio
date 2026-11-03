"""Unit tests for synthetic source normalization, NOT tenant validation."""
import importlib.util
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("hcm_adapter", HERE / "src" / "hcm_adapter.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
normalize = mod.normalize

ORACLE = {"source":"ORACLE_FUSION_HCM","event_id":"ORC-TEST","person_number":"SYN-001",
          "action":"HIRE","effective_date":"2026-11-03","legal_entity":"UAE_DEMO_01",
          "approved":True,"version":1}
SAP = {"source":"SAP_SUCCESSFACTORS_EC","event_id":"SAP-TEST","person_id_external":"SYN-002",
       "event":"TRANSFER","effective_start_date":"2026-11-03","company":"UAE_DEMO_02",
       "approved":True,"version":1}

class AdapterTests(unittest.TestCase):
    def test_oracle_and_sap_normalize(self):
        v = normalize([ORACLE, SAP])
        self.assertEqual((v["received"], v["accepted"], v["rejected"]), (2, 2, 0))
        self.assertEqual({x["source_system"] for x in v["accepted_events"]},
                         {"ORACLE_FUSION_HCM", "SAP_SUCCESSFACTORS_EC"})

    def test_duplicates_hold(self):
        v = normalize([ORACLE, ORACLE])
        self.assertEqual(v["accepted"], 1)
        self.assertIn("REPLAY_DETECTED", v["exceptions"][0]["reasons"])

    def test_unapproved_hold(self):
        v = normalize([dict(ORACLE, approved=False)])
        self.assertIn("MISSING_HUMAN_APPROVAL", v["exceptions"][0]["reasons"])

    def test_invalid_date(self):
        v = normalize([dict(SAP, effective_start_date="2026-13-03")])
        self.assertIn("INVALID_EFFECTIVE_DATE", v["exceptions"][0]["reasons"])

    def test_unknown_source(self):
        v = normalize([dict(ORACLE, source="UNKNOWN")])
        self.assertIn("UNKNOWN_SOURCE", v["exceptions"][0]["reasons"])

    def test_invalid_event_and_entity(self):
        v = normalize([dict(ORACLE, action="PAY", legal_entity="BAD")])
        self.assertEqual(set(v["exceptions"][0]["reasons"]),
                         {"UNSUPPORTED_EVENT", "UNKNOWN_LEGAL_ENTITY"})

    def test_bad_version(self):
        v = normalize([dict(ORACLE, version=True)])
        self.assertIn("INVALID_VERSION", v["exceptions"][0]["reasons"])

    def test_sensitive_extra_field_excluded(self):
        v = normalize([dict(ORACLE, bank_account="DO_NOT_COPY")])
        self.assertEqual(v["accepted"], 1)
        self.assertNotIn("bank_account", v["accepted_events"][0])

    def test_non_mapping_record(self):
        v = normalize([None])
        self.assertIn("INVALID_RECORD_TYPE", v["exceptions"][0]["reasons"])

    def test_fixture_totals(self):
        rows = json.loads((HERE / "data" / "synthetic_events.json").read_text())
        v = normalize(rows)
        self.assertEqual(v["received"], v["accepted"] + v["rejected"])
        self.assertEqual(v["release_state"], "HOLD_FOR_REVIEW")
        self.assertEqual((v["accepted"], v["rejected"]), (2, 3))

if __name__ == "__main__":
    unittest.main()
