# Working agent execution | Developer evidence

This is **not the previous animated workforce analytics slide deck**. It is a working **finite-state agent execution runtime** whose policy selects the next tool **after inspecting prior observations**. Each tool call invokes the actual Python functions in `src/hcia/engine.py` and `src/hcia/workforce_design.py`.

## What runs
A fictitious group CPO asks whether 0.8 FTE of HR workload can be reallocated without approving people changes.

1. Agent chooses the real `read_workforce` tool and reads synthetic workforce positions.
2. Agent chooses `model_capacity` to compute hypothetical capacity, new job roles and future organisation.
3. After **observing the capacity figure**, the offline policy chooses a conservative `stress_test` if the figure meets the target; otherwise it branches to a zero-adoption downside.
4. Agent invokes `review_governance` and checks reserved human-only actions.
5. Agent synthesizes a bounded final JSON answer with source traces, scenario limits, no payroll writes and zero actual headcount changes.
6. A separate unsafe employment-action request is **refused** before any tool execution.

## Real agent engineering versus unproven claims
- **Actual:** a running observe → select tool → validate → execute → observe → replan → finish loop, permission enforcement, tool schemas, repeat-call limit, step limit, tests, evidence trace and a working optional LLM provider interface.
- **Offline demonstration uses a deterministic policy**, not a live LLM. Its decisions are conditional on observations but do **not** demonstrate language-model reasoning.
- **Optional live:** `OpenAICompatiblePolicy` accepts an explicitly configured HTTPS, host-allowlisted Chat Completions endpoint, API key and model ID, and proposes a single next tool each turn. Unallowed tool names, invalid arguments, repeated calls, incomplete evidence, unsafe goals and unauthorized roles are refused by the runner. **This mode has not been invoked or validated against a live model.**
- **Not built or claimed:** real HRIS connection, production OIDC, immutable enterprise audit, production hosting, independent client reference, measured savings, signed-off job architecture, workforce implementation or G42 production qualification.

## Reproduce (Python 3.11+, from project root)
```bash
python -m scripts.demo_agent_runtime
python -m unittest discover -s tests -v
```

**Video:** `demo/Agent_Runtime_Live_Execution_Trace.mp4` is generated from the **actual execution trace JSON emitted by the working code**, with captions on screen. It is an animated CLI trace replay—not a production screencast or a filmed live external LLM session.

**Strong next evidence milestone:** configure a permitted, real model endpoint and verify native model-initiated tool decisions and recoveries on a hosted agent instance before describing it as a production-grade agentic AI solution.
