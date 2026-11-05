# Monthly HR MIS and Workforce Planning — Reporting Control Matrix

**Design**: hypothetical regulated financial-services HR team. Approval roles below are illustrative; do not infer ADIB's actual operating model.

| Step | Trigger | Maker | Checker / approver | Evidence | Failure / escalation |
|---|---|---|---|---|---|
| Close cutoff | Working day after month end | HRMS data steward | HR MIS manager | timestamped snapshot | Reject inconsistent as-of dates |
| Validate staff | HRMS ingest | HR analyst | Division HRBP | counts, duplicate/missing-key report | Quarantine row; open ITD ticket |
| Verify headcount | By business division | Divisional HR coordinator | Division Head / HRBP | month-on-month movement bridge | Material deltas referred to HR MIS lead |
| Funded plan | Finance budget version | Finance Planning | Financial Control | signed position and cost limits | Do not treat requests as approved |
| Recruitment demands | Requisition status update | TA | Budget authority | approval chain and req ID | Pending excluded from funded capacity |
| Cost MIS | Monthly roll-up | HR analyst | Financial Control | cost bridge and reconciliation | Hold executive issue on material variance |
| National workforce dashboard | Monthly | HR MIS | Emiratisation lead + Legal/Compliance | metric definition & interpretation | Stop any official claim without approval |
| Management pack | Close plus control window | HR MIS | HR Director + Finance | versioned division/group summary | Reissue with change log |
| Regulator-facing submission | As required by authoritative timetable | Approved reporting owner | Compliance/Legal and designated signatories | approved reporting template and audit log | **No direct submission from demo code** |
| Remediation | Failed control/UAT | ITD/HRIS team | HR process owner | incident, fix, rerun, sign-off | Track SLA, no silent patch |

## Three mandatory reconciliations
1. **Movement bridge:** previous active FTE + hires + transfers in - transfers out - leavers + FTE adjustments = current active FTE.
2. **Position bridge:** approved funded FTE = occupied FTE + vacant funded FTE, subject to documented over/under-allocation exceptions.
3. **Cost bridge:** approved budget, actual annualized assigned employee cost, movement-driven delta, open vacancy budget and expected hire cost must use consistent period, FTE, and cost bases.

## Controls for management decisions
- Separate actuals, budget, pipeline, requested, approved and forecast to avoid misleading precision.
- Highlight missing or mismatched cutoffs, low data coverage, negative vacancy, costs without positions and positions without funding.
- Explain if an apparent target gap is driven by approved positions vs active employees; both numerator/denominator definitions must be documented.
- No personal HR data in unprotected spreadsheets; no sensitive individuals identifiable in small cells.
- Published pack must include reporting date, source versions, definition changes and human approvers.
