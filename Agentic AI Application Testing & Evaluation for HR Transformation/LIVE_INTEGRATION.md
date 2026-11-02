# Live OpenAI LLM integration — setup and verification

## Status (2 November 2026)

**Code written; live inference NOT executed.** The execution environment did not have `OPENAI_API_KEY`, the `openai-agents` package was not preinstalled, and installing it was blocked by network/DNS access. A real OpenAI response, token charge and latency have **not** been recorded.

**Verified offline:** Python 3.13.5; 13/13 regression tests passed across the original baseline and new LLM-host protection checks. These tests are not live model evaluations.

## How to activate actual API calls

1. Create an OpenAI API project and API key at https://platform.openai.com/api-keys and confirm the API organization has available credit or billing. ChatGPT Plus billing is separate.
2. Use Python 3.10+ and a machine with package-registry and API access:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows PowerShell: .venv\\Scripts\\Activate.ps1
   python -m pip install -r requirements-live.txt
   ```
3. Set the secret **on your own computer or in GitHub Actions secrets**, never in a tracked file or a ChatGPT message:

   ```bash
   export OPENAI_API_KEY='YOUR_KEY_HERE'  # PowerShell: $env:OPENAI_API_KEY='YOUR_KEY_HERE'
   export OPENAI_MODEL='gpt-4.1-mini'
   ```
4. Run a real tool-using agent:

   ```bash
   python live_llm_agent.py "How many annual leave days can I request?"
   python live_llm_agent.py "Can I work remotely three days each week?"
   ```
5. Run the cost-limited evaluation (defaults to **four cases**):

   ```bash
   python evaluate_live.py --limit 4
   python evaluate_live.py --all  # runs the entire 16-case suite and may incur API charges
   ```

The evaluation writes `evidence/live_evaluation_results.json` with the **actual run timestamp, model-called flag, decision, policy IDs, tool traces and per-case pass/fail**. This output is intentionally `.gitignore`d: review and redact any traces before publishing. Live pass percentages are **unknown until execution**.

## GitHub workflow

The root `.github/workflows/hr-agent-live-eval.yml` enables a **manual-only** GitHub Actions evaluation. Add `OPENAI_API_KEY` as a repository Actions secret (Settings → Secrets and variables → Actions → New repository secret), then manually launch **HR Agent — Manual Live LLM Evaluation** from the Actions tab. It does **not** run automatically on push. Live API charges may apply. The workflow retains evidence as a short-lived Actions artifact rather than committing it automatically.

## Architecture & control boundaries

**Prompt → deterministic privacy pre-check → LLM (OpenAI Agents SDK) → read-only `search_hr_policies` tool → optionally `request_human_review` simulation → structured decision → host-side validation → response + trace.**

The model cannot issue binding approvals: independently enforced host rules route manager-owned decisions and exceptions to humans. The agent does not have access to real employee data, HRIS, Gmail, SharePoint, external databases or ticketing systems. `request_human_review` records a **simulated handoff only**. Direct answers must reference a policy actually retrieved by an executed tool; otherwise the host refuses to present unverified content. This doesn't completely prevent fabricated details *inside* a cited answer, so independent human review and a larger held-out evaluation set are mandatory before production use.

### Verification matrix

| Layer | Verification performed | Status |
|---|---|---|
| Original rule-based agent | Six offline regression tests | Passed 6/6 |
| LLM host safety envelope | Seven offline tests | Passed 7/7 |
| Live model API authentication | Actual HTTP/SDK call | **Not run — missing API key / installed SDK** |
| Tool calls by a real LLM | Captured production/model traces | **Not run** |
| Live response correctness | 16-scenario model-backed evaluation | **Not run** |
| Microsoft Copilot Studio connection | External tenant/connector | **Not connected** |

## Why OpenAI first, Copilot Studio second

The OpenAI Agents SDK lets this project demonstrate genuine Python agent development, structured outputs and tool-call evaluation without relying on Microsoft 365 tenant rights. Copilot Studio can be a valuable *second* implementation in a licensed tenant with Power Automate, HR policy sources and approvals. Its trial and full publishing capabilities differ by license. No Microsoft integration is necessary to run this first model-backed prototype.

## Security and cost controls

- Use a project-scoped API key with low usage limits; never post it in GitHub source or chat.
- First run one case, then four, then the full 16 only if results justify the expense.
- Use only synthetic DemoCo HR policies and prompts, not real employee data.
- Never allow autonomous approve/write tools in this evaluation project.
- Keep the human approval decision on the trusted application side, not only in the LLM prompt.
- Add held-out prompts, adversarial/multi-turn injection cases, source accuracy checks, error budgets, privacy review, access control and monitoring before real HR deployment.