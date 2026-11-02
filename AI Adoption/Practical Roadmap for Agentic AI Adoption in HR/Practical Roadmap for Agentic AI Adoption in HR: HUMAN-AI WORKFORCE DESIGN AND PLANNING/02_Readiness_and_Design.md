# Step 2: DESIGN — Organization readiness and end-to-end human–AI workflow

## Readiness assessment — evidence first

Use this **draft** seven-pillar weighted assessment: Process maturity 20%, data quality and rights 15%, identity/security/integrations 20%, applicable legal/ethics review 15%, skills/change capacity 10%, leadership/business measurement 10%, operations/testing 10%. Each pillar has a 0–4 maturity rating; **Readiness = Σ(weight × rating/4)**. A suggested ≥80/100 is only a *design threshold*; it cannot override failed mandatory controls.

### Specific readiness questions

1. **Validated task decompositions with process owner:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.
2. **Reconciled work volume and handling-time sources:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.
3. **HR/finance executive scenario ownership:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.
4. **Workforce consultation and change impact process:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.
5. **Skills architecture and reskilling plan:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.

**Non-negotiable gate:** lawful data source and processing basis (review applicable UAE/free-zone/sector requirements), approved owner, actual identity/tool enforcement, confirmed staff review capacity, emergency shutdown/manual fallback and validated benchmark. Do not pilot if any critical gate fails, regardless of weighted readiness score.

## Agent definition

- **Agent:** Human–AI Task Allocation & Capacity Scenario Agent.
- **Approved input candidates:** Approved task-level process maps, measured handling times, competency framework, workload, constraints and scenario assumptions.
- **Only authorized activities:** draft task allocation, scenario ranges, uncertainty and oversight matrices, reskilling gap plan for expert review.
- **Explicitly forbidden:** no headcount-change execution, redundancies, personnel scoring, HRIS writes, assertions that time savings equal job cuts.
- **Accountable owner:** Head of HR Transformation / Workforce Planning; independent technical enforcement by IT/Security and applicable-law review by Legal/Privacy.

## Proposed workflow (DESIGN, not deployed)

1. Human submits a task through authenticated role-scoped intake; purpose and permitted data checked.
2. Independent application policy service validates source, user/agent identity, action scope and data classification BEFORE any retrieval or tool call.
3. Agent classifies the request and retrieves only approved versioned sources; records uncertainty and attribution.
4. Agent proposes the permitted draft/checklist/diagnostic; any sensitive or consequential item moves to a named human-review queue.
5. Authorized Head of HR Transformation / Workforce Planning or delegate reviews, edits, approves or rejects; the system prevents independent high-impact writes by the agent.
6. Versioned redacted logs store request ID, tool action, source version, permission decision and reviewer outcome; monitor and allow security to revoke permissions.

## Escalate, abstain or stop

- When **falsely precise fte savings** appears, the system must **use transparent ranges and sensitivity testing**, and route unresolved matters to a trained human.
- When **unsafe delegation of accountable work** appears, the system must **human legal/business approval maintained**, and route unresolved matters to a trained human.
- When **workforce trust and morale harms** appears, the system must **meaningful consultation and communications**, and route unresolved matters to a trained human.
- When **incorrect process baseline** appears, the system must **validated time/task source and assumptions**, and route unresolved matters to a trained human.
- When **automated job loss action** appears, the system must **prohibit termination or staffing changes**, and route unresolved matters to a trained human.

## Implementation options (not asserted as tested)

Microsoft Copilot Studio, Teams, SharePoint/OneDrive, Entra ID, Power Automate and an approved HR platform **could** be used if the actual tenant supports the required policy and auditing. An alternative is a restricted Python API orchestration and deterministic policy engine. The agent must not grant or widen tool permissions through prompts; external runtime authorization, network restrictions and least-privilege access must enforce boundaries.