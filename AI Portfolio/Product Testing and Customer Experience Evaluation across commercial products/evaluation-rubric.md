# Evaluation and reporting rubric

## Scoring
Score each applicable dimension 0–4: 0 = blocked or incorrect; 1 = major friction or defect; 2 = partial success; 3 = meets expectations with minor friction; 4 = fully meets expectations with clear evidence. Use N/A for unsupported or nonapplicable behavior, and Not run for unexecuted cases. Exclude both from the scored denominator.

| Dimension | Weight | Evidence |
|---|---:|---|
| Customer onboarding and time-to-value | 15% | Registration, activation, recovery and first successful task |
| Dashboard usability and accessibility | 15% | Navigation, visual clarity, keyboard and error states |
| API functionality and reliability | 20% | Authentication, schema, status codes, valid and invalid requests |
| MCP integration and agent behavior | 20% | Setup, discovery, invocation, grounding, failure handling |
| Cross-product data consistency | 15% | Normalized comparable records and discrepancy analysis |
| Documentation and support | 15% | Quick-start completeness, discoverability and troubleshooting |

Weighted score = sum(weight × dimension score / 4) divided by sum of applicable, evaluated weights × 100. Report coverage separately. Do not interpret partial coverage as a complete readiness score.

## Issue severity
- Critical: security exposure or core data integrity failure with material impact.
- High: blocked core workflow or reproducible materially incorrect output.
- Medium: meaningful friction, recoverable failure or documentation gap.
- Low: minor usability issue or improvement opportunity.

## Evidence record
Record case ID, product channel, date/time, environment, expected outcome, actual outcome, status, severity, reproducibility, sanitized trace or screenshot, and limitations.

## Executive report structure
1. Scope, test environment and evaluation coverage.
2. Customer journey and time-to-value observations.
3. Product-by-product findings with evidence and business implications.
4. Cross-product discrepancies, integration risks and root-cause hypotheses.
5. Prioritized recommendations with acceptance criteria, proposed owner and effort.
6. Retest plan and measurement approach.

Separate verified defects from hypotheses and suggestions. Report no live results unless supported by executed tests. This rubric is a portfolio methodology, not a completed third-party product evaluation.
