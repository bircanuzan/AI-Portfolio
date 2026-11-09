"""Validate evidence-bound human or LLM qualitative review records.

No LLM is called here. The validator rejects unsupported claims and checks
that evidence quotations actually occur on cited lines of repository files.
"""
import json
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
RUBRIC_PATH = PROJECT / "rubrics" / "qualitative_review.json"


def validate_review(review, project_root=PROJECT):
    """Return a validated review or raise ValueError with a precise reason."""
    project_root = Path(project_root).resolve()
    rubric = json.loads((project_root / "rubrics" / "qualitative_review.json").read_text(encoding="utf-8"))
    if not isinstance(review, dict):
        raise ValueError("review must be an object")
    required = {"case_id", "criterion", "verdict"}
    if not required.issubset(review):
        raise ValueError("review lacks required fields")
    if review["criterion"] not in rubric["criteria"]:
        raise ValueError("unknown rubric criterion")
    verdict = review["verdict"]
    if verdict not in {"pass", "fail", "abstain"}:
        raise ValueError("verdict must be pass, fail or abstain")
    if verdict == "abstain":
        if not isinstance(review.get("reason"), str) or not review["reason"].strip():
            raise ValueError("abstentions require a reason")
        return review
    citations = review.get("evidence")
    if not isinstance(citations, list) or not citations:
        raise ValueError("pass/fail decisions require source line evidence")
    for citation in citations:
        if not isinstance(citation, dict):
            raise ValueError("evidence must be an object")
        path, line, quote = citation.get("path"), citation.get("line"), citation.get("quote")
        if not isinstance(path, str) or not path or Path(path).is_absolute():
            raise ValueError("evidence path must be relative")
        if not isinstance(line, int) or isinstance(line, bool) or line <= 0:
            raise ValueError("line must be a positive integer")
        if not isinstance(quote, str) or not quote.strip():
            raise ValueError("a non-empty quote is required")
        full = (project_root / path).resolve()
        if not full.is_relative_to(project_root) or not full.is_file():
            raise ValueError("evidence path must identify an existing project file")
        lines = full.read_text(encoding="utf-8").splitlines()
        if line > len(lines) or quote not in lines[line - 1]:
            raise ValueError("quoted source text not found at cited file and line")
    return review
