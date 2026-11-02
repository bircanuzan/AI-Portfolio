# Step 2: DESIGN — Organization readiness and end-to-end human–AI workflow

## Readiness assessment — evidence first

Use this **draft** seven-pillar weighted assessment: Process maturity 20%, data quality and rights 15%, identity/security/integrations 20%, applicable legal/ethics review 15%, skills/change capacity 10%, leadership/business measurement 10%, operations/testing 10%. Each pillar has a 0–4 maturity rating; **Readiness = Σ(weight × rating/4)**. A suggested ≥80/100 is only a *design threshold*; it cannot override failed mandatory controls.

### Specific readiness questions

1. **Publisher license and permitted report use:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.
2. **Qualified psychometric practitioner review and sign-off:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.
3. **Competency framework, norm/version governance:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.
4. **Assessment fairness and accommodation process:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.
5. **Restricted candidate report storage and processing authorization:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.

**Non-negotiable gate:** lawful data source and processing basis (review applicable UAE/free-zone/sector requirements), approved owner, actual identity/tool enforcement, confirmed staff review capacity, emergency shutdown/manual fallback and validated benchmark. Do not pilot if any critical gate fails, regardless of weighted readiness score.

## Agent definition

- **Agent:** Psychometric & Competency Assessment Evidence QA Agent.
- **Approved input candidates:** Approved competency rubric; authorized publisher report metadata; licensed extract rights; assessor notes with permission.
- **Only authorized activities:** flag missing score fields, mismatched candidate IDs and rubric evidence; draft human assessor briefing.
- **Explicitly forbidden:** no test item disclosure, invented normative scores, clinical inferences, proprietary report redistribution or candidate selection.
- **Accountable owner:** Talent Assessment Practice Lead; independent technical enforcement by IT/Security and applicable-law review by Legal/Privacy.

## Proposed workflow (DESIGN, not deployed)

1. Human submits a task through authenticated role-scoped intake; purpose and permitted data checked.
2. Independent application policy service validates source, user/agent identity, action scope and data classification BEFORE any retrieval or tool call.
3. Agent classifies the request and retrieves only approved versioned sources; records uncertainty and attribution.
4. Agent proposes the permitted draft/checklist/diagnostic; any sensitive or consequential item moves to a named human-review queue.
5. Authorized Talent Assessment Practice Lead or delegate reviews, edits, approves or rejects; the system prevents independent high-impact writes by the agent.
6. Versioned redacted logs store request ID, tool action, source version, permission decision and reviewer outcome; monitor and allow security to revoke permissions.

## Escalate, abstain or stop

- When **publisher ip or score misuse** appears, the system must **license register; prohibit restricted test material reproduction**, and route unresolved matters to a trained human.
- When **fabricated score interpretations** appears, the system must **qualified assessor checks norm, instrument version and validity**, and route unresolved matters to a trained human.
- When **unfair candidate impact** appears, the system must **job-related validity, bias review and human decision ownership**, and route unresolved matters to a trained human.
- When **sensitive psychometric data leak** appears, the system must **least privilege and retention controls**, and route unresolved matters to a trained human.
- When **automated selection** appears, the system must **no final ranking/hiring decision connector**, and route unresolved matters to a trained human.

## Implementation options (not asserted as tested)

Microsoft Copilot Studio, Teams, SharePoint/OneDrive, Entra ID, Power Automate and an approved HR platform **could** be used if the actual tenant supports the required policy and auditing. An alternative is a restricted Python API orchestration and deterministic policy engine. The agent must not grant or widen tool permissions through prompts; external runtime authorization, network restrictions and least-privilege access must enforce boundaries.