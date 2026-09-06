#!/usr/bin/env python3
"""Synchronize repository-wide mirrors for Naam canonical first-pass PDF 15-19."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE_SHA = "0f7a54882eb6a5a8f83b29060c771ef18dee2b9e108c8797184de2b97c30b7ad"
NEXT = (
    "Continue canonical Tamil first-pass transcription with PDF 20–24, preserving source order, "
    "stable page anchors and page-level historical-glyph checks. Keep all first-pass pages "
    "draft/needs-review until the later separate visual-fidelity and final historical-glyph gates pass."
)

required = [
    ROOT / "works/naam/transcription/index.json",
    ROOT / "works/naam/transcription/parts/pdf-005-009.md",
    ROOT / "works/naam/transcription/parts/pdf-010-014.md",
    ROOT / "works/naam/transcription/parts/pdf-015-019.md",
    ROOT / "works/naam/transcription/README.md",
    ROOT / "works/naam/notes/textual-notes-pdf-005-009.md",
    ROOT / "works/naam/notes/textual-notes-pdf-010-014.md",
    ROOT / "works/naam/notes/textual-notes-pdf-015-019.md",
    ROOT / "works/naam/notes/historical-glyph-audit.md",
    ROOT / "works/naam/metadata.yaml",
    ROOT / "works/naam/README.md",
    ROOT / "works/naam/PROJECT_HANDOVER.md",
    ROOT / "works/naam/NEXT_CHAT_PROMPT.md",
]
for p in required:
    if not p.exists():
        raise SystemExit(f"Missing required file: {p.relative_to(ROOT)}")

index = json.loads((ROOT / "works/naam/transcription/index.json").read_text(encoding="utf-8"))
checks = {
    "status": "partial-first-pass",
    "first_pass_pages_completed": 15,
    "current_through_pdf": 19,
    "historical_glyph_checked_pages": 15,
    "verified_pages": 0,
    "open_uncertainty_markers": 2,
}
for key, expected in checks.items():
    if index.get(key) != expected:
        raise SystemExit(f"Transcription index mismatch {key}: {index.get(key)!r} != {expected!r}")
if index.get("next_batch_pdf_range") != [20, 24]:
    raise SystemExit("Naam next batch must be PDF 20-24")

batch = (ROOT / "works/naam/transcription/parts/pdf-015-019.md").read_text(encoding="utf-8")
for needle in [
    "இந்த அன்பு உள்ளம் உலகத்தில் எல்லோருக்கும் இருந்தால்",
    "உருண்டோடிடுமே",
    "அவன் கை வலி எடுக்கும் வரை",
    "என்னே......",
    "என் மருமகளும்",
    "[பாட்டு]",
    "ஆயிரம் தெய்வங்கள் உண்டென்று தேடி",
    "பேசும் யாழே பெண் மானே",
]:
    if needle not in batch:
        raise SystemExit(f"Naam PDF 15-19 reconciled source reading missing: {needle}")
for forbidden in [
    "எல்லோருக்குமே இருந்தால்",
    "உருண்டோடிடும்...ப",
    "அவனே கை வலி",
    "என் மருமகனும் பூட்டப்பட்டு",
]:
    if forbidden in batch:
        raise SystemExit(f"Stale Naam PDF 15-19 first-pass reading remains: {forbidden}")

metadata = (ROOT / "works/naam/metadata.yaml").read_text(encoding="utf-8")
for needle in [
    "  first_pass_pages_completed: 15",
    '  first_pass_pdf_range_completed: "5-19"',
    "  pages_checked: 15",
    "  high_confidence_blocks: 6",
    '      opening: "பேசும் யாழே பெண் மானே"',
    "  canonical_tamil_transcription: partial-first-pass-through-pdf-019",
]:
    if needle not in metadata:
        raise SystemExit(f"Naam metadata checkpoint missing: {needle}")

changed: list[str] = []


def write_if_changed(path: Path, text: str) -> None:
    old = path.read_text(encoding="utf-8")
    if old != text:
        path.write_text(text, encoding="utf-8")
        changed.append(path.relative_to(ROOT).as_posix())


# data/works.json — replace only the Naam object while preserving unrelated bytes.
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
    "canonical_tamil_transcription": "partial-first-pass-through-pdf-019",
    "canonical_tamil_first_pass_pages_completed": 15,
    "canonical_tamil_first_pass_pdf_range_completed": "5-19",
    "canonical_tamil_first_pass_current_through_pdf": 19,
    "canonical_tamil_draft_pages": 15,
    "canonical_tamil_verified_pages": 0,
    "canonical_tamil_review_pages": 15,
    "canonical_tamil_open_uncertainty_markers": 2,
    "canonical_tamil_index_path": "works/naam/transcription/index.json",
    "canonical_tamil_current_batch_path": "works/naam/transcription/parts/pdf-015-019.md",
    "canonical_tamil_current_textual_notes_path": "works/naam/notes/textual-notes-pdf-015-019.md",
    "historical_glyph_audit": "partial-first-pass-through-pdf-019",
    "historical_glyph_pages_checked": 15,
    "historical_glyph_pages_verified": 0,
    "visual_fidelity_audit": "not-started",
    "mapped_source_visible_performance_structures": 6,
    "pdf_18_lyrical_duet_confirmed": True,
    "pdf_18_lyrical_duet_authorship": "not-adjudicated",
    "next_action": NEXT,
})
new_obj = json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
registry = registry[:start] + new_obj + registry[end:]
json.loads(registry)
critical = "17b9422cf2bf9cd30c90829a2dbd18115e20b8bd1cf7e5bb9da2cc0cdcc23c7f"
if critical not in registry:
    raise SystemExit("Critical Tirumbippaar EPUB checksum not preserved")
write_if_changed(registry_path, registry)

# Root README — replace only Naam current-status section.
root_readme = ROOT / "README.md"
text = root_readme.read_text(encoding="utf-8")
naam_section = f'''## நாம் status

`TVA_BOK_0064201_நாம்.pdf` is the **active cinema source**. Intake and the 45-scene structural map are complete; canonical Tamil first-pass transcription is in progress.

- source: **72 PDF pages**, image-only; SHA-256 `{SOURCE_SHA}`;
- front matter / screenplay / back matter: **PDF 1–4 / 5–71 / 72**;
- source-numbered scenes: **45 — காட்சி 1–45**, sequential;
- canonical Tamil first pass: **PDF 5–19 / 15 of 67 pages**;
- completed first-pass batches: `works/naam/transcription/parts/pdf-005-009.md`, `works/naam/transcription/parts/pdf-010-014.md`, `works/naam/transcription/parts/pdf-015-019.md`;
- verified pages: **0**; separate visual-fidelity audit: **not-started**;
- historical-glyph first-pass checked: **15/67**; final glyph-verified: **0/67**;
- open source uncertainty markers: **2**, both carried from PDF 5/9; PDF 10–19 adds none;
- PDF 15–19 scan reconciliation corrected `எல்லோருக்கும்`, `உருண்டோடிடுமே`, `அவன் கை வலி`, `என்னே`, `என் மருமகளும்`;
- PDF 16 / காட்சி 7 preserves the explicit `[பாட்டு]` booklet witness for `ஆயிரம் தெய்வங்கள்`, item-level credited on PDF 4 to **பாரதியார்**;
- PDF 18 / காட்சி 8 newly confirms a lineated lyrical duet beginning `பேசும் யாழே பெண் மானே`; authorship remains **not adjudicated**;
- downstream derivatives remain blocked pending verified Tamil.

**Next:** {NEXT}
'''
pat = re.compile(r"## நாம் status\n.*?(?=\n## )", re.S)
if not pat.search(text):
    raise SystemExit("Root README Naam section not found")
text = pat.sub(naam_section.rstrip(), text, count=1)
write_if_changed(root_readme, text)

# Master handover — update high-level bullet and active checkpoint section.
handover_path = ROOT / "docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md"
handover = handover_path.read_text(encoding="utf-8")
handover = re.sub(
    r"^- \*\*Naam / நாம்\*\* — .*?$",
    f"- **Naam / நாம்** — active work; intake/map complete; canonical Tamil first pass **PDF 5–19 / 15 of 67**; glyph first-pass **15/67**; verified **0/67**; 2 carried source uncertainties; PDF 16 Bharathiyar item witness preserved; PDF 18 lyrical duet newly source-confirmed; next PDF 20–24. Source SHA-256 `{SOURCE_SHA}`.",
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
- canonical Tamil first pass: **PDF 5–19 / 15 of 67 pages**;
- canonical verified pages: **0**;
- visual-fidelity audit: **not-started**;
- historical-glyph first-pass checked / final verified: **15/67 / 0/67**;
- open source uncertainties: **2**, both inherited from PDF 5/9;
- current batch: `works/naam/transcription/parts/pdf-015-019.md`;
- current source notes: `works/naam/notes/textual-notes-pdf-015-019.md`;
- PDF 15–19 scan-backed corrections: `எல்லோருக்கும்`, `உருண்டோடிடுமே`, `அவன் கை வலி`, `என்னே`, `என் மருமகளும்`;
- PDF 16 / scene 7: explicit `[பாட்டு]` witness, item-level source credit `ஆயிரம் தெய்வங்கள்` — `பாரதியார்`; no outside lyric witness used;
- PDF 18 / scene 8: lineated lyrical duet beginning `பேசும் யாழே பெண் மானே`, authorship **not adjudicated**;
- no first-pass page is yet `verified`;
- structured derivatives / English / reader remain blocked.

**Exact next activity:** {NEXT}

---

'''
pat = re.compile(r"## 8\. Naam active checkpoint\n.*?(?=## 9\. Ammayappan closed checkpoint)", re.S)
if not pat.search(handover):
    raise SystemExit("Master handover Naam active section not found")
handover = pat.sub(naam_handover, handover, count=1)
write_if_changed(handover_path, handover)

# Status audit — update result, matrix row, active checkpoint and conclusion.
status_path = ROOT / "docs/STATUS_CONSISTENCY_AUDIT.md"
status = status_path.read_text(encoding="utf-8")
result_pat = re.compile(r"## Result\n\n\*\*PASS for the current repository-wide checkpoint\.\*\*.*?(?=\n\nThe scene-3 post-closure)", re.S)
result_text = (
    "## Result\n\n**PASS for the current repository-wide checkpoint.** Ammayappan remains complete-verified through its Reading Room payload. "
    "**Naam / நாம்** is the active production work with intake/map complete and canonical Tamil first pass at **PDF 5–19 / 15 of 67 pages**, "
    "historical-glyph first-pass **15/67**, **0 verified pages**, and **2 carried source uncertainties**. PDF 16 preserves the booklet's "
    "item-level Bharathiyar witness for `ஆயிரம் தெய்வங்கள்`; PDF 18 newly confirms a lineated lyrical duet whose authorship remains unadjudicated."
)
if not result_pat.search(status):
    raise SystemExit("Status audit Result checkpoint not found")
status = result_pat.sub(result_text, status, count=1)
status = re.sub(
    r"^\| Naam / நாம் \|.*?$",
    "| Naam / நாம் | intake/map complete; first pass **PDF 5–19 / 15 of 67**, 0 verified | 45 source-numbered scenes mapped; derivatives blocked | not-started | not-started |",
    status,
    count=1,
    flags=re.M,
)
naam_status = f'''## Naam current checkpoint

- work: `works/naam/`;
- source: `TVA_BOK_0064201_நாம்.pdf`, **72 pages / image-only**, SHA-256 `{SOURCE_SHA}`;
- source intake / structural mapping: **complete / verified**;
- canonical Tamil first pass: **PDF 5–19 / 15 of 67 pages**;
- verified pages / visual-fidelity passed: **0 / 0**;
- historical-glyph first-pass checked / final verified: **15 / 0**;
- open uncertainty markers: **2**, both carried from PDF 5/9;
- current draft: `works/naam/transcription/parts/pdf-015-019.md`;
- current notes: `works/naam/notes/textual-notes-pdf-015-019.md`;
- PDF 15–19 source-pixel reconciliation corrected `எல்லோருக்கும்`, `உருண்டோடிடுமே`, `அவன் கை வலி`, `என்னே`, `என் மருமகளும்`;
- PDF 16 / காட்சி 7: explicit `[பாட்டு]` witness; booklet item-level credit `ஆயிரம் தெய்வங்கள்` — `பாரதியார்`; outside lyric witnesses not used;
- PDF 18 / காட்சி 8: source-visible lyrical duet beginning `பேசும் யாழே பெண் மானே`; authorship remains not adjudicated;
- PDF 15 `ஓரிடந்தனிலே...` remains dialogue-owned rather than being manufactured into a standalone song;
- downstream scene/dialogue/character/song/English layers remain blocked until verified Tamil.

**Next production phase:** {NEXT}

'''
pat = re.compile(r"## Naam current checkpoint\n.*?(?=## Ammayappan current checkpoint)", re.S)
if not pat.search(status):
    raise SystemExit("Status audit Naam checkpoint not found")
status = pat.sub(naam_status, status, count=1)
status = re.sub(
    r"Ammayappan remains closed through Reading Room payload QA PASS\. \*\*Naam / நாம்\*\* is the active production work.*?Source SHA-256 `[^`]+`\.",
    f"Ammayappan remains closed through Reading Room payload QA PASS. **Naam / நாம்** is the active production work with intake/map complete and canonical Tamil first pass at **PDF 5–19 / 15 of 67 pages**, **0 verified pages**, historical-glyph first-pass **15/67**, and **2 carried source uncertainties**. PDF 16's source-specific Bharathiyar item witness and PDF 18's newly source-confirmed lyrical duet are preserved without outside reconstruction. The next batch is PDF 20–24. Source SHA-256 `{SOURCE_SHA}`.",
    status,
    count=1,
    flags=re.S,
)
write_if_changed(status_path, status)

print("Changed files:")
for p in changed:
    print(f"- {p}")
