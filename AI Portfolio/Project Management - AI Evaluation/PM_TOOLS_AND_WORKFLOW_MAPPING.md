# Jira / Asana / MS Project — Project Tracking Field Map

**Purpose:** demonstrate practical understanding of common project-management data fields. This is a vendor-agnostic reference design only; there is **no live connection** to Jira, Asana or Microsoft Project.

| PM requirement | Generic data concept | Jira-style field | Asana-style field | MS Project-style field |
| --- | --- | --- | --- | --- |
| Work breakdown | Project work item | Issue / Epic / Task | Task / Section / Project | Task / Summary task |
| Accountable owner | Responsible person | Assignee | Assignee | Resource Name |
| Target date | Deadline | Due Date / Sprint | Due Date | Finish |
| Depends on | Predecessor constraint | Issue link (blocks) | Dependency | Predecessors |
| Progress | Status / completion | Status | Completed / Custom status | % Complete |
| Capacity | Resource availability | Story points / Sprint load / assignee | Custom numeric effort field | Resource units / Work |
| Delivery concerns | Impediment, issue, risk | Issue type / label / custom field | Task / custom field | Notes / custom fields |
| Change governance | Controlled baseline change | Change request ticket | Approval / project task | Baseline / change documentation |

## Workflow concept

Capture requirements and task hierarchy; assign accountable owners; estimate work; map dependencies; identify the critical path where applicable; review capacity versus planned effort; document risks; check schedule/cost metrics; communicate milestone status; log change approvals; compare planned versus actual progress.

## Boundaries

Fields and menus vary by edition, organization, configuration and API version. The crosswalk shows conceptual familiarity, **not** completed work in these vendor platforms. No screenshots, exported project files, credentials or sync jobs are asserted.