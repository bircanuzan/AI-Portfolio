"""Extract CV document text from uploaded bytes, without external processing."""
from __future__ import annotations

from io import BytesIO
from pathlib import Path

MAX_BYTES = 8 * 1024 * 1024


def extract_document(filename: str, raw: bytes) -> str:
    ext = Path(filename).suffix.lower()
    if len(raw) > MAX_BYTES:
        raise ValueError("File exceeds 8 MB size limit")
    if not raw:
        raise ValueError("Empty file")
    if ext == ".txt":
        text = raw.decode("utf-8-sig", errors="replace")
    elif ext == ".pdf":
        from pypdf import PdfReader
        reader = PdfReader(BytesIO(raw), strict=True)
        if len(reader.pages) > 30:
            raise ValueError("PDF exceeds 30 pages")
        text = "\n".join(p.extract_text() or "" for p in reader.pages)
    elif ext == ".docx":
        from docx import Document
        doc = Document(BytesIO(raw))
        body = [p.text for p in doc.paragraphs]
        body.extend(c.text for table in doc.tables for row in table.rows for c in row.cells)
        text = "\n".join(body)
    else:
        raise ValueError("Supported formats: TXT, PDF, DOCX")
    if not text.strip():
        raise ValueError("No extractable text. Scanned PDFs need a separate, consented OCR step.")
    return text[:120_000]
