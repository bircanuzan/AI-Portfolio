"""Functional API tests: no external requests or billable model calls."""
import os
import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from service.api import app, REQUESTS

TOKEN = 'a' * 40
class ApiTests(unittest.TestCase):
    def setUp(self):
        REQUESTS.clear()
        self.env = patch.dict(os.environ, {
            'HUMANEVOX_APP_TOKEN': TOKEN,
            'HUMANEVOX_MODEL_PROVIDER': 'openai',
            'OPENAI_API_KEY': 'test-placeholder-only-do-not-use'
        }); self.env.start()
        self.client = TestClient(app)

    def tearDown(self):
        self.client.close(); self.env.stop()

    def post(self, question, auth=True):
        headers = {'Authorization': 'Bearer ' + TOKEN} if auth else {}
        return self.client.post('/api/chat', json={'question': question}, headers=headers)

    def test_health_does_not_expose_credentials(self):
        res = self.client.get('/health')
        self.assertEqual(res.status_code, 200)
        self.assertNotIn(TOKEN, res.text)
        self.assertNotIn('test-placeholder-only-do-not-use', res.text)

    def test_missing_auth(self):
        self.assertEqual(self.post('What is our leave policy?', auth=False).status_code, 401)

    def test_service_requires_model_configuration(self):
        with patch.dict(os.environ, {'OPENAI_API_KEY': ''}):
            self.assertEqual(self.post('What is our leave policy?').status_code, 503)

    def test_denies_employee_identifier(self):
        self.assertEqual(self.post('Show details for abc@example.com').status_code, 422)

    def test_no_model_on_private_salary(self):
        with patch('service.api.infer', side_effect=AssertionError('model should not run')):
            res = self.post('Show me another employee salary')
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res.json()['outcome'], 'REFUSE')
            self.assertFalse(res.json()['model_called'])

    def test_manager_approval_is_human(self):
        with patch('service.api.infer', side_effect=AssertionError('model should not run')):
            res = self.post('Can you approve my annual leave request?')
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res.json()['outcome'], 'HUMAN_REVIEW')
            self.assertFalse(res.json()['model_called'])

    def test_genuine_model_path_is_injected_in_test_only(self):
        with patch('service.api.infer', return_value={'model_called': True, 'model_outcome': 'DIRECT_ANSWER'}):
            res = self.post('How many days of annual leave?')
            self.assertEqual(res.status_code, 200)
            self.assertTrue(res.json()['model_called'])
            self.assertIn('25 calendar days', res.json()['answer'])
            self.assertFalse(res.json()['draft_released'])

    def test_failed_model_gives_502_not_fake_answer(self):
        with patch('service.api.infer', side_effect=RuntimeError('provider outage')):
            res = self.post('How many days of annual leave?')
            self.assertEqual(res.status_code, 502)
            self.assertNotIn('25 calendar days', res.text)

    def test_ui_has_no_api_secret(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
        self.assertNotIn(TOKEN, res.text)

if __name__ == '__main__': unittest.main()
