# HR AI & Automation - Mobility Operations

**Portfolio reference implementation | Global EOR mobility operations | Python + SQL + low-code integration design | Synthetic data**

> **Status and evidence boundary:** This is a self-contained technical portfolio prototype developed to demonstrate design, testing and governance capabilities for a representative Employer-of-Record (EOR) mobility workflow. It is **not** a production deployment for Remote or an unnamed client, does not use real employee data, and is not a representation of delivered ROI. The Python demo and unit tests are runnable locally; HRIS/payroll/API/n8n integrations are architecture blueprints, not verified live connections.

## 1. Business requirement

A globally distributed EOR mobility function handles relocation, immigration document requests, employee enquiries, payroll handoffs and jurisdiction-specific compliance. Work arrives in different channels and is manually copied across case management, HRIS and payroll systems. The hypothetical client needs faster intake and triage **without** allowing an AI system to make regulated employment, immigration, payroll or legal decisions.

**Representative requirements**
- Standardize incoming cases and classify case type, urgency, data sensitivity and routing.
- Connect HRIS, case management, payroll and knowledge systems through APIs, webhooks and event messaging.
- Use specialist agents for document checking, enquiry triage, policy knowledge retrieval and data-quality review.
- Apply a **maker/checker** pattern: a maker proposes actions; an independent checker verifies risk, evidence and controls.
- Require human sign-off for immigration, payroll-impacting, status and other regulated outcomes; never auto-submit.
- Maintain least-privilege access, consent/purpose rules, audit trails, idempotent processing, retries and safe fallback.
- Measure service speed, quality, exceptions, rework, human oversight and agent performance.

## 2. Designed solution: mobility operations agent orchestration

```text
Employee / HR case / HRIS event
        |
   Event gateway (webhook + schema + idempotency)
        |
   Privacy & purpose guard -> reject / quarantine unsafe payload
        |
   Case Router Agent
        |
   +---- Document Intake Specialist: missing docs, expiry reminders
   +---- Policy Guidance Specialist: approved policy lookup, citations
   +---- Data Quality Specialist: HRIS vs case record discrepancy
   +---- Payroll Handoff Specialist: package, never post payroll
        |
   Independent Checker (grounding, permissions, regulations, risk)
        |
   Decision Policy
     | low-risk internal routing -> queue or draft
     | medium/high-risk         -> HUMAN REVIEW REQUIRED
     | unsupported/ambiguous    -> safe escalation
        |
   Audit log / event metrics / dashboard / change feedback loop
```

The prototype intentionally uses deterministic specialist logic rather than claiming a deployed LLM. This makes the maker/checker and boundary controls testable and avoids fabricated model-quality claims. An actual LLM adapter would be separately evaluated against these controls before deployment.

## 3. What is implemented in this repository

| Component | Evidence | Status |
| --- | --- | --- |
| Synthetic mobility case intake | `sample_data/cases.json` | Implemented |
| Input validation, event deduplication, risk-based case classification | `src/mobility_pipeline.py` | Implemented |
| Maker / independent checker with policy-based gating | `src/mobility_pipeline.py` | Implemented |
| Explicit human-approval state for regulated or sensitive cases | `src/mobility_pipeline.py` | Implemented |
| Data-minimized, structured audit output and run summary | `src/mobility_pipeline.py` | Implemented |
| Automated control and edge-case tests | `tests/test_mobility_pipeline.py` | Implemented; execute locally to validate |
| SQL KPIs for service performance and governance | `sql/mobility_ops_metrics.sql` | Reference queries |
| TypeScript webhook event-normalization and privacy-dispatch example | `integration/typescript_webhook_adapter.ts` | Source example only; not deployed or execution-validated |
| n8n/webhook/API orchestration | `integration/n8n_blueprint.md` | Design only |
| Make, Zapier and Retool workflow / approval comparisons | `integration/platform_choices_and_approval_design.md` | Architecture evaluation, not implemented |
| Requirements engineering / operational problem-to-system mapping | `docs/operational_requirements_and_skills.md` | Documented with traceable acceptance criteria |
| Security, threat model and controls | `docs/architecture_and_controls.md` | Design |
| Baseline/target evaluation, rollout and change plan | `docs/evaluation_and_rollout.md` | Proposed, not measured |

## 4. Quick start

Requires Python 3.10+; no third-party dependencies.

```bash
python -m src.mobility_pipeline --input sample_data/cases.json
python -m unittest discover -s tests -v
```

Expected output: for each synthetic case, a non-sensitive case ID, classification, proposed action, checker status and a disposition. All payroll, immigration approval and sensitive data-change actions remain **human approval required**; unsupported content is held for review. The sample data uses invented names/IDs only, with no Emirates ID, passport, contact details or live employee records.

## 5. Explicit success measures (targets; NOT observed results)

