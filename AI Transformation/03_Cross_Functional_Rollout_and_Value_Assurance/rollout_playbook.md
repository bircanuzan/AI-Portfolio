# 30 / 60 / 90-day AI transformation delivery

| Stage | Work | Evidence/artefacts | Exit gate |
|---|---|---|---|
| Days 1–30: baseline | Map business goals, products and processes; reconcile app inventory, costs and adoption; perform classification and risk assessment | Current-state process maps, expense register, value tree, scoped use-case backlog, owner RACI, risk register | Scope and data access accepted by sponsor, finance and IT/security |
| Days 31–60: first controlled pilot | Configure only approved technology; define input/output contract; UAT workflows, RBAC, knowledge source and human approval tests; train pilot users | Target-state process, configuration record, approval queue, test cases, quality rubric, failure/recovery plan | No critical access failure, release gate signed by data/process owner |
| Days 61–90: verify and decide | Compare matched case mix vs baseline, audit quality and time/review burden, survey users, quantify true spending changes, log failures and remediation | Adoption funnel, exception report, cost-to-serve measure, benefits/risks review, owner-backed support runbook | Sponsor, finance, operations and risk decide scale/hold/rollback |

## No-code/AI configuration checklist
- Consent, classification, source/tenant permissions, supplier data processing and residency reviewed.
- Process owner documents each trigger, mapping, failure branch, human approval, timeout and recovery.
- Team trains with safe synthetic scenarios; supervisors calibrate quality and human override.
- Audit records are access-controlled; production logs avoid prompts and personal information unless explicitly justified.
- Do not promise autonomous agents or reduce staff based on hypothetical throughput.

## Pilot failure actions
Critical access leak → pause/revoke/review. Missing knowledge citation → route to human. Incorrect recommended action → capture incident and revise test suite. Review effort above capacity → redesign/stop. Business result not improved → revisit workflow, not simply buy more models.
