# D — Benefits, KPI Design, Governance and Executive Reporting

## KPI dictionary (planned definitions)
| KPI | Formula | Source / cadence | Guardrail |
|---|---|---|---|
| Eligible-case adoption | cases processed in controlled workflow / all eligible cases | Case event log + intake register; weekly | Exclude noneligible cases consistently |
| Handling time | total active administrative minutes / completed cases | Time study/sample; baseline then monthly | **Not** queue elapsed time |
| Rework rate | cases needing corrections at least once / all submitted cases | Case state history; weekly | Define repeat submission and sampling |
| First-pass completeness | packs accepted without deficiency / all first submissions | Intake events; weekly | Avoid redefining the denominator |
| Review queue age | median and P90 business-hours awaiting assigned owner | Event timestamps; daily | Track owners, holidays and escalation paths |
| Critical route errors | confirmed unauthorized or misrouted decisions / evaluated decisions | QA/incident log; daily and monthly | Zero tolerance for unauthorized approval |
| Business-owner override rate | manually changed routing recommendations / recommendations made | Audited override events; weekly | Review justifications; do not reward low overrides |
| Employee confidence | average 1–5 answer to approved question | Anonymous survey; monthly | Response rate and qualitative comments |
| Capacity released | volume × validated minutes reduced / 60 | Operations + Finance validated study; monthly | **Potential value** until realized in agreed plan |
| Realized cash savings | finance-approved cost avoidance or cost reduction | Finance ledger and approval; quarterly | Must not substitute capacity estimate |

## Synthetic baseline and *targets* (not actual outcomes)
| Measure | Baseline assumption | Pilot target | Source of proof required |
|---|---:|---:|---|
| Monthly packs | 500 | 500 | Real monthly intake log |
| Average admin handling | 22 min | 13 min | Time-study sample |
| Rework cases | 30% | 15% | Logged corrections |
| Adoption | Not measured | 80% eligible cases at day 60 | Workflow and source-of-truth reconciliation |
| Unauthorized final approvals | No reference data | 0 | Incident log and approval event audit |
| Financial benefit | Unmeasured | AED 7,500 gross **capacity value** / mo at full realization | Finance-approved calculation |

## Executive dashboard wireframe (future Power BI)
**Page 1: Adoption & service performance**
- Eligible cases, workflow cases, adoption%, volume trend
- Completion/rework trend, missing document reasons
- Queue age (median/P90), critical exceptions, case-owner backlog

**Page 2: Benefit and cost**
- Actual minutes per case compared to formally recorded baseline
- Hours released versus deployment target
- Gross *capacity value* and finance-certified cash savings as **separate** series
- One-off spend, run-cost, net benefit, payback update, scenario sensitivity
- Breakdown by property/project/business unit only when minimum data quality and confidentiality rules permit

**Page 3: Governance and improvement**
- Approval policy violations, expired exceptions, security incidents
- AI-extraction review rate (future OCR only), source mismatch category
- Change requests, SOP revision history, action owner and due date

## Reporting and decision pack (example template)
**To:** Director of AI, Head of Handover Operations, Finance Business Partner  
**Reporting month:** *[not populated — demonstration]*  
**Summary status:** *No live deployment — illustrative portfolio design.*

| Executive question | Evidence to request before answering |
|---|---|
| Is the use case used in day-to-day work? | Eligible population and unique workflow event counts |
| Is processing genuinely faster? | Comparable 2–4 week before/after samples excluding rollout anomalies |
| Did quality improve? | Rework, escalation, errors and customer complaints |
| Are controls working? | Logged human approval events, override audit, incident trends |
| Has the investment paid off? | Finance-approved realized benefits less full costs |
| Should the group scale it? | Go/no-go recommendations and residual risks signed by owners |

## Financial scenario formula and validated local model
`hours released = monthly cases × (baseline minutes − target minutes) / 60`  
`net monthly scenario value = hours released × AED hourly rate × realization fraction − monthly run cost`  
`year-one scenario value = 12 × net monthly value − initial one-off cost`

In [`prototype/benefits_model.py`](prototype/benefits_model.py), the fictional base assumptions return **75 hours**, **AED 5,000 monthly net** and **8.4-month payback**. A **60% realization** scenario returns **AED 2,000 monthly net**, **21-month payback** and a **negative AED 18,000 year-one net value**. Tests cover these calculations. Neither case is a prediction of Azizi performance.

## Benefits ownership and continuous improvement
- **Business owner:** captures baseline, signs operational definitions and owns service outcomes.
- **Finance:** verifies costs and separates capacity, avoided cost and actual cash benefits.
- **AI Lead:** owns metric evidence traceability, backlog/priorities and monthly reporting.
- **HR/L&D and champions:** monitor correct use, confidence and training gaps.
- **Risk/Compliance:** verify audit trail, privacy incidents and user appeals.
- **Director of AI:** reviews whether to scale, hold, change or retire use cases.

### Monthly continuous-improvement loop
**Collect -> Validate -> Review with process owners -> Investigate root cause -> Prioritize change -> UAT regression -> Update SOP -> Rebaseline only with sign-off.**

**Illustrative course corrections:**
1. If adoption falls below 60% for two consecutive weeks, conduct focused user interviews and remove form friction before expanding.
2. If critical routing/approval violation occurs, halt outbound notifications and require incident/governance review.
3. If realized monthly net value remains at/below AED 0 for two months after stabilization, reforecast and propose remediation or retirement.
4. If the model's low-confidence extraction rate is high, improve source quality and manual checks rather than silently lowering thresholds.

## Lessons learned register (blank sample)
| Date | Evidence | Observation | Root cause | Action | Owner | Due | Outcome |
|---|---|---|---|---|---|---|---|
| — | — | No measured outcomes exist for this portfolio simulation | — | Establish pilot instrumentation | Business owner (proposed) | — | Not started |
