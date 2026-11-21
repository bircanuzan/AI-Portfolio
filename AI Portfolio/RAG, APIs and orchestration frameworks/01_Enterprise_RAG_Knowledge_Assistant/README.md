# Enterprise RAG Knowledge Assistant — Reference Project

**Project type:** Proposed proof-of-concept using synthetic enterprise policy documents. **Status:** Architecture and evaluation specification; no production deployment or verified benchmark results.

## Client requirement / business problem
An enterprise needs reliable answers from versioned internal policies with citations, role-aware access, documented evidence, and escalation when evidence is missing. Unrestricted LLM responses risk hallucinated answers, outdated policy references, and disclosure across departments.

## Methodology
1. Define synthetic HR, IT and operational policy corpus, including revision dates, document owners, and access labels.
2. Create an ingestion pipeline: parse, clean, chunk, attach metadata, embed, and index; re-index on document changes.
3. Retrieve by hybrid lexical/vector search, apply metadata/permission filters before generation, and optionally rerank candidates.
4. Generate grounded responses with citations and an explicit abstention route for insufficient evidence.
5. Expose service endpoints; log latency, retrieval traces, token consumption, version of evidence, and human review outcomes.
6. Evaluate retrieval separately from answer generation with a held-out, human-reviewed question set and adversarial examples.

## Proposed technology / AI
Python, FastAPI, Azure AI Search (or local FAISS), Azure OpenAI or model-agnostic LLM API, embeddings, optional LangChain/LlamaIndex, Pydantic schemas, pytest, GitHub Actions. These are design options, not claims of integrations already operated.

## Proposed API contract
- `POST /v1/ask`: {question, user_role, corpus_version} → {answer, citations, evidence_status, trace_id}
- `POST /v1/feedback`: {trace_id, rating, issue_type} → {accepted}
- `GET /health`: service readiness metadata
- Fail closed when authorization or evidence provenance is unavailable; redact sensitive log fields.

## Evaluation framework / KPIs (targets, not achieved results)
| Measure | Illustrative acceptance target | Evidence required |
|---|---:|---|
| Citation precision | ≥95% | Human review on synthetic answer set |
| Retrieval recall@5 | ≥90% | Labeled relevant passages |
| Groundedness | ≥95% | Rubric-scored responses |
| Unsupported-answer abstention | ≥95% | No-answer challenge set |
| P95 API latency | ≤4 sec | Timed staging load test |
| Unauthorized retrievals | 0 | Role-scoped adversarial tests |

## Deliverables
Architecture diagram, synthetic corpus and dataset specification, API contract, reproducible evaluation plan, risk register, human-escalation policy, acceptance test report template.

## Governance & limitations
No private/client data. Permission checks must happen before sending context to the model. No performance numbers are verified until the project is implemented and tests are run.
