import os
import sys
from pathlib import Path
import pytest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import agent


@pytest.fixture(autouse=True)
def isolate(tmp_path, monkeypatch):
    monkeypatch.setattr(agent, "DB_PATH", tmp_path / "test.sqlite3")
    monkeypatch.delenv("LLM_API_KEY", raising=False)
    monkeypatch.delenv("CASE_API_BASE", raising=False)
    monkeypatch.delenv("CASE_API_TOKEN", raising=False)


def test_policy_retrieval():
    result = agent.run("What is the leave approval process?")
    assert result["status"] == "REVIEW_REQUIRED"
    assert result["mode"] == "offline_preview"
    assert "hr_leave_policy.md" in result["sources"]


def test_unknown_policy_escalates():
    result = agent.run("qzxwfoounknown")
    assert result["status"] == "ESCALATE"


def test_human_approval_required():
    result = agent.run("Please submit a leave exception")
    assert result["status"] == "PENDING_HUMAN"
    assert agent.resolve(result["request_id"], "approve")
    assert not agent.resolve(result["request_id"], "approve")  # one-time only


def test_reject_path():
    result = agent.run("change personnel record")
    assert agent.resolve(result["request_id"], "reject")
    assert not agent.resolve(result["request_id"], "approve")


def test_case_integration_requires_configuration():
    result = agent.run("Please check CASE-123")
    assert result["status"] == "ESCALATE"
    assert result["mode"] == "case_api"


def test_case_api_can_be_called(monkeypatch):
    monkeypatch.setenv("CASE_API_BASE", "https://example.org/api")
    monkeypatch.setenv("CASE_API_TOKEN", "test-synthetic-token")
    calls = []
    def mock_request(url, headers, payload=None):
        calls.append((url, headers["Authorization"]))
        return {"case_id": "CASE-123", "status": "In progress", "synthetic": True}
    monkeypatch.setattr(agent, "_request_json", mock_request)
    result = agent.run("Status for CASE-123?")
    assert result["status"] == "READ_ONLY"
    assert calls == [("https://example.org/api/cases/CASE-123", "Bearer test-synthetic-token")]


def test_provider_error_escalates(monkeypatch):
    monkeypatch.setenv("LLM_API_KEY", "fake-test-key")
    def broken(*args, **kwargs):
        raise TimeoutError()
    monkeypatch.setattr(agent, "_request_json", broken)
    result = agent.run("What is the leave approval process?")
    assert result["status"] == "ESCALATE"


def test_reject_unsafe_api_base(monkeypatch):
    monkeypatch.setenv("CASE_API_BASE", "http://127.0.0.1:8080")
    monkeypatch.setenv("CASE_API_TOKEN", "test")
    with pytest.raises(RuntimeError):
        agent.case_lookup("CASE-123")
