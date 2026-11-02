# 03 | Seven-app Microsoft 365 Copilot use-case and exercise library

**Licensing note:** This is a workshop *design*, not proof of active features in any tenant. Check licensing and feature availability live. Work/organisational grounding requires the right access, role and supported licence; examples may need to be simplified to manual file reference or Copilot Chat depending on entitlement.

## Outlook — draft a precise stakeholder update
**Business problem:** an HR leader needs to announce an updated internal policy. **Source:** [fictional business memo](sample_materials/fictional_policy_memo.md).

**Example request:** "Using only this approved fictional memo, draft a 180-word email for department managers. State the change, effective date, actions and contact; do not invent an approval, policy exception or legal obligation. Mark anything missing as [CHECK]."

**Acceptance:** correct date, action, source evidence, audience tone, no legal assurance, no invented company facts. Human policy owner approves before sending.

## Teams — meeting decisions and accountability
**Problem:** action items get lost. **Source:** [fictional meeting notes](sample_materials/fictional_meeting_notes.md).

**Example request:** "From these authorized notes, create an action table with decision, owner, due date, dependency and confidence. Label any unnamed owner or missing date as TBD; do not infer consent or attendance."

**Acceptance:** each action matches notes, unresolved fields not invented, and no summary of meetings the user is not authorized to access.

## Word — improve a business process brief
**Problem:** a service owner needs an accessible, readable SOP. **Source:** fictional policy memo.

**Example request:** "Convert the approved text into a one-page quick reference with purpose, audience, steps and escalation. Preserve exact policy meaning, distinguish required from recommended actions, and flag unclear wording."

**Acceptance:** clear headings, correct policy/approval boundary, no invented process steps.

## PowerPoint — executive decision story
**Problem:** leadership needs a concise business case. **Source:** [synthetic quarterly business brief](sample_materials/fictional_business_case.md).

**Example request:** "Outline a five-slide executive decision deck: business problem, current baseline, proposed safe use cases, risk controls, decision required. Label all financial figures hypothetical. No unsupported ROI claims."

**Acceptance:** logical story, supported figures, sponsorship/ownership, clear ask. Verify any generated deck and capability availability before demo.

## Excel — analyse a fictional team workload
**Problem:** an operations lead needs a weekly trend analysis from structured data. **Source:** [synthetic task records](sample_materials/fictional_workload.csv).

**Example request:** "Summarise tickets by team and priority, calculate average handling minutes, identify exceptions and produce a reproducible pivot/table design. Show the calculation method and do not infer performance ratings of individuals."

**Acceptance:** independent manual formulas or Excel results reconcile against raw CSV, correct denominators and no invented records. Availability of in-app Copilot and file storage requirements vary.

## OneDrive — find the authoritative file
**Problem:** employee cannot find latest policy. **Scenario:** compare authorised sample files and document metadata.

**Example request:** "Find the newest *approved* employee onboarding checklist available to me; provide title, owner, modification date and link, and say when approval status cannot be verified."

**Acceptance:** permissions respected, approved/current status confirmed separately, cannot claim "latest" just from filename.

## SharePoint — department knowledge discovery
**Problem:** staff use outdated SOPs from different sites.

**Example request:** "Using only content I am permitted to view on the approved SharePoint site, identify the published expense procedure and any conflicting versions. Include source link and review date, and defer unresolved conflicts to the content owner."

**Acceptance:** visible provenance, no bypass of access controls, unresolved conflicts escalated.

## Universal debrief — five reviewer questions
1. Does the output answer the original business question?
2. Are every material fact, figure and date traceable?
3. Was permitted data used and were permissions maintained?
4. What must a human validate, approve or change?
5. What would we measure if this became a repeatable business workflow?
