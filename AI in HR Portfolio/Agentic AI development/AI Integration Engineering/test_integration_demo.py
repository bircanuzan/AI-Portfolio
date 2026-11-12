import unittest
from integration_demo import MockAdapter,IntegrationError,signature,valid_webhook
class IntegrationTests(unittest.TestCase):
    def setUp(self):
        self.a=MockAdapter()
        self.p={"category":"policy_question","safe_summary":"Ask HR to clarify leave rule","confirmed":True}
    def test_ok(self):
        self.assertEqual(self.a.submit(self.p,"request-001")["status"],"created")
    def test_confirmation(self):
        with self.assertRaises(IntegrationError): self.a.submit({**self.p,"confirmed":False},"request-002")
    def test_allowlist(self):
        with self.assertRaises(IntegrationError): self.a.submit({**self.p,"category":"payroll_write"},"request-003")
    def test_idempotency(self):
        self.assertEqual(self.a.submit(self.p,"request-004"),self.a.submit(self.p,"request-004"))
    def test_changed_payload_replay(self):
        self.a.submit(self.p,"request-005")
        with self.assertRaises(IntegrationError): self.a.submit({**self.p,"safe_summary":"changed"},"request-005")
    def test_signature(self):
        b=b'{"case_id":"TKT-0001"}'; secret=b"test-secret"
        self.assertTrue(valid_webhook(b,signature(b,secret),secret))
        self.assertFalse(valid_webhook(b+b"x",signature(b,secret),secret))
if __name__=="__main__": unittest.main()
