# Agentic AI Application Testing & Evaluation for HR Transformation

**Working portfolio prototype | DemoCo UAE (fictional) | Python 3.10+ | Synthetic data | 2026-11-02**

## Practical HR transformation problem

HR service teams receive repeat inquiries on annual leave, remote work, expenses, onboarding and performance reviews. An agent needs to give **policy-grounded answers** while refusing private employee data and routing exceptions or human-owned decisions to responsible staff.

## What was built and really run

This project includes a functioning, auditable **offline rule-based tool-using HR policy agent**; six explicitly synthetic HR policies; a 16-scenario Python evaluation harness; six automated regression tests; and actual execution evidence in the evidence folder.

**Scope matters:** This is **not** a foundation-model/LLM agent. No live OpenAI/Copilot model, real HRIS, actual employee data, ticketing API or client workflow was used. The simulated escalation tool only identifies the reviewer and records a trace; it does not open real tickets, approve actions or update systems. LLM resilience is **not** demonstrated.

## Architecture and technical stack

| Component | Technology | Why it matters |
|---|---|---|
| Policy documents | policies.json | 6 fictional policy sources with ID, owner and rules |
| Retrieval tool | Python regular expressions + policy keyword matching | Source selection with explicit unknown-policy response |
| Agent planner / router | Python HRPolicyAgent | Restricted choices: answer, refuse, human review or insufficient info |
| Safeguards | Privacy regex guard and action authorization checks | No employee record disclosure or autonomous approvals |
| Human-in-loop | Simulated route_to_human tool | Traceable exception handoff, not a real external ticket |
| Evaluation | evaluate.py; machine-readable JSON output | Compare predetermined prompts and expectations with actual decisions |
| Regression | Python unittest | Re-check privacy, unknown questions, side-effect controls and full suite |
| Evidence | evidence/EXECUTION_EVIDENCE.md | Real 16-case outcomes, transcripts, initial defects and corrections |

**Decision pipeline:** question → policy lookup → privacy/authority checks → exception routing → policy answer / refuse / review / insufficient evidence → auditable outcome and trace.

## Test methodology

1. Define synthetic HR policy source material and human approval boundaries.
2. Author 16 acceptance scenarios with expected decision and policy ID **before evaluating**.
3. Execute the agent, record actual answer, tool trace, owner and policy citations.
4. Pass a case only when **actual decision equals expected decision**, the correct policy is selected and direct answers contain a source citation.
5. Run six Python regression tests covering privacy, human approval boundaries, out-of-scope questions, empty requests and full evaluation.
6. Record defects and remediation openly rather than reporting only a perfect result.

### Observed results (local Python execution)

- **First run:** 13/16 passed — missing synonyms for “remotely” and “onboarding”.
- **Fix:** Updated policy retrieval keywords and re-ran.
- **Final run:** **16/16 cases passed**, **6/6 regression tests passed**.
- **Interpretation:** This is **100% on a small authored synthetic test suite only**. Not an enterprise accuracy measure, not LLM model performance, not production validation.

## Concrete test situations

| HR challenge | Agent action | Source |
|---|---|---|
| Annual leave entitlement | Gives sourced policy | HR-LEAVE-01 |
| Three remote days per week | Requests HRBP human review | HR-FLEX-02 |
| Expense above AED 500 | Requests human preapproval | HR-EXP-03 |
| AI being asked to decide performance rating | Escalates, no final decision | HR-PERF-06 |
| Request for another employee's salary | Refuses disclosure | HR-PRIV-04 |
| Parking policy not provided | States insufficient information | No fabricated source |

## Run the code

Install Python 3.10 or higher. No paid tools or third-party dependencies are needed for this tested version.

    python agent.py "Can I work remotely three days each week?"
    python evaluate.py
    python -m unittest discover -s tests -v

Running the evaluator writes a detailed JSON evidence file at **evidence/evaluation_results.json**, containing the actual answer and tool trace for every case. See **evidence/EXECUTION_EVIDENCE.md** for captured output from the verified run.

## Business outcomes demonstrated (not claimed client results)

- Reduced need for manually answering repeat policy queries **in principle**.
- Explicit human-in-the-loop controls for approvals and exception handling.
- Better testability through trace logs, acceptance cases and measurable pass/fail.
- Privacy-aware refusal and unknown-policy behavior.

The DemoCo policy values and limits are fictional examples **not UAE Labour Law**. Nothing here should be used for real HR decisions without authentic policy sources, security review and appropriate access controls.

## Skills and next implementation milestone

Python; HR workflow mapping; retrieval; agent routing; rule-based policy matching; privacy-by-design; human approvals; automated QA; adversarial cases; traceability; evaluation scoring; failure analysis; CI-ready unittest.

**Not yet implemented:** real LLM orchestration with OpenAI Agents SDK or another provider, retrieval against authenticated enterprise HR documents, verified RBAC, real ticket creation, automated multi-turn red-team tests, monitoring/latency, independent held-out test set and any production deployment.
