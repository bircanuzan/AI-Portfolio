# Requirements traceability, UAT and defects

## Requirement-to-test matrix
| Req | Acceptance criterion | Test | Owner | Planned evidence |
|---|---|---|---|---|
| FR01 | Employee opens a case with reference ID | UAT01 | HR Services | Synthetic case record |
| FR02 | Staff can view only authorised cases | UAT02 | Security | Access-denial log |
| FR03 | HR service SLA timer tracks correct business hours | UAT03 | Service Ops | Scenario timing trace |
| FR04 | Manager approves eligible request, HR retains final authority | UAT04 | HR + Manager | Approval history |
| FR05 | Data export reconciles case counts | UAT05 | BI | Source/target count report |
| FR06 | Invalid request does not create case | UAT06 | Product Owner | Validation error |
| NFR01 | Disabled account loses SSO access | SEC01 | IT Security | IAM audit result |
| NFR02 | Duplicate integration retry does not duplicate request | INT01 | IT Integration | Idempotency test trace |
| NFR03 | Nonproduction incident exercises rollback | OPS01 | IT Ops | Recovery log |

## Defect control
Record defect ID, impacted requirement, environment, exact repro steps, fictional case reference, expected/actual, severity, business impact, root cause, fix owner, regression evidence and signoff.

- **P0:** private employee data exposure, unauthorised employment/payment decision; stop release.
- **P1:** blocking core service workflow, loss of request record, duplicate or skipped approvals; stop release until corrected.
- **P2/P3:** lower-risk usability and formatting issues subject to written sponsor waiver and backlog.

No actual test result has been obtained here. Do not report these planned UAT cases as passed.

## Acceptance evidence hierarchy
Published requirement -> reviewed configuration -> performed test -> dated test evidence -> independent reviewer -> business signoff. A signed checklist alone is not a substitute for test output.
