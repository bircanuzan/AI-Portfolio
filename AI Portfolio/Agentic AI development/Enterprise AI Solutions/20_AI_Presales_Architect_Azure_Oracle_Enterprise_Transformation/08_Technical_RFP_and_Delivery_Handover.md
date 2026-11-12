# 08 — Technical RFP response, solution feasibility & delivery handover
## GulfConnect Utilities | fictional applied AI presales case

**Purpose:** Demonstrate how a solutions manager translates business needs into a reviewable RFI/RFP response and hands a proposed AI solution to responsible engineering and delivery teams.

**Evidence status:** Simulated requirement set, conceptual architecture, proposed acceptance tests and example governance documents. **No live customer tender, priced vendor quote, security approval, deployed architecture, test run, won contract or implementation handover occurred.** This does not represent Presight internal documentation or a Presight product capability claim.

## 1. Fictional buyer RFP — business and nonfunctional requirements
| RFP ID | Requirement | Proposed response | Verification / evidence owner | Status |
|---|---|---|---|---|
| R-01 | Reduce policy lookup friction | Permission-filtered RAG agent-assist over approved document store | Document owner validates source and policy-version trace | Design only |
| R-02 | Use authoritative outage status | Read-only supported API, provenance and freshness timestamp | CIS/outage integration lead supplies contract and fixtures | Design only |
| R-03 | Integrate Oracle/CRM without uncontrolled writes | API Management, supported connectors and queued flows | Oracle/CRM and integration architects validate contracts | Design only |
| R-04 | No autonomous consequential decisions | Human-reviewed drafts; explicit allow-list denies operational/billing writes | Risk/business owner approve permissions; security tests | Design only |
| R-05 | Respect role-based access | Identity, scoped entitlements, tenant/context-aware retrieval | IAM owner tests authorized/unauthorized personas | Design only |
| R-06 | Protect sensitive customer data | Classification, minimization, logging limits, retention controls | DPO/CISO + qualified UAE legal review | Design only |
| R-07 | Analytics and auditable KPIs | Curated operational facts, quality scorecard, Power BI option | Data owner reconciles definitions and data sources | Design only |
| R-08 | Security and incident readiness | Threat model, identity, secrets, monitoring and incident response | CISO, SecOps and platform team | Design only |
| R-09 | Service continuity during outages | Human fallback, disable switch, queued requests, recovery targets **TBD** | Service operations and BCP owner | Design only |
| R-10 | Measurable pilot results | Pre-registered evaluation set and baseline/target decision gate | Customer sponsor + independent QA reviewer | Not tested |
| R-11 | Maintainability and support | Runbooks, ownership, version/change control and monitoring | Product/SRE/support owners | Design only |
| R-12 | Commercial transparency | Phased SOW, explicit assumptions/exclusions, pricing on validated bill of quantities | Finance/procurement, vendor quote | Unpriced |

**Bid response rule:** mark requirements as *proposed*, *conditional* or *gap* until a named technical owner validates support. Never mark an item compliant because it appears in a conceptual diagram.

## 2. Conceptual solution architecture (not deployed)

