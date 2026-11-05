# Oracle talent reporting UAT and information control (proposed)

The following tests are *specified*, not executed in a live Oracle tenant.

| ID | Control check | Expected |
|---|---|---|
| 01 | 94 completed documents among 100 eligible employee documents | 94% review-completion KPI, no false worker-level denominator |
| 02 | Completed goal but no approved strategic parent goal | Not counted as goal aligned |
| 03 | Open Talent Review meeting | Excluded from final calibrated scores |
| 04 | One person is a candidate on two succession plans | Distinct-position coverage; no double-counting roles |
| 05 | User without authorised Talent Review access | No detailed nine-box or worker ratings |
| 06 | Less than five employees in a reporting slice | Suppress small cohort |
| 07 | Terminated employee still in goals subject area | Effective status filters correctly applied |
| 08 | Publisher scheduled quarterly output | Correct as-of date, report version and recipient controls |
| 09 | Annual talent programme spend | Reconcile to Finance general ledger |
| 10 | No Fusion HCM Analytics subscription | OTBI/Publisher case still operates; advanced analytics not falsely shown |
| 11 | Automated attrition-risk predictions | Human review and fairness control; no individual action without due process |
