# Writing Assessment
**Bircan Uzan | HumanEvoX Consultancy**

Independent synthetic portfolio exercise in comparative AI-response evaluation. Both candidate responses below are deliberately authored examples, not captured model outputs or an employer's assessment.

## Business problem and requirements
A team needs a short, reliable update about an AI-assisted workflow pilot. The evaluator must distinguish persuasive but unsupported claims from clear, evidence-grounded writing, then explain scores consistently.

The assessment covers factual accuracy, instruction adherence, clarity, tone, audience suitability, practical usefulness, internal consistency and written rationales.

## Demonstrated skills
Rubric-based evaluation; response comparison and preference ranking; evidence checking; unsupported-claim detection; critical analysis; editorial judgment; assessment design; concise reviewer feedback; decision documentation and escalation.

## Source brief
The following facts are fictional:
- A pilot lasted two weeks with 20 participating employees.
- Median task completion time was 12 minutes before and 9 minutes during the pilot.
- Review pass rate was 80% before and 85% during the pilot.
- Tasks varied and the pilot had no control group.
- The brief contains no financial-savings, headcount or production-deployment evidence.

**Writing instruction:** Write a 60-90 word update for department managers. Include the time change, quality change, one limitation and a practical next step. Use a measured professional tone and do not add unsupported claims.

## Candidate response A - deliberately flawed
> Our revolutionary AI pilot has proven that automation can transform the entire business. Across twenty employees, task time fell from twelve to nine minutes, a 25% reduction, while quality improved from 80% to 85%. These results guarantee major savings and show that staff can be replaced without affecting service. Managers should roll the system out company-wide immediately. This successful two-week exercise confirms that AI is universally faster and more accurate, with no further validation needed.

## Candidate response B - grounded alternative
> During a two-week pilot involving 20 employees, median task completion time decreased from 12 to 9 minutes, a 25% reduction. The review pass rate rose from 80% to 85%, an increase of five percentage points. These observations are encouraging, but tasks varied and there was no control group, so the pilot does not establish causation or company-wide performance. Managers should run a controlled follow-up, monitor quality by task type and retain human review before deciding whether to expand the workflow.

## Methodology
1. Read the instruction and source brief before judging style.
2. Mark each factual assertion as supported, unsupported or contradicted.
3. Check requested length, audience, measures, limitation and next step.
4. Score independently using the anchored rubric in [rubric.csv](rubric.csv).
5. Cite the exact response phrase and source fact for each material issue.
6. Compare responses after scoring; explain why a polished answer can still be unreliable.
7. Escalate unresolved evidence disputes and retain original and adjudicated scores.

## Worked assessment
Scores range from 1 (serious failure) to 5 (fully meets criterion).

| Dimension | Weight | A | B | Evidence and rationale |
|---|---:|---:|---:|---|
| Factual accuracy and support | 30 | 1 | 5 | A claims guaranteed savings, replaceable staff and universal performance without evidence. B preserves the stated limits. |
| Instruction adherence | 25 | 2 | 5 | A includes numbers and an action but omits a limitation. B covers every requested element within 60-90 words. |
| Clarity and coherence | 20 | 4 | 5 | A is readable but uses vague claims about transformation; B states the observation, limitation and decision sequence precisely. |
| Tone and audience suitability | 15 | 3 | 4 | A addresses managers but uses promotional certainty. B is professional, although the causation language could be simplified for some readers. |
| Practical usefulness | 10 | 2 | 5 | A proposes immediate rollout without validation. B proposes a controlled follow-up, task-level quality monitoring and continued human review. |

Weighted score = sum(weight × score / 5).
- A: **45/100**.
- B: **97/100**.
- Preference: **B**, based primarily on evidence support and complete adherence, not length or stylistic preference.

These are worked human/editorial example judgments. They are not model-performance measurements or inter-rater reliability statistics.

## Numerical reasoning check
Time reduction: (12 - 9) / 12 = 25%.
Quality improvement: 85% - 80% = 5 percentage points. Relative change is 6.25%; those two quantities must not be confused.

## Feedback for response A
Keep the observed time and quality figures. Remove guaranteed savings, replacement and universal-performance claims. Add the absence of a control group and variation in tasks. Replace immediate rollout with a controlled follow-up and explicit human review. Preserve an evidence-based, measured tone.

## Recordkeeping and governance
Log task_id, response_id, source_version, criterion_id, score, quotation, rationale, reviewer, timestamp and adjudication. Randomize A/B order during genuine trials; score before preference selection to reduce position bias. Use synthetic content, keep private information out of annotation platforms and obtain permission before any screen recording.

Critical flags: unsupported high-impact recommendations, fabricated sources, contradictory calculations, inappropriate personal data, or concealed uncertainty. A high total does not cancel a critical flag.

## Tools and technology
**Used:** Markdown, CSV, source comparison, weighted arithmetic and written assessment records.
**Optional:** spreadsheet scorecards and a digital annotation/review platform for team calibration. No specific commercial annotation platform, automated grader, RLHF training run or API use is claimed here. The role focuses on judgment; adding unnecessary engineering tools would not strengthen this example.

## Outputs and limitations
Delivered one synthetic brief, two authored responses, five anchored criteria, a completed comparative scorecard, a preference rationale and actionable feedback. One example pair cannot establish evaluator reliability. No second independent reviewer has calibrated these judgments.

Next steps: add diverse writing domains and borderline cases, blind response identities, collect independent reviews and measure agreement. Do not convert this demonstration into a claim of paid academic marking or production AI-training impact.
