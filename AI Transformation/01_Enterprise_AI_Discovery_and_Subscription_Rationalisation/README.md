# 01 — Enterprise AI Discovery & Subscription Rationalisation

**Client challenge:** A services business pays for overlapping AI subscriptions, cannot explain which tools access which information and lacks outcome measurement. Its teams want a new AI agent before fixing its work processes.

## Discovery framework
**Interviews:** CEO/business sponsor (objectives), finance (license spend, unit economics), IT/security (permissions and data flows), department leads (task bottlenecks), employee representatives (day-to-day work and exceptions), HR/legal (policy and governance).

**Baseline capture:** process map, product/customer journey, seat inventory, owner and contract, paid vs active seats, overlapping use cases, data classification, existing integrations, user friction, license conditions, security/legal constraints, quality baseline.

**Opportunity scoring:** strategic value, frequency, time spent, error/harm severity, data readiness, scope, integration effort, privacy exposure and change readiness. High value **never** overrides unacceptable security risk.

## Files
- [Synthetic tool inventory](data/synthetic_tool_inventory.csv)
- [Explainable Python portfolio diagnostic](src/tool_portfolio.py)
- [Regression tests](tests/test_tool_portfolio.py)
- [Prioritised 90-day roadmap](first_90_days.md)

## Method
Identify overlap and license inefficiency using evidence. Calculate *reviewable exposure* from seats and subscription rates; this is **not banked cost savings**. Separate "keep", "consolidate subject to agreement", "security review" and "pilot more carefully". Confirm ownership and contract exit restrictions. Document no-code/native integration options only after permission review.

**Skills:** client discovery, operating model, business case, AI portfolio rationalisation, process mining concepts, Excel/Power BI metrics, platform configuration planning, cost/risk analysis, responsible AI and vendor evaluation.

**Evidence:** illustrative inventory and deterministic calculator; no actual subscriptions, procurement approvals or verified costs.
