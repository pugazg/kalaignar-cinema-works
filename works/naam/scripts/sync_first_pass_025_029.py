#!/usr/bin/env python3
"""Synchronize repository-wide mirrors for Naam canonical first-pass PDF 25-29."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE_SHA = "0f7a54882eb6a5a8f83b29060c771ef18dee2b9e108c8797184de2b97c30b7ad"
CRITICAL_TIRUMBIPPAAR_SHA = "17b9422cf2bf9cd30c90829a2dbd18115e20b8bd1cf7e5bb9da2cc0cdcc23c7f"
NEXT = (
    "Continue canonical Tamil first-pass transcription with PDF 30–34, preserving source order, "
    "stable page anchors and page-level historical-glyph checks. Keep all first-pass pages "
    "draft/needs-review until the later separate visual-fidelity and final historical-glyph gates pass."
)

required = [
    ROOT / "works/naam/transcription/index.json",
    ROOT / "works/naam/transcription/parts/pdf-005-009.md",
    ROOT / "works/naam/transcription/parts/pdf-010-014.md",
    ROOT / "works/naam/transcription/parts/pdf-015-019.md",
    ROOT / "works/naam/transcription/parts/pdf-020-024.md",
    ROOT / "works/naam/transcription/parts/pdf-025-029.md",
    ROOT / "works/naam/transcription/README.md",
    ROOT / "works/naam/notes/textual-notes-pdf-005-009.md",
    ROOT / "works/naam/notes/textual-notes-pdf-010-014.md",
    ROOT / "works/naam/notes/textual-notes-pdf-015-019.md",
    ROOT / "works/naam/notes/textual-notes-pdf-020-024.md",
    ROOT / "works/naam/notes/textual-notes-pdf-025-029.md",
    ROOT / "works/naam/notes/historical-glyph-audit.md",
    ROOT / "works/naam/metadata.yaml",
    ROOT / "works/naam/README.md",
    ROOT / "works/naam/PROJECT_HANDOVER.md",
    ROOT / "works/naam/NEXT_CHAT_PROMPT.md",
]
for path in required:
    if not path.exists():
        raise SystemExit(f"Missing required file: {path.relative_to(ROOT)}")

index = json.loads((ROOT / "works/naam/transcription/index.json").read_text(encoding="utf-8"))
checks = {
    "status": "partial-first-pass",
    "first_pass_pages_completed": 25,
    "current_through_pdf": 29,
    "historical_glyph_checked_pages": 25,
    "verified_pages": 0,
    "open_uncertainty_markers": 2,
}
for key, expected in checks.items():
    if index.get(key) != expected:
        raise SystemExit(f"Transcription index mismatch {key}: {index.get(key)!r} != {expected!r}")
if index.get("next_batch_pdf_range") != [30, 34]:
    raise SystemExit("Naam next batch must be PDF 30-34")

batch = (ROOT / "works/naam/transcription/parts/pdf-025-029.md").read_text(encoding="utf-8")
for needle in [
    "## காட்சி 12",
    "## காட்சி 13",
    "## காட்சி 14",
    "தயாரப்பட்ட விஷம்",
    "மண்ணுங்கட்டியாவது",
    "ஏணிப்படியாக்கிக்",
    "காதலை நான்",
    "ஒரு அணா!",
]:
    if needle not in batch:
        raise SystemExit(f"Naam PDF 25-29 source decision missing: {needle}")

metadata = (ROOT / "works/naam/metadata.yaml").read_text(encoding="utf-8")
for needle in [
    "  first_pass_pages_completed: 25",
    '  first_pass_pdf_range_completed: "5-29"',
    "  pages_checked: 25",
    "  high_confidence_blocks: 6",
    "  canonical_tamil_transcription: partial-first-pass-through-pdf-029",
    '    source_supported_unicode: "அலைந்தான்"',
    '    source_supported_unicode: "சாணைக்கல்லிலே"',
    '    source_supported_unicode: "காதலை நான்"',
    '    source_supported_unicode: "அணா"',
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
    "canonical_tamil_transcription": "partial-first-pass-through-pdf-029",
    "canonical_tamil_first_pass_pages_completed": 25,
    "canonical_tamil_first_pass_pdf_range_completed": "5-29",
    "canonical_tamil_first_pass_current_through_pdf": 29,
    "canonical_tamil_draft_pages": 25,
    "canonical_tamil_verified_pages": 0,
    "canonical_tamil_review_pages": 25,
    "canonical_tamil_open_uncertainty_markers": 2,
    "canonical_tamil_index_path": "works/naam/transcription/index.json",
    "canonical_tamil_current_batch_path": "works/naam/transcription/parts/pdf-025-029.md",
    "canonical_tamil_current_textual_notes_path": "works/naam/notes/textual-notes-pdf-025-029.md",
    "historical_glyph_audit": "partial-first-pass-through-pdf-029",
    "historical_glyph_pages_checked": 25,
    "historical_glyph_pages_verified": 0,
    "visual_fidelity_audit": "not-started",
    "mapped_source_visible_performance_structures": 6,
    "pdf_25_29_new_performance_structures": 0,
    "pdf_26_historical_lai_decoding": "அலைந்தான்",
    "pdf_27_historical_nai_decoding": "சாணைக்கல்லிலே",
    "pdf_28_historical_lai_na_decoding": "காதலை நான்",
    "pdf_29_historical_naa_decoding": "அணா",
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
- canonical Tamil first pass: **PDF 5–29 / 25 of 67 pages**;
- completed first-pass batches: `works/naam/transcription/parts/pdf-005-009.md`, `works/naam/transcription/parts/pdf-010-014.md`, `works/naam/transcription/parts/pdf-015-019.md`, `works/naam/transcription/parts/pdf-020-024.md`, `works/naam/transcription/parts/pdf-025-029.md`;
- verified pages: **0**; separate visual-fidelity audit: **not-started**;
- historical-glyph first-pass checked: **25/67**; final glyph-verified: **0/67**;
- open source uncertainty markers: **2**, both carried from PDF 5/9; PDF 10–29 adds none;
- PDF 26 `அலைந்தான்` is source-backed `லை`; PDF 27 `சாணைக்கல்லிலே` / `சாணைக்கல்லை` are `ணை`; PDF 28 `காதலை நான்` checks `லை` / `னா`; PDF 29 `அணா` is a positive `ணா` case;
- PDF 25–29 retains source-period/colloquial forms including `மண்ணுங்கட்டியாவது`, `ஏணிப்படியாக்கிக்`, `லஷ்மி`, `ஜமீன்தாரணி யாக்க`, and `காண்டிராக்ட்காரன்`;
- PDF 16 / காட்சி 7 preserves the explicit `[பாட்டு]` booklet witness for `ஆயிரம் தெய்வங்கள்`, item-level credited on PDF 4 to **பாரதியார்**;
- PDF 18 / காட்சி 8 preserves the lineated lyrical duet beginning `பேசும் யாழே பெண் மானே`; authorship remains **not adjudicated**;
- PDF 25–29 introduces no newly distinct standalone song/lyric block;
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
    f"- **Naam / நாம்** — active work; intake/map complete; canonical Tamil first pass **PDF 5–29 / 25 of 67**; glyph first-pass **25/67**; verified **0/67**; 2 carried source uncertainties; next PDF 30–34. Source SHA-256 `{SOURCE_SHA}`.",
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
- canonical Tamil first pass: **PDF 5–29 / 25 of 67 pages**;
- canonical verified pages: **0**;
- visual-fidelity audit: **not-started**;
- historical-glyph first-pass checked / final verified: **25/67 / 0/67**;
- open source uncertainties: **2**, both inherited from PDF 5/9;
- current batch: `works/naam/transcription/parts/pdf-025-029.md`;
- current source notes: `works/naam/notes/textual-notes-pdf-025-029.md`;
- PDF 25 contains source scenes 12 and 13; PDF 29 opens scene 14;
- PDF 26 preserves `தயாரப்பட்ட விஷம்`, `மதோன்மத்த`, `மண்ணுங்கட்டியாவது`, `அலைந்தான்`;
- PDF 27 preserves `உயில் ஒரு வாள்!`, `சாணைக்கல்லிலே`, `ஏணிப்படியாக்கிக்`;
- PDF 28 preserves two unlabeled continuations and source `காதலை நான்` / `ஜமீன்தாரணி யாக்க`;
- PDF 29 preserves `காண்டிராக்ட்காரன்` and the two `அணா` payment occurrences;
- PDF 25–29 adds no new uncertainty marker and no newly distinct standalone lyric/song block;
- no first-pass page is yet `verified`;
- structured derivatives / English / reader remain blocked.

**Exact next activity:** {NEXT}

---
'''
handover = replace_section(handover, "## 8. Naam active checkpoint", "## 9. Ammayappan closed checkpoint", naam_handover)
write_if_changed(handover_path, handover)

# Status audit — update matrix row and active checkpoint.
status_path = ROOT / "docs/STATUS_CONSISTENCY_AUDIT.md"
status = status_path.read_text(encoding="utf-8")
status = re.sub(
    r"^\| Naam / நாம் \|.*?$",
    "| Naam / நாம் | intake/map complete; first pass **PDF 5–29 / 25 of 67**, 0 verified | 45 source-numbered scenes mapped; derivatives blocked | not-started | not-started |",
    status,
    count=1,
    flags=re.M,
)
naam_status = f'''## Naam current checkpoint

- work: `works/naam/`;
- source: `TVA_BOK_0064201_நாம்.pdf`, **72 pages / image-only**, SHA-256 `{SOURCE_SHA}`;
- source intake / structural mapping: **complete / verified**;
- canonical Tamil first pass: **PDF 5–29 / 25 of 67 pages**;
- verified pages / visual-fidelity passed: **0 / 0**;
- historical-glyph first-pass checked / final verified: **25 / 0**;
- open uncertainty markers: **2**, both carried from PDF 5/9;
- current draft: `works/naam/transcription/parts/pdf-025-029.md`;
- current source notes: `works/naam/notes/textual-notes-pdf-025-029.md`;
- PDF 26 `அலைந்தான்` is a source-backed `லை` decoding;
- PDF 27 `சாணைக்கல்லிலே` / `சாணைக்கல்லை` are checked `ணை` cases;
- PDF 28 `காதலை நான்` is checked against historical `லை` / `னா` forms;
- PDF 29 `அணா` is a positive `ணா` case;
- source irregulars `மண்ணுங்கட்டியாவது`, `ஏணிப்படியாக்கிக்`, `லஷ்மி`, `ஜமீன்தாரணி யாக்க`, and `காண்டிராக்ட்காரன்` remain source-controlled;
- PDF 25–29 introduces no new explicit uncertainty and no new standalone song/lyric block;
- downstream scene/dialogue/character/song/English layers remain blocked until verified Tamil.

**Next production phase:** {NEXT}

'''
try:
    status = replace_section(status, "## Naam current checkpoint", "## Ammayappan current checkpoint", naam_status)
except SystemExit:
    # Preserve compatibility if the next heading carries a numeric prefix in a future edit.
    pat = re.compile(r"## Naam current checkpoint\n.*?(?=\n## .*Ammayappan.*checkpoint\n)", re.S)
    if not pat.search(status):
        raise
    status = pat.sub(naam_status.rstrip(), status, count=1)

status = re.sub(
    r"Ammayappan remains closed through Reading Room payload QA PASS\. \*\*Naam / நாம்\*\* is now the active production work.*?Source SHA-256 `[^`]+`\.",
    f"Ammayappan remains closed through Reading Room payload QA PASS. **Naam / நாம்** is the active production work with intake/map complete and canonical Tamil first pass now at **PDF 5–29 / 25 of 67 pages**, with **0 verified pages**, historical-glyph first-pass **25/67**, and **2 carried source uncertainties**. The next batch is PDF 30–34. Source SHA-256 `{SOURCE_SHA}`.",
    status,
    count=1,
    flags=re.S,
)
write_if_changed(status_path, status)

print("Changed files:")
for path in changed:
    print(f"- {path}")
