-- Analytics example for authorized, PII-free fictional case events.
-- This SQL has not been deployed in Sigma, Tableau, Snowflake or a production HR data store.
SELECT
    region,
    category,
    COUNT(*) AS cases,
    SUM(CASE WHEN sla_met = 1 THEN 1 ELSE 0 END) * 1.0 / NULLIF(COUNT(*),0) AS sla_attainment,
    SUM(CASE WHEN human_review = 1 THEN 1 ELSE 0 END) * 1.0 / NULLIF(COUNT(*),0) AS human_review_rate,
    SUM(CASE WHEN reopened = 1 THEN 1 ELSE 0 END) * 1.0 / NULLIF(COUNT(*),0) AS reopen_rate,
    SUM(manual_minutes) / 60.0 AS logged_manual_hours
FROM synthetic_case_operations
GROUP BY region, category
ORDER BY cases DESC;
