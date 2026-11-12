# Business Process Mapping and Gap Analysis
**Illustrative case study, not a real client engagement.**
## Scenario
A hypothetical 250-employee company processes HR policy enquiries by email. Employees face slow responses and repeated routing between teams.
## AS-IS workflow
Employee emails shared inbox → Coordinator reads question → Coordinator finds correct policy owner → Owner searches documents → Owner drafts response → Coordinator replies → No structured issue data.
## Observed/potential gaps (hypotheses to validate)
Unclear ownership, duplicate requests, no version control, missing response categories, no feedback analytics.
## TO-BE workflow
Employee enters question → Intake classifies category → Approved knowledge article lookup → **Decision: supported answer?**
- Yes: show source-linked answer → employee confirms helpfulness → log aggregate metrics.
- No / sensitive / ambiguous: create human service ticket → owner resolves → approved knowledge base updated.
## Swimlane roles
Employee: request, review; HR service desk: classify, resolve and escalate; Policy owner: approve source; IT/AI team: tool access, integrations and model maintenance.
## Gap-to-action matrix
| Gap | Proposed change | Owner | Validation metric |
|---|---|---|---|
| Duplicate requests | Categorized request intake | HR Ops | Repeat enquiry rate |
| Outdated policies | Document owner and review cycle | Policy owners | Current-version coverage |
| No escalation | Ticket routing | HR Ops / IT | Escalation closure time |
| AI hallucination risk | Grounding, review and abstention | AI team / policy owners | Unsupported-answer rate |
## Prioritization
Prioritize low-risk FAQs and source governance before any AI rollout. Keep employment decisions and personal HR record changes outside automated scope.
