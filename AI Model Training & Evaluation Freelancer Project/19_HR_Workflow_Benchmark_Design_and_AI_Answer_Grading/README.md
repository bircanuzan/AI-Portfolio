# Project 19 — HR Workflow Benchmark Design and AI Answer Grading

**OpenTrain HR Workflow Benchmark Design Expert — original work sample, expanded into a reproducible portfolio case study.**

## What this project is about — in one sentence
**Design a realistic HR task with several documents, establish the correct answer, and score whether an AI assistant understands the policies, calculations, documentary evidence and exceptions.**

This is **not** an HR chatbot, a payroll-processing tool, an HRIS implementation, or an employment-law advice service. It is an **evaluation benchmark**: a test set that helps reviewers decide whether an AI answer is accurate and supportable.

## Reused work from the earlier OpenTrain application
The original benchmark case (created for the CV work sample) involves a fictional September employee exit, employee ID P-104, and five synthetic source documents:

| Source | Document | Key point |
| --- | --- | --- |
| A | Payroll policy | AED 18,000 monthly base; prorate September using days worked / 30; only approved allowances paid |
| B | Signed contract | Last day 20 September; AED 18,000 monthly base; AED 1,500 transport allowance subject to approval |
| C | Draft payroll change log | AED 18,000 base + AED 1,500 transport, neither finalised |
| D | HR exit approval | Confirms last day 20 September |
| E | Allowance register | Transport allowance pending, with no sign-off |

**Gold answer (under fictional company policy):**
- Base pay = AED 18,000 × 20 / 30 = **AED 12,000**.
- Allowance = **pending approval** and not included in determinable approved input.
- Draft payroll overstates base pay by **AED 6,000**.
- Determinable approved gross payroll input = **AED 12,000**, excluding unresolved allowance.
- Do not calculate or speculate about statutory benefits/deductions, which are outside this benchmark.

**Exact grading weights (10 points):** date + proration rule 2; AED 12,000 calculation 2; unapproved allowance/escalation 2; AED 6,000 variance 2; evidence references A–E 1; avoids statutory speculation 1.

## What you can open here
1. [01_Benchmark_Workflow_Design.md](01_Benchmark_Workflow_Design.md) — **how to design the evaluation from start to finish**, with a flow diagram and quality gates.
2. [02_Employee_Exit_Payroll_Benchmark.md](02_Employee_Exit_Payroll_Benchmark.md) — **the exact original five-document task and gold answer** presented as a standalone work sample.
3. [data/benchmark_case.json](data/benchmark_case.json) — machine-readable synthetic source documents and answer-key facts.
4. [data/sample_answers.json](data/sample_answers.json) — correct, incorrect and unsafe hypothetical model answers in a structured reviewer format.
5. [src/grade_benchmark.py](src/grade_benchmark.py) — small reproducible **rule-based score calculator** for pre-extracted structured answers. It does *not* interpret free-form LLM responses.
6. [tests/test_grade_benchmark.py](tests/test_grade_benchmark.py) — automated score and quality-gate tests.
7. [03_Human_Review_and_Quality_Gates.md](03_Human_Review_and_Quality_Gates.md) — ambiguity, source conflict and grading guidance.

## How to run the demonstration
Python 3.10+, standard library only:
- python src/grade_benchmark.py
- python -m unittest discover -s tests -v

The scoring code evaluates **structured annotations** of sample answers. An HR reviewer must first check any free-form AI answer and map it to the expected fields. The program cannot independently verify legal compliance, nuanced prose or unseen documents.

## Designed for the OpenTrain role
Demonstrates HR workflow design, multi-document analysis, payroll-input reconciliation, HR policy application, answer keys, objective rubrics, ungradeable/ambiguous case detection, quality control and human-in-the-loop AI evaluation.

**Integrity:** Created for demonstration; fictional data; not a client deployment; not UAE legal advice; no live employee data and no payroll/HRIS system access.
