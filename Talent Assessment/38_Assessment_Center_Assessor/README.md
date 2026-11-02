# Project 38 — Assessment Center Assessor

**Portfolio case study: competency-based observation, evidence-based evaluation, professional reporting, candidate debrief and development coaching.**

## What this project shows
A complete, fictional English-language assessment-centre case for a **People Operations Manager** candidate. It includes assessor materials, three simulation exercises, anchored competency ratings, structured behavioral notes, independent assessor comparison, an integrated report, a feedback conversation and a coaching follow-up plan.

**This is an original assessor-practice demonstration**. It is not a live client assignment or evidence of assessment-centre delivery, **BPS assessor qualification**, psychometric certification, Arabic-language reporting or actual candidate assessment.

## Open the project deliverables

| Item | What you'll see | Job-description requirement |
| --- | --- | --- |
| [01 — Assessment design and competency matrix](01_Assessment_Design_and_Competency_Framework.md) | Purpose, exercise-to-competency map, rating anchors, process | Competency-based evaluation |
| [02 — Assessor observations and exercise guides](02_Assessor_Observation_and_Exercise_Guides.md) | In-basket, stakeholder role-play and group discussion, evidence recording | Candidate observations |
| [03 — Professional illustrative assessment report](03_Illustrative_Candidate_Assessment_Report.md) | Integrated competency profile, balanced evidence and limitations | Professional reports |
| [04 — Candidate feedback and debrief script](04_Candidate_Feedback_and_Debrief_Script.md) | 30-minute strengths/development conversation | Candidate feedback |
| [05 — Development coaching plan](05_Post_Assessment_Development_Coaching_Plan.md) | Practical 30/60/90-day coaching journey and evaluation | Development coaching |
| [06 — Assessor calibration and quality control](06_Assessor_Calibration_Quality_and_Fairness.md) | Inter-rater checks, consensus, bias prevention and privacy | Assessment reliability |
| [07 — Certification and language eligibility](07_Assessor_Credentials_and_Language_Limitations.md) | Honest distinction between coaching credentials and assessor qualification | Role suitability |
| [Fictional candidate briefing pack](data/candidate_briefing_pack.md) | Exercise source materials and participant context | A realistic assessment |
| [Synthetic ratings](data/assessor_observations.csv) | 24 independently simulated ratings across 12 observations | Structured rating data |
| [Human-style adjudication decisions](data/adjudicated_ratings.csv) | Final decisions and evidence-based rationale | Integration and consensus |
| [Python scoring audit](src/score_assessment.py) | Validates data and calculates competency averages, exact agreement and Cohen's kappa | Scoring, evidence audit |
| [Unit tests](tests/test_assessment_scoring.py) | Positive and negative quality checks | Reproducible QA |

## Sample output
The fictitious Candidate A has integrated scores on a **1–5 evidence-based scale**:
- Analytical Thinking: **3.67**
- Stakeholder Management: **3.00**
- Decision Making: **2.67** (development priority)
- Coaching & Development: **3.33**
- Overall *descriptive* mean: **3.17 / 5**

Two simulated assessors agree on **10/12 recorded ratings (83.3%)**. Both mismatches are explicitly documented and adjudicated. These are only illustrative calibration statistics, not validated psychometric results or a hiring cutoff.

## Run the scoring example
Python 3.10+ standard library; no external systems, AI API key or personal records needed.

    python src/score_assessment.py
    python -m unittest discover -s tests -v

## Standards-informed structure
The guidance emphasizes observable behavior, assessor preparation, structured observation and recording, frame-of-reference calibration, evidence integration and responsible feedback. This is consistent with the [international assessment center guidelines](https://doi.org/10.1177/0149206314567780) and [CIPD selection guidance](https://www.cipd.org/uk/knowledge/factsheets/selection-factsheet), **without a claim of accreditation or conformity audit**.

### Important application eligibility
The Assess International opportunity described requires **recognized assessor certification or accepted equivalent** and **English and Arabic reporting**. ICF professional coaching may be valuable for developmental feedback, but it is **not automatically equivalent to BPS assessor training or certification**. This portfolio is drafted in **English only**; it does not resolve the Arabic requirement or independently confirm a recognized assessor qualification.

Reference: [Assess International company page](https://www.linkedin.com/company/assess-talent-management/). The company also offers [Assessor Practice & Skills training](https://www.assesstm.com/training_certification/assessor-practice-skills). **No application email has been sent.**