\`\`\`mermaid
flowchart LR
  A[Contact-centre agent] --> B[Authenticated agent-assist UI]
  B --> C[API gateway and orchestration]
  C --> D[Role-filtered policy retrieval]
  D --> E[Approved versioned knowledge store]
  C --> F[Read-only CIS / outage / CRM interfaces]
  C --> G[Permitted language model endpoint]
  G --> H[Draft and source citations]
  F --> H
  H --> I{Human review}
  I -->|Approve/edit| J[Customer reply or authorized ticket workflow]
  I -->|Reject/escalate| K[Live specialist]
  C --> L[Audit, monitoring and quality metrics]
  M[Identity, privacy, security and BCP controls] -.governs.-> C
  M -.governs.-> D
  M -.governs.-> F
  M -.governs.-> G
\`\`\`

**Illustrative Azure-oriented option** (subject to architectural review): front end on an approved managed service; Entra-based identity; API Management and Functions/Logic Apps for routing; Service Bus for durable asynchronous tasks; permission-filtered Azure AI Search for governed retrieval; an approved model endpoint; Azure Monitor-style operational evidence; data ingestion/curation for Power BI. The existing Oracle/CIS/CRM system remains authoritative. Named services are candidate designs only; no tenant, deployment or license is implied.

**Failure design**
- If the outage feed is unavailable or older than the customer-approved freshness rule: suppress estimated restoration statements, show “source unavailable” and route to an agent.
- If retrieval lacks an approved source or role entitlement: refuse to answer and escalate.
- If the model output conflicts with a source-system status: source wins; block automated publication and log the anomaly.
- If identity, access-control, observability or human review is unavailable: stop the AI-assisted path and fall back to existing customer-service procedure.
- Never expose a write tool to meter switching, reconnection or billing approval in this pilot.

## 3. Solution architecture decisions that engineers must validate
| Decision | Proposed choice | Why | Open validation |
|---|---|---|---|
| System of record | Preserve existing CIS/outage and Oracle/CRM platforms | Reduces migration and integrity risk | API support, rate limits, data authority |
| Retrieval | Document-permission-aware RAG | Reduces unsupported policy assertions | Index ACLs, deletion, revisions, multilingual tests |
| GenAI role | Drafting and summarizing, not deciding | Human accountability on high-impact cases | Output safety and review UX |
| Integration | Controlled API/queue patterns | Auditability and resilience | Retry, idempotency, DLQ, performance |
| Analytics | Source-reconciled operational KPIs | Avoids untrusted ROI stories | Baselines, reconciliation, data lineage |
| Operations | Managed PaaS initially if fit | Lower operational burden than running clusters | Resilience, IAM, cost, approved hosting region |

## 4. Illustrative technical handover packet
**Inputs to engineering**
- Business use-case catalogue and out-of-scope operations.
- Requirement traceability R-01–R-12 and open questions.
- Logical flows, system-of-record map, preliminary data classification.
- Proposed API contracts: source system; endpoint owner; authentication; purpose; fields; timeout; retry/idempotency; rate limit; freshness; error fallback; retention. **Contracts are not yet obtained.**
- Test identity matrix and authorized access expectations.
- Candidate vendor/partner questionnaire and option scorecard from file 07.
- Target measurable pilot outcomes and evaluation cases from file 06.

**Required engineering outputs before any implementation**
- Signed high/low-level design, capacity sizing, API feasibility and supported-integration confirmation.
- Information security and privacy approvals; architecture decision records; approved service regions and subprocessors.
- Versioned test fixtures and synthetic/authorized data; performance, access and incident test plans.
- Bill of materials and vendor quotes; an agreed effort estimate and implementation schedule.
- Operational support, monitoring, backup/recovery and fallback procedures.

## 5. RACI / decision rights
| Deliverable | Solutions manager | Client business sponsor | Solution/Integration engineer | Security/privacy | Product/Delivery lead |
|---|---|---|---|---|---|
| Discovery, value story, proposal draft | **R** | **A** for business need | C | C | C |
| Technical architecture feasibility | C | I | **A/R** | C | C |
| Privacy and security controls | C | I | R for implementation | **A** for sign-off | C |
| Pilot scope and delivery plan | R for requirements | **A** for scope | R for effort | C | R for orchestration |
| Actual implementation/UAT | C | **A** for acceptance | R for build/integration | C/approval gate | **R** for delivery |
| Commercial and contract approval | C | **A** | C | C | C, with procurement/legal approval |

R = responsible, A = accountable, C = consulted, I = informed. Approvals must follow each organization's actual delegated authority; the table is an **illustrative allocation**.

## 6. Candidate UAT and negative tests — NOT EXECUTED
| Test ID | Scenario / input | Expected behaviour | Actual output | Evidence |
|---|---|---|---|---|
| UAT-01 | Approved policy question | Source-version-cited draft for authorized agent | **Not run** | Capture document version, exact output, reviewer |
| UAT-02 | Outage ETA with no source estimate | No invented restoration time | **Not run** | API fixture and audit trace |
| UAT-03 | Stale status timestamp | Source unavailable message + escalation | **Not run** | Time-controlled fixture |
| UAT-04 | Unauthorized customer record request | Deny cross-account access | **Not run** | Roles and access logs |
| UAT-05 | Prompt injection inside source document | Reject source instructions, follow policy controls | **Not run** | Injected fixture and output |
| UAT-06 | Billing reversal/reconnection request | No autonomous write; refer to authorized owner | **Not run** | Tool policy and gateway logs |
| UAT-07 | Integration timeout | Safe fallback with bounded retries | **Not run** | Failure injection evidence |
| UAT-08 | Policy updated/deleted | Correct version or removal reflected in retrieval | **Not run** | Re-index/deletion trace |

Proposed exit gates: zero unresolved critical privacy/control issues; verified case-by-case outputs for safety scenarios; signed functional acceptance and reliability thresholds; named recovery owner. Sample size and numerical thresholds **TBD with the client**. No pass rates should be reported until real execution evidence exists.

## 7. Presales-to-delivery gates and change control
- **P0 — Opportunity qualified:** sponsor, accountable data owner, problem, scope and business case hypothesis.
- **P1 — Proposal technically reviewed:** architecture, risk register, exclusions, provider support, estimate and compliance matrix.
- **P2 — SOW approved:** procurement/legal/security and any sector-specific gating; acceptance and change-control terms.
- **P3 — Build authorized:** engineering plan, environment, data permissions, fixtures, roles and monitoring.
- **P4 — UAT passed:** independent reviewer evidence, defects resolved, operations fallback and client sign-off.
- **P5 — Go-live decision:** security/BCP approval, support readiness, rollback and sponsor release authority.
- **P6 — Value review:** baseline-adjusted operational results with Finance and customer-service leadership.

**Change requests:** track CR ID, description, security impacts, delivery estimate, commercial change, sponsor decision and version. No scope is silently added by the solutions consultant.

## 8. Example bid-level risk register
| Risk | Impact | Proposed mitigation | Required owner |
|---|---|---|---|
| Unsupported or stale CIS/outage interface | High | Contract check, freshness rule, safe fallback | Integration architect |
| Sensitive customer data enters model context | High | Minimize fields, access controls, provider terms, audit | DPO/CISO |
| Hallucinated restoration estimate | Critical | Source-only status, no estimation, human review, tests | Service risk owner |
| Vendor-model or region assumptions prove false | High | Written verification and alternative design | Architect/procurement |
| No verified process baseline | Medium | Discovery measurement before value claim | Customer operations/Finance |
| Outage of agent-assist service | Medium–High | Existing manual service fallback, RTO/RPO review | BCP/operations |
| Bid oversells untested features | High | Compliance status labels and signed technical review | Presales leader |

## 9. QHSE, business continuity, privacy and governance
- QHSE/operational safety: AI cannot directly trigger electricity/water supply action. Safety-critical operating procedures remain with designated operators.
- Privacy: customer identifiers and records use approved purpose limitation and data access; law and retention policies require qualified review.
- Information security: least privilege, secrets vault, audit trail, vulnerability management and incident ownership.
- Business continuity: design manual fallback, service restoration, dependency mapping and continuity exercises before go-live.
- Governance: versioned decisions, evidence register, DPA/vendor contract, architecture approval, change log, customer UAT and release sign-off.

## 10. Product/field feedback loop
During *future actual* discovery/pilot, log customer feedback with exact reproduction steps, affected workflow, business severity, privacy/security category, suggested product change, product owner, target release and retest evidence. This is a **process design**, not a record of real Presight field feedback.

## Scope boundary and interview-ready description
**What this demonstrates:** business-to-technical translation, presales solution shaping, detailed RFP mapping, interdisciplinary handover, controlled AI solution architecture, governance and evidence standards.

**What it does not demonstrate:** independently implemented cloud engineering, certified solution architecture, utility operations authority, real customer procurement, successful deployments, actual end-user testing, measured savings or employment/partnership with Presight.

**Suggested interview phrasing:** "I developed a fictional utilities-sector proposal and technical handover package to demonstrate how I structure client requirements, frame a responsible AI solution, document open technical decisions and align engineering, security and delivery owners before a bid or pilot is committed."
