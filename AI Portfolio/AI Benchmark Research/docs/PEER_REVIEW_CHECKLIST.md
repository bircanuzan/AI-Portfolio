# Peer reviewer & benchmark auditor worksheet

**Task ID / version:** ______  
**Reviewer:** ______  
**Date / source freeze:** ______  
**Model or task under review:** ______

## Independent blind review (pass / revise / reject)
- [ ] One stable, unique short answer; exact wording and temporal cutoff.
- [ ] Answer key can be independently reconstructed from linked official/primary evidence.
- [ ] Relevant source pages are reachable; exact section/page, retrieval date and document version captured.
- [ ] Search strategy requires the intended reasoning/retrieval challenge, not merely an obscure spelling.
- [ ] No direct answer leakage or copied held-out benchmark questions/answers.
- [ ] Distractors documented; alternate correct interpretations ruled out.
- [ ] Non-English naming, time zone, units, old/new registry IDs checked where relevant.
- [ ] No unsafe personal information or prohibited collection methods.
- [ ] Source authenticity and conflicts reviewed; secondary-source repetitions not counted as independent verification.
- [ ] Grading aliases reflect formatting only, not changed meaning.
- [ ] Live test settings and raw permitted tool logs archived when outcome claims are made.
- [ ] Failure mechanism matches observed evidence; ambiguity not scored as model error.

## Scored release rubric (0–2 each; maximum 12)
| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Verifiability | Unsupported | Partial | Primary-sourced, inspectable |
| Unambiguity | Multiple answers | Needs revision | One accepted answer |
| Difficulty | Trivia | Moderate hops | Demonstrated hard after pilot |
| Reproducibility | Missing | Partial traces | Frozen records and run settings |
| Diagnostic value | Unclear | Plausible | Root-cause evidence |
| Safety & quality | Unsafe/unreviewed | Mitigation needed | Cleared and reviewed |

**Automatic rejection:** an invalid ground truth, an irreparable ambiguity, unauthorized access, or leaked held-out key.  
**Pass threshold:** 10/12 plus all automatic gates satisfied, with **two independent reviewers** for released advanced tasks. This threshold is a proposed local rubric, not a published industry standard.

## Adjudication record
- Author's answer and source: ______
- Blind reviewer's independent answer and source: ______
- Contradiction or changed edition: ______
- Decision: accepted / revision / rejected
- Justification and timestamp: ______
- Version change log: ______

**Critical note:** local unit tests verify grader behavior. They do **not** substantiate claims that a benchmark is difficult or breaks a state-of-the-art model.