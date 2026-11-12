"""Offline tests of host-side protections; no actual model or API calls."""
import sys
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from live_llm_agent import ModelReply, policy_search, privacy_preflight, validate_model_reply, run_live

class LiveSafetyEnvelopeTests(unittest.TestCase):
    def test_remote_policy_retrieval(self):
        self.assertEqual(policy_search("remote work two days")[0]["policy_id"], "HR-FLEX-02")

    def test_unknown_policy_returns_no_sources(self):
        self.assertEqual(policy_search("employee parking permits"), [])

    def test_sensitive_request_blocked_pre_model(self):
        d = privacy_preflight("Export private employee medical records")
        self.assertEqual(d.outcome, "REFUSE")
        self.assertFalse(d.model_called)

    def test_host_rejects_unretrieved_source(self):
        reply = ModelReply("DIRECT_ANSWER", "Everyone receives 400 days!", ["HR-LEAVE-01"])
        d = validate_model_reply("How many annual leave days?", reply, set(), ["mock_model_output"])
        self.assertEqual(d.outcome, "INSUFFICIENT_INFO")

    def test_host_enforces_human_review(self):
        reply = ModelReply("DIRECT_ANSWER", "I approve three remote days.", ["HR-FLEX-02"])
        d = validate_model_reply("Can I work remotely three days?", reply, {"HR-FLEX-02"}, [])
        self.assertEqual(d.outcome, "HUMAN_REVIEW")
        self.assertEqual(d.escalation_team, "HR Business Partner")

    def test_verified_source_is_attached(self):
        reply = ModelReply("DIRECT_ANSWER", "25 calendar days annually.", ["HR-LEAVE-01"])
        d = validate_model_reply("How many days of annual leave?", reply, {"HR-LEAVE-01"}, [])
        self.assertEqual(d.outcome, "DIRECT_ANSWER")
        self.assertIn("Verified source: HR-LEAVE-01", d.answer)

    @patch.dict("os.environ", {"OPENAI_API_KEY": ""})
    def test_missing_api_key_is_explicit(self):
        with self.assertRaisesRegex(RuntimeError, "OPENAI_API_KEY is not configured"):
            run_live("What is the annual leave policy?")

if __name__ == "__main__":
    unittest.main()
