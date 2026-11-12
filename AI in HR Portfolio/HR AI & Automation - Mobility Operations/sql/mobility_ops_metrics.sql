-- HR AI & Automation - Mobility Operations
-- Reference SQL for a privacy-minimized audit mart (SQLite-friendly syntax).
-- Illustrative table and reports, NOT executed on live HRIS/payroll data.
CREATE TABLE IF NOT EXISTS mobility_case_audit (
  trace_id TEXT PRIMARY KEY,
  tenant_ref TEXT NOT NULL,
  event_ref TEXT NOT NULL,
  case_category TEXT NOT NULL,
  jurisdiction TEXT NOT NULL,
  proposed_action TEXT NOT NULL,
  checker_passed INTEGER NOT NULL,
  disposition TEXT NOT NULL,
  reason_code TEXT NOT NULL,
  risk TEXT NOT NULL,
  policy_version TEXT NOT NULL,
  timestamp_utc TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS ix_mobility_ops_window
  ON mobility_case_audit(timestamp_utc, jurisdiction, case_category);

-- Workload mix, gates and safe fallback; break down by jurisdiction.
SELECT
  jurisdiction,
  case_category,
  COUNT(*) AS cases,
  SUM(CASE WHEN disposition = 'human_approval_required' THEN 1 ELSE 0 END)
    AS human_approval_cases,
  SUM(CASE WHEN disposition = 'manual_escalation' THEN 1 ELSE 0 END)
    AS manual_escalations,
  SUM(CASE WHEN checker_passed = 0 THEN 1 ELSE 0 END)
    AS checker_rejections,
  ROUND(100.0 * SUM(CASE WHEN disposition = 'manual_escalation' THEN 1 ELSE 0 END)
        / NULLIF(COUNT(*), 0), 2) AS fallback_pct
FROM mobility_case_audit
GROUP BY jurisdiction, case_category
ORDER BY cases DESC;

-- Policy control drift view. Any fall in checker-pass or rise in
-- manual escalations should be investigated, never used to weaken gates.
SELECT
  policy_version,
  date(timestamp_utc) AS reporting_day,
  COUNT(*) AS processed,
  ROUND(100.0 * SUM(CASE WHEN checker_passed = 0 THEN 1 ELSE 0 END)
         / NULLIF(COUNT(*), 0), 2) AS checker_reject_pct
FROM mobility_case_audit
GROUP BY policy_version, date(timestamp_utc)
ORDER BY reporting_day DESC;

-- Production measures require separate permissioned case lifecycle mart:
-- time-to-resolution, reopens, SLA, signed human approvals, quality labels,
-- validated staffing hours and measured outcomes. Do not infer ROI from
-- counts in this minimal demo audit table.
