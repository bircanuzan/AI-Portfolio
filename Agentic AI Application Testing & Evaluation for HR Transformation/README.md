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


## Next milestone — real OpenAI LLM integration (code added, execution pending)

This repository now includes an **OpenAI Agents SDK** implementation, a paid-API evaluation harness, seven new offline host-side safety tests, private-key configuration examples, and a **manual GitHub Actions workflow**. The model gets a read-only policy-search function tool and a simulated human-review tool; structured outputs and source/approval boundaries are independently validated in application code.

**Execution status:** A real model call has NOT been made in this environment. No OPENAI_API_KEY was available, the Agents SDK was not installed and network access blocked package installation. New offline protection tests passed **7/7**, bringing automated tests to **13/13**. Do not interpret these as real LLM evaluation results.

**[How to connect the live API and verify](LIVE_INTEGRATION.md)** · **[Execution status](evidence/LIVE_RUN_STATUS.md)** · **[Live Python model integration](live_llm_agent.py)** · **[Live evaluation runner](evaluate_live.py)** · **[Offline guardrail tests](tests/test_live_agent.py)**

From an Internet-enabled machine with an API key stored in a private environment variable:

    python -m pip install -r requirements-live.txt
    python live_llm_agent.py "How many annual leave days can I request?"
    python evaluate_live.py --limit 4

Alternatively run the repository's manually triggered GitHub Actions workflow after setting the OPENAI_API_KEY Actions secret. No automatic API spending is configured.


## No-manual-setup open-weight LLM demonstration (GitHub Actions)

An optional genuine LLM evaluation was added to avoid requiring new API keys, API billing, or plugin authorization. It runs the public **Qwen2.5 0.5B Instruct (Apache 2.0)** locally on a GitHub Actions CPU runner using **llama.cpp** and sends requests to a local **OpenAI-compatible HTTP chat-completions endpoint**. **This is NOT OpenAI's paid API, Microsoft Copilot, or an enterprise-ready model.**

- **[Real model integration and evaluation code](local_open_weight_llm.py)**: local policy search, route controls, actual HTTP model completions for approved-policy questions, numeric checks, raw model draft, separate approved policy answer.
- **[No-key workflow](../../.github/workflows/hr-open-weight-live.yml)**: downloads public GGUF weights, starts llama.cpp, executes unit tests, makes real model requests, uploads evidence; attempts to commit synthetic results automatically.
- **[Evidence file after a successful execution](evidence/local_llm_results.json)**: available *only after* the workflow really completes; absent means no completed live run has been proven.
- **Trigger:** automatic when the file `run_local_model.trigger` is created or changed, or manually through workflow_dispatch. There are no scheduled or continuously billed model services.

**Important:** The code and workflow alone are NOT proof that the model executed. The GitHub Actions job must succeed and yield real raw model drafts before describing the portfolio as 'live tested'. The existing key-based OpenAI Agents SDK implementation is a separate integration that cannot be connected to a private OpenAI API account without that account's credentials and billing authorization.


## Verified real local LLM inference — November 2, 2026

GitHub Actions successfully ran a **real, open-weight Qwen2.5 0.5B Instruct LLM** inside a temporary llama.cpp server. An OpenAI-compatible local HTTP API returned **three actual model completions** across **six** synthetic HR cases. **6/6 host-side routing outcomes passed**, but generated answer quality was mixed: the model omitted the 25-day annual-leave amount and produced unsupported onboarding details. Those drafts were recorded, never served as verified policy facts.

- **[Actual captured LLM responses and timestamps](evidence/first_run_qwen_0_5b.json)**
- **[Evaluation findings and observed defects](evidence/REAL_MODEL_FINDINGS.md)**
- **[Current automatically generated evidence](evidence/local_llm_results.json)**
- **[Actual working local LLM adapter](local_open_weight_llm.py)**

**Model provider and scope:** self-hosted open-weight Qwen, **not OpenAI API or Copilot**; free public synthetic demonstration, not an enterprise-grade continuously hosted agent. The OpenAI API branch is still separately prepared but requires API account credentials that ChatGPT cannot provision.
