"""Run the PR-202 synthetic candidate benchmark: python benchmark.py."""
import json
from candidate_patches import CANDIDATES

CASES = [
    {"id": "B01", "source": "PORT=8080", "expected": {"PORT": "8080"}},
    {"id": "B02", "source": "URL=https://example.test?a=1", "expected": {"URL": "https://example.test?a=1"}},
    {"id": "B03", "source": "# comment\n\nENV=dev", "expected": {"ENV": "dev"}},
    {"id": "B04", "source": " NAME = test ", "expected": {"NAME": "test"}},
    {"id": "B05", "source": "A=1\nA=2", "error": "ValueError"},
    {"id": "B06", "source": "lowercase=1", "error": "ValueError"},
    {"id": "B07", "source": "KEY_ONLY", "error": "ValueError"},
    {"id": "B08", "source": "TOKEN=a=b=c", "expected": {"TOKEN": "a=b=c"}},
]


def run():
    results = []
    for name, implementation in CANDIDATES.items():
        failures = []
        for case in CASES:
            try:
                observed = implementation(case["source"])
                actual_error = None
            except Exception as exc:
                observed = None
                actual_error = type(exc).__name__
            passed = (actual_error == case["error"]) if "error" in case else (
                actual_error is None and observed == case["expected"])
            if not passed:
                failures.append({"case_id": case["id"],
                                 "expected": case.get("expected", case.get("error")),
                                 "observed": actual_error or observed})
        results.append({"candidate": name, "passed": len(CASES) - len(failures),
                        "total": len(CASES), "failures": failures})
    return {"kind": "synthetic-candidate-evaluation", "cases": len(CASES),
            "results": results}


if __name__ == "__main__":
    output = run()
    print(json.dumps(output, indent=2, sort_keys=True))
    baseline = next(r for r in output["results"] if r["candidate"] == "reference")
    if baseline["passed"] != baseline["total"]:
        raise SystemExit("Reference regression: benchmark specification must be checked")
