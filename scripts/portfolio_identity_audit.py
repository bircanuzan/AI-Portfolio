"""Public portfolio identity audit.

Scans relative paths and extractable document text against privacy-preserving
digests of restricted organization identifiers. No organization names appear
in the scanner or its configuration. Generic product/platform references are
not restricted by this policy.

Run: python scripts/portfolio_identity_audit.py
"""
from __future__ import annotations

from collections import defaultdict
import hashlib
import re
from pathlib import Path
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
RESTRICTED_HASH_PREFIXES = {
    "105c9f70cb837b549bbc", "68e03a5fd40a2a5f6106", "8417bed310833297d586",
    "5f87998e665fd43c4a47", "a40cfc43a2228d5224cf", "6ae673f23d6e6529b29b",
    "f4f39116af1b3c9fbe00", "18e19502fa470d47ec0c", "6291c857c2292e358f01",
    "626858e017b57b84c2c0", "c2b2bc503875b8261108", "f55a85b2f2eb0790b99d",
    "ba6ae2780cd4d333730b", "d78f10bf7d7164815a91", "e94d1700e2c2e385c633",
    "5f5f9123f219945e8573", "e3ce68c12e30c4d4cb50", "60fbbbeb66e018657636",
    "141378bfac540755570c", "ce749e840dcada0f9196", "a93d389aa4c082805a27",
    "165d825ee0d42720d9ec", "2db08657b592ffb4fe5f", "c1ca91b07ac87c852b66",
    "232ed6f9fabf14e3bb55", "d1f11fa82a381b330980", "da43398b91cc0724cea8",
    "1538f1bcd550e920e563", "da7b4a85a86ec0a7f1db", "2995ff81d719dc2131e0",
    "56018fe135c84cb3af99", "334a9fe615fa3ecc0923", "a0a06db16cd426ce7406",
    "fb8843acc351c0c79d95", "cfcda0f427fa765487e3", "e06ce2f797a4ba33eae8",
    "97a6eb426111984bea4e", "b1a12b20962faab48107", "5f8ef80f9864dc659cc9",
    "2efb1646bbd9f93af479", "f2ab30b1ecf545754fbd", "e632d1dda4a3f7aa3b64",
}
BRAND_IN_PATH_ONLY = {"ae0b6d3ac5af96588d35", "473f3fe895a41d6cf4c0"}
TEXT_EXTS = {".md", ".txt", ".py", ".csv", ".json", ".yml", ".yaml", ".sql",
             ".js", ".css", ".html", ".svg", ".xml", ".dax", ".bpmn", ".rtf",
             ".dat", ".gitignore", ".dockerfile", ".example", ".srt"}
MAX_BYTES = 8_000_000


def tokenize(text: str):
    normalized = unicodedata.normalize("NFKC", text).casefold()
    return re.findall(r"[a-z0-9]+", normalized)


def hits_for_text(text: str, *, check_brand: bool = False):
    tokens = tokenize(text)
    result = set()
    restricted = RESTRICTED_HASH_PREFIXES | (BRAND_IN_PATH_ONLY if check_brand else set())
    for i in range(len(tokens)):
        for n in range(1, 6):
            if i + n > len(tokens):
                break
            phrase = " ".join(tokens[i:i + n])
            short_hash = hashlib.sha256(phrase.encode("utf-8")).hexdigest()[:20]
            if short_hash in restricted:
                result.add(short_hash)
    return sorted(result)


def extract_content(path: Path):
    ext = path.suffix.casefold()
    if path.stat().st_size > MAX_BYTES:
        raise ValueError("file too large for reliable text scan")
    if ext in TEXT_EXTS or path.name in {"Dockerfile", ".gitignore"}:
        return path.read_text(encoding="utf-8", errors="replace")
    if ext == ".pdf":
        from pypdf import PdfReader
        reader = PdfReader(str(path))
        return "\n".join(p.extract_text() or "" for p in reader.pages)
    if ext == ".xlsx":
        from openpyxl import load_workbook
        wb = load_workbook(path, read_only=True, data_only=False)
        texts = []
        for ws in wb:
            texts.append(ws.title)
            for row in ws.iter_rows():
                texts.extend(str(cell.value) for cell in row if cell.value is not None)
        wb.close()
        return "\n".join(texts)
    return None


def run():
    inspected = 0
    matched = defaultdict(list)
    unreadable = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or ".git" in path.parts:
            continue
        rel = path.relative_to(ROOT).as_posix()
        inspected += 1
        path_hits = hits_for_text(rel, check_brand=True)
        try:
            content = extract_content(path)
        except Exception as exc:
            unreadable.append((rel, type(exc).__name__))
            content = None
        body_hits = hits_for_text(content) if content else []
        if path_hits or body_hits:
            matched[rel] = {"path": path_hits, "content": body_hits}
    print("Identity audit: inspected=", inspected,
          " flagged_files=", len(matched), " unreadable=", len(unreadable))
    for path, kinds in list(matched.items())[:600]:
        print("FLAG", path, "path_hits=", len(kinds["path"]),
              "content_hits=", len(kinds["content"]))
    for path, failure in unreadable[:100]:
        print("UNREADABLE", path, failure)
    if matched or unreadable:
        print("STATUS: REVIEW REQUIRED. No claim of a fully anonymized repository.")
        return 1
    print("STATUS: No restricted names found in scanned paths or extractable text.")
    return 0


if __name__ == "__main__":
    sys.exit(run())