- **Intake turnaround:** baseline median hours vs post-pilot median hours.
- **Routing accuracy:** correct owner queue / all reviewed cases, sliced by jurisdiction and category.
- **Unauthorized automated decisions:** target **zero** in the controlled pilot.
- **Human-review recall:** risky cases flagged / all independently labeled risky cases; target **100%** on the safety regression suite.
- **Data leakage:** count of sensitive fields written to telemetry, target **zero**.
- **Duplicate prevention:** repeated event IDs create at most one canonical case event.
- **Safe-fallback rate**, **manual rework**, **agent-checker disagreement** and **reopen rate**, reported weekly.
- **Time saved:** independently validated before/after observation, never inferred from raw automation counts.

## 6. Role-to-requirement mapping

| Job requirement | Demonstrated artifact |
| --- | --- |
| Process redesign, DRI ownership | `docs/evaluation_and_rollout.md` phases, RACI, gates |
| HRIS/case/payroll integration | `integration/n8n_blueprint.md`, event contracts |
| Low-code and scripting | Python source and unit tests; typed TypeScript webhook example; n8n blueprint; Make/Zapier/Retool architecture assessment (not deployed) |
| Multi-agent maker/checker, approvals | `src/mobility_pipeline.py`, unit tests |
| Guardrails, retries, fallbacks | `docs/architecture_and_controls.md`, test cases |
| Tracing, RBAC, privacy/audit | minimized JSON audit schema, threat model |
| SQL/BI operational dashboards | `sql/mobility_ops_metrics.sql` |
| Team training, adoption, governance | `docs/evaluation_and_rollout.md` |

## 7. Application screening capabilities — evidence-based mapping

The following matrix responds to the **HR AI & Automation Operations Lead – Mobility** screening topics without conflating a portfolio prototype with previously delivered client work.

| Screening requirement / skill | Evidence in this portfolio | Evidence boundary |
| --- | --- | --- |
| Independently translate an operational problem into system requirements | `docs/operational_requirements_and_skills.md`: problem statement, user story, acceptance criteria, non-functional requirements, traceability matrix | Independent representative problem, not proof of a prior-employer implementation |
| Personally build or configure low-code workflows (n8n, Make, Zapier, Retool) | `integration/n8n_blueprint.md` and `integration/platform_choices_and_approval_design.md` document workflow and platform selection | **Blueprints only** here; do not describe these as configured live workflows |
| Self-directed technical/systems/automation learning | Python maker/checker demo, unit tests, SQL reference, independently authored TypeScript adapter and systems-integration design | Evidences prototype engineering; separate evidence needed for historical employer-based claim |
| Design around sensitive data, access controls, auditability and compliance | Python strict schema/PII flag/minimized audit; `docs/architecture_and_controls.md`; approval matrix, RBAC/ABAC, GDPR/jurisdiction considerations | Some controls coded; production IAM, logging immutability and compliance sign-offs are proposed |
| Light scripting and custom agents/integrations with Python or TypeScript | `src/mobility_pipeline.py` and `integration/typescript_webhook_adapter.ts` | Python code plus TS source example; not a production integrated service |

**Relevant technology keywords:** **Python 3, TypeScript, n8n, Make, Zapier, Retool, REST APIs, JSON, webhooks, OAuth2, SQL, HRIS, EOR mobility, AI agent orchestration, maker/checker validation, human-in-the-loop approvals, RBAC, ABAC, audit trails, GDPR-aware design, idempotency, exceptions and retries, unit tests, requirements engineering, stakeholder workflows, change adoption and operational analytics.**

**Demonstrated vs considered:** Python logic/tests and TypeScript event-normalization source are present in this repository. n8n, Make, Zapier, Retool and production HRIS/payroll connectors are comparison/design artifacts only. No real employee data or claimed customer business outcomes.

## 8. Example case studies

**A. Immigration document completeness (synthetic):** A case is missing a document. Specialist recommends a checklist follow-up; checker allows a draft instruction only. An immigration decision or filing cannot be automated; a qualified Mobility/Legal owner reviews the case.

**B. Cross-system payroll mismatch (synthetic):** HRIS and case records disagree on effective dates. Specialist proposes a discrepancy ticket and reconciliation package; checker sets human approval required before any payroll-impacting change.

**C. Low-risk knowledge routing (synthetic):** A general approved-policy FAQ request can be routed to a policy queue with an evidence-citation requirement; no bespoke legal/immigration advice is issued.

## 9. Technology footprint

**Implemented in the codebase:** Python 3, standard-library dataclasses, JSON, deterministic rule engine, unittest, minimized structured audits and synthetic fixtures. **Additional authored source example:** TypeScript event validation and privacy dispatch gate (`integration/typescript_webhook_adapter.ts`; no demonstrated runtime/deployment).  
**Reference architecture / compared tooling:** n8n, Make, Zapier, Retool, webhook/event gateway, REST/JSON APIs, OAuth2/service identity, HRIS, payroll, case management, relational SQL, Tableau/Sigma/Power BI, encrypted secret storage and observability. No claim of live deployment of these reference systems.

**Portfolio:** [AI-in-HR-Portfolio](https://github.com/bircanuzan/AI-in-HR-Portfolio)

**Vacancy used for requirements analysis:** [Remote: HR AI & Automation Operations Lead – Mobility](https://apply.remote.com/jobs/f5e1d99a-5562-4725-9e64-ab1b342000e1). This independent case study is not affiliated with Remote.
