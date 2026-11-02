"""Deterministic, auditable skills evidence checks — not an AI hiring decision."""
from __future__ import annotations

import re
from dataclasses import asdict, dataclass

ALIASES: dict[str, tuple[str, ...]] = {
    "generative ai": ("genai", "gen ai", "generative ai", "large language models", "llms"),
    "python": ("python",),
    "sql": ("sql", "postgresql", "mysql", "tsql", "t-sql"),
    "power bi": ("power bi", "powerbi"),
    "excel": ("microsoft excel", "excel"),
    "oracle hcm": ("oracle hcm", "oracle fusion hcm", "oracle cloud hcm"),
    "workday": ("workday",),
    "power automate": ("microsoft power automate", "power automate"),
    "copilot studio": ("copilot studio", "microsoft copilot studio"),
    "api integration": ("api integration", "api integrations", "rest api", "restful api"),
    "recruitment": ("talent acquisition", "recruitment", "recruiting"),
    "emiratisation": ("emiratisation", "emiratization"),
    "saudisation": ("saudisation", "saudization"),
    "stakeholder management": ("stakeholder management", "stakeholder engagement"),
    "learning development": ("learning and development", "learning & development", "l&d"),
}


def requirements(value: str | list[str]) -> list[str]:
    parts = re.split(r"[,;\n]", value) if isinstance(value, str) else value
    seen: set[str] = set()
    result: list[str] = []
    for raw in parts:
        item = re.sub(r"\s+", " ", str(raw).strip()).casefold()
        if item and item not in seen:
            seen.add(item)
            result.append(item)
    return result


@dataclass(frozen=True)
class Evidence:
    requirement: str
    found: bool
    matched_term: str | None
    snippet: str | None

    def to_dict(self) -> dict:
        return asdict(self)


def evidence_for(text: str, terms: list[str]) -> list[Evidence]:
    """Whole-word/phrase checks, including declared aliases. No inference or verification."""
    if not isinstance(text, str):
        raise TypeError("Document text must be a string")
    results = []
    for term in requirements(terms):
        candidates = ALIASES.get(term, (term,))
        match = None
        matched = None
        for phrase in candidates:
            pattern = r"(?<!\w)" + re.escape(phrase).replace(r"\ ", r"\s+") + r"(?!\w)"
            m = re.search(pattern, text, flags=re.IGNORECASE)
            if m and (match is None or m.start() < match.start()):
                match, matched = m, phrase
        if match:
            a = max(0, match.start() - 42)
            b = min(len(text), match.end() + 42)
            snippet = re.sub(r"\s+", " ", text[a:b]).strip()
            # Evidence is a text match, not proof of competency. Mask common contact PII.
            snippet = re.sub(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}", "[email]", snippet)
            snippet = re.sub(r"(?<!\w)(?:\+?\d[\d()\s.-]{7,}\d)(?!\w)", "[phone]", snippet)
            results.append(Evidence(term, True, matched, snippet))
        else:
            results.append(Evidence(term, False, None, None))
    return results


def coverage(required: list[Evidence], preferred: list[Evidence]) -> dict:
    """Coverage of *mentioned keywords*, not candidate aptitude or job suitability."""
    def count(xs: list[Evidence]) -> tuple[int, int]:
        return sum(item.found for item in xs), len(xs)
    req_found, req_total = count(required)
    pref_found, pref_total = count(preferred)
    if req_total and pref_total:
        pct = round(100 * (0.7 * req_found / req_total + 0.3 * pref_found / pref_total))
    elif req_total:
        pct = round(100 * req_found / req_total)
    elif pref_total:
        pct = round(100 * pref_found / pref_total)
    else:
        pct = 0
    return {"coverage_percent": pct, "required_found": req_found, "required_total": req_total,
            "preferred_found": pref_found, "preferred_total": pref_total,
            "missing_required": [x.requirement for x in required if not x.found],
            "warning": "Keyword coverage only. A recruiter must verify evidence and make all decisions."}


def analyze(text: str, required: str | list[str], preferred: str | list[str]) -> dict:
    req = evidence_for(text, requirements(required))
    pref = evidence_for(text, requirements(preferred))
    return {"required": [e.to_dict() for e in req],
            "preferred": [e.to_dict() for e in pref], "summary": coverage(req, pref)}


RUBRIC = {
    0: "No evidence supplied",
    1: "Limited evidence — major follow-up needed",
    2: "Partial evidence — material gaps remain",
    3: "Meets the documented role criterion",
    4: "Strong evidence beyond the criterion",
}


def assess_competencies(scores: dict[str, int]) -> dict:
    """Human-entered ratings; do not automatically advance or reject candidates."""
    if not scores:
        return {"average": None, "rated": 0}
    if any(not isinstance(v, int) or v not in RUBRIC for v in scores.values()):
        raise ValueError("Scores must be integers from 0 to 4")
    return {"average": round(sum(scores.values()) / len(scores), 2), "rated": len(scores)}
