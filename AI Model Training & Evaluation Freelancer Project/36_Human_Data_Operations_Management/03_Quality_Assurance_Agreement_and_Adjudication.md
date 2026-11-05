# 03 | Quality assurance, inter-rater agreement, reviewer calibration and release

## Dataset structure
- data/source_requests.csv — 18 intentionally fictional case texts
- data/annotations.csv — two independent fictional label passes, annotator IDs A and B
- data/adjudicated_gold.csv — standalone reference labels established for this exercise
- data/operations_events.csv — simulated annotation task operations

## Gate 1 — structural validation
Every source case must have exactly one valid label per expected annotator, one gold label, nonempty text and unique IDs. Unknown class codes or duplicate annotator-case combinations are a **hard failure**. All annotation references must exist in source.

## Gate 2 — annotation quality
- **Observed agreement:** A/B exact-match count divided by items scored by both.
- **Cohen's kappa:** (observed agreement - chance expected agreement) / (1 - chance expected agreement), using empirical label marginals. Low sample sizes and unbalanced classes require interpretation.
- **Gold checks:** correct labelled cases / independent gold cases, separately for A and B. Synthetic gold examples are not representative quality results.
- **Disagreement themes:** other vs policy, other vs benefits and confusion between mobility/recruitment.
- **Calibration target:** illustrative 80% minimum agreement before extending an example pilot. This threshold is *not* a universal data industry standard.

## Gate 3 — adjudication
Store reviewer decision and reason: category-specific evidence, policy version, source ambiguity, guideline update and authorized reviewer. Re-run confidence and error samples. Preserve original labels for audit, never silently overwrite.

## Gate 4 — release
Quality lead, data security owner and project sponsor approve the dataset's **permitted use** (human eval, model testing, training if separately licensed). This repository does not authorize real training on any private human data.

## Binary example acceptance checklist
- Are 18 unique source cases present?
- Are all labels in the approved six-class taxonomy?
- Does every case have one A and one B annotation?
- Do all 18 cases have a gold label?
- Are original source records unmodified?
- Are A/B disagreements clearly listed and assigned?
- Are adjudication evidence and guideline versions recorded?
- Was sensitive data removed/approved at intake?
- Did the calibration gate pass before expanding the sample?
- Is the release purpose and data-access authorization documented?

The fictional dataset is intentionally designed to fail the 80% calibration gate; it is a quality-improvement demonstration.
