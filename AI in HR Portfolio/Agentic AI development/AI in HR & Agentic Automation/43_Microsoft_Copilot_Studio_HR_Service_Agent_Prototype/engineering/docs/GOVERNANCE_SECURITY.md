# Agent governance and security review — business-side controls + technical gaps

**Threat model:** Employee policy misstatement, outdated policy, malicious instruction injection, non-authorised data access, employee impersonation, false approval completion, unreviewed employment letters, cost runaway and inadequate traceability. No real employee data is used.

| Risk | Existing local mitigation | Mandatory production evidence still missing |
|---|---|---|
| Inaccurate FAQ | Approved/current sample policy retrieval with cited source ID/version/hash | Independent HR gold answers, real model hallucination tests, calibrated relevance scores |
| Unsafe personal action | Specific request patterns route to internal human queue | Access controls enforced on tools, IAM and HRIS, prompt injection red-team, breach testing |
| Approval overreach | Queue is PENDING and requires a reviewer token to update; no letter generation/send | Teams/n8n/Power Automate actual run, identity authentication and segregation of duties |
| Sensitive information | Sample policy files only; SQL audit excludes raw prompts | Privacy impact assessment, encryption, retention/deletion, geographic residency and DLP |
| Wrong access | No HRIS connectors installed | Least-privilege Entra ID/RBAC per user and tool, independent permission testing |
| Policy drift | Effective dates, approval bit, source SHA-256 | Revocation, expiry scheduling, model retraining/regression, owner signoffs |
| Model risk | Offline deterministic path does not call LLM | Real Azure/OpenAI evaluations: answer correctness, groundedness, refusals, latency, token/cost and incident dashboard |
| Workflow outage | No external action is asserted; uncertain requests queued locally | Retry/idempotency, circuit breakers, dead-letter queue, alerting and recovery test |

## NIST AI RMF functional mapping (reference only)
- **Govern:** documented scope, named HR policy owner, technical owner, security reviewer, change authority and STOP/HOLD release authority.
- **Map:** identified employee request types, individual data impacts, business process, data sources and human decision rights.
- **Measure:** test set, policy citation quality, handoff recall, adversarial and privacy tests, cost/latency and per-version regression.
- **Manage:** release gates, remediation ownership, incident severity, manual override/kill switch, monitoring and retirement plan.

This mapping is not NIST accreditation, regulatory compliance certification or a third-party audit. See https://www.nist.gov/itl/ai-risk-management-framework .

## Release gates
1. Independent policy-owner verification on a meaningfully larger, stratified holdout test set; target metrics agreed before evaluation.
2. Zero unauthorised HRIS writes and confirmed least-privilege connector audit.
3. Verified mandatory human handling for every high-impact case in release benchmark; accessibility and appeal mechanisms.
4. Actual Azure/LLM and n8n/approvals trace capture, reviewer signoffs, secret handling and rollback tested.
5. Post-pilot monitoring, cost caps and quality/employee impact outcomes reviewed.

**Current decision: HOLD.** The local developer-written fixtures are not evidence that release gates are met. No production deployment or real third-party AI security tests occurred.
