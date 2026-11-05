"""Prepare an anonymized portfolio revision on a separate branch.

All matching is against irreversible hash prefixes from the repository
identity audit. No employer/client name list is published in this script.
This operation edits text and filenames; it does not rewrite Git history.
"""
from __future__ import annotations

import hashlib
from pathlib import Path
import re
import sys
from urllib.parse import quote

import portfolio_identity_audit as audit

ROOT = Path(__file__).resolve().parents[1]
TOKEN_RX = re.compile(r"[a-zA-Z0-9]+")
URL_RX = re.compile(r"https?://[^\\s<>\\\"')]+", re.I)
TEXT_EXTS = audit.TEXT_EXTS
NAME_MAP = {
    "105c9f70cb837b549bbc": "fictional_bank",
    "68e03a5fd40a2a5f6106": "fictional_bank",
    "a40cfc43a2228d5224cf": "clean_energy_group",
    "6ae673f23d6e6529b29b": "recognition_programme",
    "f4f39116af1b3c9fbe00": "research_university",
    "18e19502fa470d47ec0c": "research_university",
    "6291c857c2292e358f01": "ai_enterprise",
    "626858e017b57b84c2c0": "ai_enterprise",
    "2db08657b592ffb4fe5f": "enterprise_crm",
    "c1ca91b07ac87c852b66": "operations_group",
    "232ed6f9fabf14e3bb55": "software_group",
    "d1f11fa82a381b330980": "software_group",
    "2995ff81d719dc2131e0": "service_operations",
    "ae0b6d3ac5af96588d35": "independent_portfolio",
    "473f3fe895a41d6cf4c0": "independent_portfolio",
}
DEFAULT_NAME = "sector_organization"


def named_spans(text: str, *, paths: bool):
    toks = list(TOKEN_RX.finditer(text))
    restricted = audit.RESTRICTED_HASH_PREFIXES | (audit.BRAND_IN_PATH_ONLY if paths else set())
    matches = []
    i = 0
    while i < len(toks):
        found = None
        for n in range(min(5, len(toks) - i), 0, -1):
            phrase = " ".join(t.group(0).lower() for t in toks[i:i+n])
            digest = hashlib.sha256(phrase.encode("utf-8")).hexdigest()[:20]
            if digest in restricted:
                found = (toks[i].start(), toks[i+n-1].end(), digest, n)
                break
        if found:
            matches.append(found)
            i += found[3]
        else:
            i += 1
    return matches


def scrub(text: str, *, paths=False):
    if not paths:
        def rewrite_url(m):
            return "https://example.invalid/anonymized-source" if named_spans(m.group(0), paths=False) else m.group(0)
        text = URL_RX.sub(rewrite_url, text)
    matches = named_spans(text, paths=paths)
    for start, end, digest, _ in reversed(matches):
        repl = NAME_MAP.get(digest, DEFAULT_NAME)
        text = text[:start] + repl + text[end:]
    return text


def rename_files():
    sources = [p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts]
    mappings = {}
    for path in sources:
        relative = path.relative_to(ROOT).as_posix()
        new = scrub(relative, paths=True)
        if new != relative:
            mappings[relative] = new
    # Reject collision before performing any mutation.
    all_old = {p.relative_to(ROOT).as_posix() for p in sources}
    destinations = list(mappings.values())
    if len(set(destinations)) != len(destinations):
        raise RuntimeError("Anonymization created duplicate destinations")
    if any(dst in all_old and dst not in mappings for dst in destinations):
        raise RuntimeError("Anonymization would overwrite an existing file")
    for old, new in sorted(mappings.items(), key=lambda x: x[0].count("/"), reverse=True):
        dest = ROOT / new
        dest.parent.mkdir(parents=True, exist_ok=True)
        (ROOT / old).rename(dest)
    print("RENAMED_PATHS", len(mappings))
    return mappings


def revise_text(mappings):
    modified = 0
    substitutions = []
    for old, new in mappings.items():
        substitutions.append((old, new))
        substitutions.append((quote(old, safe="/"), quote(new, safe="/")))
        basename_old, basename_new = old.rsplit("/", 1)[-1], new.rsplit("/", 1)[-1]
        if basename_old != basename_new and basename_old not in {"README.md", "SKILL.md"}:
            substitutions.append((basename_old, basename_new))
    substitutions.sort(key=lambda p: len(p[0]), reverse=True)
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.suffix.casefold() not in TEXT_EXTS:
            continue
        if path.stat().st_size > audit.MAX_BYTES:
            continue
        orig = path.read_text(encoding="utf-8", errors="replace")
        new = orig
        for a, b in substitutions:
            if a in new:
                new = new.replace(a, b)
        new = scrub(new)
        if new != orig:
            path.write_text(new, encoding="utf-8")
            modified += 1
    print("CHANGED_TEXT_FILES", modified)


def revise_pdfs():
    try:
        import fitz
    except ImportError:
        raise RuntimeError("PyMuPDF required to verify/redact restricted text in PDFs")
    changed = 0
    for p in ROOT.rglob("*.pdf"):
        doc = fitz.open(p)
        dirty = False
        for page in doc:
            t = page.get_text("text")
            hits = named_spans(t, paths=False)
            phrases = sorted({t[start:end] for start, end, _, _ in hits}, key=len, reverse=True)
            for phrase in phrases:
                rects = page.search_for(phrase)
                if not rects:
                    print("UNREDACTABLE_PDF_PHRASE", p.relative_to(ROOT), "length=", len(phrase))
                    raise RuntimeError("Unable to redact PDF content reliably")
                for rect in rects:
                    page.add_redact_annot(rect, fill=(1, 1, 1))
                    dirty = True
            if phrases:
                page.apply_redactions()
        if dirty:
            tmp = p.with_name(p.stem + "_sanitized.tmp.pdf")
            doc.save(tmp, garbage=4, deflate=True)
            doc.close()
            tmp.replace(p)
            changed += 1
        else:
            doc.close()
    print("REDACTED_PDFS", changed)


def main():
    maps = rename_files()
    revise_text(maps)
    revise_pdfs()
    check = audit.run()
    if check:
        print("Review audit failures; anonymization branch must not be merged yet.")
        return 1
    print("Anonymized working tree passes privacy audit.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
