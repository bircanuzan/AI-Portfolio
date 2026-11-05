# Reproducible Local Test Evidence (Synthetic)

**Scope of claim:** A locally executable **rules-based** Python route and business-case calculator were tested against fictional rows during portfolio preparation. This is a **software unit demonstration**, not Azure Document Intelligence evaluation, Microsoft Power Automate execution, enterprise UAT, or live Azizi data.

## Reproduction steps
From the repository root:

```bash
cd 45_AI_Lead_Systems_and_Process
python -m unittest discover -s prototype -p 'test_*.py' -v
python prototype/benefits_model.py
```

## Observed result of local Python run
- **7 unit test functions passed**.
- Test suite includes **all 12 synthetic handover CSV records** with expected decision assertions.
- Unknown readiness and uncleared payments always go to `HUMAN_REVIEW`.
- Missing required identifiers or documents go to `NEEDS_DOCUMENTS`.
- A complete record becomes `READY_FOR_HUMAN_APPROVAL` — **never** `HANDOVER_APPROVED`.
- Modelled base scenario: **75 capacity hours/month**, **AED 5,000 net monthly scenario**, **8.4-month simple payback**.
- Modelled conservative scenario: **AED 2,000 net monthly scenario**, **21-month payback**, **negative AED 18,000 year-one value**.

## Controls / limitations
- No PDF extraction, generative model call, OCR test, persistent audit/event store, customer notification, security verification or enterprise workflow integration occurs.
- Output `needs_human: true` is an explicit invariant; required **human review** is not the same as completed human approval.
- Audit timestamps, permission checks and approval evidence are specified in design documents but not built in this local prototype.
- Real ROI, UAT approval, production adoption and live operational benefits remain **unmeasured/unverified**.

An interviewer can inspect code and run the fixture suite; this is stronger evidence of a *reproducible logical demonstrator* than claiming a non-existent implementation.
