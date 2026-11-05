# 06 — AI solution discovery, executive storyline & demonstration plan
## Scenario: GulfConnect Utilities customer service intelligence (fictional)

**Status:** Original Presight Manager – Solutions JD-aligned design exercise. GulfConnect Group, its utilities division, all stakeholders, enquiries, data and outcomes are fictional. No Presight affiliation, customer engagement, deployed agent, real customer demonstration, field observation or measured operational outcome is claimed.

### Executive problem and proposition
A hypothetical UAE utilities operator has fragmented customer service requests, an approved outage/status system, a customer-information system (CIS), CRM history and policy documents. Contact-centre agents spend time locating approved procedures and checking authoritative status records. Leadership wants more consistent answers **without permitting a language model to invent an outage estimate, authorize reconnection or change a customer account**.

**Proposed solution:** A governed agent-assist workspace (not an autonomous utility-control agent) that combines:
1. **Authoritative structured data** — status and ticket identifiers from approved CIS/outage/CRM APIs only, with timestamps and permissions.
2. **Policy retrieval** — permission-filtered retrieval-augmented generation (RAG) over approved and versioned customer-service policies, with document citations.
3. **Workflow orchestration** — reviewed draft responses and human-managed service-ticket escalation; no model-triggered switching, billing adjustment or other consequential action.
4. **Analytics** — operational measures covering handle time, first-contact resolution, grounded-answer quality, escalation, customer satisfaction and access violations, reviewed against genuine baselines.

### Stakeholders and 90-minute discovery
| Time | Stakeholder | Discovery question | Evidence / decision |
|---|---|---|---|
| 0–15m | COO, customer experience lead | Which service problems matter and what is the baseline? | Sponsor, success hypothesis, scope |
| 15–30m | Contact-centre manager | Which intents recur; where do agents lose time? | Intent catalogue, exception path |
| 30–45m | CIS/outage/CRM owners | Which APIs are authoritative, supported and timestamped? | Source map and API feasibility |
| 45–60m | CISO, DPO, risk, compliance | Which data may be accessed and retained, and by whom? | Classification, residency and approvals |
| 60–75m | Enterprise architect and delivery lead | Which integration, availability and support constraints matter? | Preliminary NFRs, ADRs, pilot effort |
| 75–90m | CFO/procurement and sponsor | What is a defensible value case and pilot commitment? | Evidence gaps, decision gate, action owners |

**Mandatory follow-ups:** confirm integration contracts, channel accessibility, data-rights/legal basis, Arabic/English policy handling if required, accessibility, provider tenancy/residency, service availability target, outage-status timestamp SLA, and security testing authority. None is assumed approved.

### Use-case prioritization (design, not measured ranking)
- **Pilot A — Service policy agent assist:** retrieve approved policy excerpt, show source/version, prepare a *draft* for human review. High controllability when documents are governed.
- **Pilot B — Ticket/outage status lookup:** show API-supplied status and “last updated”; stop or route to a person when the feed is unavailable/stale. No inferred restoration time.
- **Defer C — Bill adjustments and service reconnection:** controlled financial / safety-impacting actions require separate process and explicit authorized approval; exclude from the initial pilot.
- **Defer D — Outage prediction:** data-quality, ground-truth, model monitoring and safety validation required before any ML feasibility claim.

### Eight-slide executive storyline and speaker guidance
| Slide | Main message | Evidence or visual | Speaker question |
|---|---|---|---|
| 1 | Customer friction is a service and trust issue | Current journey with handoffs; baseline **TBD** | What would better service change? |
| 2 | Separate verified facts from AI-generated language | CIS/outage source vs policy documents | Which data is authoritative? |
| 3 | Controlled assistant, not autonomous operations | Human approval and source boundaries | What must AI never decide? |
| 4 | Use the existing Oracle/CRM estate where viable | Conceptual architecture and integration options | Which systems can be reused? |
| 5 | Show a narrow agent-assist pilot | Scripted scenarios and proposed review controls | What would agents actually see? |
| 6 | Measure quality before expanding | Evaluation matrix, audit log, fallback | What evidence would earn trust? |
| 7 | Stage spend and value realization | Cost, adoption, controls and sensitivity | Which assumptions need finance sign-off? |
| 8 | Sponsor a timeboxed technical discovery | Named owners, checkpoints and exit criteria | Who approves the next gate? |

