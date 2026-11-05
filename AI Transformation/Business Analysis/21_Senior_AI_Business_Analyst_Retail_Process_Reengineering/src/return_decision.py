"""Synthetic retail return decision prototype. Not POS/OMS/WMS integration."""
from dataclasses import dataclass
from decimal import Decimal

@dataclass(frozen=True)
class ReturnRequest:
    receipt_id: str
    item_id: str
    original_price_aed: Decimal
    days_after_purchase: int
    original_promo_code: str
    damaged: bool = False

def evaluate_return(req, already_processed=frozenset(), policy_window_days=30):
    if not req.receipt_id or not req.item_id or req.original_price_aed < 0:
        return {"decision":"hold", "reason":"incomplete_sale_evidence"}
    token=f"{req.receipt_id}:{req.item_id}"
    if token in already_processed:
        return {"decision":"reject", "reason":"duplicate_request"}
    if req.days_after_purchase < 0 or req.days_after_purchase > policy_window_days:
        return {"decision":"review", "reason":"policy_exception"}
    if req.damaged:
        return {"decision":"review", "reason":"condition_exception"}
    return {"decision":"approve", "reason":"eligible_under_fictional_policy",
            "approved_refund_aed":str(req.original_price_aed),
            "pricing_basis":"original_receipt_value_not_current_list_price"}

if __name__=="__main__":
    print(evaluate_return(ReturnRequest("R-104","SKU-55",Decimal("89.50"),5,"PROMO15")))
