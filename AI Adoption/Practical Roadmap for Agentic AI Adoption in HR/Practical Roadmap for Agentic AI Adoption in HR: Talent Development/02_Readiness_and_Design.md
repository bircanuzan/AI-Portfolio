# Step 2: DESIGN — Organization readiness and end-to-end human–AI workflow

## Readiness assessment — evidence first

Use this **draft** seven-pillar weighted assessment: Process maturity 20%, data quality and rights 15%, identity/security/integrations 20%, applicable legal/ethics review 15%, skills/change capacity 10%, leadership/business measurement 10%, operations/testing 10%. Each pillar has a 0–4 maturity rating; **Readiness = Σ(weight × rating/4)**. A suggested ≥80/100 is only a *design threshold*; it cannot override failed mandatory controls.

### Specific readiness questions

1. **Validated role-specific competency models:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.
2. **Employee choice, notice and lawful processing:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.
3. **Learning/mentoring options available and current:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.
4. **Manager coaching and feedback capacity:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.
5. **Fair development access and dispute mechanism:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.

**Non-negotiable gate:** lawful data source and processing basis (review applicable UAE/free-zone/sector requirements), approved owner, actual identity/tool enforcement, confirmed staff review capacity, emergency shutdown/manual fallback and validated benchmark. Do not pilot if any critical gate fails, regardless of weighted readiness score.

## Agent definition

- **Agent:** Competency Gap-to-Individual Development Plan Co-Design Agent.
- **Approved input candidates:** Approved job family skills, documented consented development inputs, learning/mentoring catalogue and competency rubric.
- **Only authorized activities:** draft skills-gap narrative with traceable evidence, SMART goals, learning/coaching options, manager/employee discussion template.
- **Explicitly forbidden:** no autonomous high-potential labels, ratings, promotion, salary, protected-trait inference or employee enrollment without approval.
- **Accountable owner:** Talent Development Lead; independent technical enforcement by IT/Security and applicable-law review by Legal/Privacy.

## Proposed workflow (DESIGN, not deployed)

1. Human submits a task through authenticated role-scoped intake; purpose and permitted data checked.
2. Independent application policy service validates source, user/agent identity, action scope and data classification BEFORE any retrieval or tool call.
3. Agent classifies the request and retrieves only approved versioned sources; records uncertainty and attribution.
4. Agent proposes the permitted draft/checklist/diagnostic; any sensitive or consequential item moves to a named human-review queue.
5. Authorized Talent Development Lead or delegate reviews, edits, approves or rejects; the system prevents independent high-impact writes by the agent.
6. Versioned redacted logs store request ID, tool action, source version, permission decision and reviewer outcome; monitor and allow security to revoke permissions.

## Escalate, abstain or stop

- When **unfair opportunities** appears, the system must **review comparable employees' access to development options**, and route unresolved matters to a trained human.
- When **unsupported skill-gap inference** appears, the system must **ground in consented documented evidence**, and route unresolved matters to a trained human.
- When **unwanted personal profiling** appears, the system must **data minimization and employee control**, and route unresolved matters to a trained human.
- When **unavailable or irrelevant course** appears, the system must **verify learning catalogue validity**, and route unresolved matters to a trained human.
- When **unauthorized hr career decision** appears, the system must **no HRIS/performance write connector**, and route unresolved matters to a trained human.

## Implementation options (not asserted as tested)

Microsoft Copilot Studio, Teams, SharePoint/OneDrive, Entra ID, Power Automate and an approved HR platform **could** be used if the actual tenant supports the required policy and auditing. An alternative is a restricted Python API orchestration and deterministic policy engine. The agent must not grant or widen tool permissions through prompts; external runtime authorization, network restrictions and least-privilege access must enforce boundaries.