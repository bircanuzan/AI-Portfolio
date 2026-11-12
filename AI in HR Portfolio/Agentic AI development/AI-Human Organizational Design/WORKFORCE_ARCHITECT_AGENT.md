# AI-Human Organizational Design — Native Tool-Calling Workforce Architect

**THIS is the agent developer implementation** for designing human/agent task allocations, future job roles and organizational structures — **not** the unrelated interactive workforce analytics dashboard.

Integrated into the existing **AI-Human Organizational Design** project, not a duplicate top-level portfolio project. It reuses the actual tested [workforce redesign engine](src/hcia/workforce_design.py) and synthetic [task and org architecture fixture](data/synthetic_workforce_redesign.json).

## Critical evidence distinction

| Capability | State |
|---|---|
| Native Responses API function-call loop, tool schemas, strict allowlisting and tool execution | **Implemented** in Python |
| Iterative model planning based on returned tool evidence | **Implemented for live mode**, but **not yet tested against a real hosted model** |
| Offline provider protocol and safety tests | **Executed by GitHub Actions**, scripted model stub, **not LLM inference** |
| Model-selected task assignments and human-owned future organization | **Validated by deterministic controls** after model submission |
| Live LLM trace with real API/model responses | **Not yet supplied**; requires user-configured API credentials and paid/available model access |
| Enterprise HRIS access, real employees, autonomous HR action, real organizational approvals and financial ROI | **Not implemented or claimed** |

**Do not claim that the scripted demonstration is a real AI model session.**

## Architecture

    Executive user goal
        ↓
    Native LLM (Responses API) chooses next function
        ↓
    Restricted function registry / schema and argument validation
        ├── inspect_work [7 task groups, evidence]
        ├── simulate_capacity [real Python capacity model]
        ├── compare_scenarios [alternative assumptions]
        ├── inspect_future_organization [8 roles / 7 org units]
        ├── review_governance [human-only approvals]
        └── submit_blueprint [strict task/role/reporting/approval gate]
        ↓
    Function outputs are returned to the model → next decision
        ↓
    Draft design, **never an approved workforce change**

The model can select a tool and scenario multiplier dynamically, redesign all eight human roles and propose new reporting relationships between seven known organization units, then reason over tool feedback. Organizational reporting cycles and unidentified roles are rejected. The code verifies that all activities are accounted for and no sensitive employment decisions are given to AI. Final output is a structured human-reviewable draft with an auditable call trace, not an HRIS write.

## Run the **offline model-protocol stub** (no model inference)

From \`Agentic AI development/AI-Human Organizational Design\`:

    python -m src.hcia.workforce_architect --demo --out demo/workforce_design_stub_trace.json
    python -m unittest tests.test_workforce_architect_agent -v

The \`--demo\` output is honest engineering/evaluation evidence, not a live LLM demo.

## Run with a REAL model (requires permitted API access)

1. Install the OpenAI Python SDK in your local environment: \`python -m pip install openai\`.
2. Set \`OPENAI_API_KEY\` in your secure environment (do **not** enter a key in GitHub or commit it).
3. Optionally set \`OPENAI_MODEL\` to your available function-tool-capable model.
4. From the HCIA project directory, run:

    python -m src.hcia.workforce_architect --live --model gpt-4.1-mini --out demo/live_workforce_design_trace.json

The SDK uses native **Responses API function calls**. It does not use the retired Assistants API. Actual API model/tool access and associated charges depend on your separate API credentials.

If a live run fails or model returns invalid proposals, no employment actions occur. The runner refuses unauthorized calls, invented roles, unsafe task allocation and premature finish.

## Testable user request

"Design accountable human and AI responsibilities for a fictional multi-entity enterprise. Use task decomposition, challenge AI adoption assumptions with a low/high scenario, define future roles and organization units, and surface employee-risk approvals before proposing a plan."

## What a production pilot still requires
- An authorized sandbox for the chosen model and governed data sources.
- Real model execution/evaluation traces, action-selection failures and prompt-injection tests.
- Secure HRIS/ATS connectors and approved identity/permissions.
- Human review workflow (CHRO, CISO, Finance, ER/Legal), signed-off decisions and rollback.
- Workforce impact consultation and validated economic baselines, not hypothetical savings.

**This module demonstrates development of an LLM-tool-using workforce architect, not the claim that a live LLM tool chain or enterprise workforce transformation has already been executed.**
