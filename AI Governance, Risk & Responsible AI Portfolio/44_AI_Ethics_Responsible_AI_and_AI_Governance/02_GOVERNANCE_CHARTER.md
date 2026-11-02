# Fictional Enterprise AI Governance Charter — v0.1
**Organisation:** SampleCo UAE (imaginary). **Sponsor:** COO. **Control owner:** Responsible AI Officer (second-line). **Scope:** all internally built, purchased, embedded, predictive, generative and autonomous AI uses. **Approval:** proposed, not adopted.

## Policy objectives
- Protect fundamental rights, dignity, fairness, privacy, security, safety and lawful use.
- Keep a named **human accountable** for every AI-assisted material decision.
- Maintain a traceable inventory of systems, providers, versions, intended purpose, end users, data, risk tier and current approvals.
- Require impact assessment, controls and independently reviewed evidence commensurate with risk.
- Permit innovation via sandboxes **without production data or autonomous production actions** until approved.
- Monitor AI output quality, abuse, drift, changes, incidents and eventual retirement.

## Roles, decision rights and three lines of defence
| Accountability | Responsible | Independent challenge and sign-off |
|---|---|---|
| Business outcome, use-case purpose, user notices | Business system owner (1st line) | AI Governance Committee |
| Model/agent design, tests, safety, logs, release | Product + Engineering (1st line) | AI Assurance Lead (separate reviewer) |
| Data quality, lineage, classification and retention | Data Steward / DPO team | Privacy Officer / Legal |
| Threat review, secrets, tool privileges, penetration testing | Information Security | CISO delegate |
| Ethical impact, tiering, control requirements, exceptions | AI Governance Office (2nd line) | Enterprise Risk committee |
| Independent audit of programme operation | Internal Audit (3rd line) | Audit Committee |
| Production go-live | Named business executive | Governance Committee for high-tier / material change |

**Conflict-of-interest rule:** the engineer or vendor implementing a system cannot certify their own high-tier release. No approval by silence.

## Internal AI tiers (NOT EU AI Act statutory classification)
- **T1 Low:** assistance without personal data or consequential action; authorised for limited use after baseline reviews.
- **T2 Moderate:** identifiable information or business process influence; impact assessment, privacy/security reviews and documented UAT.
- **T3 High:** affects employment/financial outcomes, vulnerable individuals, consequential automated recommendations or access to critical systems. Requires independent ethics and fairness review, model assurance and **mandatory human final decision**.
- **T4 Prohibited by SampleCo policy:** covert inference of protected/sensitive traits, discriminatory decision rules, autonomous material adverse decisions without meaningful human oversight, unapproved mass export of PII, or safety-critical agent actions beyond authorised controls. **NO_GO**.

### Governance committee
Monthly and urgent incident-triggered meetings: COO chair, Legal/DPO, Risk, CISO, Data/ML, HR, Operations, Internal Audit (observer). Quorum COO or delegated sponsor plus Risk, Security, Privacy and system owner. Record versions, objections and the accountable approver. Conflict escalations go to Board Risk Committee.

### Lifecycle gates
0. Discovery / register system -> 1. Privacy and ethical impact screening -> 2. Risk tier and control plan -> 3. Build/vendor review -> 4. Independent prelaunch TEVV and UAT -> 5. Formal GO/HOLD/NO_GO -> 6. Post-launch monitoring -> 7. Material change revalidation -> 8. Incident response or retirement. Every stage requires an evidence link and a named owner.

### Non-negotiables
- Human appeal/contestability and accessible explanation for affected individuals where appropriate.
- Privacy-by-design: data minimisation, purpose limitation, least privilege, approved retention and deletion.
- Vendor model/agent version changes trigger reassessment for material impacts.
- Material model error, privacy breach, harmful bias, tool misuse or loss of human override -> suspend and investigate.
- Project-level risk acceptance never overrides law or fundamental rights.

### Measurements and cadence
Coverage of AI inventory, percent impact-assessed, percent gated pre-release, number overdue high risks, high-severity incidents, independent QA completion, control exceptions overdue, incident-to-containment hours, model monitoring coverage, 90-day remedial closure. Weekly operational review, monthly committee and quarterly board report.

### Framework application
NIST **GOVERN**: charter and accountability; **MAP**: system inventory and context; **MEASURE**: testing and evidence; **MANAGE**: decisions, mitigation and monitoring. ISO/IEC 42001 informs the management-system cycle; ISO/IEC 23894 informs risk treatment. No claim of conformity audit or certificate.
