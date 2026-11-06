"""A deterministic checklist for human-entered workshop assessment scores."""
KEYS=("task_clear","context_sufficient","format_defined",
      "verification_plan","privacy_and_approval")
def assess(scores):
    if set(scores)!=set(KEYS):raise ValueError("five required dimensions")
    if any(type(scores[k]) is not int or scores[k] not in (0,1,2) for k in KEYS):
        raise ValueError("integer checklist scores 0,1,2 required")
    total=sum(scores.values())
    return {"score_of_10":total,"ready_for_supervised_practice":total>=8,
            "priority_gaps":[k for k in KEYS if scores[k]<2]}
