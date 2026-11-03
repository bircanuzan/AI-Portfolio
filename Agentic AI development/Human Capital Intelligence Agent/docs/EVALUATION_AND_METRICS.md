# Technical evaluation and performance evidence

## Test classes
- Six distinct analytics tool functions and an executive six-tool composite call.
- Expected outputs on synthetic preauthored scenarios (see scripts/benchmark.py).
- Recruiting funnel invariants, cross-entity scopes and unknown-tool refusal.
- Role/permission denial, extra-field rejection, unauthenticated requests and restricted rewards.
- Aggregate compensation cell suppression and no individual salary access.
- Audit HMAC tampering detection and fail-closed audit requirement.
- Mock HTTPS integration, host allowlist, schema validation and refusal of personal record identifiers.
- Optional LLM fallback when not configured: no invented live model result.

## Metrics
- **Scenario pass rate:** exact match / total scripted expected metric values.
- **Latency:** clock from in-process Python executive_brief invocation; median/p95/p99 with repetitions. This excludes HTTP, authentication, database, cloud and LLM inference. No production SLO can be inferred.
- **Reliability:** unit/API/integration passing tests; then staging must introduce concurrency, malformed inputs, timeouts, 429/5xx, egress failure, audit fault injection, model failover and recovery. No claims from scripted tests alone.
- **Groundedness and explainability:** every metric cites a synthetic fixture and section; model summary will require faithfulness rubric, manual evaluation and real-source trace before production.
- **Workforce outcome metrics:** actual manual minutes saved per verified task, error rate, rework, employee fairness/access, service quality and total cost, compared against preregistered baselines after an authorised pilot.

## Benchmark execution
    python -m unittest discover -s tests -v
    python scripts/benchmark.py

GitHub Actions workflow hcia-ci.yml runs the same commands on a pinned Python major/minor and publishes benchmark-results.json as an artifact when it succeeds. Do not advertise test pass counts or latency figures until an actual execution record has been obtained and inspected.

## Known failure modes and mitigations
1. Empty population or metric denominator → explicit null rate rather than divide-by-zero.
2. Bad recruitment funnel values → validation failure before tool execution.
3. Unallowlisted tool or wrong entity → refusal, no fallback to generic function.
4. Privilege mismatch → HTTP 403 and no analytics.
5. Missing audit store/secret → HTTP 503, no unlogged analytics.
6. Connector failures/host mismatch → raise bounded integration error; data not invented.
7. Model endpoint timeout/schema failure → degrade to human analysis and show unavailable status.
8. Small rewards cohorts → suppress rows; no employee-level outputs.
9. Biased or unrepresentative data → uncertainty disclosure; real fairness testing still required.
10. Model hallucination → no authority to change numeric metrics or approve work.

## Claims policy
Outputs are fictional, reproducible local demonstrations. A high synthetic test score does not validate real-world HR decisions, bias, security, workload benefit, cloud reliability or enterprise readiness.
