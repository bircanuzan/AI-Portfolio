# Enterprise AI toolkit: selection and vendor evaluation

## Candidate tools — evaluate, do not assume deployment
| Function | Candidate classes and examples | Controlled pilot |
|---|---|---|
| Coding | GitHub Copilot, Sourcegraph Cody, approved IDE assistant | scoped PRs and test review |
| QA / testing | AI test generation and CI-integrated assistants | seeded regression suite |
| Product / research | Perplexity Enterprise or an approved enterprise retrieval tool | source-cited competitive/feature brief |
| Documentation / knowledge | Enterprise LLM + retrieval over access-controlled documents | versioned product documentation QA |
| Commercial content | Approved marketing assistant (e.g., Jasper) | RFP answer drafts with verified claims |
| Process automation | Make, Zapier or internal workflow orchestrator | sandbox request routing and approval |
| Integration | Approved LLM API, tool calling and MCP-compatible connectors | allowlisted tools with least privilege |

**Selection principle:** compare current pricing, data terms, availability, model options and residency in procurement; no assumptions about vendor support or product security posture.

## Weighted assessment rubric
| Criterion | Weight | Test evidence |
|---|---:|---|
| Privacy, security and data handling | 25% | data-processing terms, retention, SOC/ISO evidence, tenant controls |
| Measured task quality | 20% | blind benchmark accuracy, review burden, test output |
| Engineering/integration fit | 15% | APIs, SSO, RBAC, logs, CI and MCP controls |
| Net economic value | 15% | cost + review time + measured benefit |
| Usability and adoption | 10% | activation and weekly active users |
| Regulatory/compliance alignment | 10% | jurisdictional sign-off and audit evidence |
| Vendor resilience/portability | 5% | export, lock-in, fallback and SLA |

Compute `weighted_score = SUM(weight_i * score_i/5)` yielding 0–100. **Security and legal requirements are gates**, not compensatable scores.

## Two-week evaluation protocol
1. Define 10–30 representative tasks per function; use synthetic or explicitly approved de-identified datasets.
2. Randomize baseline vs AI-assisted tasks where practical; record complexity and human-review time.
3. Track completion time, error severity, satisfaction, acceptance/revert rate and actual cost.
4. Conduct security/privacy reviews and red-team exercises (prompt injection, data leakage and unsupported claims).
5. Publish decision: reject / extend pilot / approve limited rollout, with owner and expiry date.

## Living toolkit register columns
`tool_id | vendor | purpose | business_owner | system_owner | data_class | approved_data | jurisdiction | model_version | integration | monthly_cost | adoption_7d | task_quality | review_minutes | risk_level | approval_status | review_date | exit_plan`

## Example score — illustrative calculation only
A candidate with criterion scores `[4,4,3,3,4,4,3]` yields `(25×4 + 20×4 + 15×3 + 15×3 + 10×4 + 10×4 + 5×3)/5 = 73/100`. This **does not mean approved**: any failed privacy/security gate rejects it.
