# Generalist Annotation & Response Quality Rubric

All ratings are completed by a human reviewer; the script validates and aggregates those judgments.

| Criterion | Meaning | Weight |
|---|---|---:|
| factual_support | Claims are supported by supplied ground truth or verifiable evidence | 35% |
| relevance | Directly responds to the task | 20% |
| coherence | Clear, internally consistent, understandable | 15% |
| instruction_following | Observes format, scope and constraints | 20% |
| completeness | Addresses requested elements without inventing missing information | 10% |

Score anchors (each dimension): **0** unacceptable / clear violation; **1** serious issue; **2** mixed; **3** satisfactory with minor defect; **4** fully meets criteria.

**Critical rule:** a factual-support score of 0 triggers human escalation regardless of average. No unsupported number, legislation, scientific assertion, or medical recommendation may be accepted automatically. Ratings are not a substitute for domain-expert verification.

**Reviewer feedback template:** observation → exact evidence/quote location → effect on user/task → recommended change → final human disposition. Use neutral, specific language and preserve the source/task version.

**Record-level QA:** required fields, scores integer 0-4, known defect category, task ID, reviewer note, rubric version. On disagreement >1 score point per dimension, hold for adjudication.
