"""Integration-contract tests use a fake HTTPS response, not a live HR system."""
import json
import os
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from src.hcia.integrations import validate_snapshot,read_aggregate_snapshot,IntegrationError

class FakeResponse:
    def __init__(self,doc):
        self.doc=doc
    def __enter__(self):
        return self
    def __exit__(self,*args):
        return False
    def read(self,count):
        return json.dumps(self.doc).encode()

class TestExternalContracts(unittest.TestCase):
    def setUp(self):
        self.snapshot={"schema_version":"1","source_system":"synthetic ATS",
                       "entity_id":"CORP","period":"2026-Q3","aggregates":{"applicants":100,"hires":6}}

    def test_good_aggregate_contract(self):
        self.assertEqual(validate_snapshot(self.snapshot),self.snapshot)

    def test_personal_fields_rejected(self):
        record={**self.snapshot,"aggregates":{"employee_id":"E123","hires":7}}
        with self.assertRaises(IntegrationError):
            validate_snapshot(record)

    def test_list_rows_rejected(self):
        record={**self.snapshot,"aggregates":{"person_rows":[{"id":"1"}]}}
        with self.assertRaises(IntegrationError):
            validate_snapshot(record)

    def test_unapproved_source_rejected(self):
        with self.assertRaises(IntegrationError):
            read_aggregate_snapshot("random_http")

    def test_misconfigured_endpoint_denied(self):
        with patch.dict(os.environ,{"HCIA_ATS_URL":"http://unsafe.test/metrics",
                                    "HCIA_ATS_TOKEN":"token",
                                    "HCIA_INTEGRATION_HOST_ALLOWLIST":"unsafe.test"}):
            with self.assertRaises(IntegrationError):
                read_aggregate_snapshot("ats")

    def test_fake_https_adapter_read(self):
        def fake_open(request,timeout):
            self.assertEqual(request.full_url,"https://tenant.example/api/metrics")
            self.assertEqual(timeout,8)
            self.assertTrue(request.get_header("Authorization").startswith("Bearer "))
            return FakeResponse(self.snapshot)
        with patch.dict(os.environ,{"HCIA_ATS_URL":"https://tenant.example/api/metrics",
                                    "HCIA_ATS_TOKEN":"test-token",
                                    "HCIA_INTEGRATION_HOST_ALLOWLIST":"tenant.example"}):
            out=read_aggregate_snapshot("ats",opener=fake_open)
        self.assertEqual(out["aggregates"]["hires"],6)

if __name__=="__main__":
    unittest.main()
