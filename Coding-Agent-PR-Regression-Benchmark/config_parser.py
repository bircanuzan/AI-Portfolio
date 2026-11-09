"""Reference implementation for synthetic PR-202."""
import re

KEY_RE = re.compile(r"[A-Z][A-Z0-9_]*\Z")


def parse_config(source: str) -> dict[str, str]:
    """Parse KEY=VALUE lines, rejecting malformed or duplicate keys."""
    if not isinstance(source, str):
        raise TypeError("source must be str")
    result: dict[str, str] = {}
    for line_no, raw in enumerate(source.splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            raise ValueError(f"missing equals sign at line {line_no}")
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if not KEY_RE.fullmatch(key):
            raise ValueError(f"invalid key at line {line_no}")
        if key in result:
            raise ValueError(f"duplicate key at line {line_no}")
        result[key] = value
    return result
