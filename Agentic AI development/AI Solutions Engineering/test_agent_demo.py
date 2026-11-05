import unittest
from agent_demo import respond
class SolutionsTests(unittest.TestCase):
    def test_grounded_answer(self):
        self.assertEqual(respond("annual leave route")["source_policy"],"HR-LEAVE-01")
    def test_no_approval(self):
        self.assertEqual(respond("approve leave")["decision"],"escalate")
    def test_privacy(self):
        self.assertEqual(respond("colleague salary")["decision"],"refuse")
    def test_no_silent_ticket(self):
        self.assertNotEqual(respond("unknown")["decision"],"draft")
        self.assertEqual(respond("unknown",confirmed=True)["decision"],"draft")
if __name__=="__main__": unittest.main()
