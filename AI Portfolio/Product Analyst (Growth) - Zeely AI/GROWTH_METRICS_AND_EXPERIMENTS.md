# Growth Analytics — Metric Contracts and Experiment Plan

**Status:** portfolio reference methodology. All schemas and examples are synthetic and are not Zeely customer data.

## Funnel event schema
Example event contract: `event_id`, `anonymous_id`, `user_id`, `session_id`, `event_name`, `event_timestamp_utc`, `platform`, `channel`, `experiment_id`, `variant`, `subscription_id`, `amount_usd`, `payment_status`.

Required checks: event deduplication, consistent UTC timestamps and attribution windows, event ordering, consent scope, test assignment persistency, and identities reconciled without double counting.

## KPI dictionary
| KPI | Definition / denominator | Caveat |
| --- | --- | --- |
| Visitor→activation | Unique eligible visitors who activate within fixed attribution window ÷ eligible visitors | Window and bot filtering must be specified |
| Activation→purchase | Activated eligible users with first successful purchase ÷ activated eligible users | Never mix all-time and same-cohort denominators |
| Paid conversion | Unique eligible visitors becoming payers within horizon ÷ eligible visitors | Exclude failed payments and refunds based on disclosed policy |
| D7 / D30 retention | Eligible cohort users active on target day or within stated interval ÷ original cohort users | Use only cohorts old enough to observe period |
| ARPU | Recognized net revenue for period ÷ eligible active or total users, explicitly chosen | State whether non-payers are included |
| ARPPU | Recognized net revenue ÷ paying users | Don't confuse with ARPU |
| Observed cohort LTV | Cumulative net revenue of a signup cohort over known horizon ÷ original cohort size | Do not infer infinite-horizon LTV from short observation |
| LTV estimate | Assumption-based projection from retention, contribution margin, expansion/refunds, and discounting | Show sensitivity and validate with backtests |
| Subscription churn | Churned subscriptions during interval ÷ active subscriptions at interval start | Exclude planned pauses only if metric policy says so |

## Experiment framework
1. **Question and hypothesis:** example: is a new onboarding flow increasing D7 activation without increasing refund rate?
2. **Unit of randomization:** stable user ID; verify assignment is mutually exclusive and persistent.
3. **Primary metric:** activation rate by eligible assigned users (intention-to-treat) and defined observation horizon.
4. **Guardrails:** failed payment rate, D7 retention, cancellation/refunds, revenue per assigned user, data-quality issues.
5. **Power and size:** specify minimum detectable effect, baseline, alpha, desired power and planned duration before exposure.
6. **Sanity checks:** sample ratio mismatch, covariate balance, event loss, leakage, novelty effects and peeking.
7. **Evaluation:** absolute and relative uplift, confidence interval, p-value where justified; avoid describing correlation as causation for nonrandomized segments.
8. **Decision:** ship, iterate, reject or extend based on primary, guardrails, uncertainty and practical economics.
9. **Documentation:** preserve experiment ID, dates, owner, targeting, exposures, exclusions, metric SQL version and decision history.

## Segmentation and monetization
Segment by cohort, channel, plan tier and activation behavior. Report each segment's size and confidence interval; limit multiple-comparison fishing. Decompose price-test impact into conversion, net revenue per visitor, churn, refunds and cohort LTV, with a pre-agreed profitability guardrail.

## Self-service scorecard & alerts
Publish timestamp freshness, data quality status, funnel stage rates, D1/D7/D30 retention, cohort revenue, ARPU/ARPPU and experiment status. Alert only on sustained, cohort-aware anomalies after volume, seasonality and telemetry checks; assign owner/runbook and escalation path.

## Relevant technical evidence
[Existing people analytics project](../People%20Analytics%20%26%20HR%20Data/README.md) demonstrates metric validation, Python checks, dashboards and assumptions-driven cohort analysis. Consumer subscription examples in this document are **transferable analytics methods**, not historical employer outcomes.
