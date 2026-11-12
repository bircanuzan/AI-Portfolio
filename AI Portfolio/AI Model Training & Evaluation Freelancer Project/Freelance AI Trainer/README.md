# Freelance AI Trainer | Workplace GenAI Prompt Clinic

> **Portfolio status:** Independent, synthetic demonstration. No confidential information, employer/client work, actual model-training delivery or production deployment is claimed. All records and ratings are invented to exercise the methodology.


## Objective
Design a short, hands-on enterprise learning session for professionals who want to use generative AI safely and effectively for day-to-day work. This is **human training on AI tools**, not model annotation, and deliberately distinct from the model-evaluation projects.

## 90-minute workshop agenda
| Time | Module | Practical output |
|---|---|---|
| 0-10 min | Business goals, preassessment and safe-use rules | Baseline task and privacy checklist |
| 10-25 min | How generative AI works and fails | Hallucination and uncertainty exercise |
| 25-45 min | Prompt engineering: role, context, task, constraints, format and verification | Participant prompt template |
| 45-65 min | Workplace labs: summarize, draft, compare, analyze | Before/after prompt revisions |
| 65-80 min | Automation workflow map and human review gates | Safe AI-supported workflow plan |
| 80-90 min | Assessment, feedback, next steps | Scored demonstration and action plan |

## Audience-specific exercises
- **HR:** anonymized interview rubric or competency framework with prohibited sensitive data removed.
- **Finance:** synthetic spreadsheet summary and cross-check of figures.
- **Business operations:** convert an SOP to a checklist, verify each step and escalation.
- **Marketing:** draft and revise a value proposition, flag any invented proof claims.

## Deliverables
- `facilitator_guide.md`: delivery instructions and troubleshooting playbook.
- `participant_prompt_guide.md`: reusable safe prompt templates and an editable exercise.
- `data/scoring_criteria.json`: transparent assessment criteria and rubric anchors.
- `src/prompt_assessment.py`: offline checklist validator for a participant prompt plan.
- `tests/test_prompt_assessment.py`: regressions for missing safeguards.

## Measurement
Pre/post exercise rubric score; completion and accuracy improvement on matched synthetic tasks; participant confidence (self-report, not proof of capability); follow-up adoption at 30 days with consent. Avoid unmeasured ROI claims.

## Run
```bash
python -m unittest discover -s "AI Model Training & Evaluation Freelancer Project/Freelance AI Trainer/tests"
```

## Safeguards
No sensitive personal/customer information pasted into public AI tools. Every AI-generated output requires factual review, permission checks and human final approval when business decisions, finance, HR or compliance are involved.
