# HR MIS Data Dictionary and Data Lineage

**Case**: fictional October 2026 UAE-bank month-end. This dictionary is a proposed specification, not an ADIB or CBUAE data standard.

## Grains and primary keys
| Source | Grain | Primary key | Required fields | Control |
|---|---|---|---|---|
| HRMS employee snapshot | One worker at one cutoff | employee_id + as_of | employee_id, division, as_of, status, FTE, emiratisation_group, annual_cost_aed | Unique active/current worker; HRMS sign-off |
| Funded position plan | One division allocation per cutoff (demo only) | division + as_of | funded_fte, budget_aed, target_pct | Finance-approved control total |
| Requisition log | One job request per approval event | req_id | division, requested_fte, approval_status | Approved != pending; no double counting |

## Definitions
- **Employee headcount**: distinct active people present at the month-end snapshot, regardless of FTE.
- **Employee FTE**: sum of active contractual FTE (0 < FTE <= 1 for each employee in this simplified scenario); contractors require an explicit separate inclusion rule.
- **Emirati FTE**: active FTE where fictional group = Emirati; nationality and official eligibility definitions must be validated by authorized HR/Compliance personnel, never inferred from names.
- **Funded FTE**: approved allocation shown in Finance-certified workforce budget; not the same as total requests.
- **Open vacancy FTE**: max(funded FTE - active FTE, 0); flagged if active exceeds funded capacity.
- **Annualized employee cost**: fictional annual cost allocation per current employee; no claim it equals payroll expense, accounting accrual, or UAE wage reporting.
- **Budget variance**: annualized active cost minus Finance-authorized annual budget; positive indicates overspend.
- **Target FTE gap**: illustrative target denominator × target share minus Emirati FTE, rounded upward at zero; **not** an official legal test.
- **Forecast**: expected hires/exits applied after report cutoff to actual FTE; approved reqs alone do not prove a hire will occur.
- **Data-quality exception**: missing/duplicate IDs, unknown division, malformed date, invalid FTE/cost, impossible approval state, or inconsistent source cutoff.

## Lineage
```
HRMS employee effective-dated records --> month-end snapshot --> validations
Finance position & budget register ------> approved funded plan --> reconcile by division
TA requisition approval log -------------> approved/pending requests --> scenario inputs
All validated sources --> division FTE, vacancies, costs, illustrative national workforce measures
                     --> owner-reviewed MIS --> HR/Finance management pack
                     --> Compliance validation gate BEFORE any regulator-facing report
```

## Required evidence retained for monthly close
1. Source-system timestamp, extraction query/version, snapshot cutoff and record counts.
2. HR divisional sign-off for actual headcount/FTE and employee movement exceptions.
3. Finance signature for authorized position and people-cost allocation values.
4. Reconciliation workbook with missing keys, duplicates, cost/position variances and resolution IDs.
5. Approved metric dictionary/version and target interpretation; compliance/legal applicability decision.
6. Executive pack version, reviewers, corrections, distribution and approval log.

## Privacy and safe reporting
No employee names, Emirates IDs, passport data, actual salaries or identifiable records appear in this demonstration. Group/division aggregates may still require access control and minimum-cell thresholds in production; enforce those through institutional policy.
