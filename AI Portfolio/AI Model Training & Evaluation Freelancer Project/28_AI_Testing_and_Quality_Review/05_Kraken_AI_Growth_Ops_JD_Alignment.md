# Kraken — AI Growth Ops | Job-description-aligned operations & QA lab

**Source role:** https://jobs.ashbyhq.com/kraken.com/cb0b46c6-bdb1-4928-8112-da1d5ac4d36f
**Work mode:** UAE eligible, remote, full time (checked 2 November 2026).
**Provenance:** original independent portfolio exercise using fictional platform events. No Kraken systems, users, production agents or applications were accessed or tested. No past employment at Kraken is claimed.

## Requirement → skill → evidence
| Kraken requirement | Practical artifact | Evidence boundary |
| --- | --- | --- |
| Test new releases, rules, edge cases and regressions | `qa_demo/test_agent_ops_eval.py`; regression matrix below | Automated tests of fabricated events, not company platform |
| Catch and report reproducible bugs | Template and cases below; severity, expected/actual, steps | Hypothetical examples only |
| Monitor agent performance and activity | `qa_demo/agent_ops_eval.py` + JSON fixture | Offline counts; no live telemetry |
| Maintain approval and exception queues | Approver gate tests; HOLD/ESCALATE decision logic | No real approvals or writes |
| Check agent outputs against standards | Policy/output flags with explicit stop criteria | Rule-based example, not LLM judgment |
| Maintain runbooks, checklists, release notes | Runbook, gates and release log below | Draft operational practice |
| Work across product, engineering and operators | RACI & escalation SLA | Proposed operating model |
| Dashboard interpretation, QA literacy, prompt clarity | Report metrics and prompt-output failure test ideas | No Mixpanel/Jira integration |

## Fictional system under review
The invented growth platform generates agent events for content approval, targeting rules and messaging. A controlled checker must prevent unauthorized release, route non-compliant output for escalation and preserve traceable decisions.

### Regression matrix
- KRA-01: approved, checked, policy-compliant output → PASS
- KRA-02: approval required but missing → HOLD, never PASS
- KRA-03: policy violation even when approved → ESCALATE
- KRA-04: output QA not performed → REVIEW
- KRA-05: duplicate event IDs → reject input and log defect
- KRA-06: empty/malformed JSON or unknown status → fail closed
- KRA-07: changed prompts/rules → rerun full case set against the previous version
- KRA-08: escalation queue unowned past SLA → alert operations and halt affected release (proposed)

## Local reproduction
From this project folder:

```bash
python qa_demo/agent_ops_eval.py qa_demo/agent_events_synthetic.json
python -m unittest qa_demo.test_agent_ops_eval -v
```

Output is a deterministic report of **synthetic fixtures**, not a recorded Kraken run. Capture dated terminal output with git commit hash before stating an execution result.

## Defect and QA ticket sample (illustrative)
**KRA-EX-001** | Severity P1 | Environment: synthetic lab | Scenario KRA-02 | Steps: submit requires_approval=true and approved=false, then evaluate | Expected: HOLD | Example hypothetical failure: PASS | Impact: unauthorized action | Owner: engineering triage | Status: **NOT OBSERVED; TEST HYPOTHESIS**. Attach reproducible input, expected output, actual output only after a real failed execution.

## Operational runbook
1. Check release/build ID, rules, policy version and sample size.
2. Execute positive, negative and boundary tests; log input, expected, actual and trace ID.
3. For policy violations or missing approvals: halt affected output; do not silently clear the queue.
4. Classify severity: P0 unauthorized irreversible action; P1 release-blocking approval/policy breach; P2 functional defect; P3 display/copy issue.
5. Create defect with redacted steps, logs, owner, customer impact and reproduction details.
6. Re-test against a fixed build and run adjacent regressions; close only after evidence.
7. Publish release notes, unresolved exceptions, runbook updates and release decision.

**Suggested release gate:** zero unresolved P0/P1; all authorization-negative tests pass; approvals attributed to named owners; evidence links stored with date/build ID. These are proposed gates, not measured achievements.

## Skills and tools
Test planning; functional/regression QA; bug reproduction; agent-output checklists; incident and exception queues; human-in-the-loop approvals; Python 3; JSON; REST/API concepts; Git/GitHub Actions; SQL/Power BI familiarity; Jira/Mixpanel familiarity as *nice-to-have or learning*, not deployed integrations. No Jira, Mixpanel or Kraken access claimed.
