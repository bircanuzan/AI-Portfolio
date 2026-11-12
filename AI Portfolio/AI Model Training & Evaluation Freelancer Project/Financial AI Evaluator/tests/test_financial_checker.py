import unittest
import importlib.util
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"src"/"financial_checker.py"
spec=importlib.util.spec_from_file_location("finance",p)
f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)
class FinanceTests(unittest.TestCase):
    def test_margin_error(self):
        x=f.check({"id":"a","type":"profit_margin","revenue":100000,
             "net_income":12500,"claimed_margin_percent":14.3})
        self.assertEqual(x["expected_percent"],12.5)
        self.assertFalse(x["claim_matches"])
    def test_balanced(self):
        self.assertTrue(f.check({"id":"a","type":"balance_sheet","assets":100,"liabilities":60,"equity":40})["balanced"])
    def test_partial_receipt(self):
        self.assertEqual(f.check({"id":"a","type":"reconciliation","invoice_amount":15000,
            "bank_receipt_amount":14000,"expected_outstanding":1000})["outstanding"],1000)
    def test_mismatch(self):
        x=f.check({"id":"a","type":"entity_mismatch","invoice_candidate_id":"A","bank_receipt_candidate_id":"B"})
        self.assertFalse(x["ids_match"])
if __name__=="__main__":unittest.main()
