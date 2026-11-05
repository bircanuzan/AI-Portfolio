# Enterprise Oracle HCM-to-ERP/Finance: architecture decisions and operational assurance

**Enhances the existing Oracle Solution Architecture project. Does not duplicate HCM configuration or HDL import.**

## ADR-01: Finance exclusively owns accounting outcomes
Oracle HCM owns worker and assignment data; Finance owns eligible cost centres, the general ledger, finance controls and journal/posting decision authority. Workforce events may be carried to an approved integration layer, but **an HR event is not an ERP journal**. An AI agent must never post or approve a journal.

## ADR-02: Multi-subsidiary canonical contract
The existing [architecture document](02_Target_Architecture_Integration_and_Data.md) defines a fictional staging event with `event_id`, `worker_id`, `event_type`, `effective_date`, `subsidiary`, `cost_center`, `approved_by` and `finance_reference_valid`. These are custom simulator fields, **not Oracle API payloads**. Each event gets a correlation ID, mapping version, named owner and finance reference check.

## ADR-03: Controlled recovery
| Failure | Expected owner / containment |
|---|---|
| Invalid finance cost centre | Finance master-data owner; hold before ERP action |
| Duplicate worker event | IT idempotency control; no second staging release |
| Missing HR approval | HR process owner; reject and log |
| Retroactive transfer | HR+Finance coordinated exception and cut-off review |
| Missing target system | IT replay approval + bounded retry and incident |
| Unreconciled batch | Independent Finance reconciliation and escalation |
| Overprivileged account | Security control owner; deny and investigate |

## ADR-04: Evidence and measurement
Each batch should have mutually exclusive received / accepted-for-staging / rejected / deferred statuses, plus downstream finance acknowledgements. Staging acceptance **cannot be described as completed ERP posting**.

## Reproducible evidence
[Existing Python financial staging validator](src/validate_changes.py) and [test cases](tests/test_validation.py) cover non-posting finance controls, invalid cost centre, missing HR approval and duplicate event. The Oracle HCM-specific [HDL exercise](../02_Oracle_Fusion_HCM_Solution_Architecture_and_Engineering/04_HDL_Job_Data_Preflight.md) is purposely outside this project.

**Current capability:** business-led logical HCM/ERP/OCI/OIC architecture and locally testable *synthetic* event controls only. No production Oracle ERP/HCM solution, OIC connection, accounting journal or client implementation is claimed.
