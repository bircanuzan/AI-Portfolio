"""Offline, auditable HR policy agent baseline (Python standard library only).

IMPORTANT: tool-using *rule-based* baseline, NOT a live LLM. Demonstrates retrieval,
restricted tool routing, human escalation and evaluation using synthetic policies.
"""
from __future__ import annotations
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path

POLICY_PATH = Path(__file__).with_name('policies.json')
SENSITIVE = re.compile(r'\b(salary|payroll|medical|passport|emirates\s+id|bank\s+(?:details|account)|personal\s+data|employee\s+record|ssn)\b', re.I)
DISCLOSE = re.compile(r'\b(show|give|share|send|export|download|list|reveal|access|tell\s+me|print)\b', re.I)
EXCEPTION = re.compile(r'\b(exception|override|urgent|emergency|without\s+approval|refus(?:ed|es|al)|deny|denied|rejected|special\s+approval|missing\s+receipt|lost\s+(?:my\s+)?receipt)\b', re.I)
AUTO_DECIDE = re.compile(r'\b(approve|authorize|decide|assign|finaliz(?:e|ing)|issue)\b', re.I)
REMOTE_DAYS = re.compile(r'\b(three|four|five|[3-9])\s+(?:remote\s+)?days?\b', re.I)
HIGH_EXPENSE = re.compile(r'\b(?:aed\s*)?([5-9]\d{2}|[1-9]\d{3,})\s*(?:aed)?\b', re.I)

@dataclass
class Decision:
    outcome: str
    answer: str
    policy_ids: list[str]
    tool_trace: list[str]
    escalation_team: str | None = None

class HRPolicyAgent:
    """Uses allowlisted policy lookup + restricted decision/triage tools."""
    def __init__(self, policy_path: Path = POLICY_PATH):
        self.policies = json.loads(Path(policy_path).read_text(encoding='utf-8'))

    def search_policy(self, question: str) -> dict | None:
        """Simple transparent keyword retrieval, not an LLM/vector search."""
        lower = question.lower()
        ranked = [(sum(bool(re.search(r'\b'+re.escape(k)+r'\b', lower)) for k in p['keywords']), p)
                  for p in self.policies]
        best = max(ranked, key=lambda row: row[0])
        return best[1] if best[0] > 0 else None

    @staticmethod
    def route_to_human(policy: dict, reason: str, trace: list[str]) -> Decision:
        trace.append('create_review_ticket:SIMULATED_NO_EXTERNAL_WRITE')
        return Decision('HUMAN_REVIEW', f"Human review needed: {reason} Route to {policy['owner']}; no approval or HR system change was made.",
                        [policy['id']], trace, policy['owner'])

    def run(self, question: str) -> Decision:
        trace = ['input_received', 'policy_lookup']
        if not isinstance(question, str) or not question.strip():
            return Decision('INSUFFICIENT_INFO', 'Provide a specific HR policy question.', [], trace)
        question = question[:3000]  # fixed input bound
        policy = self.search_policy(question)
        if not policy:
            trace.append('no_grounded_policy')
            return Decision('INSUFFICIENT_INFO', 'I cannot verify that from the available DemoCo policies. Ask HR Operations.', [], trace)
        trace.append(f"policy_found:{policy['id']}")
        lower = question.lower()

        # Data privacy rule overrides all other routing. No employee records are loaded.
        if SENSITIVE.search(question) and DISCLOSE.search(question):
            trace.append('privacy_guard:deny_disclosure')
            return Decision('REFUSE', 'I cannot disclose another person’s private HR data. Contact authorized HR staff using the verified access process.',
                            ['HR-PRIV-04'], trace)

        if policy['id'] == 'HR-PERF-06' and AUTO_DECIDE.search(question):
            return self.route_to_human(policy, 'An AI system cannot make a final performance or promotion decision.', trace)
        if policy['id'] == 'HR-LEAVE-01' and AUTO_DECIDE.search(question):
            return self.route_to_human(policy, 'Leave approval is manager-owned.', trace)
        if EXCEPTION.search(question):
            return self.route_to_human(policy, 'The request falls outside the standard workflow or needs an exception.', trace)
        if policy['id'] == 'HR-FLEX-02' and REMOTE_DAYS.search(lower):
            return self.route_to_human(policy, 'More than two remote-working days requires an HRBP exception review.', trace)
        if policy['id'] == 'HR-EXP-03' and HIGH_EXPENSE.search(lower):
            return self.route_to_human(policy, 'Expense exceeds AED 500 and requires pre-approval.', trace)
        trace.append('answer_from_approved_policy')
        return Decision('DIRECT_ANSWER', policy['policy'] + f" [Source: {policy['id']}]", [policy['id']], trace)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='DemoCo synthetic HR policy agent')
    parser.add_argument('question', nargs='?', default='How much annual leave can I request?')
    args = parser.parse_args()
    print(json.dumps(asdict(HRPolicyAgent().run(args.question)), indent=2, ensure_ascii=False))
