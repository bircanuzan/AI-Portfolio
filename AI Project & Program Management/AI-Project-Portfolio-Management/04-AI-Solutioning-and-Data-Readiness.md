# 04 | AI Solution Patterns, Integration Design and Data Readiness
**Illustrative architecture only; real solution requires Architecture and InfoSec review.**

## Options evaluated
| Pattern | Appropriate use | Main risks | Human control |
|---|---|---|---|
| RAG copilot | Approved policy retrieval, summarization | Wrong citation, prompt injection, source drift | Source verification and reviewer |
| Agentic workflow | Multi-step triage with approved tool calling | Excess privilege, unsafe actions, cascading failure | Tool allow-list, approval before writes |
| Predictive ML | Prioritization of flagged cases | Drift, bias, false positives, explainability | Analyst review; never automatic denial |
| Rules/analytics | Deterministic workflow and KPI reporting | Incomplete exception handling | Rule owner and QA |
| Low-code automation | SLA reminders and approved routing | Integration errors, hidden escalations | Approval controls, rollback |
**Architecture decision:** start AI-001 as *RAG copilot*, not an autonomous agent or model-driven approval decision.

## High-level integration sequence
1. Employee authenticated through corporate identity/SSO; role verified.
2. User requests analysis of **approved, redacted** sample.
3. API gateway calls a sandbox retrieval service over versioned, permission-filtered policy index.
4. Service obtains eligible reference snippets, provenance and policy effective dates.
5. LLM service produces cited response in a constrained schema; redacts disallowed fields.
6. Validator checks citation integrity, allowed output format and sensitive content.
7. Human reviewer approves/corrects; audit log records model version and relevant source IDs.
8. Draft handoff may be passed to a separate workflow **only** after owner approval.

**System interfaces to define:** identity provider, document store, policy CMS, case management, logging/SIEM, model endpoint, secrets management, analytics dashboard. APIs and payloads are design assumptions, not completed integrations.

## Data-readiness register
| Dataset | Owner | Classification | Quality concern | Required gate |
|---|---|---|---|---|
| Approved policy corpus | Compliance policy owner | Internal confidential | Outdated/duplicate versions | Version/date review |
| Merchant applications | Merchant Ops | Confidential/PII | Missing or inconsistent fields | Data minimization, PII masking |
| Ticket metadata | Operations | Internal | Incomplete ownership fields | Schema checks |
| Evaluation set | AI/Quality owner | Synthetic / redacted | Representativeness | Human-labeled test cases |
| Model telemetry | Technology | Controlled | Sensitive prompt leakage | Retention and access policy |

## Data handling controls
- **Data access:** owner authorization, need-to-know, audit logging; document any cross-border transfer/residency constraint.
- **Ingestion:** schema/lineage/source-of-truth validation; reject malformed or unapproved sources.
- **Masking and anonymization:** irreversible synthetic replacement for demonstrations; do not mistake pseudonymization for anonymity.
- **Sandbox:** isolation from live payment rails, production credentials and personal data; approve read-only prototypes first.
- **Security:** prompt injection tests, content filters, malware checks on uploads, encryption and secrets rotation.
- **Performance and safety:** latency, cost ceiling, answer-quality benchmark, hallucination rate, abstention behavior, and rate limiting.
- **Change control:** model/source changes trigger regression testing and release review.

## AI solution design decision record ADR-001
**Question:** retrieve and cite policy vs fine-tune a new model?  
**Option chosen:** constrained RAG prototype because policy provenance and version controls can be evaluated without training a proprietary model on sensitive material.  
**Conditions:** approved environment, policy access, evaluation set, relevant control sign-offs.  
**Open issue:** confirm corporate-approved AI model, vendor contractual terms and residency.
