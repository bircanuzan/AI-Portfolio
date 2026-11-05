import unittest
from evaluate import grade
class EvalTests(unittest.TestCase):
    def test_pass(self):
        self.assertEqual(grade([{"id":"x","category":"a","expected":"refuse","required":["cannot"]}],[{"id":"x","decision":"refuse","message":"cannot"}])["passed"],1)
    def test_missing_fails(self):
        self.assertEqual(grade([{"id":"x","category":"a","expected":"answer"}],[])["passed"],0)
    def test_forbidden_fails(self):
        self.assertEqual(grade([{"id":"x","category":"a","expected":"refuse","forbidden":["approved"]}],[{"id":"x","decision":"refuse","message":"approved"}])["passed"],0)
if __name__=="__main__":unittest.main()
