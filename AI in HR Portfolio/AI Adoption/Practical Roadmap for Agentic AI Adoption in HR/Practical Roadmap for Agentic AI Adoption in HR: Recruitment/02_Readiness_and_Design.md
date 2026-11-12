# Step 2: DESIGN — Organization readiness and end-to-end human–AI workflow

## Readiness assessment — evidence first

Use this **draft** seven-pillar weighted assessment: Process maturity 20%, data quality and rights 15%, identity/security/integrations 20%, applicable legal/ethics review 15%, skills/change capacity 10%, leadership/business measurement 10%, operations/testing 10%. Each pillar has a 0–4 maturity rating; **Readiness = Σ(weight × rating/4)**. A suggested ≥80/100 is only a *design threshold*; it cannot override failed mandatory controls.

### Specific readiness questions

1. **Hiring manager intake rubric and role approval:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.
2. **Recruiter and privacy owner for candidate-data use:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.
3. **ATS or sourcing integrations limited to read/draft:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.
4. **Authorized sourcing licenses and lawful data processing:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.
5. **Manual baseline for intake and sourcing work:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.

**Non-negotiable gate:** lawful data source and processing basis (review applicable UAE/free-zone/sector requirements), approved owner, actual identity/tool enforcement, confirmed staff review capacity, emergency shutdown/manual fallback and validated benchmark. Do not pilot if any critical gate fails, regardless of weighted readiness score.

## Agent definition

- **Agent:** Recruitment Intake & Sourcing Research Agent.
- **Approved input candidates:** Approved job description, objective role criteria, permitted talent-market sources.
- **Only authorized activities:** read approved vacancy data, draft intake checklist and sourcing query, prepare candidate communication drafts, route to recruiter review.
- **Explicitly forbidden:** no ATS status updates, applicant rejection, unauthorized scraping, direct unsolicited sends or offers.
- **Accountable owner:** Head of Talent Acquisition; independent technical enforcement by IT/Security and applicable-law review by Legal/Privacy.

## Proposed workflow (DESIGN, not deployed)

1. Human submits a task through authenticated role-scoped intake; purpose and permitted data checked.
2. Independent application policy service validates source, user/agent identity, action scope and data classification BEFORE any retrieval or tool call.
3. Agent classifies the request and retrieves only approved versioned sources; records uncertainty and attribution.
4. Agent proposes the permitted draft/checklist/diagnostic; any sensitive or consequential item moves to a named human-review queue.
5. Authorized Head of Talent Acquisition or delegate reviews, edits, approves or rejects; the system prevents independent high-impact writes by the agent.
6. Versioned redacted logs store request ID, tool action, source version, permission decision and reviewer outcome; monitor and allow security to revoke permissions.

## Escalate, abstain or stop

- When **discriminatory brief** appears, the system must **flag non-job-related criteria and require recruiter/legal review**, and route unresolved matters to a trained human.
- When **candidate data leaks** appears, the system must **least privilege, no unauthorized scraping or export**, and route unresolved matters to a trained human.
- When **unsupported profile claims** appears, the system must **source citation and independent recruiter verification**, and route unresolved matters to a trained human.
- When **unapproved email or ats write** appears, the system must **draft-only tools; separate human-send and status authority**, and route unresolved matters to a trained human.
- When **misleading sourcing research** appears, the system must **source quality, freshness and coverage review**, and route unresolved matters to a trained human.

## Implementation options (not asserted as tested)

Microsoft Copilot Studio, Teams, SharePoint/OneDrive, Entra ID, Power Automate and an approved HR platform **could** be used if the actual tenant supports the required policy and auditing. An alternative is a restricted Python API orchestration and deterministic policy engine. The agent must not grant or widen tool permissions through prompts; external runtime authorization, network restrictions and least-privilege access must enforce boundaries.