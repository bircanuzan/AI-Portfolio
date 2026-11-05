# Digital-worker probation & performance scorecard — evidence-aware review

## Evaluation categories
| Competency | Evidence required | Go-live rule |
|---|---|---|
| Policy accuracy | Independent HR benchmark with real agent responses and valid citations | >=95% on predefined holdout; review by policy owner |
| Safe handoff | High-impact, missing-source, personal-data and adversarial scenarios | 100% human-required recall in the release benchmark |
| Data/permission safety | IAM and connector penetration tests, privacy impact, security incident simulation | No unacceptable high-severity finding |
| Workflow reliability | Actual Power Automate/Teams flow histories and retries | Separate approver + auditable outcomes |
| Employee experience | Representative user testing and accessibility review | Meet measured acceptance criteria |
| Business value | Baseline vs supervised pilot, including rework and supervision | Net value with full costs documented |
| Auditability | Source/version, agent ID, context, decision, action and human signoffs | Complete required audit events |

## Evidence now available
Project 43 **ran 28 prompts through actual local deterministic JavaScript code**; 26 matched expected decisions and policy IDs (92.9%). All recorded responses, including two conservative failures, are retained in the [evidence dataset](../43_Microsoft_Copilot_Studio_HR_Service_Agent_Prototype/evidence/2026-10-29_test_run.json). “What is the annual leave policy?” returned a sample policy response with HR-POL-002 v0.1 citation; “What's my remaining leave balance?” returned human escalation; an employment letter request returned approval-required metadata **without invoking a workflow**.

**This score does not evaluate an AI/LLM or Copilot Studio**. It is a reproducible local program test, not a real employee or production service performance appraisal. The old 12-row [CSV](data/agent_assessment_cases.csv) is independently authored synthetic test data, not an output transcript.

## Decision
**HOLD:** 2 synonym intent misses; no tenant deployment, real model observations, independent red team, human approval delivery, legal/privacy validation, or quantified ROI. Even a perfect local score would not justify enterprise rollout.

## Proposed 30/60/90-day probation review
- Days 1–30: configure Copilot Studio in sandbox; source-policy access, technical boundary tests, independent test design.
- Days 31–60: test actual model and connectors in shadow mode; capture reviewed transcripts and flow approvals.
- Days 61–90: supervised gated pilot (only after security and HR signoff); measure rework, satisfaction, human reviewer workload and true cost-to-serve.

**Approvals:** HR Ops Owner pending; Security pending; Policy Owner pending; Engineering pending; Compliance pending.
