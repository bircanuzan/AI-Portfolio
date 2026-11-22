# AI Evaluation - Human Resources Expertise

HumanEvoX independent HR-domain AI evaluation portfolio project, designed around the **Alpheva AI — Human Resources Expert** domain evaluation vacancy: https://www.alpheva.ai/jobs/76042b19-12ff-4bfd-a509-265485861fc1/

## Scope

The project demonstrates how an HR subject-matter expert can assess AI-generated advice and agent action proposals in six human capital areas: talent acquisition, employer branding, HR operations, talent management, total rewards, and organizational design/workforce planning. Cross-cutting controls cover evidence, fairness, policy specificity, approvals and audit-ready feedback.

**Purpose:** evaluate AI-generated reasoning in real HR workflows, provide ideal reference standards, precise pass/fail rubric criteria, identify hallucinations, unsupported decisions and risky automation. Human experts retain employment decision rights.

## Realistic synthetic demonstration

- [Domain skills, AI techniques and technical tools](JD_SKILLS_TECH_AI.md) mapped to the Alpheva role and independent portfolio work
- [Evaluation method and model-review rubric](EVALUATION_METHOD.md): task creation, source grounding, SME scoring, exception handling and quality assurance
- [Synthetic HR evaluation cases](data/hr_eval_cases.json): eight fictional model-output examples and pass/fail expectations
- [Deterministic HR evaluation engine](src/hr_evaluation.py): evidence/approval safety checks and expected failure classification
- [Unit tests](tests/test_hr_evaluation.py): repeatable checks of policy, evidence, decision rights, failure capture and invalid cases

## Reproduce locally

    python "AI in HR Portfolio/AI Evaluation - Human Resources Expertise/src/hr_evaluation.py"
    python -m unittest discover -s "AI in HR Portfolio/AI Evaluation - Human Resources Expertise/tests" -v

Python 3.11+ standard library. The inputs, outputs and policy version are synthetic, not employee records and not employment law guidance.

## Evidence honesty

**Implemented:** synthetic dataset, deterministic checks, reference evaluation and Python tests. **Not implemented here:** live LLM inference, external Alpheva platform, RLHF training pipeline, annotation platform, production ATS/HRIS data access or actual agent deployment. Enterprise systems in the JD matrix are domain context / integration options, not claimed integrations.

The project is NOT an Alpheva commission, endorsement or paid client delivery. It should be described on a CV as an **independent AI evaluation demonstration**. It does not imply access to confidential HR data or real employment decision-making.
