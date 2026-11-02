# Step 4 — GOVERN: UAE-first governance roadmap, standards and risk controls

Governance starts in prioritization and design, applies throughout the pilot and becomes stricter as autonomy or scope increases.

## A. UAE applicability comes first

### 1. UAE federal Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)

**Why relevant:** HR agents often process personal data. Counsel/privacy must determine whether this federal regime, DIFC/ADGM regime, sector-specific law, government exclusions or cross-border requirements apply.

**Design decisions:** purpose and lawful-basis review, data minimization, need-to-know access, explicit retention/deletion, processor/vendor evaluation, international transfer review, employee request/rights handling, incident assessment.

**How verified:** signed legal applicability and data-flow memo; user-role denial tests; inspection of logs/storage; vendor record and retention tests. No claim that a particular cloud configuration automatically ensures UAE PDPL compliance.

### 2. Digital Dubai AI Ethics Guidelines and Self-Assessment

**Why:** Encourage fairness, accountability, transparency and explainability, and expose governance gaps across design/maintenance.

**Controls:** case sensitivity classification, human review gates, documented explanation and policy source, fairness/error pattern reviews, self-assessment with mitigation register.

**Evidence:** dated assessment, actions closed, independent review. These ethics guidelines are recommended/not compulsory and a self-assessment is NOT an external certification.

### 3. UAE Charter for the Development and Use of AI

**Why:** National policy principles stress human oversight, safety, privacy, bias mitigation, transparency, governance and alignment with applicable laws.

**Controls:** human ownership of significant HR decisions; approved use cases and rights-based escalation; refusal/hold for unfair or unsafe actions; incident accountability.

**Evidence:** signed policy, RACI, documented risk assessment, named HR approver.

### 4. Dubai Universal Blueprint / Dubai AI Seal (where supplier relevant)

**Why:** Dubai's strategic AI initiative and AI supplier verification mechanism may support procurement diligence.

**Controls:** independently assess supplier security, DPA, hosting/data flows, permissions and delivery evidence. A vendor AI Seal (if applicable) is **not** a substitute for system-specific safety testing or legal review.

## B. Global standards applied as practical methods

| Framework | What it is | Application to THIS agent | Evidence |
|---|---|---|---|
| ISO/IEC 42001:2023 | AI management-system standard | Governance policy, owner, documentation, change control and management review | Signed policy, review log |
| ISO/IEC 23894:2023 | AI risk-management guidance | Identify/matrix harms; mitigation, residual risk and reassessment | Risk register |
| ISO/IEC 42005:2025 | AI system impact-assessment guidance | Document effects on employees and HR service quality across lifecycle | Impact assessment |
| ISO/IEC 38507:2022 | Governance guidance for organizations | Executive accountability and approval authority | RACI, decisions |
| NIST AI RMF 1.0 / NIST GenAI Profile | Voluntary risk framework and GenAI profile | GOVERN: roles; MAP: use, data, impacts; MEASURE: evaluations; MANAGE: monitoring/hold | Versioned evidence |
| OWASP Top 10 for Agentic Applications 2026 | Security risk resource | Goal hijack, tool misuse, privilege abuse, memory poisoning, trust exploitation, cascading failures | Threat model, adversarial tests |
| OECD / UNESCO principles | Nonbinding trustworthy/human-centered guidance | Explainability, meaningful human control, inclusion | Notices, fairness check |

**Scope note:** ISO conformity or certification is NOT claimed. The EU AI Act is only considered if materially and territorially applicable to an organization; do not assume any UAE-only HR activity is automatically governed by it.

## C. Controls chosen, why they matter, and proof required

| Control / owner | Why this one? | Evidence of enforcement |
|---|---|---|
| AC01 — HR-approved use-case and agent charter | Prevent scope creep | Signed inventory, tool matrix |
| AC02 — Entra/SSO identity and RBAC | Deny unauthorized employees or agents | Role-negative tests |
| AC03 — Retrieval from versioned, approved HR policies only | Reduce obsolete or invented policy advice | Citation/version tests |
| AC04 — Read-only HR data and blocked payroll/ATS writes | Limit consequential harm | Actual tool denial logs |
| AC05 — Structured approval and human escalation | Preserve accountable judgment | Approval/rejection trace |
| AC06 — Data minimization, retention and vendor flow controls | Protect employee privacy | DPA/data map, logging inspection |
| AC07 — Prompt injection/tool misuse protection | Defend untrusted email/docs | Offensive test suite with real traces |
| AC08 — Confidential case detection and abstention | Route complex/sensitive cases to humans | Sensitivity-recall test |
| AC09 — Response correctness and fairness review | Prevent unsafe/unfair recommendations | Adjudicated scorecard |
| AC10 — Audit logs and independent incident ownership | Reconstruct decisions/stop failures | Trace completeness and drill |
| AC11 — Prompt/model/tool versioning and regression gate | Prevent silent degradation | Release records and retest |
| AC12 — Kill switch, rollback and safe fallback | Contain compromise/outage | Actual disable/revocation drill |

**Gaps and exceptions:** Record owner, severity, remediation, compensating controls and expiry. No critical unmitigated issue can be overridden by a high value score.

Full crosswalk: [11_Governance_Control_Matrix.csv](11_Governance_Control_Matrix.csv); risk register: [12_Risk_Register.csv](12_Risk_Register.csv).