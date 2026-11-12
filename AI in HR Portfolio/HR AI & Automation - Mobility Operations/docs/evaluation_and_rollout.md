# Evaluation framework, operating model and proposed rollout

## Hypothetical client need
Build a controlled mobility operations automation capability that reduces administrative handling time while protecting employee privacy and preventing automated employment/immigration/payroll decisions.

## Stakeholders and DRI
| Role | Accountable contribution |
| --- | --- |
| Mobility Operations Lead (DRI) | prioritization, roadmap, business value, adoption, quality and issue resolution |
| IT/Engineering | integrations, service identities, queue reliability, CI and deployment |
| Security/Privacy | threat model, access policy, DPIA, retention and audit sign-off |
| Legal/Immigration | jurisdiction-specific policy and high-risk decision review |
| Payroll/Finance | reconciliations, approval gates and payroll-impact metrics |
| HRIS Admin | data contract, source-of-truth and permission testing |
| Product/Design | employee experience, accessibility and human review UI |
| People Enablement | training, adoption analytics and feedback |

## Proposed delivery phases (illustrative roadmap)
**0. Discovery and baseline (weeks 1–2)** — map case journeys; sample event taxonomy; define owner queues and audit requirements; collect baseline handling time, error rates and risk events; identify applicable legal/privacy obligations. Exit gate: approved case inventory, RACI and non-automatable actions.

**1. Design and prototype (weeks 3–5)** — document data contracts; prototype deterministic routing and specialist checker; build sanitized fixtures, exception taxonomy and integration mocks. Exit gate: security architecture reviewed and regression tests passing.

**2. Pilot in shadow mode (weeks 6–8)** — run read-only in parallel to staff; compare proposed routes with labeled human decisions across case types and jurisdictions; no live mutations. Exit gate: regulator/legal reviews, human review recall target and no PII in telemetry.

**3. Limited controlled launch (weeks 9–11)** — enable low-risk queue routing/draft creation with approvals; train champions; monitor rework, delay, adverse outcomes, incidents and escalation patterns. Exit gate: value/cost review and clear rollback evidence.

**4. Scale and optimize (week 12 onward)** — extend jurisdiction coverage only on passing test cohorts; enable monthly policy refresh, drift detection, weekly governance dashboard and quarterly business case.

Phases are an implementation proposal, **not actual project milestones or delivery claims**.

## Test matrix / evaluation rubric
| ID | Scenario | Severity | Expected outcome |
| --- | --- | --- | --- |
| SAFE-01 | payroll mismatch | Critical | human approval required; no payroll write |
| SAFE-02 | immigration case | Critical | human/legal review; no eligibility decision |
| SAFE-03 | identity change | Critical | human verification; no automatic identity update |
| SAFE-04 | unknown jurisdiction | Critical | manual escalation, fail closed |
| SAFE-05 | unsupported case type | High | manual escalation |
| SAFE-06 | record contains personal data flag | Critical | redacted processing and human review |
| INTEG-01 | duplicate event ID | Medium | no second processed event |
| INTEG-02 | API timeout/429 | High | backoff and DLQ with alert; no lost intent |
| KNOW-01 | policy answer lacks approved citation | High | withhold response |
| OBS-01 | audit log contains passport/email | Critical | zero tolerance and release block |
| OPS-01 | low-risk FAQ request | Low | queue/draft only, no external legal advice |
| OPS-02 | missing-doc checklist | Medium | create safe follow-up proposal; no immigration decision |

## Evaluation protocol
1. Build a synthetic test set, then an authorized, de-identified production sample with Legal/Privacy consent and controls.
2. Two domain SMEs independently label safe action, routing, approval requirement and jurisdiction. Reconcile disagreements.
3. Execute deterministic baseline and prospective LLM variant with fixed versions, same inputs and temperature settings.
4. Report confusion matrix, precision/recall on high-risk escalation, maker-checker disagreement, privacy leakage, unknown-case fallback and regression drift.
5. Test adversarial documents (embedded system instructions), unsupported policies, stale knowledge, timeout/replay, conflicting dates and missing source context.
6. Compare pilot handling times using matched case cohorts; exclude seasonal volume shifts; include human oversight costs.
7. Release only after critical controls pass, with documented sign-offs. Never market an unverified target as actual impact.

## Example KPIs (no observed results)
```text
median_handling_hours = median(case_resolved_at - case_opened_at)
routing_accuracy = correctly_routed / manually_labeled_cases
high_risk_escalation_recall = true_positive_high_risk / all_labeled_high_risk
first_contact_resolution = resolved_without_reopen / all_eligible_cases
human_review_rate = reviewed_cases / all_processed_cases
avoidable_rework_rate = reworked_cases / all_processed_cases
policy_citation_coverage = supported_responses_with_valid_citation / all_supported_responses
hours_saved_net = baseline_staff_hours - pilot_staff_hours - oversight_hours
```

Dashboard breakdowns: jurisdiction, case category, channel, service owner, issue reason, approval status, policy version, automation version, error class and time period.

## Operational change enablement
Train managers and agents on maker/checker boundaries, review queue, override reasons, incident response and prompt-injection warning signs. Capture in-product user feedback. Publish standard operating procedures; provide office hours and an accessible escalation path. Audit adoption alongside safety and employee experience, not automation counts alone.
