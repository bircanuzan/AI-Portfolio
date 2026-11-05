import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from tts_preview import prepare_request, preview

class TTSPreviewTests(unittest.TestCase):
    def test_endpoint_and_payload(self):
        spec = prepare_request("Hello learners", "approved123")
        self.assertEqual(spec["body"]["text"], "Hello learners")
        self.assertIn("/v1/text-to-speech/approved123", spec["url"])

    def test_preview_no_network(self):
        result = preview("Safety first", "approved123")
        self.assertFalse(result["billable_request_sent"])
        self.assertEqual(result["characters"], 12)

    def test_rejects_empty_text(self):
        with self.assertRaises(ValueError):
            prepare_request("", "approved123")

    def test_rejects_invalid_voice_id(self):
        with self.assertRaises(ValueError):
            prepare_request("Hello", "a/b")

if __name__ == "__main__":
    unittest.main()
