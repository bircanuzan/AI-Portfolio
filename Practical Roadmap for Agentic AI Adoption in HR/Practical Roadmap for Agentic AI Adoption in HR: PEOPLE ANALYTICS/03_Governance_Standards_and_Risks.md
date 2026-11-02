# Step 4: GOVERN — UAE-first standards, safeguards, legal assessment and accountable controls

Governance is active in Steps 1–5, not postponed until after the pilot.

## UAE / Dubai applicability review (mandatory if relevant)

1. **UAE Personal Data Protection Law (Federal Decree-Law No. 45 of 2021), where applicable:** Determine legal and sector/free-zone scope, data purpose, lawful processing arrangements, vendors, storage, transfers, access and deletion. DIFC, ADGM and sector regimes may differ; obtain legal advice, do not assume one law applies universally.
2. **Digital Dubai AI Ethics and its self-assessment:** Evaluate fairness, accountability, transparency and explainability; track gaps. Digital Dubai says its ethics self-assessment guidance is recommended rather than compulsory, not an audit or certificate.
3. **UAE Charter for the Development and Use of AI:** Design for human oversight, safety, privacy, transparency and accountability; a charter is not a substitute for binding requirements.
4. **UAE employment, professional, equality and IP obligations, where applicable:** Review decisions affecting workers or applicants, permissions to use assessment instruments or licensed learning content, and individual rights; do not invent a mandatory AI-specific certification.
5. **Dubai Blueprint / AI Seal, where relevant:** Treat supplier verification as procurement information, not proof that this particular agent is safe/compliant.

## Global standards as an operating method, not compliance claims

| Source | Concrete implementation | Proof to request |
|---|---|---|
| ISO/IEC 42001:2023 AI management system | Governance policy, accountable owner, AI inventory and change approval | Policy approval, version and management reviews |
| ISO/IEC 23894 AI risk management | Harm identification, mitigation, residual-risk ownership | Reviewed risk register and approvals |
| ISO/IEC 42005 AI impact assessment | Lifecycle impacts on affected people and fairness | Signed impact worksheet and stakeholder feedback |
| ISO/IEC 38507 organizational governance | Human authority for high-impact decisions | RACI and management decision log |
| NIST AI RMF / GenAI Profile | GOVERN roles; MAP context; MEASURE tests; MANAGE incidents/changes | Evaluation reports, risk decisions and operations records |
| OWASP agentic security guidance | Prompt injection, tool misuse, privilege escalation and agent identity threats | Independent adversarial tests and denied-tool traces |

**No ISO certification, regulator clearance or legal conformity is claimed.** The EU AI Act is applicable only when legal scope is established, not automatically because the organization operates in the UAE.

## Workstream-specific material risks and design controls

1. **Reidentification in small groups.** Why it matters: the agent can create adverse people analytics outcomes if this failure is uncontrolled. **Control:** Minimum cohort-size guard and suppression. **Required proof:** an authorized negative test, recorded human review and permission/response trace, not simply an AI-generated assertion.

2. **Incorrect denominator or metric.** Why it matters: the agent can create adverse people analytics outcomes if this failure is uncontrolled. **Control:** Approved semantic layer and SQL unit tests. **Required proof:** an authorized negative test, recorded human review and permission/response trace, not simply an AI-generated assertion.

3. **Fabricated causal story.** Why it matters: the agent can create adverse people analytics outcomes if this failure is uncontrolled. **Control:** Uncertainty language, source attribution and analyst review. **Required proof:** an authorized negative test, recorded human review and permission/response trace, not simply an AI-generated assertion.

4. **Unauthorized raw employee data access.** Why it matters: the agent can create adverse people analytics outcomes if this failure is uncontrolled. **Control:** Aggregate-only read views, access and export limits. **Required proof:** an authorized negative test, recorded human review and permission/response trace, not simply an AI-generated assertion.

5. **Discriminatory personnel inference.** Why it matters: the agent can create adverse people analytics outcomes if this failure is uncontrolled. **Control:** No individual scores or consequential decisions. **Required proof:** an authorized negative test, recorded human review and permission/response trace, not simply an AI-generated assertion.

## General mandatory enforcement controls

- C01 — Human-approved agent charter, allowed purpose and owner; source inventory.
- C02 — Independent identity, RBAC and least-privilege access on every tool call.
- C03 — Versioned trusted sources, accuracy review and explicit abstention.
- C04 — No unapproved external communication or consequential system writes.
- C05 — Personal-data minimization, secure vendor flow and retention controls.
- C06 — Prompt-injection, tool abuse and exfiltration testing including actual DENY logs.
- C07 — Human oversight, fair outcomes, appropriate appeal and expert review.
- C08 — Redacted traceability, monitoring, change/retest gates, kill switch and manual fallback.

**Go/hold rule:** any demonstrated critical access violation, unauthorized high-impact action, serious privacy breach, missed human safeguard or unavailable rollback is a HOLD regardless of business benefit.