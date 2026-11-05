# 04 — Root-Cause Analysis and 30/60/90-Day Improvement Plan
## Synthetic pilot findings
This test intentionally places disagreement in selected cases. The observed errors are *scripted demonstration inputs*, not evidence of actual annotator behavior. Quality release must remain on HOLD until adjudication and rework pass objective gates.

| Priority | Operational problem | Proposed experiment | Accountable | Success measure |
|---|---|---|---|---|
| P0 | Label disagreement above gate | Run a 12-case blinded calibration set; publish boundary examples and class precedence rules | QA lead | Agreement >=90% and kappa improving |
| P0 | Unresolved records threaten model data quality | Human adjudicate all disagreement IDs with reason and version; block export until approved | Ops manager / SME | 100% critical exceptions resolved |
| P1 | Manual source errors | Add schema validation, duplicate-source tests and source lineage register | Data steward | Zero mandatory-field errors |
| P1 | Variable review effort | Route high-risk cases to experienced reviewers and keep unbiased QA sample | Ops manager | Lower median effort without quality regression |
| P2 | Limited operational visibility | Create weekly Power BI/Excel tracker with case states and event timestamps | Analytics lead | Real SLA/aging measured and adopted |
| P2 | Ambiguous cross-team handoffs | Introduce RACI and escalation thresholds with product/ML/privacy teams | Ops manager | Fewer unowned exceptions |

## Delivery cadence
**Days 1–30 — Stabilize:** agree scope, taxonomy, evidence requirements, risk tiers, SLA definitions and staff training. Benchmark baseline with double-review calibration.
**Days 31–60 — Scale deliberately:** implement batch allocation, 100% schema checks, high-risk 100% QA and risk-based sampling, signed handoffs. Use actual event logs before claiming cycle-time gains.
**Days 61–90 — Optimize:** QA trend review, capacity model, cross-functional post-mortem; assess experimentation against baseline and document changes.

## Business recommendation
Do not optimize throughput by weakening annotation gates. Treat **accepted, provenance-linked records per reviewer-hour** as a composite productivity objective, paired with minimum agreement, gold accuracy and privacy control thresholds. A reported gain is valid only when compared to a pre-registered baseline using similar case mix and the same measurement definition.
