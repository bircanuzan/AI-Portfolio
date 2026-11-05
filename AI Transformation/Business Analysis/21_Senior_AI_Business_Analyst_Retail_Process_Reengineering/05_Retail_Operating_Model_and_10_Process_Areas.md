# Retail end-to-end process architecture: ten functions

**Independent retail transformation case study.** Fictional 60-store company, no access to live retail data, no real programme savings.

| Process | As-Is handoff / failure | To-Be design | KPI | Business owner |
|---|---|---|---|---|
| Merchandising | Category assortment edits emailed to item-master team | Approved catalog workflow, versioned item attributes | Item master correction rate | Chief Merchandise Officer |
| Supply Chain | Supplier ASN and DC receipt mismatch | Event-based supplier-receipt reconciliation | Dock-to-stock time | Supply Chain Director |
| Inventory | POS/OMS/WMS available quantities disagree | Stock ledger event, nightly reconcile, exception queues | Inventory accuracy % | Head of Inventory |
| Pricing | Manual price spreadsheet imported to POS | Authorised price service and effective-date contracts | Shelf-to-POS mismatch % | Pricing Director |
| Promotions | Promo eligibility differs across channels | Shared promotion decision rules and version ID | Promo disputes/1,000 transactions | Trade Marketing |
| POS | Offline till replay can duplicate transaction | Idempotent receipt event and duplicate prevention | Unreconciled till exceptions | Retail Operations |
| Fulfilment | OMS pick/pack and courier scans delayed | State transition and exception event ownership | On-time fulfilment % | Fulfilment Lead |
| Returns | Manual proof, promo lookup, approval and refund | Verified policy checks, automatic simple cases, manager exception | Return handling time, errors | Store Operations |
| CRM | Customer notifications and loyalty reverse points delayed | Consent-aware case event and status | Complaint resolution time | CX Director |
| Finance | Refund / sales settlements reconciled in batch | Approved journal mapping and unmatched transaction queue | Reconciliation age | Financial Controller |

## Interview and observational discovery
Recruit stakeholder SMEs from business and IT; sample business events with documented consent and access approvals. Log each process trigger, queues, workarounds, exception frequency, rekeying steps, customer complaints, system of record and control owner. Confirm data-quality and actual baseline *before* prioritizing automations.

## BPMN 2.0 / SIPOC / VSM / RACI
- Model customer request, rules validation, gateway, approval, refund, stock update, finance settlement and customer status.
- SIPOC identifies each source/recipient of event information.
- Value Stream Map uses separate touch-time, wait-time and errors.
- RACI defines accountable retail process owner, store manager, IT integration, data owner and security review.

## Lean & Six Sigma
Define (customer pain), Measure (time/error/cost), Analyze (5 Whys, queue causes, hand-offs), Improve (API/rule/approval redesign), Control (monitoring, SOP, ownership). Never count illustrative savings as verified client outcomes.
