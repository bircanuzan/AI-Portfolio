# ISO/IEC 42001-inspired practical implementation — HumanEvoX
**Status:** documented design and locally tested decision-gate demo. **Not** an implemented, independently audited or certified ISO 42001 management system. Exact requirement/Annex A wording is not reproduced; consult the licensed standard.

| Phase | Management-system theme | Actual deliverables / activity | Owner and sign-off | Evidence / acceptance |
|---|---|---|---|---|
| 0 — Discover | Context, scope and interested parties | Determine legal entity/jurisdiction, AIMS boundary, stakeholders, vendors, candidate data flows | Business owner + privacy counsel | Signed scope; processing map; list of applicable legal obligations |
| 1 — Plan | Leadership, AI policy, roles & objectives | Approved AI-use charter; named human decision owner; boundaries; KPIs; RACI | HumanEvoX leadership | Approved policy; objectives; version history |
| 2 — Assess | Risk/opportunities and AI system impact | Inventory agents and versions; record intended use, unacceptable uses, risks, impacts, fairness and privacy | AI risk lead, HR owner, DPO/counsel | Risk register, impact assessments, treatment approvals |
| 3 — Control | Operational controls and documented information | Tool permissions; least privilege; human review; approved sources; vendor and data protection controls | Tech + privacy + process owners | Proof of configuration; approval records; supplier due diligence |
| 4 — Test | Evaluation and verification | Real LLM adversarial/equity/privacy tests *if deployed*; synthetic gate tests may inform baseline | Independent reviewer | Versioned cases, actual model responses, trace IDs, defect logs, sign-off |
| 5 — Check | Monitoring, audit, management review | Metrics on harmful outputs, escalations, time-to-close, incidents, drift; internal audit | Governance lead + management | Trend report, audit findings, management review |
| 6 — Act | Corrective action and improvement | Root-cause, fixes, retesting, risk reapproval and update policies | Control owner | CAPA log, test rerun, follow-up audit |

## Defined system boundary for the case
A hypothetical HumanEvoX recruitment assistant may *draft* policy explanations and candidate messages using approved sources. It may not autonomously make hiring decisions, contact candidates, export candidate files or delete records. Every real action must be implemented behind an authorization boundary; this code is only an offline illustration.

## Minimal AIMS artefact inventory and maturity
- **Prepared in this repository:** documented scope proposal, risk register, draft policy, control register, synthetic cases, reproducible deterministic gate, observed local test outcomes, procedural evidence checklist.
- **Requires live work:** qualified accountable owners; actual processing inventory; organization-specific legal advice; genuine privacy and AI impact assessments; real agent + supplier reviews; written management approvals; real human approval controls; security architecture; independent evaluation and internal audit; management review and operating metrics.
- **Not represented as obtained:** PECB certification; ISO company certification; 2 years AI work; 300 AIMS hours; client project; live AI agent output.

## Practical success gates
- High-impact HR decisions cannot be autonomously executed.
- Any request with personal data and missing recorded basis is denied before tool execution.
- Any outward transfer without verified safeguards is denied; even approved transfers remain human-gated.
- Tool calls and outputs must be attributable to actor, purpose, model/policy version and human decision, with retention limits.
- No release without legal/supplier sign-offs and measured LLM evaluation against independently defined metrics.

## 30/60/90-day real-implementation backlog
- **Days 1–30:** scope and accountable sponsor, legal applicability, approved purposes, inventory, policy baseline, risk appetite.
- **Days 31–60:** live-approved test environment, review of processor agreements, guardrail integration, test cases with preserved actual responses, human approval workflow.
- **Days 61–90:** independent review, measured pilot, monitoring, incident exercise, CAPA, executive management review and go/no-go.
These are future targets, **not achievements or PECB hours**.
