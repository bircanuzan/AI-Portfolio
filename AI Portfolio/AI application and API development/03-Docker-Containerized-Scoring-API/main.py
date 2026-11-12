"""Pure-Python demo service packaged in Docker. POST /score or GET /health."""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def respond(self, status: int, payload: dict) -> None:
        data = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self) -> None:
        self.respond(200 if self.path == "/health" else 404,
                     {"status": "ok"} if self.path == "/health" else {"error": "not_found"})

    def do_POST(self) -> None:
        if self.path != "/score":
            self.respond(404, {"error": "not_found"})
            return
        try:
            size = int(self.headers.get("Content-Length", "0"))
            if size > 4096 or size < 1:
                raise ValueError("invalid payload size")
            request = json.loads(self.rfile.read(size))
            values = request["values"]
            if not isinstance(values, list) or not values or len(values) > 100:
                raise ValueError("values must be 1-100 numbers")
            if any(type(v) not in (int, float) for v in values):
                raise ValueError("numeric values only")
            self.respond(200, {"mean": sum(values) / len(values)})
        except (ValueError, KeyError, TypeError, json.JSONDecodeError):
            self.respond(400, {"error": "invalid_request"})

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
