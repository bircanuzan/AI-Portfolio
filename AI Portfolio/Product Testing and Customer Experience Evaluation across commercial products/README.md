# Product Testing and Customer Experience Evaluation across commercial products

**Portfolio project | Independent evaluation framework | AI-enabled SaaS, APIs and MCP integrations**

## Executive overview
This project defines a repeatable end-to-end evaluation of three interconnected commercial product interfaces: a web-based temperature/geospatial analytics dashboard, a REST temperature data API, and a Model Context Protocol (MCP) integration for AI assistants. The objective is to assess the customer journey from first registration through successful data retrieval, AI-assisted consumption and feedback, translating technical and usability observations into prioritized product improvements.

**Status:** Evaluation methodology and test design; no third-party product tests or client outcomes are claimed.

## Business requirement
Assess the first-time customer experience and production-readiness signals across an integrated product suite. Identify onboarding friction, documentation gaps, functional defects, data inconsistencies, integration barriers and opportunities to improve adoption, customer satisfaction and time-to-value.

## Scope and methodology
| Workstream | Evaluation activities | Evidence / deliverable |
|---|---|---|
| Customer onboarding | API-key registration, email delivery, spam handling, activation, dashboard login, error recovery and support escalation | Customer journey map, friction log |
| Dashboard testing | Navigation, city/location search, map interactions, data visualization, units, date selection, accessibility, responsive layouts, empty and error states | UX heuristic review, screenshots without sensitive data |
| REST API testing | Read quick-start and API reference; configure authentication; retrieve temperature data for supported US locations; validate schemas, units, timestamps, missing data, HTTP status codes, invalid inputs and documented rate limits | API test cases and sanitized request/response evidence |
| MCP integration | Configure an authorized MCP client using the documented transport and authentication; discover tools, inspect schemas, invoke read-only temperature queries and compare outputs to direct API responses | Integration test matrix, tool-call traces |
| AI-assisted experience | Evaluate prompt-to-tool selection, parameter mapping, grounding, ambiguous locations, unsupported geography, failure handling and transparent uncertainty | Agent evaluation rubric and regression cases |
| Cross-product QA | Compare matching location, time, units and data source across dashboard, API and MCP; investigate mismatches | Reconciliation log and issue register |
| Customer feedback | Assess onboarding clarity, value proposition, discoverability, documentation, reliability and support journey from a new customer perspective | Executive feedback report and prioritized roadmap |

## Execution approach
1. Define personas (new customer, developer, AI integration engineer), expected outcomes and supported geographic scope.
2. Establish a controlled test dataset with several US cities, explicit timestamps/time zones and consistent units. Include unsupported inputs as negative cases.
3. Follow the documented onboarding and quick-start guides; record time-to-first-success and friction at each step.
4. Run positive, negative, boundary and regression cases; record expected versus observed outcomes and reproducibility.
5. Compare API, dashboard and MCP outputs under equivalent conditions, accounting for documented refresh cadence, rounding and aggregation.
6. Score usability and technical quality separately; categorize issues by severity, business impact, confidence and remediation effort.
7. Prepare actionable recommendations, acceptance criteria and retest plan.

## Technologies and tools
Proposed toolchain (select according to product documentation and authorized environment):
- REST APIs, HTTP, JSON, OpenAPI/Swagger, API keys and environment variables
- Postman, cURL, Python, requests, pytest, JSON Schema and pandas
- Browser developer tools, Chrome/Edge, Playwright and accessibility checks (WCAG-informed)
- Model Context Protocol (MCP), MCP Inspector, Claude Code, Cursor or Codex as compatible clients
- Structured test case management, evidence logs, defect tracking and data reconciliation

## Skills demonstrated by the framework
Product QA, customer experience evaluation, UX research, customer journey mapping, SaaS testing, API testing, functional and negative testing, integration testing, MCP tool evaluation, agentic AI testing, LLM grounding assessment, data quality validation, technical documentation review, troubleshooting, automation design, root-cause analysis, risk-based prioritization and executive communication.

## Quality metrics and reporting
| Metric | Measurement |
|---|---|
| Onboarding success | Successful activation / attempted activations |
| Time-to-first-value | Elapsed time from registration to first successful data retrieval |
| Functional pass rate | Passed cases / executed cases |
| API response reliability | Successful valid requests / attempted valid requests |
| API latency | Median and p95 elapsed response time |
| Cross-channel consistency | Comparable records within documented tolerance / comparable records |
| MCP tool-call success | Successful valid tool invocations / valid invocation attempts |
| Grounded answer rate | Correctly sourced answers / evaluated answerable prompts |
| Documentation task success | Completed documented workflows / attempted workflows |
| Issue resolution | Verified closed issues / issues scheduled for retest |

All metrics are defined for future execution; no measured values or commercial outcomes are asserted.

## Deliverables
- [Test case matrix](test-matrix.csv)
- [Evaluation and reporting rubric](evaluation-rubric.md)
- Customer journey map, sanitized evidence log, technical defect register and executive recommendations (templates/outputs to be populated during an authorized evaluation).

## Governance
Use only authorized accounts and documented endpoints. Never publish API keys, credentials, private customer data or confidential materials. Use synthetic or permitted data, avoid excessive requests, redact evidence and distinguish observations from hypotheses. Findings require reproducible evidence before being represented as verified.
