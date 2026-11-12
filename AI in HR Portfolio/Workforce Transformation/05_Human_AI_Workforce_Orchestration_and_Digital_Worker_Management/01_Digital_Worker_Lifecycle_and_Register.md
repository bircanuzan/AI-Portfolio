# Digital worker lifecycle and minimum register

## Why the CHRO and CAIO both own the design
The CHRO owns work and human consequences; the CAIO/CTO owns technical delivery, identity and model quality; CISO/Legal control risk. Neither the model nor a vendor is accountable for adverse employment decisions.

## Synthetic agent/worker register
| ID | Agent role | Business owner | Permitted behavior | Prohibited behavior | Monitoring |
|---|---|---|---|---|---|
| A-POL | HR policy assistant | HR service owner | Cite versioned general policy; draft non-personal FAQs | Personal benefits determinations, HRIS reads/writes | Source accuracy, abstention, complaints |
| A-RPT | Workforce reporting assistant | People analytics owner | Explain approved aggregate KPI definitions | Individual employee profiling, silent access escalation | Data lineage, completeness, privacy |
| A-TRI | Service triage helper | Operations owner | Classify generic request; propose queue | Close disputes or approve actions | Routing accuracy, exception burden |

Identity is **illustrative**; no tenant service principals or agent credentials are provisioned.

## Digital worker job specification fields
Worker ID; role/goal; owner; sponsor; model and version; allowed users; authorized data sources; allowed tools; denied actions; access expiry; risk tier; test set; evaluation results; business baseline; approval chain; incident contact; rollback/retirement policy; human appeal route; cost model.

## Lifecycle
1. **Applicant:** Proposed scope, data classification, benefits and business owner.
2. **Assessment:** Security/privacy/HR risk evaluation and test suite; reject unsafe autonomy.
3. **Probation — SHADOW:** Read-only dry-runs; inspect citations, false confidence, unsafe answers and escalations.
4. **PILOT:** Limited audience, manual signoff, access and cost caps; instrument every material output.
5. **ACTIVE:** Time-bound authorization, periodic independent audits, feedback and drift monitoring.
6. **SUSPENDED/RETIRED:** Disable tokens and workflows, preserve appropriate audit records, revert to human service and notify affected parties.

**Stage-gate rule:** Promotion to PILOT or ACTIVE must be a recorded human decision after independent evidence; script outputs cannot approve deployment.

## Human-agent management and HR policy
Managers require a way to see failed tasks, override recommendations, escalate exceptions and coach staff. Junior employees continue supervised cases and rotations rather than outsourcing all entry-level learning tasks. Employee impact assessments and local legal requirements are prerequisites for any real deployment.

## Metrics
Escalation precision/recall, unsupported requests correctly refused, source accuracy, task success by risk tier, human review minutes, rework, incident count, cost per verified resolved case, user satisfaction and agent suspension lead time. Do not treat token volume or answer speed as business value.