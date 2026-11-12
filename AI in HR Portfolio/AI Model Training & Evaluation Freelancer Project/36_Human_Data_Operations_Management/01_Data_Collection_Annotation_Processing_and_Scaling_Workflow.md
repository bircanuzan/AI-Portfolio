# 01 | Human data operations — end-to-end workflow

## Operating scenario
Use 18 **fictional** HR service requests to evaluate an AI intake classification task, before any real model is approved for use. The organization must understand data access, work assignment, quality and review throughput.

## From intake to approved data

~~~mermaid
flowchart TD
    A[Approved synthetic or licensed source] --> B[Capture provenance and permission]
    B --> C[Validate schema / redact identifiers / de-duplicate]
    C --> D[Versioned annotation task and taxonomy]
    D --> E[Independent human annotators A and B]
    E --> F[Schema and completeness checks]
    F --> G[Agreement / disagreement / gold QA]
    G --> H{Quality gate passed?}
    H -- No --> I[Human adjudication + guideline clarification]
    I --> J[Recalibrate and resample]
    J --> E
    H -- Yes --> K[Approved evaluation dataset version]
    K --> L[Report quality, speed and exceptions]
    L --> M[Controlled release / change log]
~~~

## Data intake contract
Fields: case_id (unique pseudonymous key), short case_text (fictional or permissioned and redacted), synthetic flag, source version, allowed-use scope, language and documented date. Never store names, IDs, passport numbers, actual payslips, confidential client correspondence or unapproved records.

## Processing checks
1. Ingest only from documented approved sources.
2. Validate unique ID, nonblank text, data type and task scope.
3. Flag possible sensitive data before annotation; use a restricted handling workflow.
4. Normalize encoding, but **do not rewrite meaning** or silently remove ambiguity.
5. Create immutable source version ID and documented sampling method.
6. Assign two independent annotator passes, prevent copying another rater's judgment.
7. Validate labels, request rationale for ambiguous samples, calculate agreement.
8. Route conflicts to a designated adjudicator and retain decisions.
9. Rerun all QA checks before release.
10. Record whether dataset is eligible for evaluation, training or neither.

## Scale plan and operational ownership
- **Pilot (18 cases here):** test instructions, disagreements, owner handoffs and reporting definitions.
- **Controlled batch:** stratified sampling across queue types, daily reviewer capacity, automated prechecks and issue queue.
- **Enterprise scale:** lineage, role-based project access, independent gold sample, protected annotator tooling, versioned guideline updates, batch-level dashboards and incident processes.

## Exception examples
Incomplete request -> label other if no actionable category; conflicting salary + visa request -> mark for adjudication, **never force a confident label without precedence**; real passport -> secure intake/redaction; unrecognized code -> reject annotation row; duplicated case -> halt release.

## What would be submitted to stakeholders
Data contract, SOP, sample pack, QA results, disagreement analysis, release decision, open issues, training plan, staffing estimate, KPI dashboard and next corrective action.
