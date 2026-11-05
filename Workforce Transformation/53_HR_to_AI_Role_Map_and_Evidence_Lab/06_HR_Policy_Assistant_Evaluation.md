# Case 3 — HR policy assistant: 20-question evaluation

**Hypothetical client pain point:** employees need prompt answers to routine HR service questions, while confidential requests and exceptions must be redirected to human HR staff.

**Artifacts:**
- [20 fictional input prompts + independently authored expected routes](data/hr_policy_20_evaluation_cases.csv)
- [Offline deterministic Python router and evaluator](scripts/policy_evaluator.py)
- [Reference-rule execution summary and individual cases](evidence/local_deterministic_evaluation.json)
- Related independently developed [Project 43 HR service agent](../43_Microsoft_Copilot_Studio_HR_Service_Agent_Prototype/)

**Local system design:** rule-based route selection with five fictional policy topics: leave, sick leave, remote work, payroll cycle and overtime. Sensitive or third-party employee information gets a REFUSE result; explicit policy exceptions/harassment/appeals get ESCALATE; unknown questions are not hallucinated.

**Evaluation:** For each question compare actual (route, policy ID) against an expected answer. Summarise per-case pass/fail and manually inspect failure patterns. Two deliberately hard cases (holiday wording and health schedule adjustment) reveal unhandled paraphrases and escalation ambiguity in a keyword-only approach. The errors are kept visible for audit.

~~~bash
python scripts/policy_evaluator.py
~~~

**Interpretation:** This tests an executable deterministic routing example, **not an LLM, Claude, Microsoft Copilot Studio, a production policy bot, a legal knowledge base, or genuine customer-service quality**. Performance on these 20 crafted examples is not representative of live usage. No actual employee data is used.

**Suggested follow-on if a real tenant is available:** add approved source citations, adversarial/ambiguous paraphrase sets, privacy boundary tests, versioned policy evidence, human approval handoff, latency/cost logging, and real anonymised output captures with consent.
