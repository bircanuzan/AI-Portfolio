# Oracle HCM Functional Configuration UAT — Proposed Test Specification

All cases are **unexecuted in Oracle**. Local Python checks only logical cross-references and control criteria.

| Test | Scenario | Acceptance outcome in a future authorised tenant | Reviewer |
|---|---|---|---|
| CFG01 | Legal employer and BU hierarchy | Correct legal employer, BU and country mappings | HR/Finance |
| CFG02 | Reference data set | Only business-unit accessible reference values exposed | HRIS |
| CFG03 | Departments, jobs, grades, locations | All position associations resolve to approved masters | HRIS/Talent |
| CFG04 | Position FTE/effective start | Position fields valid and versioned | HR Ops |
| CFG05 | Maker/checker | Maker cannot approve same request | Access control owner |
| CFG06 | Cross-entity transfer | Approved ownership, effective dating and payroll handoff | HR/Finance |
| CFG07 | Bad job/grade ID | Controlled validation exception, no silent creation | HRIS |
| CFG08 | Privileged HR/Payroll attributes | Least-privilege denial demonstrated | Security |
| CFG09 | Oracle release regression | All relevant core-HR configuration interactions tested | HCM Product Owner |
| CFG10 | Deployment and rollback | Release evidence and support signoffs collected | IT & HR |

## Evidence hierarchy
1. **Now:** model, rules, authored test specifications, synthetic code and local run results if actually executed.
2. **Before real implementation:** approved tenant design, role/access review, setup proof, API / data dependencies.
3. **After real execution:** timestamped and redacted configuration evidence, independent results, defects, rollback and owner acceptance.

The [existing Project 14 release governance](14_Release_UAT_Go_Live_Governance/) owns go/no-go and post-go-live decisions. This file does not duplicate that programme.

**Security:** do not put employee IDs, health, salary, bank or credentials in this public portfolio.
