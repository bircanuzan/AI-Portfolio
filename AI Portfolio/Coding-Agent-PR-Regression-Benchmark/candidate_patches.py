"""Intentionally defective synthetic candidate patches for benchmark testing."""
from config_parser import parse_config


def allow_duplicate_keys(source: str) -> dict[str, str]:
    """Defect: accepts repeated keys, silently replacing earlier values."""
    # Keep the remaining reference behavior to isolate one failure mode.
    lines = []
    for raw in source.splitlines():
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if "=" in stripped:
            key = stripped.split("=", 1)[0].strip()
            lines = [line for line in lines
                     if line.split("=", 1)[0].strip() != key]
        lines.append(raw)
    return parse_config("\n".join(lines))


def truncate_equals_in_value(source: str) -> dict[str, str]:
    """Defect: truncates the value after the second equals sign."""
    normalized = []
    for raw in source.splitlines():
        if raw.strip() and not raw.strip().startswith("#") and "=" in raw:
            pieces = raw.split("=")
            raw = pieces[0] + "=" + pieces[1]
        normalized.append(raw)
    return parse_config("\n".join(normalized))


CANDIDATES = {
    "reference": parse_config,
    "duplicate-key-defect": allow_duplicate_keys,
    "value-truncation-defect": truncate_equals_in_value,
}
