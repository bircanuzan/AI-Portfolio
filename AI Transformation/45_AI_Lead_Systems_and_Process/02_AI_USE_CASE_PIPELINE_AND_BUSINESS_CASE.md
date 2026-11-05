# A — AI/Automation Use Case Pipeline and Business Case

## Intake and prioritization framework
Every idea receives an owner, problem statement, current metric, expected value, feasibility evidence, risk level, business sponsor, dependencies and next-gate decision.

**Scoring (1–5, higher = more desirable):**
- Business impact 30%; feasibility 25%; data readiness 15%; control/risk manageability 20%; change readiness 10%.
- Score out of 100 = 20 × (0.30I + 0.25F + 0.15D + 0.20C + 0.10A).
- **Mandatory stop gates:** unapproved handling of personal data, missing accountable owner, non-auditable decisions, no human appeal, or unavailable legal/contractual source documents. High score cannot override a stop gate.

| ID | Opportunity | I / F / D / C / A | Score / 100 | Proposed decision |
|---|---|---|---:|---|
| UC-01 | Handover document intake and approval routing | 5/4/4/3/3 | **80** | Pilot first after policy/data sign-off |
| UC-02 | Supplier invoice extraction and duplicate detection | 4/4/4/4/4 | **80** | Parallel feasibility discovery; human AP approval required |
| UC-03 | Customer enquiry chatbot with approved knowledge | 4/3/3/2/3 | **62** | Hold pending content governance and legal escalation design |
| UC-04 | Construction milestone forecasting | 5/2/2/3/2 | **62** | Data audit and historical backtesting before proposal |

Ties are not an automatic approval. UC-01 is the demonstration pilot because its workflow, business acceptance criteria and human escalation can be specified and locally simulated. UC-02 is an equally ranked candidate pending additional financial control review.

## UC-01 business case: illustrative assumptions
| Variable | Value | Interpretation |
|---|---:|---|
| Monthly volume | 500 cases | Hypothetical workload |
| AS-IS effort | 22 min/case | Manual touch time, not calendar lead time |
| Target TO-BE effort | 13 min/case | Unvalidated stretch target |
| Hourly loaded capacity cost | AED 100 | Planning rate; not an actual payroll rate |
| One-off design/build/change cost | AED 42,000 | Hypothetical |
| Monthly license, support and QA | AED 2,500 | Hypothetical |
| Savings realization | 100% base / 60% sensitivity | Capacity value only if sustainably redeployed or costs avoided |

### Transparent calculations
- Capacity hours saved/month = 500 × (22 − 13) ÷ 60 = **75 hours**.
- Base potential capacity value = 75 × AED 100 = **AED 7,500/month**.
- Base net operating benefit = 7,500 − 2,500 = **AED 5,000/month**.
- Base simple payback = 42,000 / 5,000 = **8.4 months**.
- Base year-one net value after initial cost = 12 × 5,000 − 42,000 = **AED 18,000**; **42.9%** year-one ROI on one-off cost.
- **Conservative 60% realized:** 7,500 × 60% − 2,500 = **AED 2,000/month**; payback = **21 months**; year-one value **−AED 18,000**.

**Financial integrity:** these are conditional forecasts, not achieved savings. Time freed is *capacity*, not cash savings unless a documented staffing, overtime or service-quality benefit is realized. Benefits must not double count reduced rework, lower handling time, and avoided overtime.

## Stage gates and delivery governance
| Gate | Required evidence | Decision |
|---|---|---|
| G0 idea intake | Sponsor, owner, use case, expected business problem | Accept for discovery / reject |
| G1 business qualification | AS-IS baseline, risk screen, stakeholder priority | Rank / hold |
| G2 design approval | BRD, data privacy review, controls, estimated cost, ROI sensitivity | Approve controlled pilot / rework |
| G3 pilot acceptance | UAT traces, defects, accessibility, security, SOP, owner sign-off | Controlled rollout / no-go |
| G4 stabilization | 30/60/90-day adoption and benefits versus baseline | Scale / remediate / retire |

**Governance cadence:** weekly backlog triage led by AI Lead; monthly prioritization with Director of AI; quarterly benefit realization with Finance/operations. Keep decisions and rationale in the use-case register.
