# SAP EC integration security, UAT and support gates

## Security and access
SAP SuccessFactors supports role-based permissions, with distinct permissions for OData and CompoundEmployee. Full HRIS SOAP access and restricted CompoundEmployee access have different implications and should not both be blindly granted to the same role. Approve integration scopes with security/data protection owners.

## UAT plan
| ID | Scenario | Expected |
|---|---|---|
| SAP-01 | Full master replication reference sample | Mapped employee keys and legal entities reconcile |
| SAP-02 | Delta with previous checkpoint | Only authorised change set staged |
| SAP-03 | Correction to prior effective-dated row | Superseded version tracked and reconciled |
| SAP-04 | API account denied restricted segment | Access denied; incident and exception logged |
| SAP-05 | Duplicate event replay | Quarantined, no double downstream action |
| SAP-06 | Invalid company / mapping | Rejected for HRIS owner signoff |
| SAP-07 | SOAP/transport timeout | Retry with bounded backoff, no silent data loss |
| SAP-08 | Restricted privacy field included | Redact or block before onward sharing |

## Release gates
Signed field ownership -> correct API and release documentation -> limited service account -> approved test cases -> no critical permission exposure -> reconciliation -> restart test -> documented go/no-go -> monitoring and hypercare.

## Operational evidence template
Record interface name, entity scope, approved data elements, API/RBP roles, integration version, delta checkpoint, run counts, validation failures, ticket references, root cause, actual test result and reviewer. Keep employees and proprietary configurations out of public repositories.

**Status:** Test scenarios and delivery design only, not a tested SAP integration.
