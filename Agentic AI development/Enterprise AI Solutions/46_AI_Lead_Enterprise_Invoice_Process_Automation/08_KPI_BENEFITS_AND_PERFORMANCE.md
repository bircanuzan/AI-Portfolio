# D — Benefit Realisation, Adoption KPI Dashboard and Learning Loop

## Design rules
Only compare **actual post-launch** results with an **approved matched baseline**. Keep process KPIs, AI quality KPIs and cash savings separate. The repository contains **no actual adoption data**.

## KPI dictionary
| KPI | Exact calculation | Frequency | Owner | Proposed target / stop trigger |
|---|---|---|---|---|
| Adoption | unique invoices processed in new workflow ÷ all in-scope invoices | weekly | AP manager | ≥80% by pilot end (assumption) |
| First-pass extraction accepted | fields accepted without correction ÷ fields reviewed | weekly | AP quality | ≥95% high-confidence fields (validate) |
| Route accuracy | human-confirmed correct routes ÷ routes audited | weekly | AP controls | ≥98%; critical cases 100% |
| Exception rate | cases routed to exception queue ÷ received unique invoices | weekly | AP supervisor | segment by entity/reason; no arbitrary reduction target |
| Manual active touch time | sampled active minutes per eligible invoice | monthly | FP&A / AP | measure against 20-min assumed baseline |
| End-to-end cycle p90 | p90 hours from intake to ERP posting | weekly | AP manager | agree after pilot baseline |
| Escalation SLA | SLA-met cases ÷ cases due | weekly | queue owner | ≥95% proposal |
| Critical control bypasses | unauthorized approval/posting/bank-change events | live | Control owner | **zero**; halt on 1 |
| Audit event completeness | cases with required complete event chain ÷ sampled cases | weekly | Risk & audit | 100% for release gate |
| Change readiness | users passing scenario assessment ÷ users in pilot | pre-launch | L&D | 100% before access |
| Champion activation | active champion groups ÷ pilot groups | biweekly | AI Lead | agreed group coverage |
| Realized monetary savings | verified invoices/infrastructure/overtime costs actually avoided | monthly | Finance | Finance-attested only |

## Illustrative dashboard layout (not a populated real dashboard)
```
DIRECTOR OF AI | CROSS-GROUP ENABLEMENT SCORECARD
Reporting period: [to be populated after actual rollout]
Portfolio: 6 proposed | 1 design-priority | 0 production deployments
PROCESS: intake / touch time / p50-p90 cycle / exceptions by entity
CONTROL: duplicate flags / bank-change flags / approval violations / audit completeness
AI QUALITY: field-level accuracy by vendor layout / human correction rate / drift
ADOPTION: active users / routed invoice share / training pass / champion coverage
VALUE: agreed baseline / measured hours released / verified CASH vs CAPACITY
DECISIONS: pause | remediate | scale | retire + accountable owner/date
```

## Benefits measurement plan
1. Lock 8–12 weeks pre-pilot timestamps across comparable supplier groups, invoice values and entities; note seasonality.
2. Run 4–6 week supervised pilot with same definitions, mix and sampling plan; double-check errors manually.
3. Stratify invoices (PO/no-PO; value band; entity; vendor layout; exception). Report denominator explicitly.
4. Calculate observed touch-time delta, actual eligibility, error/rework, human review cost and full vendor/licence/support cost.
5. Distinguish **gross capacity hours** from **net realizable cash**; Finance verifies any claim of staffing or overtime avoidance.
6. Review cohort variation and unintended harm (vendors unable to access portal; late invoices due to false positives).
7. Director of AI monthly stage gate: scale, remediate, pause or withdraw, with evidence links and owner.

### Financial example and audit
Base *hypothetical* capacity value: 4,147.2h/year × AED120/h = AED497,664. Year-one planned cost AED380,000, indicative net capacity value AED117,664. This is an **assumption-driven projection**, not independently verified, cash savings or ROI achieved. See business-case sensitivity.

## Sample weekly reporting narrative template
> “Pilot coverage: [n]/[N] invoices, adoption [x%]. [n] of [N] reviewed routes confirmed correct; [n] control bypasses. Measured touch time [x] vs matched baseline [y] minutes. Of [h] hours potentially released, Finance recognises [AED] verified cost avoidance. Top issues: [1–3]. Decision requested: [pause/remediate/expand].”

## Continuous improvement governance
- Weekly operations review: issue counts, root causes, corrective action dates.
- Biweekly model/document quality review: layout drift, confidence calibration, escalation false positives.
- Monthly benefits board: compare original business case to actual and challenge forecast accuracy.
- Quarterly policy review: delegated limits, retention and vendor bank verification.
- No inference from the **synthetic routing sample** to production accuracy, adoption or financial impact.