"""HumanEvoX synthetic agentic-AI governance gate (stdlib-only demo).

Not legal advice; no live integrations, candidate records, or LLM inference.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

ALLOWED_TOOLS = {
    'answer_hr_policy', 'draft_candidate_message', 'send_candidate_message',
    'rank_candidates', 'export_candidate_data', 'delete_candidate_record',
    'update_candidate_status',
}
HUMAN_APPROVAL_TOOLS = {'send_candidate_message', 'delete_candidate_record', 'update_candidate_status'}
HIGH_IMPACT_TOOLS = {'rank_candidates'}


def evaluate(case: dict) -> dict:
    """Deterministic control evaluation. DENY > ESCALATE > ALLOW."""
    case_id = str(case.get('case_id', 'UNSPECIFIED'))
    tool = case.get('tool', '')
    controls = []
    reasons = []
    decision = 'ALLOW_DEMO_ONLY'

    def flag(status: str, control: str, reason: str) -> None:
        nonlocal decision
        controls.append(control)
        reasons.append(reason)
        precedence = {'ALLOW_DEMO_ONLY': 0, 'ESCALATE_HUMAN': 1, 'DENY': 2}
        if precedence[status] > precedence[decision]:
            decision = status

    if case.get('prompt_injection', False):
        flag('DENY', 'C-01', 'Tool/policy instruction override detected in untrusted input.')
    if tool not in ALLOWED_TOOLS:
        flag('DENY', 'C-02', 'Tool outside allowlisted agent capabilities.')
    if case.get('personal_data', False) and not case.get('lawful_basis_recorded', False):
        flag('DENY', 'C-03', 'No recorded lawful-basis review for personal-data processing.')
    if case.get('data_export', False) and not case.get('transfer_safeguards_approved', False):
        flag('DENY', 'C-04', 'Data transfer/safeguards review absent or unapproved.')
    if tool == 'export_candidate_data':
        flag('ESCALATE_HUMAN', 'C-05', 'Export is never autonomous in this pilot.')
    if tool in HUMAN_APPROVAL_TOOLS and not case.get('human_approval', False):
        flag('ESCALATE_HUMAN', 'C-06', 'State-changing action requires recorded human approval.')
    if tool in HIGH_IMPACT_TOOLS:
        flag('ESCALATE_HUMAN', 'C-07', 'Candidate ranking/selection requires substantive human assessment.')
    if tool == 'answer_hr_policy' and not case.get('source_verified', False):
        flag('ESCALATE_HUMAN', 'C-08', 'Authoritative policy source not verified or current.')
    if case.get('sensitive_data', False) and not case.get('sensitive_data_review', False):
        flag('DENY', 'C-09', 'Special-category/sensitive data handling not approved.')
    if not controls:
        controls.append('C-10')
        reasons.append('All configured demo guard conditions satisfied; no external action performed.')
    return {
        'case_id': case_id,
        'decision': decision,
        'control_ids': controls,
        'reasons': reasons,
        'evidence_status': 'LOCAL_DETERMINISTIC_SIMULATION',
    }


def run_suite(cases: list[dict]) -> dict:
    outcomes = []
    for case in cases:
        actual = evaluate(case)
        actual['expected'] = case.get('expected')
        actual['passed'] = actual['decision'] == case.get('expected')
        outcomes.append(actual)
    return {
        'scope': 'Synthetic HumanEvoX agentic recruiting governance cases',
        'engine': 'Deterministic Python rules; NO LLM, no external service',
        'total': len(outcomes),
        'passed': sum(row['passed'] for row in outcomes),
        'failed': sum(not row['passed'] for row in outcomes),
        'results': outcomes,
    }


if __name__ == '__main__':
    here = Path(__file__).resolve().parent.parent
    input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else here / 'data' / 'synthetic_scenarios.json'
    report = run_suite(json.loads(input_path.read_text(encoding='utf-8')))
    print(json.dumps(report, indent=2))
    sys.exit(0 if report['failed'] == 0 else 1)
