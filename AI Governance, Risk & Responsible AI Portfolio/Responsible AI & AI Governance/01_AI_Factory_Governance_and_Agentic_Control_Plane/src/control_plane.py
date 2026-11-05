"""Offline governance-as-code; NOT a live LLM, agent runtime, production IAM or certified security system."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]

def read_inventory():
    with (ROOT / "data" / "ai_inventory.json").open(encoding="utf-8") as stream:
        systems = json.load(stream)
    ids = [s["system_id"] for s in systems]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate AI systems")
    return {s["system_id"]: s for s in systems}

def read_scenarios():
    with (ROOT / "data" / "scenarios.json").open(encoding="utf-8") as stream:
        return json.load(stream)

def release_gate(system):
    """Only author-defined synthetic sandbox readiness, not production clearance."""
    gaps = []
    for field, expected in (
        ("risk_assessment", "COMPLETE"),
        ("privacy_review", "PASS_SYNTHETIC"),
        ("security_review", "PASS_SYNTHETIC"),
        ("model_evaluation", "PASS_SYNTHETIC"),
        ("human_oversight", "DOCUMENTED"),
    ):
        if system.get(field) != expected:
            gaps.append(field)
    if system.get("high_impact") and system.get("fairness_review") != "PASS_SYNTHETIC":
        gaps.append("independent_fairness_review")
    for field in ("owner", "risk_owner", "jurisdiction"):
        if not system.get(field):
            gaps.append(field)
    if system.get("environment") != "sandbox":
        gaps.append("environment_unverified")
    return {
        "system_id": system["system_id"],
        "screening": "HOLD" if gaps else "CONDITIONAL_SYNTHETIC_SANDBOX",
        "gaps": gaps,
        "production_authorized": False,
    }

def decide(request, systems):
    """Evaluate a proposed action without executing it. Nothing may call external tools."""
    system_id = request.get("system_id")
    system = systems.get(system_id)
    def verdict(code, rationale):
        return {
            "case": request.get("id", "UNNAMED"),
            "system_id": system_id,
            "decision": code,
            "rationale": rationale,
            "external_action_executed": False,
            "production_authorized": False,
        }
    if system is None:
        return verdict("DENY_UNKNOWN_SYSTEM", "Unregistered AI system")
    if request.get("external_transfer") is True:
        return verdict("DENY_EXTERNAL_TRANSFER", "No external transfers supported")
    if request.get("personal_data") is True and not system.get("personal_data"):
        return verdict("DENY_DATA_SCOPE", "Personal data not in approved synthetic scope")
    if request.get("role") not in system.get("roles", []):
        return verdict("DENY_ROLE", "Role absent from declared allowlist")
    if request.get("tool") not in system.get("tools", []):
        return verdict("DENY_TOOL", "Action absent from approved tool list")
    units = request.get("task_units")
    if type(units) is not int or units < 0 or units > 10:
        return verdict("DENY_BUDGET", "Task units invalid or above limit")
    if request.get("source") not in system.get("sources", []):
        return verdict("HOLD_SOURCE", "Data or knowledge source not approved")
    if request.get("source_current") is not True:
        return verdict("HOLD_STALE_SOURCE", "Source freshness not verified")
    prompt = str(request.get("prompt", "")).lower()
    if any(value in prompt for value in (
        "ignore previous instructions", "reveal secrets", "bypass safety"
    )):
        return verdict("HOLD_INJECTION_INDICATOR", "Illustrative string flag, not complete protection")
    if release_gate(system)["screening"] == "HOLD":
        return verdict("HOLD_RELEASE", "System assessment/review incomplete")
    if request.get("tool") in system.get("approval_required", []) and request.get("human_approved") is not True:
        return verdict("HUMAN_APPROVAL_REQUIRED", "Requires verified independent human authorization")
    return verdict("ALLOW_SIMULATION", "Passes authored sandbox test only; no actual action")

def hash_chain(decisions):
    """Offline tamper-evident audit chain. Not immutable or independent evidence storage."""
    output = []
    prior = "GENESIS"
    for decision in decisions:
        canonical = json.dumps(decision, sort_keys=True, separators=(",", ":"))
        digest = hashlib.sha256((prior + "|" + canonical).encode("utf-8")).hexdigest()
        output.append({"previous_hash": prior, "decision": decision, "sha256": digest})
        prior = digest
    return output

def verify_chain(events):
    prior = "GENESIS"
    for event in events:
        canonical = json.dumps(event["decision"], sort_keys=True, separators=(",", ":"))
        digest = hashlib.sha256((prior + "|" + canonical).encode("utf-8")).hexdigest()
        if event.get("previous_hash") != prior or event.get("sha256") != digest:
            return False
        prior = digest
    return True

def run():
    systems = read_inventory()
    scenarios = read_scenarios()
    decisions = [decide(item, systems) for item in scenarios]
    results = [{
        "id": request["id"],
        "expected": request["expected"],
        "actual": result["decision"],
        "matched": request["expected"] == result["decision"],
    } for request, result in zip(scenarios, decisions)]
    return {
        "readiness": [release_gate(s) for s in systems.values()],
        "scenario_results": results,
        "decisions": decisions,
        "audit": hash_chain(decisions),
    }

if __name__ == "__main__":
    result = run()
    print(json.dumps({
        "scope": "SYNTHETIC OFFLINE EVALUATION",
        "scenarios": len(result["scenario_results"]),
        "matches": sum(x["matched"] for x in result["scenario_results"]),
        "valid_hash_chain": verify_chain(result["audit"]),
        "production_authorized": False,
        "live_model_tested": False,
    }, indent=2))
