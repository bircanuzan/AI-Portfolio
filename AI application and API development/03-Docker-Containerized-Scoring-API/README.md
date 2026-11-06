# Containerized standard-library scoring service

**Featured technology:** Docker  
**Status:** educational prototype; results are not claimed as production deployments.  
**Scenario:** Package a credential-free JSON scoring endpoint in a small Python container; no external services needed.

## What this project demonstrates
- A focused, readable example of Docker used for a specific business problem.
- Synthetic or openly described example data; no customer, candidate, or employee information.
- Explicit local setup and constraints; production security and deployment are out of scope.

## Quick start
```bash
python -m venv .venv
# activate your environment
pip install -r requirements.txt
docker build -t portfolio-score-api . && docker run --rm -p 8080:8080 portfolio-score-api
```

## Acceptance checks
1. Install the listed dependencies in a clean environment.
2. Execute the command above; confirm the expected type of output for the synthetic scenario.
3. Record dependency versions, latency, runtime costs (if applicable), and any model failure cases before using this with real data.

## Limitations
The code is a starting reference example, not a claim that a production deployment or benchmark has been completed. Check current upstream APIs and service terms before use.

