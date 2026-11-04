"""Generate an evidence-linked executive AI risk pack from synthetic controls."""
from pathlib import Path
import json
import sys
import tempfile
from collections import Counter
from control_plane import run, verify_chain

def generate(folder):
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    result = run()
    summary = {
        "classification": "SYNTHETIC OFFLINE RULE CHECKS",
        "scenario_count": len(result["scenario_results"]),
        "expected_matches": sum(c["matched"] for c in result["scenario_results"]),
        "unexpected": [c for c in result["scenario_results"] if not c["matched"]],
        "decision_types": dict(Counter(x["decision"] for x in result["decisions"])),
        "readiness": result["readiness"],
        "audit_chain_self_check": verify_chain(result["audit"]),
        "live_llm_model_evaluated": False,
        "production_authorized": False,
        "independently_audited": False,
        "iso_42001_certified": False
    }
    (folder / "summary.json").write_text(json.dumps(summary, indent=2)+"\n", encoding="utf-8")
    (folder / "scenario_results.json").write_text(json.dumps(result["scenario_results"], indent=2)+"\n", encoding="utf-8")
    with (folder / "offline_audit_chain.jsonl").open("w", encoding="utf-8") as out:
        for item in result["audit"]:
            out.write(json.dumps(item, sort_keys=True)+"\n")
    lines = [
        "# Executive AI Risk Committee — Synthetic Board Report",
        "",
        "**Recommendation: HOLD all production releases.** These are author-defined scenario tests only.",
        "",
        "Scenario results matched: "+str(summary["expected_matches"])+"/"+str(summary["scenario_count"]),
        "Offline hash chain self-check: "+str(summary["audit_chain_self_check"]),
        "No real LLM was executed, no deployed technical controls were attested and no ISO conformity audit was completed.",
        "",
        "## AI Factory system readiness"
    ]
    for item in result["readiness"]:
        lines.append("- "+item["system_id"]+": "+item["screening"]+"; gaps: "+
                     (", ".join(item["gaps"]) or "none under offline rule set"))
    lines.extend(["", "## Open CAPA", "- Independent model and fairness evaluation.",
        "- Real privacy/DPO and sector-specific legal applicability review.",
        "- Production identity, authorization, egress monitoring and tool sandbox.",
        "- Real incident escalation, override/appeals and audit retention.",
        "- Named executive risk acceptance after staged and monitored pilot.",
        "", "Sandbox allowed means only author-defined rule check passed, NOT production safety."])
    (folder / "BOARD_REPORT.md").write_text("\n".join(lines)+"\n", encoding="utf-8")
    if summary["unexpected"] or not summary["audit_chain_self_check"]:
        raise RuntimeError("Author-defined test regression")
    return summary

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(json.dumps(generate(sys.argv[1]), indent=2))
    else:
        with tempfile.TemporaryDirectory(prefix="humanevox_rai_") as temp:
            print(json.dumps(generate(temp), indent=2))
