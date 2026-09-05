#!/usr/bin/env python3
"""Apply one direct-scan-supported post-closure heading correction to Ammayappan.

PDF 10 / logical p.8 visibly prints `மாடம்`. The canonical layer currently has
`மடாலயம்` at that occurrence. This script changes only the PDF 10 occurrence,
keeps the page verified after local source recheck, and records the correction.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "works" / "ammaiyappan"
FULL = WORK / "transcription" / "full-text.md"
NOTES = WORK / "notes" / "post-fidelity-corrections.md"


def page_span(text: str, pdf: int) -> tuple[int, int]:
    start_m = re.search(rf"<!-- source: pdf={pdf}\b.*?status=verified -->", text)
    if not start_m:
        raise SystemExit(f"verified page anchor missing: PDF {pdf}")
    next_m = re.search(rf"<!-- source: pdf={pdf+1}\b", text[start_m.end():])
    end = start_m.end() + next_m.start() if next_m else len(text)
    return start_m.start(), end


def main() -> None:
    text = FULL.read_text(encoding="utf-8")
    start, end = page_span(text, 10)
    page = text[start:end]
    old = "## மடாலயம்"
    new = "## மாடம்"
    if page.count(old) != 1:
        raise SystemExit(f"expected exactly one PDF 10 old heading, found {page.count(old)}")
    if new in page:
        raise SystemExit("PDF 10 already contains corrected heading")
    page = page.replace(old, new, 1)
    updated = text[:start] + page + text[end:]
    # Preserve the genuine later மடாலயம் heading elsewhere in the work.
    if "## மடாலயம்" not in updated:
        raise SystemExit("guard failed: no later genuine மடாலயம் heading remains")
    if "<!-- source: pdf=10 printed=8 status=verified -->" not in page:
        raise SystemExit("PDF 10 verified anchor unexpectedly changed")
    FULL.write_text(updated, encoding="utf-8")

    entry = """# அம்மையப்பன் — post-fidelity source corrections

Canonical authority: `transcription/full-text.md`  
Controlling source: `TVA_BOK_0064230_அம்மையப்பன்.pdf`

## PDF 10 / logical printed p.8 — structural heading

- state before correction: canonical page had `மடாலயம்` as the transition heading;
- direct rendered-scan reading: **`மாடம்`**;
- action: corrected only this PDF 10 occurrence to `மாடம்`;
- reason: direct source-visible structural heading; the earlier `notes/scene-heading-audit.md` also recorded `மாடம்`;
- local visual recheck: **PASS**;
- historical-glyph impact: **none**;
- page status after correction: **verified**;
- global replacement: **not used**;
- downstream reconciliation: no scene/dialogue/character/translation derivatives existed yet, so no downstream content regeneration was required.

## PDF 16 / logical printed p.14 — reconciliation note, no correction

The canonical heading `சுகதேவன் அறை.` retains its source-visible terminal punctuation. The older intake ledger's `சுகதேவன் அறை` is treated as punctuation-under-specified structural metadata, not as authority to remove source punctuation.
"""
    NOTES.write_text(entry, encoding="utf-8")
    print("PASS: PDF 10 மடாலயம் -> மாடம்; PDF 10 remains verified")


if __name__ == "__main__":
    main()
