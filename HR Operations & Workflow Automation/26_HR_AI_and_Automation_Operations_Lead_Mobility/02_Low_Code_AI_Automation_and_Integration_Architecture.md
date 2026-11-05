# 02 — Automation and integration architecture

## Conceptual solution
~~~mermaid
flowchart LR
    A[Employee / Customer HR Portal] --> B[Case API / Webhook]
    B --> C[Authentication + RBAC + Consent]
    C --> D[Maker: propose routing / extraction]
    D --> E[Checker: validate scope, access, policy version]
    E --> F{Requires human specialist?}
    F -- Yes --> G[Mobility / Immigration Specialist Queue]
    F -- No --> H[Approved Public FAQ / Status Acknowledgement]
    G --> I[Authorized Human Decision]
    I --> J[Scoped Case Management API]
    J --> K{Approved payroll date impact?}
    K -- Yes --> L[Approved Payroll Event Queue]
    K -- No --> M[HRIS/Case reconciliation]
    L --> M
    H --> M
    M --> N[Redacted Audit + KPI Events]
~~~

## Separation of systems
- **HRIS**: authenticated employment record; no direct anonymous writes.
- **Mobility case platform**: request, status, approval and communication history.
- **Document vault**: restricted storage, retention classification and delete/hold rules for immigration evidence.
- **Payroll**: receives only signed effective-date changes from an authorized source.
- **Automation orchestration**: n8n/Make/Retool/Zapier candidate; source-controlled workflows, environment isolation, isolated credentials, retries and safe dead-letter queues.
- **Agent steps**: intake classification and safe source-linked policy FAQ proposal; separate checker validates PII, permission, trace and escalation.

## Safe API contract (design only)
POST /mobility/v1/case-events
Request body: request_id, pseudonymous_case_ref, event_type, region_code, prior_status, new_status, approved_actor_role, source_system, idempotency_key.
Reject requests containing passport image, full passport number, unmasked national IDs or unapproved employee data.
Headers: Authorization token from approved identity provider and X-Correlation-ID.
Outcomes: 202 accepted, 400 invalid data, 403 permission refused, 409 duplicate, 429 rate limited, 503 dependency unavailable.

## Idempotency and retry
Retry limited transient infrastructure errors with jitter/exponential backoff. Never retry side-effecting payroll mutation blindly; first query idempotency status. Route poisoned messages to a monitored dead-letter queue with manual repair. Maintain per-event status independent from LLM generated text.

## Choosing low-code vs Python
Use low-code for approved connectors, orchestrated task queues and simple human approval. Use Python for field validation, evaluation cases and business logic requiring version-controlled tests. Avoid doing immigration/legal interpretation in scripts.

## Sandbox n8n artifact
The included n8n JSON is an illustrative manual-run workflow using synthetic fields and a safe routing label. It is **not connected** to Remote systems and intentionally cannot update production data.
