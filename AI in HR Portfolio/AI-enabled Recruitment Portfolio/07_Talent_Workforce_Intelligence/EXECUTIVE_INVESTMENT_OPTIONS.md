# CHRO & CAIO investment appraisal — three alternatives, no assumed AI advantage

**Project 07 executive extension: workforce capacity & resource economics.** This does not repeat Project 55's algorithmic fairness controls or Project 01's clinical licensing.

## Decision
A fictional employer considers: (1) manual baseline; (2) standardised non-AI process; (3) human-reviewed AI-assisted drafting. The executive must determine whether any additional process/tooling cost is justified **before** buying AI software.

## Synthetic input assumptions
- **5,000** yearly workflow units, assumed **24 minutes** handling each, **AED 100/hour** hypothetical fully loaded cost.
- Adoption and time avoidance are *not observed*; no experiment or client implementation.
- Standardised workflow: 25% potential avoidable time, 75% effective adoption, 0.5 minute extra oversight per case; AED 12,000 annual platform + 8,000 assurance + 20,000 one-time change.
- AI-assisted drafting: 45% potential avoidable time, 70% effective adoption, 1 minute extra mandatory human review; AED 42,000 annual platform + 30,000 assurance + 70,000 one-time change.
- No cash saving is attributed to hours. No revenue, attrition or candidate outcomes forecasted.

## Reproducible result on invented assumptions
| Option | Net capacity change (hours) | Hypothetical capacity value | One-time + annual cost | First-year capacity value less cost |
|---|---:|---:|---:|---:|
| Manual baseline | 0.00 | AED 0 | AED 0 | AED 0 |
| Non-AI process simplification with human approval | 333.33 | AED 33333 | AED 40000 | AED -6667 |
| Optional drafting assistant with mandatory human review | 546.67 | AED 54667 | AED 142000 | AED -87333 |

**Decision from this fictional exercise:** do not fund AI on assumed productivity claims. First document actual work and test simpler process improvement. A positive capacity value in other inputs still does **not** justify a cash ROI claim; the costs of adoption, fairness, review, data handling and training must be validated.

## Work samples
- [Inputs — labelled invented economic assumptions](data/synthetic_executive_options.json)
- [Python option comparison with guardrails](src/executive_value_options.py)
- [Unit tests / negative controls](tests/test_executive_value_options.py)
- [Versioned reproducible scenario evidence](evidence/synthetic_executive_options.json)

Run locally:
```bash
python src/executive_value_options.py --out evidence/synthetic_executive_options.json
python -m unittest discover -s tests -v
```

## Board and finance checks required before capital approval
1. Measure actual review work, error rates, useful adoption and costs over sufficiently comparable periods.
2. Use independently reviewed contract prices and realistic implementation/assurance effort.
3. Distinguish hours made available, actual redeployment, headcount changes, contractor spend and bankable savings.
4. Define failure scenarios (low adoption, model error, high human review, higher vendor cost, poor candidate experience) and explicitly budget intervention.
5. Confirm legal basis, access, vendor security, job-valid assessment, human appeals, external validation and candidate safety **before** AI/high-consequence use.
6. Pilot with pre-agreed source, numerator, denominator, thresholds and named Finance/HR/CAIO owners.

This model is **capacity economics, not workforce optimisation by dismissals or real talent-market forecasting.**

[CHRO steering brief](../EXECUTIVE_STEERING_BRIEF.md) · [AI/human work allocation](../HUMAN_AI_RECRUITMENT_OPERATING_MODEL.md)
