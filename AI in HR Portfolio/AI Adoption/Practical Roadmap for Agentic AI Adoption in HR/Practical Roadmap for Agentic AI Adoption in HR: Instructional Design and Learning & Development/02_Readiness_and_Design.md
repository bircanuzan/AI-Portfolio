# Step 2: DESIGN — Organization readiness and end-to-end human–AI workflow

## Readiness assessment — evidence first

Use this **draft** seven-pillar weighted assessment: Process maturity 20%, data quality and rights 15%, identity/security/integrations 20%, applicable legal/ethics review 15%, skills/change capacity 10%, leadership/business measurement 10%, operations/testing 10%. Each pillar has a 0–4 maturity rating; **Readiness = Σ(weight × rating/4)**. A suggested ≥80/100 is only a *design threshold*; it cannot override failed mandatory controls.

### Specific readiness questions

1. **Evidence-based learning needs and learner profiles:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.
2. **Licensed source material with clear usage rights:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.
3. **Instructional design quality rubric and accessible learning standards:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.
4. **Instructional SME availability and review capacity:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.
5. **LMS test-only access and learner impact evaluation:** What documented procedures, named owners, access logs or validated datasets demonstrate readiness? If evidence is missing, mark UNASSESSED rather than pass.

**Non-negotiable gate:** lawful data source and processing basis (review applicable UAE/free-zone/sector requirements), approved owner, actual identity/tool enforcement, confirmed staff review capacity, emergency shutdown/manual fallback and validated benchmark. Do not pilot if any critical gate fails, regardless of weighted readiness score.

## Agent definition

- **Agent:** Learning Needs-to-Curriculum Design Agent.
- **Approved input candidates:** Approved skills framework, learner needs analysis, licensed training assets, accessibility policy and SME-approved content.
- **Only authorized activities:** draft learning objectives, curriculum map, storyboard, activities and aligned assessment blueprint for SME review.
- **Explicitly forbidden:** no unapproved LMS publishing, certifications, copyrighted content copying, unsupported regulated instruction or learner profiling.
- **Accountable owner:** Head of Learning & Development; independent technical enforcement by IT/Security and applicable-law review by Legal/Privacy.

## Proposed workflow (DESIGN, not deployed)

1. Human submits a task through authenticated role-scoped intake; purpose and permitted data checked.
2. Independent application policy service validates source, user/agent identity, action scope and data classification BEFORE any retrieval or tool call.
3. Agent classifies the request and retrieves only approved versioned sources; records uncertainty and attribution.
4. Agent proposes the permitted draft/checklist/diagnostic; any sensitive or consequential item moves to a named human-review queue.
5. Authorized Head of Learning & Development or delegate reviews, edits, approves or rejects; the system prevents independent high-impact writes by the agent.
6. Versioned redacted logs store request ID, tool action, source version, permission decision and reviewer outcome; monitor and allow security to revoke permissions.

## Escalate, abstain or stop

- When **copyright violation** appears, the system must **source rights review and no restricted text reproduction**, and route unresolved matters to a trained human.
- When **pedagogically misaligned assessment** appears, the system must **objective-to-assessment mapping reviewed by ID SME**, and route unresolved matters to a trained human.
- When **inaccessible content** appears, the system must **accessibility, language and inclusive-design QA**, and route unresolved matters to a trained human.
- When **false or unsafe subject claims** appears, the system must **cite approved source and mandate SME validation**, and route unresolved matters to a trained human.
- When **unapproved publication** appears, the system must **lMS publishing API disabled for agent**, and route unresolved matters to a trained human.

## Implementation options (not asserted as tested)

Microsoft Copilot Studio, Teams, SharePoint/OneDrive, Entra ID, Power Automate and an approved HR platform **could** be used if the actual tenant supports the required policy and auditing. An alternative is a restricted Python API orchestration and deterministic policy engine. The agent must not grant or widen tool permissions through prompts; external runtime authorization, network restrictions and least-privilege access must enforce boundaries.