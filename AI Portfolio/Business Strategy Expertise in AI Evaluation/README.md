# Business Strategy Expertise in AI Evaluation

An independent portfolio framework by Bircan Uzan, HumanEvoX Consultancy.

## Purpose and evidence status

This folder shows how business-domain judgement can be translated into auditable AI evaluation tasks. It is aligned with Alpheva's Business Strategy Expert role. The worked examples are fictional and manually authored. This is a documented evaluation design with a reusable rubric and worked cases, not a completed client engagement, live model benchmark or production deployment.

## Business requirement

Review AI-generated strategic recommendations and distinguish persuasive writing from decisions supported by evidence, arithmetic and implementation constraints. Produce reference answers and scoring criteria that another reviewer can apply consistently.

## JD-to-capability mapping

| Role requirement | Evaluation activity | Review artifact |
| --- | --- | --- |
| Market analysis | Check market definitions, geography, dates, sources and uncertainty | Evidence ledger and assumption list |
| Strategic alternatives | Compare at least two viable options against explicit objectives | Options matrix with rationale |
| Unit economics | Recalculate contribution, break-even and downside scenarios | Transparent calculations with units |
| Execution trade-offs | Test staffing, capacity, dependencies and sequencing | Feasibility and risk assessment |
| Model response review | Identify unsupported conclusions and consequential mistakes | Annotated response with severity |
| Reference answers | Explain defensible conclusions and acceptable alternatives | Answer key with evidence references |
| Scoring criteria | Separate independently observable criteria | Anchored rubric and reviewer notes |
| Asynchronous collaboration | Make review decisions reproducible | Case ID, version, source and change log |

## Skills demonstrated by the framework

Business problem framing; requirements analysis; operating-model review; scenario analysis; evidence appraisal; assumption checking; KPI interpretation; risk identification; rubric design; response-quality assessment; error classification; written explanations; reviewer calibration.

Professional experience in consulting, workforce programmes and service operations supplies domain context. The synthetic financial examples below are learning/evaluation artifacts, not claims of paid financial-strategy delivery.

## Technology and tools

**The JD specifies no programming language, model provider or software product.** Its essential requirements are domain expertise, reliable evaluation and precise written reasoning.

Tools suitable for implementing this design:

| Tool or format | Purpose | Status in this folder |
| --- | --- | --- |
| Markdown | Document prompts, reference reasoning and rubric anchors | Implemented |
| Spreadsheet formulas / Excel | Independently check margins, capacity and sensitivity assumptions | Calculations documented; workbook not included |
| CSV / JSONL | Store versioned cases and structured review records | Proposed extension |
| Python, decimal | Automate repeatable arithmetic checks without binary float rounding | Proposed extension; no code supplied |
| Power BI | Summarise error patterns and reviewer agreement | Proposed extension; no dashboard supplied |
| LLM APIs | Collect candidate responses with model/version metadata | Proposed extension; no API calls performed |

These are practical implementation choices, not technologies required by the employer.

## Review workflow

1. Define the decision, business objective and constraints.
2. Assemble a source pack and mark missing facts.
3. Write a prompt and an answer key that permits more than one defensible strategy.
4. Review the candidate response against the rubric.
5. Recalculate material numbers and challenge unsupported certainty.
6. Record exact evidence for each failure and its business consequence.
7. Write a corrected response and explain why it is better.
8. Calibrate disagreements with a second domain reviewer before acceptance.

## Reusable rubric

Score each dimension 0 (material failure), 1 (partially supported), or 2 (supported and complete).

| Dimension | Full-credit evidence |
| --- | --- |
| Factual grounding | All material claims trace to the provided pack or are explicitly assumptions |
| Numerical correctness | Correct formulas, units, periods and arithmetic |
| Alternative comparison | Viable options assessed against the stated objective |
| Feasibility | Capacity, resources, prerequisites and timing considered |
| Risk and uncertainty | Material downside and missing information explained |
| Decision clarity | Recommendation is conditional where appropriate and actionable |

A fabricated source or a material arithmetic error that reverses the recommendation requires revision regardless of total score. The 12-point total is a proposed review aid, not a validated predictor of model quality.

## Error record template

Case ID; response version; source-pack version; disputed passage; error category; supporting evidence; business consequence; severity; proposed correction; reviewer; decision; unresolved questions.

Use critical severity for errors that could reverse a material commitment, major for substantive omissions, and minor for presentation issues that do not change the decision.

## Worked examples and current output

See [worked_cases.md](worked_cases.md) for three synthetic examples covering margin feasibility, capacity constraints and unsupported market expansion.

Delivered: a JD-aligned method, eight capability mappings, six rubric dimensions, a review-record template and three manually checked examples. No live-model scores, commercial ROI, client savings or inter-rater reliability results are claimed.

## Governance and limitations

Use synthetic or permissioned data. Remove customer and employee identifiers. Domain reviewers retain final judgement; financial, legal and employment commitments require the relevant authorised decision maker. Statistical agreement, model comparisons and real-world effectiveness remain untested.

Role reference: https://alpheva.ai/jobs/98ba8be6-228d-498f-9901-ed86b96f0f02/

[AI portfolio](../README.md)
