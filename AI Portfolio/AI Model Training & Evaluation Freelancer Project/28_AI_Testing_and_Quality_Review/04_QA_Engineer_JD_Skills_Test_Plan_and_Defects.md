# software quality engineering — QA Engineer JD alignment and test engineering extension

**Source:** published QA-engineering role (remote, Dubai). **Project type:** synthetic local QA lab, not a external employer client project, real employer delivery or testing of external employer applications.

## JD → capability → practical evidence
| Advertised requirement | This project's artifact | Evidence / caveat |
|---|---|---|
| Test plans, cases and representative data | This file: traceability, positive/negative scenarios | Original synthetic test plan |
| Functional and regression QA | `qa_demo/test_api.py` | Python unittest |
| API and integration testing | `qa_demo/service.py`, `qa_demo/test_api.py`, Postman collection | Local mock HTTP app, not production API |
| Automated web UI | `qa_demo/playwright_smoke_optional.py` | Optional browser example; browser installation needed |
| Defect logging & retesting | Defect template below and incident workflow | No actual production defects |
| CI/CD automation | `.github/workflows/qa-demo-ci.yml` | GitHub Actions on project change; inspect workflow run for proof |
| Python or JS automation | Python standard-library HTTP tests; Playwright Python optional | Runnable local tests |
| Jira/TestRail/Zephyr, Agile | Defect fields and sprint acceptance/retest policy | Template; no real Jira workspace |
| ISTQB | Test-design techniques mapping | **No certificate claimed** |
| JMeter/k6, security, mobile testing | Planned acceptance/extensions | Not implemented or claimed |

## System under test (SUT)
A miniature local HTTP case-triage endpoint: GET /health, POST /cases and GET /cases/{id}. Sensitive updates must be explicitly confirmed, while unauthorized category and invalid inputs are rejected. **It is purposely not a real AI system.**

## Traceability matrix
| ID | Requirement | Test type | Expected |
|---|---|---|---|
| API01 | Service health | API smoke | 200 + ok |
| API02 | Valid case creation | Functional | 201 + case ID |
| API03 | Missing explicit confirmation | Negative/security | 400 |
| API04 | Disallowed write category | Negative/security | 400 |
| API05 | Duplicate idempotency key | Regression | Same case ID; no duplicate |
| API06 | Changed payload on reused key | Negative/integration | 409 |
| API07 | Retrieve created case | Integration | 200 with correct status |
| API08 | Retrieve missing case | Boundary | 404 |
| API09 | Malformed JSON | Negative | 400 |
| UI01 | Local form renders and client validation works | Optional Playwright | Required field feedback |

## Test levels and release gate
Requirements review → test-case design (equivalence partitions, boundaries) → Python API smoke → regression on every pull request → UAT with business owner → manual exploratory checks → defect triage and retest. Do not release with unresolved severity-1 privacy/unauthorized-write defects.

## Defect ticket template (ready for Jira, TestRail/Zephyr)
`Defect ID | Severity | Environment | Build/commit | Requirement/test ID | Preconditions | Steps | Input (redacted) | Expected | Actual | Evidence | Owner | Status | Fixed version | Re-test result`

Example **illustrative**, not observed: "QA-EX-01; P1; sandbox; API06; same key with new payload; expected 409; actual to be measured; owner TBD; status NOT EXECUTED."

## Metrics and measurement
Test case coverage = requirements with passing tests / requirements in scope. Defect escape rate, time to resolve, reopen rate, flaky test rate, automated build pass %, p95 response time. No employer production metrics are reported. Capture GitHub Actions run permalink, logs and test result after execution.

## Run locally
`python -m unittest discover -s qa_demo -p 'test_api.py' -v` from this project folder, or run the entire root project's test suite. See `qa_demo/README.md`.

**Integrations planned:** Postman, Playwright/Selenium/Cypress/Appium, Jira, CI/CD, JMeter/k6 and basic OWASP API risk checks. Only the subset actually present in code or documentation is demonstrated here.
