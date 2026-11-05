# 02 — Retail as-is discovery, exceptions and baselines

**Every number below is a fictitious planning assumption, not customer observation.**

## Discovery scope and system hand-offs
| Area | Key as-is process | Potential disconnect | Baseline evidence needed |
|---|---|---|---|
| Merchandising | Seasonal assortment approval | Category-to-ERP item master | Catalog change lead time |
| Supply chain | Supplier PO -> delivery -> DC receipt | ASN not linked to receiving | Dock-to-stock time |
| Inventory | Stock receipt -> cycle count -> availability | POS/WMS stock mismatch | Discrepancy %, shrink |
| Pricing | Price change approval | ERP/POS/ecomm refresh lag | Incorrect-ticket rate |
| Promotions | Promo configuration and redemption | Eligibility mismatch | Promo dispute % |
| POS | Scan -> pay -> receipt | Offline queue and discounts | Transaction failure % |
| Fulfilment | Pick, pack, dispatch | OMS to last-mile scan gaps | On-time dispatch % |
| Returns | Initiate, validate, inspect, refund | Manual finance/CRM handoffs | Minutes/return, exceptions |
| CRM | Customer contact and loyalty | Duplicate profiles | Resolution SLA |
| Finance | Settlement and GL reconciliation | Batch lag and mismatch | Days to close, rework |

## Synthetic baseline (returns automation PoV)
- 1,000 returns/month; 23 minutes manual handling per return.
- 8% require avoidable rework; AED 65/hour loaded operational labour cost.
- Projected future state: 13 minutes/return and 3% avoidable rework.
- One-time illustration cost AED 75,000; monthly operations cost AED 2,000.
- No real retailer interviews were conducted; baseline must be confirmed using observation, workflow logs, store sampling, POS/ERP records and finance validation.

## Gap analysis
AS-IS: inconsistent master data, manual approvals, duplicate entry, hardcoded discount policy, scattered SOPs. TO-BE: canonical approved product/promo identifiers, automated validations, exception-only human review, idempotent refund orchestration, reconciliation and live KPI evidence.

## Risks and assumptions
Refund eligibility differs by category; local consumer protection and tax treatment require legal/finance review; promotions may be time-bound; POS offline periods must not create double refunds; store workers need a manual override and clear reason code.