### Demo run-of-show: three illustrative **scripted** examples
These are *intended interface behaviours written by the portfolio author*, **not recorded model outputs or successful system tests**.

**Case D-01 — Policy-backed response**
- Sample user: “What documents do I need to request a new connection?”
- Proposed UI: policy snippet, approved document title/version, retrieved citation and *draft* response.
- Human action: agent reviews source and account-specific eligibility; clicks approve/edit; activity logged.
- Failure rule: missing or conflicting policy version -> “I cannot verify this from approved guidance” + escalation.

**Case D-02 — Outage status**
- Sample user: “When will supply return to my district?”
- Proposed UI: authoritative outage API returns an ID, state and timestamp, if available.
- Guardrail: never fabricate restoration estimate; stale/missing feed -> clearly say status is unavailable and route to live support.
- Human action: verify account permissions, advise only the authorized status field.

**Case D-03 — High-risk financial action**
- Sample user: “Reverse my bill and reconnect the meter now.”
- Proposed UI: “I cannot approve a billing reversal or operational reconnection. I can create a request for an authorized team to review.”
- Human action: finance/utility operations follows existing approval and safety procedures; zero autonomous control-system writes.

### Pilot proof plan and proposed acceptance criteria
| Test | Proposed threshold / condition | Evidence to capture | Status |
|---|---|---|---|
| Grounded policy answers | 100% of policy claims trace to correct approved source; sample size pre-agreed | Prompt, retrieved passage, version and reviewer judgement | **Not run** |
| Outage truthfulness | 0 fabricated status or restoration estimates in high-risk scenarios | API fixture + output + timestamp check | **Not run** |
| Unauthorized action | 0 writes to billing, meter or outage-control endpoints from assistant | Tool allow-list, integration logs, security test | **Not run** |
| Privacy/access | No cross-customer data exposure in representative permission tests | Test identities, access decisions, audit trace | **Not run** |
| Human escalation | Correct routing for all defined exceptions | Scenario ID, expected routing, assigned team | **Not run** |
| Usability/adoption | Agreed improvement vs actual baseline, with agent feedback | Agent task observation, surveys and telemetry | **Not run** |

A production pilot also requires security, legal/privacy, engineering, operations and sponsor acceptance. Proposed percentages are not actual project test results.

### Illustrative value calculation — **not actual ROI**
Assume **120,000** annual inbound enquiries; **20%** are in a *potentially assistable* category; **3 minutes** saved per assisted case. Gross potential capacity = 120,000 × 0.20 × 3 / 60 = **1,200 agent-hours/year**. This is **not** a verified saving: applicability, answer quality, adoption, human review time, recontacts, licences, implementation and monitoring costs have not been measured. Real ROI must use approved baselines, sensitivity cases and Finance validation, and distinguish capacity released from cash benefit.

### Proposed implementation gates
G0 discovery: sponsor, source systems and data permissions known.  
G1 design: architecture and threat model approved by owners.  
G2 limited PoV: synthetic or authorized representative test data; reproducible evaluation.  
G3 controlled pilot: authorized users, monitored outputs, human approval.  
G4 scale decision: verified service, safety, adoption, economic and security evidence.

### Field-to-product feedback example (blank template, not a real observation)
| Field | Example collection rule |
|---|---|
| Feedback ID / date | Assigned at actual workshop or test |
| Persona, need, business impact | Directly sourced and consented |
| Product limitation | Reproducible evidence link, severity, workaround |
| Owner | Product manager / engineering / client |
| Decision | Backlog, defer, reject with reason |
| Closed-loop confirmation | Product release + customer retest reference |

### Ownership boundary
**Solutions manager:** discovery, business storyline, documented options, prioritization and stakeholder alignment.  
**Architect/engineering:** validate integrations, API limits, performance, failure modes and feasible architecture.  
**Risk/security/legal:** review data access, privacy and high-consequence controls.  
**Delivery/product:** scope implementation, resource and support plans.  
**Client sponsor:** accept business goals, procurement and production release.

This is a **client-facing solution-shaping artifact**, not evidence of an implemented Presight product, successful presales win or live utility customer rollout.