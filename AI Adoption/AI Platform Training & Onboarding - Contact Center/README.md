# AI Platform Training & Onboarding — Contact Center

**Project type:** Original simulated enterprise onboarding package for AI image/video creative workflows. **No sector_organization affiliation, actual production onboarding, tested third-party model output, or completed platform certifications are claimed.**

## Scenario and goal
A fictional UAE contact-center customer-support team has to create safe, brand-consistent visual and short-form training assets in an approved AI creative platform. The training specialist must onboard agents, teach prompting and media review, detect poor generations, escalate product defects, and hand off only competent agents to Operations.

## Intended audience
New contact-center agents, team leaders and creative-operations specialists. Assume mixed AI literacy, bilingual customer population, onsite/remote delivery, restricted client data and a training-to-production release gate.

## Demonstration package
1. [90-minute hands-on facilitator guide](workshop_and_onboarding_plan.md).
2. [Prompt-writing lab, image and video test cases, expected checks](prompt_lab_and_test_cases.md).
3. [Quick user guide, fault tree and escalation matrix](user_guide_troubleshooting_escalation.md).
4. [Competency rubric and production-release procedure](competency_and_handoff.md).
5. [Synthetic cohort observation log](synthetic_training_tracker.csv).
6. [Offline Python performance and feedback report](training_metrics.py).

## Skills and methods from the two vacancy briefs
- **Learning design:** TNA, learner segmentation, objectives, ADDIE, Bloom, constructivist exercises, structured handouts, feedback, accessibility and QA.
- **Software / product onboarding:** classroom + remote demonstration, hands-on exercises, reference material preparation, client progress tracking, learner Q&A.
- **Creative AI:** image/video prompt structure, reference use, aspect ratios, consistency, storyboarding, iteration, artifact review and content-rights/privacy awareness.
- **Operations:** trainer metrics, retraining, blocker logs, Solution Architect escalation, human approvals, readiness assessment and agent handoff.
- **Analytics:** completion, attempt rate, prompt quality, output QA, proficiency, learner sentiment and remediation.

## Tools and evidence limitations
Platform-agnostic design is compatible with workflows on Runway, Adobe Firefly, Canva AI or comparable **approved** image/video tools; the actual UI, outputs, limits, pricing, rights and safety behavior vary. These named products are **training targets to validate**, not proof of hands-on deployments. Offline scripts use Python 3; spreadsheets can be imported to Excel or Power BI. Demo footage and screenshots are **not** included; capturing real interaction is a next step.

## Run report
`python training_metrics.py`

## Evidence needed to convert design into a tested demonstration
Get authorized platform access; record a 5-minute desktop walkthrough using synthetic prompts; retain prompts, outputs, timestamps, model/version, reviewer notes and evidence captures; deliver a 3–5-learner pilot; update the assessment CSV with consented anonymized results; log defects and technical escalations. Do not upload client media or personal data.
