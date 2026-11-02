# Organizational readiness — can the organization adopt this HR agent safely?

This is a separate **pre-pilot** decision. A good use case does not mean the organization is ready.

## 1. Conduct evidence-based readiness interviews and controls review

Run workshops with HR Ops, IT/identity, information security, legal/privacy, HR leadership, finance, employee representatives where appropriate, and support-desk supervisors. Review real artifacts rather than self-reported optimism.

| Dimension (weight) | What must be assessed | Acceptable evidence |
|---|---|---|
| Process & policy quality (20) | Standard intake taxonomy; approved, current policy owners; exception rules | Versioned approved policies, sample ticket map and owners |
| Data & knowledge suitability (15) | Accuracy, lawful use, permissions, classification, retention and multilingual policy coverage | Data inventory, permissions audit, source QA |
| Identity / integrations / security (20) | SSO, RBAC, tool scoping, environment isolation, logging and revoke | IAM review, connector list, denied action test |
| UAE legal / AI governance (15) | PDPL or special regime applicability, ethics, impact assessment, risk owner | Counsel review, assessment, RACI |
| People / adoption (10) | HR service lead, user cohort, training, escalation staffing | Signed owner commitments, training plan |
| Leadership / economics (10) | Sponsor, budget, baseline owner, willingness to stop | Funding and baseline measurement plan |
| Operations / evaluation (10) | Incident operations, sample design, rubric and test capacity | Test plan, escalation rota, monitoring runbook |

**Ratings:** 0 = absent; 1 = documented intent only; 2 = partial / unverified; 3 = implemented with some evidence; 4 = verified and repeatable.  
**Readiness % = Σ(weight × rating/4).** Unknown and missing evidence are **NOT RATED**, not silently treated as passing. A *proposed* entry gate is ≥80/100 with every mandatory item approved.

## 2. Mandatory hard-stop checks (cannot be averaged away)

- [ ] An HR business owner accepts responsibility for outcomes and policy sources.
- [ ] Privacy/legal determine applicable UAE laws, processing basis and vendor/data movement restrictions. DIFC, ADGM, sector and cross-border requirements assessed where relevant.
- [ ] All pilot data and policies are appropriately authorized; sensitive records excluded from scope.
- [ ] Entra/SSO or equivalent authentication, role checks and a tool allow-list are configured independently from model prompts.
- [ ] Agent cannot change ATS/HRIS/payroll, send messages or access confidential records without appropriate separate authorization; initial mode is restricted.
- [ ] Critical-case routing and manual fallback staff available.
- [ ] Security can revoke credentials and disable the tool; incident-response owner accepts duty.
- [ ] Agreed evaluation rubric and baseline instrumentation exist before exposure to users.

**Decision:** READINESS PASS / CONDITIONAL HOLD / NOT READY. The CSV is blank because no actual organization was assessed.

## 3. Capability and stakeholder gaps

- **HR:** service design and approved policy lifecycle; specify what requires a human.
- **IT:** identity, service account boundaries, versioning, integrations and sandbox.
- **Security:** threat model, prompt injection, privileged tool action blocks, alerting.
- **Legal/privacy:** applicable personal data requirements, vendor terms, retention and transfers.
- **HR users:** onboarding and practical escalation/override experience.
- **Finance/analytics:** baseline, attribution, cost model and scorecard.

## 4. Adoption/change approach

Explain which tasks are automated and which remain human-owned. Build with HR service agents, not around them: shadow workflow, collect error reports, publish known limitations, train on approvals and escalation, provide a visible help contact and feedback channel. Measure adoption and trust without penalizing staff for escalating safety concerns.

## 5. Readiness gate

Do not launch solely because a numerical score is high. Document unresolved control gaps, owners, dates, residual risk and explicit approval. Reassess after policy, connector, jurisdiction or operating-model changes.

**Evidence:** [Blank readiness scoring template](10_Readiness_Assessment_Template.csv).