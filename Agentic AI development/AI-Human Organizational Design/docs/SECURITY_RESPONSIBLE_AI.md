# Security, privacy, responsible AI and failure boundaries

## Threat model and current safeguards
| Threat | Demo safeguard | Unimplemented / production control needed |
|---|---|---|
| Unauthenticated access | No token → HTTP 401 | OIDC/JWT verification, revocation, MFA, API gateway and rate limits |
| Analyst privilege escalation | Role + entity scope; no implicit cross-entity permissions | Entra groups/SCIM, ABAC, entitlement review and independent penetration test |
| Arbitrary tool execution | Allowlisted capability enum; no natural-language tool execution | Policy-as-code with supply-chain review and adversarial evaluation |
| Employee PII exposure | Aggregates only, no employee records; min size 5 for rewards | DLP, reidentification testing, k-anonymity policy per metric and jurisdiction |
| Unauthorized HR decision | Read-only; zero enterprise writes; humans own decisions | Maker-checker, approved workflows, case references and full audit integration |
| Audit modification | HMAC-chained SQLite events, unit test tamper detection | WORM/immutable audit store, backup, SIEM, key custody and rotation |
| Model hallucination | Narrative optional only; result values computed outside model | Grounded evaluation with hallucination rubrics and independent reviewer |
| Data exfiltration via endpoint | Operator allowlist, HTTPS and token injection | Private endpoints, egress proxies, certificate pinning where appropriate |
| Data poisoning / stale metrics | Synthetic schema/funnel validation and per-result provenance | Data lineage, approvals, reconciliation and temporal checks |
| Service failure | No audit → deny rather than return private analytics | HA, retry/queue, telemetry, operational SLAs and runbooks |

## Responsible AI controls
1. **Purpose limitation:** decision support only; no individual worker judgement or automated actions.
2. **Data minimisation:** do not import employee or applicant PII into public GitHub, API logs or unapproved LLM prompts.
3. **Human autonomy:** documented human owner for hiring, reward, succession, performance, employee relations, termination and restructures.
4. **Bias evaluation:** test fair access to opportunities and disparate output effects with approved lawful data, protected-trait handling and legal counsel. **No empirical fairness conclusion is made from synthetic aggregate fixtures.**
5. **Explainability:** formula outputs, source record version, scope, nulls and caveats; avoid overclaiming statistical significance.
6. **Escalation:** missing/invalid authorisation → deny; unknown entity/tool → refuse; unsupported integration → no data; model timeout → manual interpretation; data anomaly → analyst investigation.
7. **Accountability:** developer, enterprise sponsor, CPO, Legal, InfoSec, HRIS and Data Governance assign owners and residual risks before production.

## Important adverse use case
A manager tries to obtain one employee's salary or evaluate an identifiable person's suitability. The API accepts only pre-enumerated metrics and entities, contains no employee record accessor and returns no individual salary; reward output is cohort-only. This is an **architectural denial**, not a demonstration of comprehensive privacy compliance.

## Bias test plan (not yet validated)
Prepare lawful, independently reviewed labelled cases with disaggregated opportunity/selection or service metrics; specify a preregistered test and minimum sample, evaluate confidence intervals, underpowered segments, error disparities, mitigation changes and human escalation. Test against law and applicable organizational standards. Do not use the agent to determine protected attributes or generate sensitive profiles.
