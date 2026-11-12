# Evidence register, reproduction & limitations

## Source and originality
- Input: role description supplied in this conversation on 3 November 2026.
- Original work: fictional Cedar Gulf Group, authored case data, frameworks, decision-control logic and unit-test specifications.
- No sector_organization internal information, pay data, organisation charts, proprietary grade conventions, policy thresholds or employee records.
- References to Mercer IPE, Aon and named enterprise software are contextual examples, **not licensed implementation evidence**.

## Reproduction
From repository root:

    python "Organizational Effectiveness/src/oe_control_engine.py"
    python -m unittest discover -s "Organizational Effectiveness/tests" -v

The first command reports synthetic baseline, departmental cost controls, employee-pay differences, recommended hiring paths, job factors, strategy status and theoretical low/medium-risk AI exposure. The second checks validation, budget accounting, grade calibration, exception handling, reconciliation and high-impact task exclusion. No external packages, network, secrets, account keys or paid tools are required.

## Expected deliberate triggers, to check by actual execution
- E02 discrepancy: payroll annual base is AED 5,000 lower than HRIS.
- REQ-01: valid funded vacancy recommended for human approval, never approved by engine.
- REQ-02: no approved position / unbudgeted → HCC escalation.
- REQ-03: hiring freeze exception → CPO escalation.
- REQ-04: legal rehire hold → hold pending Legal.
- REQ-05: incomplete supplier checks → vendor hold.
- ACT03: high-impact grades/terminations → excluded from unattended AI savings.

## Roadmap to actual evidence
1. Document a real client's consent, source permissions and legal requirements, plus agreed master data dictionary.
2. Replace synthetic fixtures with correctly governed/anonymised data and assess joins, effective dates and coverage.
3. Validate job evaluation with licensed practitioners and approved internal compensation policies.
4. Agree delegated authority and finance rules, connect source APIs securely, reconcile output to evidence.
5. Record baseline controls, independent UAT and production governance sign-off.
6. Measure live service and workforce outcomes without double-counting automation hypothetical hours.

**Status:** source artifacts prepared for local execution; none of these controls operate on a live organisation, payroll/HRIS, recruitment or AI service.
