# Reproduce local synthetic gate results

This is a deterministic rule-checking demo that uses completely fictional JSON records to show what an AI governance-office prelaunch checklist could **flag**, not to approve a real AI deployment.

```bash
cd "AI Governance, Risk & Responsible AI Portfolio/44_AI_Ethics_Responsible_AI_and_AI_Governance"
python governance_gate.py synthetic_gate_cases.json --output synthetic_gate_results.json
python -m unittest test_governance_gate.py -v
```

**Interpreting a GO:** It means only that the fictional input record contains `true` for mandatory controls. The script **does not** authenticate documents, test a real AI model, identify discrimination, validate legal compliance, reach a regulatory conclusion, deploy an agent, or grant organisational permission.

**Fields**
- `tier`: sample internal policy tier, T1 low, T2 moderate, T3 consequential, T4 prohibited by company policy.
- `critical_findings`: critical defect count; any positive count blocks.
- `autonomous_adverse_decision`, `unapproved_sensitive_export`: hard block conditions.
- Baseline: inventory, impacts, privacy, security, system card, monitoring and evidence.
- T2: UAT and oversight. T3: independent QA, fairness review, committee approval, human final decision and red team.
- Conditional requirements: vendor review, GenAI security and revalidation after material changes.

**Expected artificial dataset outcomes:** SC-001 HOLD, SC-002 HOLD, SC-003 NO_GO, SC-004 GO, SC-005 HOLD, SC-006 GO, SC-007 NO_GO, SC-008 GO, SC-009 HOLD, SC-010 NO_GO. Sample 'GO' cases are hypothetical all-green control statements, **not** evidence of operational readiness.
