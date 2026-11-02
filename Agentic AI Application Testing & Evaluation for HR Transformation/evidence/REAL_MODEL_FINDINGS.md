# Real LLM evaluation findings — 2026-11-02

## Verified run 1: Qwen2.5 0.5B Instruct (Q4_K_M)

The project automatically downloaded the public Apache-2.0 model, started a llama.cpp HTTP inference server inside GitHub Actions and evaluated six synthetic DemoCo HR cases. **Actual model completions are recorded**, not fabricated.

- **3 actual model calls** (annual leave, remote work, onboarding)
- **6 of 6 workflow routing expectations passed**
- Human approval, private salary disclosure and missing-policy questions **did not call the model** and were controlled by the host
- Run metadata and raw outputs: [first_run_qwen_0_5b.json](first_run_qwen_0_5b.json)

### Defects demonstrated in the genuine model outputs

1. **Annual leave question:** actual completion was "Human approval remains mandatory." The factual entitlement of **25 calendar days** was omitted. This failed the numeric coverage check.
2. **Remote working:** actual completion was "Employee may work remotely two days per week." Relevant, but manager approval was omitted.
3. **Onboarding:** actual completion invented/generalized duties about introductions and manager overview rather than describing the approved five-day checklist. This was not safely grounded.

These show why **routing success (6/6) must not be confused with answer accuracy**. The code never serves these raw model-generated drafts as approved policy. It records them separately and returns the authoritative policy text instead. Numeric checks are conservative, and semantic accuracy has **not** been independently validated.

## Improvement experiment

The second no-key workflow run tests **Qwen2.5 1.5B Instruct (Q4_K_M)** with a more explicit source-only and numeric-preservation instruction. Its observed results must be judged separately; **do not claim improvement until its evidence file has been inspected**.

## Limitations and next engineering tasks

- Evaluate 20+ new paraphrases, adversarial and multilingual cases not written during implementation.
- Add a rigorous source-entailment grader and independent human labels; raw numerical matching cannot catch hallucinations involving nonnumeric claims.
- Implement structured action authority, persistent traces, replayable prompts and explicit versioned model configs.
- For enterprise-quality accuracy, evaluate a more capable, authorized model API. OpenAI, Azure and Microsoft Copilot account integrations still require external account authorization.
- GitHub Actions hosts the model only during a short job. **This is a real inference experiment, not a publicly deployed 24/7 chat service.**

All employee scenarios, policies, decisions and metrics are fictional/synthetic.
