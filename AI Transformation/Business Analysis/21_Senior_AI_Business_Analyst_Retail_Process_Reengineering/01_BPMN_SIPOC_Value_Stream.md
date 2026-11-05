# 01 — BPMN 2.0, SIPOC and Value Stream Mapping

## SIPOC: retail returns-to-refund
| Supplier | Input | Process | Output | Customer |
|---|---|---|---|---|
| Shopper / POS / OMS | Receipt, line items, identity, payment | Accept and verify return | Validated return case | Store operations, shopper |
| WMS / inventory | Stock receipt and condition | Inspect and restock/quarantine | Inventory movement | Supply chain / planning |
| Pricing/promotion service | Effective promotional rule | Reconcile eligible refund | Authorized refund amount | Finance, customer |
| CRM and ERP | Account and accounting codes | Update records, reconcile settlement | CRM status and GL entry | Finance, customer service |

## AS-IS pain (interviews + observation required in real client)
Manual operator searches three screens; price override may be used when promotion data differ; paperwork goes to finance; stock updated hours after return; refund exceptions routed ad hoc; CRM often not updated.

## VALUE STREAM MAP — invented example
| Stage | Process time | Waiting time | Problem |
|---|---:|---:|---|
| Validate order in POS | 4 min | 1 min | Missing OMS mapping |
| Verify promo/refund eligibility | 5 min | 12 min | Manual price check |
| Accept return & inventory movement | 6 min | 18 min | WMS batch delay |
| Refund approval & ERP reconciliation | 8 min | 45 min | Missing approval trail |
| **TOTAL** | **23 min** | **76 min** | **99 min lead time** |

Process cycle efficiency (PCE) = 23 / 99 = **23.2%** synthetic. Do **not** claim observed baseline.

## To-be BPMN logic (process model included)
Start return -> lookup original sale -> [eligible?] -> validate policy -> [price or identity exception?] -> manual review OR approved refund -> update POS and stock -> post finance -> CRM notice -> monitor mismatches. Error paths must hold transaction, prevent duplicate refunds, and escalate.

## Lean waste / root causes
Waiting (manual approval queue); defects (wrong promo price), motion (system switching), overprocessing (duplicate reconciliation), inventory (incorrect stock count). Use 5 Whys with store/finance SMEs and validate causal claims with samples.

## Six Sigma DMAIC
**Define** return exceptions, **Measure** baseline, **Analyze** promo and integration causes, **Improve** automated validation, **Control** with exception dashboard and process owner signoff.

## Model
[Open editable BPMN 2.0 XML](bpmn/retail_returns_as_is.bpmn). This is a demonstration process model, not a validated production integration.
