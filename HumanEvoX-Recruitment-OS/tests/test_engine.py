import pytest
from humanevox.engine import analyze, requirements, assess_competencies
from humanevox.templates import invitation_ics, outreach_draft, conversation_guide
from datetime import datetime
from zoneinfo import ZoneInfo


def test_requirements_dedupe():
    assert requirements("Python, SQL; python\nPower BI") == ["python", "sql", "power bi"]


def test_exact_phrases_and_aliases():
    x = analyze("Led talent acquisition using Workday and PowerBI; strong Python.",
                "recruitment,workday,power bi,java", "Python")
    assert [e["found"] for e in x["required"]] == [True, True, True, False]
    assert x["summary"]["coverage_percent"] == 82
    assert x["summary"]["missing_required"] == ["java"]


def test_no_substring_false_positive():
    x = analyze("I developed JavaScript integrations and worked in sqlserver tooling", "java,sql", "")
    assert x["summary"]["required_found"] == 0


def test_no_auto_suitability():
    x = analyze("HR professional", "python,sql", "")
    assert "recruiter" in x["summary"]["warning"]
    assert x["summary"]["coverage_percent"] == 0


def test_empty_skills_and_score():
    assert analyze("anything", "", "")["summary"]["coverage_percent"] == 0
    assert assess_competencies({"communication": 3, "analysis": 4}) == {"average": 3.5, "rated": 2}
    with pytest.raises(ValueError):
        assess_competencies({"x": 5})


def test_ics_timezone_and_not_an_actual_booking():
    raw = invitation_ics("HumanEvoX Interview", datetime(2026, 11, 4, 10, tzinfo=ZoneInfo("Asia/Dubai")), 30)
    assert b"DTSTART:20261104T060000Z" in raw
    assert b"STATUS:TENTATIVE" in raw


def test_no_call_action():
    assert "Do not record audio or start an AI call" in conversation_guide("Recruiter")
    assert "Hello" in outreach_draft("Aisha Example", "HR Manager")[1]
