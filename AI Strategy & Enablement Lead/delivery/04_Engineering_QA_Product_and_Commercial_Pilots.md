# Cross-functional controlled pilots

## Pilot A — Engineering: AI-assisted pull requests
**Workflow:** developer writes acceptance criteria -> assistant proposes code/tests -> human reviews diff + dependencies -> security/static scans -> CI -> merge approval.
**Design:** comparable tasks, stratify by complexity; alternate control vs AI workflows.
**Metrics:** median time to accepted PR, code-review corrections/PR, escaped defects, security findings, generated-code acceptance.
**Stop rule:** sensitive code leakage, unsafe dependency changes or declining quality.

## Pilot B — QA: regression test design
**Workflow:** user story -> AI-drafted edge cases -> QA validates traceability -> human-created/approved test suite -> CI executes.
**Metrics:** mutation-testing effectiveness, test relevance, coverage delta, false assertions, triage minutes.
**Failure probes:** missing-negative cases, duplicate tests, flaky test creation and unsupported assertions.

## Pilot C — Product: grounded product requirements
**Workflow:** approved customer feedback -> human-curated context -> LLM-assisted draft -> versioned source references -> product manager acceptance.
**Metrics:** specification turnaround, traceability coverage, unsupported claims and post-review rework.
**Controls:** source retrieval restricted by client/project permissions; prohibit unapproved customer data uploads.

## Pilot D — Commercial: knowledge and RFP enablement
**Workflow:** approved marketing/product content -> access-controlled retrieval -> draft response -> commercial / legal verification -> customer-specific approval.
**Metrics:** verified-answer accuracy, cycle time, review burden and retraction rate.
**Controls:** never fabricate SOC/ISO status, contractual claims, product commitments or regulatory coverage.

## Data capture schema
`experiment_id, team, cohort, task_type, difficulty, baseline_minutes, ai_minutes, review_minutes, accepted, defect_severity, token_or_license_cost, reviewer, consent_status, data_class`

All metrics require actual task samples; no productivity gains are asserted in this design.

## Workflow architecture
```text
Approved source -> policy gate -> bounded LLM/tool invocation
                -> schema validation -> human verification
                -> existing SDLC / product / CRM system
                -> event-based measurement and audit log
```
