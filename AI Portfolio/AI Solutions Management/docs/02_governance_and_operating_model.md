# 02 — AI Governance, Risk, Privacy & Operating Model

## Operating model
The AI Solutions Manager is accountable for **product roadmap, execution coordination, inventory and value reporting**, but does not unilaterally approve privacy, security, legal or budget risks. Product owners from each subsidiary remain accountable for their use cases; control owners retain decision authority.

## RACI (illustrative)
R = responsible, A = accountable, C = consulted, I = informed.

| Activity | AI Manager | Business Owner | IT/Security | Legal/DPO | Procurement | Finance |
|---|---|---|---|---|---|---|
| Use-case intake and priority | A/R | R | C | C | I | C |
| Data privacy/security approval | C | R | A (security) | A (privacy/legal) | I | I |
| Vendor selection/contract | R | C | C | C | A | C |
| Budget and business case | R | A | I | I | C | A (financial signoff) |
| Access provisioning | C | A (request) | R | C | I | I |
| Pilot rollout and UAT | A | R | R | C | I | I |
| Adoption and support | A | R | R | C | I | I |
| Monthly reporting/renewals | A/R | C | C | C | R | R |

A cells denote accountability within each specialist decision; approval may require more than one control owner rather than a single overriding approver.

## Tool lifecycle and decision gates
1. **Register:** tool ID, vendor, owner, purpose, entity, data classification, seats, renewal and licensing terms.
2. **Classify use:** employee/customer interaction? personal data? confidential documents? voice/video? automated external decisions?
3. **Review controls:** information security, Legal, DPO/privacy and responsible AI; each records approve / approve with conditions / reject.
4. **Procure and provision:** approved contract, budget, named users, minimum privileges, SSO/MFA where supported, expiry and recertification.
5. **Pilot:** prohibited-data rules, audit trail, red-team/test cases, human review and kill switch.
6. **Scale or retire:** formal owner signoff, monitoring, incident response and regular risk re-assessment.

## Privacy and responsible AI review checklist
- Lawful purpose and documented processing role; data minimisation and retention/deletion.
- Vendor subprocessors, data residency/cross-border transfers, retention and model-training opt-out terms **verified**, not assumed.
- Personal/sensitive data protection: DPA, DPIA where required, deletion rights and access logging.
- Security review: SSO/MFA, RBAC, API secret handling, encryption, monitoring, breach response, vendor SOC/ISO evidence as applicable.
- Model safety: factuality, reliability, hallucination risk, bias, harmful content, prompt injection and misuse testing.
- Output governance: protected brands/IP, third-party rights, content provenance and a human approval gate.
- Customer-facing decisions: opt-out/appeals, appropriate notices, escalation and accessible human support.
- Enterprise AI usage policy: define allowed, restricted and prohibited information and use cases.

## Controls by platform category
| Platform category | Example controls to verify |
|---|---|
| Claude / enterprise assistants | Confidential input policy, vendor retention/training terms, prompt injection, human fact checks |
| Synthesia / generated video | Consent for voice/avatar, licensing, approvals before publication, authenticity disclosure |
| Telnyx / communications | Telecommunications compliance, recording consent, call/OTP restrictions, PII flow mapping |
| Midjourney / image generation | Brand rights, sensitive imagery, copyright/trademark review, public-facing approval |

**Do not assume** any platform's current policy, SLA, pricing, storage region, certifications, model-training practice or enterprise feature; check contract and current vendor documentation.

## Risk register (sample)
| Risk | Likelihood/impact | Owner | Mitigation | Escalation |
|---|---|---|---|---|
| Sensitive data in AI prompt | High/High | DPO + InfoSec | Training, DLP, approved gateways | Suspend affected workflow |
| Tool spend without usage | Medium/Medium | AI Manager + Finance | Monthly seat audit | Reduce/retire seats |
| Vendor outage | Medium/High | IT Service Owner | Support SLA, fallback, tested rollback | Incident commander |
| Inaccurate customer output | Medium/High | Business Product Owner | Human review + QA | Pause publication |
| Unapproved vendor update | Medium/High | AI Manager + Security | Change notification, regression tests | Freeze deployment |

## Evidence/artefact pack for any release
Approved intake, requirements and data map, risk/control decisions, vendor agreement or PO, approved budget, UAT results, user guidance, access inventory, support owner, rollback plan, audit record and renewal decision.
