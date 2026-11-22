-- Illustrative SQL for a clean table of accepted, synthetic transactions.
-- The Python demo performs the authoritative input validation before loading.
SELECT
  DATE_TRUNC('month', order_date) AS report_month,
  country,
  channel,
  COUNT(DISTINCT order_id) AS orders,
  SUM(revenue_usd) AS revenue_usd,
  SUM(cost_usd) AS cost_usd,
  SUM(revenue_usd - cost_usd) AS gross_profit_usd,
  ROUND(100.0 * SUM(revenue_usd - cost_usd) / NULLIF(SUM(revenue_usd), 0), 2) AS gross_margin_pct
FROM accepted_esim_orders
GROUP BY 1,2,3
ORDER BY 1,2,3;
