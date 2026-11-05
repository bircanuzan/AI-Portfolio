# Evaluation findings and next-step delivery roadmap

**System under test:** Offline fictional Python-design keyword router; reference outputs independently calculated in JavaScript-equivalent logic. No cloud calls or enterprise pilot.

| Measure | Evidence |
|---|---:|
| Number of questions | 20 |
| Correct route + policy | 18 |
| Mismatches | 2 |
| Fixture match rate | 90.0% |
| Real LLM accuracy | Not measured |

### Preserved failures
- **Q06** — *Can I work while working from home?*: expected `ANSWER/REMOTE`, actually `UNKNOWN/NONE`. Root issue: missing paraphrase / vocabulary in exact keyword triggers.
- **Q10** — *How do I record working extra hours?*: expected `ANSWER/OVERTIME`, actually `UNKNOWN/NONE`. Root issue: missing paraphrase / vocabulary in exact keyword triggers.

### Risk-based remediation plan
**Gate 1 — HR approval:** Validate official company policy source, approver, version and jurisdiction. The current document set is imaginary.

**Gate 2 — Safety & coverage:** Add paraphrases, negative tests, multilingual queries, topic conflict and data-access attempts; rerun after every source revision.

**Gate 3 — Human workflow:** Define complaint, harassment and policy exception routing with access-controlled ticketing; test service-level and authentication controls.

**Gate 4 — Optional real AI:** Consider enterprise Copilot Studio/LLM only with a dedicated tenant, documented privacy review, versioned test data, model-output capture and human acceptance criteria.

### Business outcomes
This is a **self-contained demonstrable QA method**, not a real measured reduction in HR tickets or evidence of labour-law compliance. Proposed outcome measures would be collected only in an approved future pilot.
