# Step 2: DESIGN — Organization readiness and end-to-end human–AI workflow

## Readiness assessment — evidence first

Use this **draft** seven-pillar weighted assessment: Process maturity 20%, data quality and rights 15%, identity/security/integrations 20%, applicable legal/ethics review 15%, skills/change capacity 10%, leadership/business measurement 10%, operations/testing 10%. Each pillar has a 0–4 maturity rating; **Readiness = Σ(weight × rating/4)**. A suggested ≥80/100 is only a *design threshold*; it cannot override failed mandatory controls.

### Specific readiness questions

1. **Single owned definition for workforce metrics:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.
2. **Governed data catalogue and reconciled source systems:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.
3. **Row-level security and minimum group-size suppression:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.
4. **Analyst peer review and SQL/version tests:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.
5. **Privacy sign-off for aggregate use and transfers:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.

**Non-negotiable gate:** lawful data source and processing basis (review applicable UAE/free-zone/sector requirements), approved owner, actual identity/tool enforcement, confirmed staff review capacity, emergency shutdown/manual fallback and validated benchmark. Do not pilot if any critical gate fails, regardless of weighted readiness score.

## Agent definition

- **Agent:** Aggregate Workforce Insight & Data Quality Triage Agent.
- **Approved input candidates:** Approved aggregate HR data mart, controlled metric glossary, query permissions and time-period definitions.
- **Only authorized activities:** read aggregate-approved SQL views, validate denominators, flag anomalies, draft source-backed report for analyst review.
- **Explicitly forbidden:** no direct HRIS writes, row-level employee histories, small-cell disclosure, causal claims without evidence or worker-targeting outcomes.
- **Accountable owner:** People Analytics Lead; independent technical enforcement by IT/Security and applicable-law review by Legal/Privacy.

## Proposed workflow (DESIGN, not deployed)

1. Human submits a task through authenticated role-scoped intake; purpose and permitted data checked.
2. Independent application policy service validates source, user/agent identity, action scope and data classification BEFORE any retrieval or tool call.
3. Agent classifies the request and retrieves only approved versioned sources; records uncertainty and attribution.
4. Agent proposes the permitted draft/checklist/diagnostic; any sensitive or consequential item moves to a named human-review queue.
5. Authorized People Analytics Lead or delegate reviews, edits, approves or rejects; the system prevents independent high-impact writes by the agent.
6. Versioned redacted logs store request ID, tool action, source version, permission decision and reviewer outcome; monitor and allow security to revoke permissions.

## Escalate, abstain or stop

- When **reidentification in small groups** appears, the system must **minimum cohort-size guard and suppression**, and route unresolved matters to a trained human.
- When **incorrect denominator or metric** appears, the system must **approved semantic layer and SQL unit tests**, and route unresolved matters to a trained human.
- When **fabricated causal story** appears, the system must **uncertainty language, source attribution and analyst review**, and route unresolved matters to a trained human.
- When **unauthorized raw employee data access** appears, the system must **aggregate-only read views, access and export limits**, and route unresolved matters to a trained human.
- When **discriminatory personnel inference** appears, the system must **no individual scores or consequential decisions**, and route unresolved matters to a trained human.

## Implementation options (not asserted as tested)

Microsoft Copilot Studio, Teams, SharePoint/OneDrive, Entra ID, Power Automate and an approved HR platform **could** be used if the actual tenant supports the required policy and auditing. An alternative is a restricted Python API orchestration and deterministic policy engine. The agent must not grant or widen tool permissions through prompts; external runtime authorization, network restrictions and least-privilege access must enforce boundaries.