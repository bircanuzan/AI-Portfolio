# 07 | AI Factory Capability and Reusable Solution Backlog
**Goal:** connect cross-use-case requirements to platform investment, avoiding one-off solutions.

| Capability | Owner to confirm | Shared benefit | Minimum governance / acceptance |
|---|---|---|---|
| Secure sandbox environments | Platform / Infrastructure | All AI pilots | No prod secrets; logging, isolation |
| Role-based API gateway | Architecture | Controlled integrations | AuthN/AuthZ, quotas, secure contracts |
| Versioned retrieval corpus | Data / Knowledge | Merchant + dispute assistants | Provenance, owner, dates and access rules |
| Redaction / anonymization pipeline | Data Governance | All sensitive use cases | Policy-based masking, quality checks |
| AI evaluation harness | AI/Model QA | Reusable accuracy/safety testing | Gold test sets, scorecards, regression |
| Prompt/model version registry | Forward Deployed AI Lead | Reproducibility | Approved versions, roll-back |
| Human approvals and workflow routing | Business Transformation | Prevent autonomous adverse decisions | Maker-checker and audit |
| Observability and cost dashboard | Platform Ops / Finance | Value/latency/quality visibility | Alerts, budgets, logs, retention |
| AI Champion onboarding toolkit | Portfolio Office | Consistent discovery | Standard intake, BRD and gate checklist |
| Portfolio/benefits dashboard | Portfolio Lead | Steering decision support | Auditable status/evidence refresh |

## Dependency diagram (text)
Policy source and data-owner approval → masking/indexing → sandbox retrieval service → model evaluation → human-review workflow → controlled pilot → production gate.

## Capability request example AF-004: redaction service
**Problem:** two planned copilots require safe review of restricted document excerpts.  
**Capabilities:** entity-detection suggestions with human verification, deterministic masking, tests for false negatives, audit record and role-based access.
**Acceptance:** InfoSec-approved controls, measured false-negative rate on representative redacted test sets, no use on live documents before approval.
**Risks:** residual re-identification and over-masking; both require review.
**Decision required:** designate accountable platform owner and fund discovery with Data Governance.

## Team coordination
**Forward Deployed AI Lead:** system architecture and engineering plan; **Data Scientists:** evaluation and model risk evidence; **Data Engineering:** lineage/ingestion; **Architecture and InfoSec:** integrations and control standards; **AI Champions:** value and user requirements; **Portfolio Lead:** dependencies and prioritized governance/decision flow.

**Not a production AI Factory:** this is the capability map and coordinating operating model, not an implemented platform.
