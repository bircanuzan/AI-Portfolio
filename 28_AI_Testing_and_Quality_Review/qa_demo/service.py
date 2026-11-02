"""Tiny loopback-only HTTP case API for QA demos; no production authentication."""
from __future__ import annotations
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import threading

ALLOWED_CATEGORIES = {"policy_question", "letter_request"}

class CaseStore:
    def __init__(self):
        self.cases = {}
        self.keys = {}
        self.counter = 0
        self.lock = threading.Lock()

    def create(self, payload, key):
        if not isinstance(payload, dict):
            return 400, {"error": "object required"}
        if payload.get("confirmed") is not True:
            return 400, {"error": "explicit confirmation required"}
        if payload.get("category") not in ALLOWED_CATEGORIES:
            return 400, {"error": "category not allowed"}
        summary = payload.get("safe_summary")
        if not isinstance(summary, str) or not 1 <= len(summary.strip()) <= 200:
            return 400, {"error": "invalid summary"}
        if not isinstance(key, str) or not 8 <= len(key) <= 100:
            return 400, {"error": "invalid idempotency key"}
        normalized = json.dumps({"category": payload["category"],
                                "safe_summary": summary.strip(),
                                "confirmed": True}, sort_keys=True)
        with self.lock:
            if key in self.keys:
                earlier, case_id = self.keys[key]
                if earlier != normalized:
                    return 409, {"error": "idempotency conflict"}
                return 200, dict(self.cases[case_id])
            self.counter += 1
            case_id = f"TKT-{self.counter:04d}"
            row = {"case_id": case_id, "category": payload["category"], "status": "created"}
            self.cases[case_id] = row
            self.keys[key] = (normalized, case_id)
            return 201, dict(row)

    def get(self, case_id):
        with self.lock:
            if case_id not in self.cases:
                return 404, {"error": "case not found"}
            return 200, dict(self.cases[case_id])

class Handler(BaseHTTPRequestHandler):
    store = CaseStore()

    def write_json(self, status, body):
        data = json.dumps(body).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path == "/health":
            return self.write_json(200, {"status": "ok"})
        if self.path.startswith("/cases/") and len(self.path) > 7:
            return self.write_json(*self.store.get(self.path.split("/",2)[2]))
        return self.write_json(404, {"error": "not found"})

    def do_POST(self):
        if self.path != "/cases":
            return self.write_json(404, {"error": "not found"})
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length < 1 or length > 4096:
                raise ValueError("invalid body length")
            body = json.loads(self.rfile.read(length).decode("utf-8"))
        except (ValueError, UnicodeError, json.JSONDecodeError):
            return self.write_json(400, {"error": "invalid JSON"})
        return self.write_json(*self.store.create(body, self.headers.get("Idempotency-Key")))

    def log_message(self, fmt, *args):
        # Demo intentionally avoids recording payloads or employee identifiers.
        pass

if __name__ == "__main__":
    print("Local synthetic QA API on 127.0.0.1:8765")
    ThreadingHTTPServer(("127.0.0.1",8765),Handler).serve_forever()
