# Step 2: DESIGN — Organization readiness and end-to-end human–AI workflow

## Readiness assessment — evidence first

Use this **draft** seven-pillar weighted assessment: Process maturity 20%, data quality and rights 15%, identity/security/integrations 20%, applicable legal/ethics review 15%, skills/change capacity 10%, leadership/business measurement 10%, operations/testing 10%. Each pillar has a 0–4 maturity rating; **Readiness = Σ(weight × rating/4)**. A suggested ≥80/100 is only a *design threshold*; it cannot override failed mandatory controls.

### Specific readiness questions

1. **Survey notices and anonymity/consent governance:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.
2. **Reliable thresholded aggregation and suppression:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.
3. **OD leadership sponsorship and consultation process:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.
4. **Human review coding rubric and source traceability:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.
5. **Action execution/feedback owners and ethical escalation:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.

**Non-negotiable gate:** lawful data source and processing basis (review applicable UAE/free-zone/sector requirements), approved owner, actual identity/tool enforcement, confirmed staff review capacity, emergency shutdown/manual fallback and validated benchmark. Do not pilot if any critical gate fails, regardless of weighted readiness score.

## Agent definition

- **Agent:** Aggregate Organizational Diagnosis & Change Experiment Agent.
- **Approved input candidates:** Properly authorized anonymized survey summaries, sufficiently large aggregates, approved change data and OD framework.
- **Only authorized activities:** classify aggregate themes, express uncertainty, draft interventions and change feedback checkpoints for OD owner.
- **Explicitly forbidden:** no individual employee monitoring, low-cell reidentification, unreviewed quotations, retaliation recommendations or restructuring decisions.
- **Accountable owner:** Organizational Development Lead; independent technical enforcement by IT/Security and applicable-law review by Legal/Privacy.

## Proposed workflow (DESIGN, not deployed)

1. Human submits a task through authenticated role-scoped intake; purpose and permitted data checked.
2. Independent application policy service validates source, user/agent identity, action scope and data classification BEFORE any retrieval or tool call.
3. Agent classifies the request and retrieves only approved versioned sources; records uncertainty and attribution.
4. Agent proposes the permitted draft/checklist/diagnostic; any sensitive or consequential item moves to a named human-review queue.
5. Authorized Organizational Development Lead or delegate reviews, edits, approves or rejects; the system prevents independent high-impact writes by the agent.
6. Versioned redacted logs store request ID, tool action, source version, permission decision and reviewer outcome; monitor and allow security to revoke permissions.

## Escalate, abstain or stop

- When **response reidentification** appears, the system must **suppress distinctive quotes and small groups**, and route unresolved matters to a trained human.
- When **unjustified causal explanation** appears, the system must **require evidence, alternatives and hypotheses**, and route unresolved matters to a trained human.
- When **retaliation/surveillance misuse** appears, the system must **no individual rankings or negative-comment attribution**, and route unresolved matters to a trained human.
- When **biased sentiment coding** appears, the system must **independent human review and language coverage**, and route unresolved matters to a trained human.
- When **unapproved intervention/restructure** appears, the system must **oD and leadership approval before changes**, and route unresolved matters to a trained human.

## Implementation options (not asserted as tested)

Microsoft Copilot Studio, Teams, SharePoint/OneDrive, Entra ID, Power Automate and an approved HR platform **could** be used if the actual tenant supports the required policy and auditing. An alternative is a restricted Python API orchestration and deterministic policy engine. The agent must not grant or widen tool permissions through prompts; external runtime authorization, network restrictions and least-privilege access must enforce boundaries.