import unittest
from decimal import Decimal
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from return_decision import ReturnRequest,evaluate_return

def req(**changes):
    data={"receipt_id":"R-104","item_id":"SKU-55","original_price_aed":Decimal("89.50"),
          "days_after_purchase":5,"original_promo_code":"PROMO15"}
    data.update(changes)
    return ReturnRequest(**data)

class ReturnDecisionTests(unittest.TestCase):
    def test_receipt_amount_not_catalog_price(self):
        x=evaluate_return(req())
        self.assertEqual(x["decision"],"approve")
        self.assertEqual(x["approved_refund_aed"],"89.50")
    def test_double_processing(self):
        self.assertEqual(evaluate_return(req(),already_processed={"R-104:SKU-55"})["reason"],"duplicate_request")
    def test_policy_exception(self):
        self.assertEqual(evaluate_return(req(days_after_purchase=45))["decision"],"review")
    def test_damaged_return(self):
        self.assertEqual(evaluate_return(req(damaged=True))["decision"],"review")
    def test_missing_receipt(self):
        self.assertEqual(evaluate_return(req(receipt_id=""))["decision"],"hold")
if __name__=="__main__":unittest.main()
