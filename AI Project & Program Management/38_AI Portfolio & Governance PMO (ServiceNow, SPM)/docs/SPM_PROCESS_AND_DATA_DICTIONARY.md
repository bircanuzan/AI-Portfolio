# ServiceNow SPM — Functional Design and Data Dictionary

The names below use standard *business concepts* in ServiceNow Strategic Portfolio Management. **These are illustrative integration fields, not assertions of specific ServiceNow database table/field API names.** Actual mappings must be reviewed in the tenant and product release.

| SPM domain | Demonstration records | Operational purpose | Governance control |
|---|---|---|---|
| Demand | demand_id, category, sponsor, stage, score, disposition | Capture AI use case / pilot demand | Mandatory classification and value evidence |
| Project | project_id, originating_demand, state, milestone, release gate | Convert qualified demand to controlled delivery | Linked approvals and RAID |
| Product | product_id, source demand, service owner, go-live, EOL policy | Transition successful pilot to product | Handover and lifecycle evidence |
| Funding | approved allocation, fiscal period, funding owner | Record authorised financial envelope | Approver, approval date and amount |
| Cost plan | estimated operating/capital costs by period | Forecast plan and compare with actual | Flag gap versus approved funds |
| Portfolio | strategy pillar, portfolio manager, risk band | Strategy fit and consistent taxonomy | Classification validation |
| Reporting | pipeline, financial health, risk exposure, benefit review | VP forum decision pack | Dated data-quality control |

## Demand-to-project and demand-to-product flow
```text
AI demand -> Intake check -> Qualification score -> Portfolio forum
                                   |
                     approve / defer / reject (logged)
                                   |
                     Approved + funding + control gates
                                   |
               +-------------------+-------------------+
               |                                       |
           PROJECT                                 PRODUCT
      charter/BRD/milestones                 owner/service/runbook
       UAT/security/RAID                       support/EOL policy
               |                                       |
           acceptance                     operational handover
               +-------------------+-------------------+
                                   |
                         benefits tracking & audit
```

## Data quality design
- Unique IDs; no blank owner, title, stage, business-case evidence or taxonomy.
- A funded project must reference approved demand and finance sign-off.
- Project costs and funding are reconciled in the same currency and fiscal period.
- Last-update and milestone dates should trigger age and overdue flags.
- AI use cases must have model, data, product and compliance dependencies.
- Deferrals/rejections retain original intake, decision reason, forum/date and resubmission plan.

## SPM user-support model
Tier 1: answer documented workflow/classification questions and validate completeness.
Tier 2: investigate financial, project and reporting inconsistencies with module owners.
Tier 3: escalate platform configuration, security roles, integrations and complex defects to authorised ServiceNow admins.

## ServiceNow reading
Official ServiceNow funding documentation explains that project/demand cost plans, portfolio capital/operating targets, project budget plans and forecasts are separate financial objects. This demonstration keeps approved funding separate from proposed cost and avoids treating cost estimates as approvals.
