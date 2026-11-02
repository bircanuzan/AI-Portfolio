"""Illustrative evidence-aware HR-to-AI role matcher. No hiring predictions."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    profile = json.loads((ROOT / "config/sample_profile.json").read_text(encoding="utf-8"))
    roles = json.loads((ROOT / "config/role_requirements.json").read_text(encoding="utf-8"))
    out = []
    for role in roles:
        score = 0.0
        gaps = []
        for skill, required in role["skills"].items():
            level = profile["skills"].get(skill, 0)
            weight = role["weights"][skill]
            score += weight * min(level / required, 1.0)
            if level < required:
                gaps.append(f"{skill} ({level}/{required})")
        out.append((score, role["role"], gaps, role["portfolio"]))
    for score, name, gaps, evidence in sorted(out, reverse=True):
        print(f"{score:5.1f}/100 | {name}")
        print("  Evidence portfolio: " + evidence)
        print("  Gaps to verify: " + (", ".join(gaps) if gaps else "none in this simplified model"))
    print("\nScore = weighted evidence coverage, NOT employability, interview probability,")
    print("a vacancy match or a recommendation to claim unverified experience.")
    print("Apply knockout checks (UAE, Arabic, sales quotas, training delivery) to each real JD.")

if __name__ == "__main__":
    main()
