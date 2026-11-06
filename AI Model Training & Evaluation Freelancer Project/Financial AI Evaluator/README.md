# Financial AI Evaluator | Evidence-Based Financial Reasoning QA

> **Portfolio status:** Independent, synthetic demonstration. No confidential information, employer/client work, actual model-training delivery or production deployment is claimed. All records and ratings are invented to exercise the methodology.


## Purpose
Build a repeatable expert-review framework for AI responses on banking, insurance, accounting, risk and financial operations. Emphasize correctness of the arithmetic, assumptions, source references and multi-document reconciliation rather than the fluency of an answer.

## JD-aligned responsibilities
- **Response assessment:** rate factual accuracy, accounting reasoning, assumption transparency, consistency across documents and fidelity to the prompt.
- **Error discovery:** identify incorrect denominators, period mismatches, unsupported regulatory claims, omitted risks and contradictions.
- **Document cross-referencing:** align simulated invoice, bank receipt, balance sheet and operational ledger references before stating a conclusion.
- **Test-case construction:** create adversarial spreadsheet and finance scenarios with precomputed reference calculations and documented expected outcomes.
- **Human feedback:** specify the wrong step, correct computation, supporting input and preferred response.
- **Remote QA delivery:** keep a versioned review log, unresolved questions and calibrated rubrics.

## Synthetic cases
1. Profit margin: revenue 100,000, net income 12,500; correct margin is 12.5%, not 14.3%.
2. Balance sheet: assets 200,000; liabilities 85,000 and equity 115,000; equation balances.
3. Receipt reconciliation: invoice I-100 amount 15,000 with a bank receipt of 14,000; 1,000 remains outstanding.
4. Multi-document mismatch: a supplier invoice claims the wrong candidate ID; stop, do not silently reconcile as paid.

## Deliverables
- `financial_evaluation_protocol.md`: scoring anchors, financial-specific defect taxonomy, control standards.
- `data/financial_cases.json`: fully synthetic reference data.
- `src/financial_checker.py`: deterministic arithmetic checks (not a full model evaluator).
- `tests/test_financial_checker.py`: basic numerical tests.

## Run
```bash
python -m unittest discover -s "AI Model Training & Evaluation Freelancer Project/Financial AI Evaluator/tests"
python "AI Model Training & Evaluation Freelancer Project/Financial AI Evaluator/src/financial_checker.py" "AI Model Training & Evaluation Freelancer Project/Financial AI Evaluator/data/financial_cases.json"
```

## Limitations
The scripts verify calculations against supplied values only. They cannot independently verify source authenticity, regulatory correctness, IFRS compliance, external facts or whether AI-generated written reasoning is complete. Those require qualified human judgment and authoritative references.
