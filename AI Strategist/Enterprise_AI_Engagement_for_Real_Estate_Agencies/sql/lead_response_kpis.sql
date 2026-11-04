-- Demonstration SQL (PostgreSQL). Synthetic table: lead_events.
-- Scope: eligible inquiries with consent to contact; reports data coverage separately.
-- Do not use this observational query to claim AI treatment impact.
WITH base AS (
  SELECT
    agency_id,
    received_at,
    response_at,
    booked_viewing,
    EXTRACT(EPOCH FROM (response_at - received_at)) / 60.0 AS response_minutes
  FROM lead_events
  WHERE consent_to_contact = TRUE
),
agency_metrics AS (
  SELECT
    agency_id,
    COUNT(*) AS eligible_leads,
    COUNT(response_at) AS answered_leads,
    COUNT(*) FILTER (WHERE response_at IS NULL) AS unanswered_leads,
    COUNT(*) FILTER (WHERE booked_viewing = TRUE) AS booked_viewings,
    COUNT(*) FILTER (WHERE response_minutes BETWEEN 0 AND 5) AS answered_within_5m,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY response_minutes)
      AS median_first_response_minutes
  FROM base
  GROUP BY agency_id
)
SELECT
  agency_id, eligible_leads, answered_leads, unanswered_leads,
  booked_viewings,
  ROUND(100.0 * booked_viewings / NULLIF(eligible_leads, 0), 2) AS booking_rate_pct,
  ROUND(100.0 * answered_within_5m / NULLIF(answered_leads, 0), 2) AS sla_5m_of_answered_pct,
  ROUND(median_first_response_minutes::numeric, 2) AS median_first_response_minutes
FROM agency_metrics
ORDER BY agency_id;
