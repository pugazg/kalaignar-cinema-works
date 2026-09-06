#!/usr/bin/env python3
"""Synchronize repository-wide mirrors for Naam canonical first-pass PDF 20-24."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE_SHA = "0f7a54882eb6a5a8f83b29060c771ef18dee2b9e108c8797184de2b97c30b7ad"
CRITICAL_TIRUMBIPPAAR_SHA = "17b9422cf2bf9cd30c90829a2dbd18115e20b8bd1cf7e5bb9da2cc0cdcc23c7f"
NEXT = (
    "Continue canonical Tamil first-pass transcription with PDF 25–29, preserving source order, "
    "stable page anchors and page-level historical-glyph checks. Keep all first-pass pages "
    "draft/needs-review until the later separate visual-fidelity and final historical-glyph gates pass."
)

required = [
    ROOT / "works/naam/transcription/index.json",
    ROOT / "works/naam/transcription/parts/pdf-005-009.md",
    ROOT / "works/naam/transcription/parts/pdf-010-014.md",
    ROOT / "works/naam/transcription/parts/pdf-015-019.md",
    ROOT / "works/naam/transcription/parts/pdf-020-024.md",
    ROOT / "works/naam/transcription/README.md",
    ROOT / "works/naam/notes/textual-notes-pdf-005-009.md",
    ROOT / "works/naam/notes/textual-notes-pdf-010-014.md",
    ROOT / "works/naam/notes/textual-notes-pdf-015-019.md",
    ROOT / "works/naam/notes/textual-notes-pdf-020-024.md",
    ROOT / "works/naam/notes/historical-glyph-audit.md",
    ROOT / "works/naam/metadata.yaml",
    ROOT / "works/naam/README.md",
    ROOT / "works/naam/PROJECT_HANDOVER.md",
    ROOT / "works/naam/NEXT_CHAT_PROMPT.md",
]
for path in required:
    if not path.exists():
        raise SystemExit(f"Missing required file: {path.relative_to(ROOT)}")

index_path = ROOT / "works/naam/transcription/index.json"
index = json.loads(index_path.read_text(encoding="utf-8"))
checks = {
    "status": "partial-first-pass",
    "first_pass_pages_completed": 20,
    "current_through_pdf": 24,
    "historical_glyph_checked_pages": 20,
    "verified_pages": 0,
    "open_uncertainty_markers": 2,
}
for key, expected in checks.items():
    if index.get(key) != expected:
        raise SystemExit(f"Transcription index mismatch {key}: {index.get(key)!r} != {expected!r}")
if index.get("next_batch_pdf_range") != [25, 29]:
    raise SystemExit("Naam next batch must be PDF 25-29")

batch = (ROOT / "works/naam/transcription/parts/pdf-020-024.md").read_text(encoding="utf-8")
for needle in [
    "நீதானா...?",
    "## காட்சி-10.",
    "எங்கம்மா?",
    "தூர பந்து",
    "மட்டாக",
    "கெளரவம்",
]:
    if needle not in batch:
        raise SystemExit(f"Naam PDF 20-24 source decision missing: {needle}")
if "நீதானு...?" in batch:
    raise SystemExit("Stale modern-lookalike reading remains: நீதானு...?")

metadata = (ROOT / "works/naam/metadata.yaml").read_text(encoding="utf-8")
for needle in [
    "  first_pass_pages_completed: 20",
    '  first_pass_pdf_range_completed: "5-24"',
    "  pages_checked: 20",
    "  high_confidence_blocks: 6",
    "  canonical_tamil_transcription: partial-first-pass-through-pdf-024",
    '    source_supported_unicode: "நீதானா...?"',
]:
    if needle not in metadata:
        raise SystemExit(f"Naam metadata checkpoint missing: {needle}")

changed: list[str] = []


def write_if_changed(path: Path, text: str) -> None:
    old = path.read_text(encoding="utf-8")
    if old != text:
        path.write_text(text, encoding="utf-8")
        changed.append(path.relative_to(ROOT).as_posix())


def replace_section(text: str, heading: str, next_heading: str, replacement: str) -> str:
    pattern = re.compile(
        rf"{re.escape(heading)}\n.*?(?=\n{re.escape(next_heading)}\n)",
        re.S,
    )
    if not pattern.search(text):
        raise SystemExit(f"Section not found: {heading} -> {next_heading}")
    return pattern.sub(replacement.rstrip(), text, count=1)


# data/works.json — update only the Naam object and preserve unrelated bytes.
registry_path = ROOT / "data/works.json"
registry = registry_path.read_text(encoding="utf-8")
needle = '"id":"naam"'
pos = registry.find(needle)
if pos < 0:
    pos = registry.find('"id": "naam"')
if pos < 0:
    raise SystemExit("Naam registry object not found")
start = registry.rfind("{", 0, pos)
if start < 0:
    raise SystemExit("Could not locate Naam object start")
depth = 0
in_str = False
esc = False
end = None
for i in range(start, len(registry)):
    ch = registry[i]
    if in_str:
        if esc:
            esc = False
        elif ch == "\\":
            esc = True
        elif ch == '"':
            in_str = False
        continue
    if ch == '"':
        in_str = True
    elif ch == "{":
        depth += 1
    elif ch == "}":
        depth -= 1
        if depth == 0:
            end = i + 1
            break
if end is None:
    raise SystemExit("Could not locate Naam object end")
obj = json.loads(registry[start:end])
if obj.get("source_sha256") != SOURCE_SHA:
    raise SystemExit("Naam source SHA mismatch in registry")
obj.update({
    "canonical_tamil_transcription": "partial-first-pass-through-pdf-024",
    "canonical_tamil_first_pass_pages_completed": 20,
    "canonical_tamil_first_pass_pdf_range_completed": "5-24",
    "canonical_tamil_first_pass_current_through_pdf": 24,
    "canonical_tamil_draft_pages": 20,
    "canonical_tamil_verified_pages": 0,
    "canonical_tamil_review_pages": 20,
    "canonical_tamil_open_uncertainty_markers": 2,
    "canonical_tamil_index_path": "works/naam/transcription/index.json",
    "canonical_tamil_current_batch_path": "works/naam/transcription/parts/pdf-020-024.md",
    "canonical_tamil_current_textual_notes_path": "works/naam/notes/textual-notes-pdf-020-024.md",
    "historical_glyph_audit": "partial-first-pass-through-pdf-024",
    "historical_glyph_pages_checked": 20,
    "historical_glyph_pages_verified": 0,
    "visual_fidelity_audit": "not-started",
    "mapped_source_visible_performance_structures": 6,
    "pdf_18_lyrical_duet_confirmed": True,
    "pdf_18_lyrical_duet_authorship": "not-adjudicated",
    "pdf_21_historical_na_decoding": "நீதானா...?",
    "next_action": NEXT,
})
new_obj = json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
registry = registry[:start] + new_obj + registry[end:]
json.loads(registry)
if CRITICAL_TIRUMBIPPAAR_SHA not in registry:
    raise SystemExit("Critical Tirumbippaar EPUB checksum not preserved")
write_if_changed(registry_path, registry)

# Root README — replace only Naam current-status section.
root_readme = ROOT / "README.md"
text = root_readme.read_text(encoding="utf-8")
naam_readme = f'''## நாம் status

`TVA_BOK_0064201_நாம்.pdf` is the **active cinema source**. Intake and the 45-scene structural map are complete; canonical Tamil first-pass transcription is in progress.

- source: **72 PDF pages**, image-only; SHA-256 `{SOURCE_SHA}`;
- front matter / screenplay / back matter: **PDF 1–4 / 5–71 / 72**;
- source-numbered scenes: **45 — காட்சி 1–45**, sequential;
- canonical Tamil first pass: **PDF 5–24 / 20 of 67 pages**;
- completed first-pass batches: `works/naam/transcription/parts/pdf-005-009.md`, `works/naam/transcription/parts/pdf-010-014.md`, `works/naam/transcription/parts/pdf-015-019.md`, `works/naam/transcription/parts/pdf-020-024.md`;
- verified pages: **0**; separate visual-fidelity audit: **not-started**;
- historical-glyph first-pass checked: **20/67**; final glyph-verified: **0/67**;
- open source uncertainty markers: **2**, both carried from PDF 5/9; PDF 10–24 adds none;
- PDF 21 `நீதானா...?` is a source-backed historical-`னா` decoding; the apparent modern-lookalike `நீதானு...?` is rejected;
- PDF 20–24 retains source-period forms including `போறு ஞானம்!`, `மாடெல்லே`, `பாலிலா`, `தூர பந்து`, `மட்டாக`, and `கெளரவம்`;
- PDF 16 / காட்சி 7 preserves the explicit `[பாட்டு]` booklet witness for `ஆயிரம் தெய்வங்கள்`, item-level credited on PDF 4 to **பாரதியார்**;
- PDF 18 / காட்சி 8 preserves the lineated lyrical duet beginning `பேசும் யாழே பெண் மானே`; authorship remains **not adjudicated**;
- PDF 20–24 introduces no newly distinct standalone song/lyric block;
- downstream derivatives remain blocked pending verified Tamil.

**Next:** {NEXT}
'''
text = replace_section(text, "## நாம் status", "## ராஜா ராணி status", naam_readme)
write_if_changed(root_readme, text)

# Master handover — update high-level bullet and active checkpoint section.
handover_path = ROOT / "docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md"
handover = handover_path.read_text(encoding="utf-8")
handover = re.sub(
    r"^- \*\*Naam / நாம்\*\* — .*?$",
    f"- **Naam / நாம்** — active work; intake/map complete; canonical Tamil first pass **PDF 5–24 / 20 of 67**; glyph first-pass **20/67**; verified **0/67**; 2 carried source uncertainties; PDF 21 `நீதானா...?` historical-`னா` decoding recorded; next PDF 25–29. Source SHA-256 `{SOURCE_SHA}`.",
    handover,
    count=1,
    flags=re.M,
)
naam_handover = f'''## 8. Naam active checkpoint

Work: `works/naam/`  
Source: `TVA_BOK_0064201_நாம்.pdf`

- intake / whole-scan map: **complete / verified**;
- source SHA-256: `{SOURCE_SHA}`;
- screenplay range: **PDF 5–71 / 67 pages**;
- source-numbered scenes: **காட்சி 1–45**, sequential;
- canonical Tamil first pass: **PDF 5–24 / 20 of 67 pages**;
- canonical verified pages: **0**;
- visual-fidelity audit: **not-started**;
- historical-glyph first-pass checked / final verified: **20/67 / 0/67**;
- open source uncertainties: **2**, both inherited from PDF 5/9;
- current batch: `works/naam/transcription/parts/pdf-020-024.md`;
- current source notes: `works/naam/notes/textual-notes-pdf-020-024.md`;
- PDF 21 `நீதானா...?` is source-backed historical `னா`; apparent `நீதானு...?` is rejected;
- PDF 20–24 preserves `போறு ஞானம்!`, `மாடெல்லே`, standalone `எங்கம்மா?`, `தூர பந்து`, `மட்டாக`, `கெளரவம்` and exact scene-heading variation `காட்சி-10.` / `காட்சி 11`;
- PDF 20–24 adds no new uncertainty marker and no newly distinct standalone lyric/song block;
- no first-pass page is yet `verified`;
- structured derivatives / English / reader remain blocked.

**Exact next activity:** {NEXT}

---
'''
handover = replace_section(handover, "## 8. Naam active checkpoint", "## 9. Ammayappan closed checkpoint", naam_handover)
write_if_changed(handover_path, handover)

# Status audit — update result, matrix row, active checkpoint and conclusion.
status_path = ROOT / "docs/STATUS_CONSISTENCY_AUDIT.md"
status = status_path.read_text(encoding="utf-8")
status = re.sub(
    r"\*\*PASS for the current repository-wide checkpoint\.\*\*.*?(?=\n\nThe scene-3 post-closure)",
    "**PASS for the current repository-wide checkpoint.** Ammayappan remains complete-verified through its Reading Room payload. **Naam / நாம்** is the active production work with intake/map complete and canonical Tamil first pass at **PDF 5–24 / 20 of 67 pages**, historical-glyph first-pass **20/67**, **0 verified pages**, and **2 carried source uncertainties**. PDF 21 records the historical-`னா` decoding `நீதானா...?`; PDF 20–24 adds no new uncertainty marker or standalone lyric/song block.",
    status,
    count=1,
    flags=re.S,
)
status = re.sub(
    r"^\| Naam / நாம் \|.*?$",
    "| Naam / நாம் | intake/map complete; first pass **PDF 5–24 / 20 of 67**, 0 verified | 45 source-numbered scenes mapped; derivatives blocked | not-started | not-started |",
    status,
    count=1,
    flags=re.M,
)
naam_status = f'''## Naam current checkpoint

- work: `works/naam/`;
- source: `TVA_BOK_0064201_நாம்.pdf`, **72 pages / image-only**, SHA-256 `{SOURCE_SHA}`;
- source intake / structural mapping: **complete / verified**;
- canonical Tamil first pass: **PDF 5–24 / 20 of 67 pages**;
- verified pages / visual-fidelity passed: **0 / 0**;
- historical-glyph first-pass checked / final verified: **20 / 0**;
- open uncertainty markers: **2**, both carried from PDF 5/9;
- current draft: `works/naam/transcription/parts/pdf-020-024.md`;
- current notes: `works/naam/notes/textual-notes-pdf-020-024.md`;
- PDF 21 `நீதானா...?` is a historical-`னா` source decoding; `நீதானு...?` is not accepted;
- exact source forms include `போறு ஞானம்!`, `மாடெல்லே`, standalone `எங்கம்மா?`, `தூர பந்து`, `மட்டாக`, and `கெளரவம்`;
- PDF 20–24 adds no new uncertainty marker and no new standalone lyric/song block;
- PDF 16 Bharathiyar item evidence and PDF 18 unadjudicated lyrical-duet evidence remain unchanged;
- downstream scene/dialogue/character/song/English layers remain blocked until verified Tamil.

**Next production phase:** {NEXT}
'''
status = replace_section(status, "## Naam current checkpoint", "## Ammayappan current checkpoint", naam_status)
status = re.sub(
    r"Ammayappan remains closed through Reading Room payload QA PASS\. \*\*Naam / நாம்\*\* is the active production work.*?Source SHA-256 `[^`]+`\.",
    f"Ammayappan remains closed through Reading Room payload QA PASS. **Naam / நாம்** is the active production work with intake/map complete and canonical Tamil first pass at **PDF 5–24 / 20 of 67 pages**, **0 verified pages**, historical-glyph first-pass **20/67**, and **2 carried source uncertainties**. The next batch is PDF 25–29. Source SHA-256 `{SOURCE_SHA}`.",
    status,
    count=1,
    flags=re.S,
)
write_if_changed(status_path, status)

print("Changed files:")
for path in changed:
    print(f"- {path}")
