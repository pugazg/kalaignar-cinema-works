#!/usr/bin/env python3
"""Synchronize Naam canonical first-pass checkpoint through PDF 34."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE_SHA = "0f7a54882eb6a5a8f83b29060c771ef18dee2b9e108c8797184de2b97c30b7ad"
NEXT = (
    "Continue canonical Tamil first-pass transcription with PDF 35–39, preserving source order, "
    "stable page anchors, page-level historical-glyph checks, and the PDF 35–36 / scene-21 lyrical "
    "block exactly as printed. Keep all first-pass pages draft/needs-review until the later separate "
    "visual-fidelity and final historical-glyph gates pass."
)

required = [
    ROOT / "works/naam/transcription/index.json",
    ROOT / "works/naam/transcription/parts/pdf-030-034.md",
    ROOT / "works/naam/notes/textual-notes-pdf-030-034.md",
    ROOT / "works/naam/metadata.yaml",
    ROOT / "works/naam/README.md",
    ROOT / "works/naam/transcription/README.md",
    ROOT / "works/naam/notes/historical-glyph-audit.md",
    ROOT / "works/naam/PROJECT_HANDOVER.md",
]
for path in required:
    if not path.exists():
        raise SystemExit(f"Missing required file: {path.relative_to(ROOT)}")

index = json.loads((ROOT / "works/naam/transcription/index.json").read_text(encoding="utf-8"))
checks = {
    "status": "partial-first-pass",
    "first_pass_pages_completed": 30,
    "current_through_pdf": 34,
    "historical_glyph_checked_pages": 30,
    "verified_pages": 0,
    "open_uncertainty_markers": 2,
}
for key, expected in checks.items():
    if index.get(key) != expected:
        raise SystemExit(f"Transcription index mismatch {key}: {index.get(key)!r} != {expected!r}")
if index.get("next_batch_pdf_range") != [35, 39]:
    raise SystemExit("Naam next batch must be PDF 35-39")

batch = (ROOT / "works/naam/transcription/parts/pdf-030-034.md").read_text(encoding="utf-8")
for needle in [
    "## காட்சி 15",
    "## காட்சி 16",
    "## காட்சி 17.",
    "## காட்சி 18.",
    "## காட்சி 19.",
    "## காட்சி 20.",
    "தவறான",
    "இவனை",
    "ஜமீனையே",
    "அவளை",
    "பஞ்சணை",
]:
    if needle not in batch:
        raise SystemExit(f"Naam PDF 30-34 source decision missing: {needle}")

changed: list[str] = []

def write_if_changed(path: Path, text: str) -> None:
    old = path.read_text(encoding="utf-8") if path.exists() else ""
    if old != text:
        path.write_text(text, encoding="utf-8")
        changed.append(path.relative_to(ROOT).as_posix())


def sub_once(text: str, pattern: str, repl: str, *, flags: int = 0) -> str:
    out, n = re.subn(pattern, repl, text, count=1, flags=flags)
    if n != 1:
        raise SystemExit(f"Expected one replacement for pattern: {pattern}")
    return out

# Work-local metadata.
path = ROOT / "works/naam/metadata.yaml"
text = path.read_text(encoding="utf-8")
for old, new in [
    ("first_pass_pages_completed: 25", "first_pass_pages_completed: 30"),
    ('first_pass_pdf_range_completed: "5-29"', 'first_pass_pdf_range_completed: "5-34"'),
    ("first_pass_current_through_pdf: 29", "first_pass_current_through_pdf: 34"),
    ("first_pass_current_through_printed_page: 29", "first_pass_current_through_printed_page: 34"),
    ("draft_pages: 25", "draft_pages: 30"),
    ("review_pages: 25", "review_pages: 30"),
    ("pages_checked: 25", "pages_checked: 30"),
    ("partial-first-pass-through-pdf-029", "partial-first-pass-through-pdf-034"),
    ('current_batch_path: "transcription/parts/pdf-025-029.md"', 'current_batch_path: "transcription/parts/pdf-030-034.md"'),
    ('current_textual_notes_path: "notes/textual-notes-pdf-025-029.md"', 'current_textual_notes_path: "notes/textual-notes-pdf-030-034.md"'),
    ("pdf_25_29_new_performance_structures: 0", "pdf_30_34_new_performance_structures: 0"),
]:
    if old not in text:
        raise SystemExit(f"Metadata old checkpoint missing: {old}")
    text = text.replace(old, new, 1)
needle = '    - "transcription/parts/pdf-025-029.md"\n'
if '    - "transcription/parts/pdf-030-034.md"' not in text:
    text = text.replace(needle, needle + '    - "transcription/parts/pdf-030-034.md"\n', 1)
insert_after = '''  batch_025_029_consequential_decodings:\n    - pdf_page: 26\n      source_supported_unicode: "அலைந்தான்"\n      family: "லை"\n    - pdf_page: 27\n      source_supported_unicode: "சாணைக்கல்லிலே"\n      family: "ணை"\n    - pdf_page: 28\n      source_supported_unicode: "காதலை நான்"\n      family: "லை / னா"\n    - pdf_page: 29\n      source_supported_unicode: "அணா"\n      family: "ணா"\n'''
extra = '''  batch_030_034_consequential_decodings:\n    - pdf_page: 31\n      source_supported_unicode: "தவறான"\n      family: "றா"\n    - pdf_page: 31\n      source_supported_unicode: "இவனை"\n      family: "னை"\n    - pdf_page: 32\n      source_supported_unicode: "அவனை / ஜமீனையே"\n      family: "னை"\n    - pdf_page: 34\n      source_supported_unicode: "அவளை"\n      family: "ளை"\n    - pdf_page: 34\n      source_supported_unicode: "பஞ்சணை"\n      family: "ணை"\n'''
if "batch_030_034_consequential_decodings" not in text:
    if insert_after not in text:
        raise SystemExit("Metadata PDF25-29 decoding block missing")
    text = text.replace(insert_after, insert_after + extra, 1)
text = sub_once(text, r'next_action: ".*?"\n', f'next_action: "{NEXT}"\n')
write_if_changed(path, text)

# Work README.
path = ROOT / "works/naam/README.md"
text = path.read_text(encoding="utf-8")
text = text.replace("PDF 5–29 / 25 of 67 pages", "PDF 5–34 / 30 of 67 pages")
text = text.replace("25 pages checked / 0 final-verified", "30 pages checked / 0 final-verified")
text = text.replace("`transcription/parts/pdf-025-029.md`", "`transcription/parts/pdf-025-029.md`, `transcription/parts/pdf-030-034.md`", 1)
text = text.replace("Current textual notes: `notes/textual-notes-pdf-025-029.md`", "Current textual notes: `notes/textual-notes-pdf-030-034.md`")
text = text.replace("PDF **5–29** has now been transcribed as source-order draft material in five five-page batches. The newest batch contains `காட்சி 12`, `காட்சி 13`, and opens `காட்சி 14`.", "PDF **5–34** has now been transcribed as source-order draft material in six five-page batches. The newest batch continues `காட்சி 14`, contains `காட்சி 15–19`, and opens `காட்சி 20`.")
text = text.replace("PDF 10–29 adds **0** new uncertainty markers", "PDF 10–34 adds **0** new uncertainty markers")
text = text.replace("**0** of the twenty-five first-pass pages are called verified yet.", "**0** of the thirty first-pass pages are called verified yet.")
marker = "- PDF 29 `அணா` is a positive historical-`ணா` case;\n"
if "PDF 31 `தவறான`" not in text:
    text = text.replace(marker, marker + "- PDF 31 `தவறான` is checked historical `றா`; PDF 31 `இவனை` and PDF 32 `அவனை` / `ஜமீனையே` are checked historical `னை`;\n- PDF 34 `அவளை` is checked historical `ளை`; PDF 34 `பஞ்சணை` is checked historical `ணை`;\n", 1)
text = text.replace("PDF 20–29 introduces no newly distinct standalone lyric/song block.", "PDF 20–34 introduces no newly distinct standalone lyric/song block.")
text = sub_once(text, r'## Exact next activity\n\n\*\*.*?\*\*\n\Z', f'## Exact next activity\n\n**{NEXT}**\n', flags=re.S)
write_if_changed(path, text)

# Transcription README.
path = ROOT / "works/naam/transcription/README.md"
text = path.read_text(encoding="utf-8")
text = text.replace("PDF 5–29 / 25 pages", "PDF 5–34 / 30 pages")
text = text.replace("25/67", "30/67", 1)
text = text.replace("`parts/pdf-025-029.md`;", "`parts/pdf-025-029.md`, `parts/pdf-030-034.md`;", 1)
text = text.replace("current batch: `parts/pdf-025-029.md`", "current batch: `parts/pdf-030-034.md`")
text = text.replace("PDF 6–29: visible printed numerals 6–29", "PDF 6–34: visible printed numerals 6–34")
text = text.replace("PDF 10–29 introduced **0 new explicit uncertainty markers**.", "PDF 10–34 introduced **0 new explicit uncertainty markers**.")
if "## PDF 30–34 source decisions" not in text:
    insertion = '''\n## PDF 30–34 source decisions\n\nThe sixth batch continues `காட்சி 14`, contains `காட்சி 15–19`, and opens `காட்சி 20`.\n\nSource-specific decisions include:\n\n- PDF 30 retains `பேசிக் கிடாததே தவறு!`, `கூலி கேட்டா உதையா!`, and the boxing-fighter transition;\n- PDF 31 `தவறான` is a checked historical-`றா` case and `இவனை` is checked historical `னை`;\n- PDF 32 preserves `குற்ற மாச்சுதுங்களே...`; `அவனை` / `ஜமீனையே` are checked historical `னை`;\n- PDF 32→33 preserves the physical cross-page split `சொந்த` / `மாக்குவேன்.`;\n- PDF 33 preserves abbreviated role labels `ஜீவா`, `கும`, `மாத்` and source `மாத்திரை` / `தைலம்`;\n- PDF 34 preserves the unlabeled `எல்லோரும் இருங்கள்!...`, source `அங்கே மீனு இருந்தாள்`, `அவளை`, and `பஞ்சணை`;\n- PDF 30–34 introduced **0 new explicit uncertainty markers** and no new standalone song/lyric block.\n\nSee `../notes/textual-notes-pdf-030-034.md` for the batch decision log.\n'''
    text = text.replace("\n## Performance / lyric evidence encountered so far\n", insertion + "\n## Performance / lyric evidence encountered so far\n", 1)
text = text.replace("PDF 20–29 introduces no newly distinct standalone song/lyric block.", "PDF 20–34 introduces no newly distinct standalone song/lyric block.")
text = sub_once(text, r'## Next activity\n\n\*\*.*?\*\*.*?\n\Z', f'## Next activity\n\n**{NEXT}**\n', flags=re.S)
write_if_changed(path, text)

# Historical glyph audit.
path = ROOT / "works/naam/notes/historical-glyph-audit.md"
text = path.read_text(encoding="utf-8")
text = text.replace("| PDF 25–29 | 5 | 5 | 0 | 5 | partial-first-pass |\n| PDF 30–71 | 42 | 0 | 0 | 0 | not-started |\n| **Total** | **67** | **25** | **0** | **25** | **partial-first-pass** |", "| PDF 25–29 | 5 | 5 | 0 | 5 | partial-first-pass |\n| PDF 30–34 | 5 | 5 | 0 | 5 | partial-first-pass |\n| PDF 35–71 | 37 | 0 | 0 | 0 | not-started |\n| **Total** | **67** | **30** | **0** | **30** | **partial-first-pass** |")
rows = '''| 31 | 31 | historical `றா` cluster | `தவறான` | `றா` | enlarged source pixels | draft-supported |\n| 31 | 31 | historical `னை` cluster | `இவனை` | `னை` | enlarged source pixels | draft-supported |\n| 32 | 32 | historical `னை` clusters | `அவனை` / `ஜமீனையே` | `னை` | enlarged source pixels | draft-supported |\n| 34 | 34 | historical `ளை` cluster | `அவளை` | `ளை` | enlarged source pixels | draft-supported |\n| 34 | 34 | historical `ணை` cluster | `பஞ்சணை` | `ணை` | enlarged source pixels | draft-supported |\n'''
if "| 31 | 31 | historical `றா` cluster" not in text:
    anchor = "| 29 | 29 | historical `ணா` cluster in payment wording | `அணா` | `ணா` | enlarged source pixels; repeated source occurrence | draft-supported |\n"
    if anchor not in text:
        raise SystemExit("Glyph audit table anchor missing")
    text = text.replace(anchor, anchor + rows, 1)
if "## PDF 30–34 glyph/text findings" not in text:
    section = '''\n## PDF 30–34 glyph/text findings\n\n- PDF 31 `தவறான` is a source-backed historical-`றா` decoding;\n- PDF 31 `இவனை` and PDF 32 `அவனை` / `ஜமீனையே` are checked historical-`னை` cases;\n- PDF 34 `அவளை` is a checked historical-`ளை` case;\n- PDF 34 `பஞ்சணை` is a checked historical-`ணை` case;\n- PDF 32 source `குற்ற மாச்சுதுங்களே...`, PDF 33 source `மாத்திரை` / `தைலம்`, and PDF 34 source `அங்கே மீனு இருந்தாள்` remain unmodernized first-pass readings;\n- PDF 30–34 introduced **0 new explicit uncertainty markers**.\n\nThe non-glyph items above are source-fidelity decisions and do not create replacement rules.\n'''
    text = text.replace("\n## Source-irregular forms retained\n", section + "\n## Source-irregular forms retained\n", 1)
text = text.replace("PDF 20–29 introduces no newly distinct standalone lyric/song structure.", "PDF 20–34 introduces no newly distinct standalone lyric/song structure.")
text = text.replace("PDF 10–29 introduced **0 new explicit uncertainty markers**.", "PDF 10–34 introduced **0 new explicit uncertainty markers**.")
text = sub_once(text, r'## Next activity\n\n.*?\n\Z', f'## Next activity\n\n{NEXT}\n', flags=re.S)
write_if_changed(path, text)

# Project handover.
path = ROOT / "works/naam/PROJECT_HANDOVER.md"
text = path.read_text(encoding="utf-8")
text = text.replace("PDF 5–29 / 25 of 67 pages", "PDF 5–34 / 30 of 67 pages")
text = text.replace("25/67", "30/67", 1)
text = text.replace("`transcription/parts/pdf-025-029.md`;\n", "`transcription/parts/pdf-025-029.md`;\n- `transcription/parts/pdf-030-034.md`;\n", 1)
text = text.replace("`notes/textual-notes-pdf-025-029.md`;\n", "`notes/textual-notes-pdf-025-029.md`;\n- `notes/textual-notes-pdf-030-034.md`;\n", 1)
if "### PDF 30–34" not in text:
    section = '''\n### PDF 30–34\n\n- continues scene 14, contains scenes 15–19, and opens scene 20;\n- PDF 31 `தவறான` is checked historical `றா`; `இவனை` is checked historical `னை`;\n- PDF 32 `அவனை` / `ஜமீனையே` are checked historical `னை`; the physical cross-page `சொந்த` / `மாக்குவேன்.` boundary is preserved;\n- PDF 33 preserves source `மாத்திரை` / `தைலம்` and abbreviated role labels;\n- PDF 34 preserves unlabeled speech, `அங்கே மீனு இருந்தாள்`, historical `அவளை` (`ளை`) and `பஞ்சணை` (`ணை`);\n- PDF 30–34 introduces **0** new uncertainty markers and no new standalone lyric/song block;\n- all 30 first-pass pages remain **draft / needs-review**, not verified.\n'''
    text = text.replace("\n## Historical Tamil glyph rule\n", section + "\n## Historical Tamil glyph rule\n", 1)
text = text.replace("PDF 20–29 introduces no newly distinct standalone song/lyric block.", "PDF 20–34 introduces no newly distinct standalone song/lyric block.")
text = sub_once(text, r'## Exact next activity\n\n> \*\*.*?\*\*.*?\n\Z', f'## Exact next activity\n\n> **{NEXT}**\n', flags=re.S)
write_if_changed(path, text)

# Fresh next-chat prompt.
prompt_path = ROOT / "works/naam/NEXT_CHAT_PROMPT.md"
prompt = f'''# Next Chat Prompt — நாம்\n\nContinue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/naam/`.\n\n## LIVE MAIN IS AUTHORITATIVE\n\nFetch live `main` first and preserve newer durable work.\n\nCurrent durable checkpoint when this prompt was prepared:\n\n- source intake / mapping: **complete / verified**;\n- canonical Tamil first pass: **PDF 5–34 / 30 of 67 pages**;\n- verified pages: **0**;\n- historical-glyph first-pass checked: **30/67**;\n- historical-glyph final verified: **0/67**;\n- open uncertainty markers: **2**;\n- next batch: **PDF 35–39**.\n\n## Controlling source\n\nAttach/resolve `TVA_BOK_0064201_நாம்.pdf` before source-level visual work. Recorded source identity: **72 PDF pages**, **115,948,588 bytes**, SHA-256 `{SOURCE_SHA}`, image-only; screenplay PDF **5–71**.\n\n## Mandatory startup\n\nRead completely before changing canonical text:\n\n1. `docs/CINEMA_WORKS_PROCESSING_GUIDE.md`\n2. `docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`\n3. `docs/ARCHIVAL_WORKFLOW.md`\n4. `docs/SOURCE_POLICY.md`\n5. `docs/TRANSCRIPTION_GUIDE.md`\n6. `works/naam/README.md`\n7. `works/naam/metadata.yaml`\n8. `works/naam/mapping.md`\n9. `works/naam/transcription/README.md`\n10. `works/naam/transcription/index.json`\n11. all completed `works/naam/transcription/parts/pdf-*.md` through `pdf-030-034.md`\n12. all completed `works/naam/notes/textual-notes-pdf-*.md` through `textual-notes-pdf-030-034.md`\n13. `works/naam/notes/historical-glyph-audit.md`\n14. `works/naam/PROJECT_HANDOVER.md`\n\n## Frozen first-pass batches PDF 5–34\n\nDo not redo or silently rewrite PDF 5–34 unless new direct scan evidence resolves an existing uncertainty or demonstrates a concrete transcription error. Known open uncertainties remain exactly **2**: damaged PDF 5 introductory text and one unclear PDF 9 montage word. PDF 10–34 adds no new uncertainty markers.\n\nRecent historical-glyph precedents: PDF 31 `தவறான` (`றா`) and `இவனை` (`னை`); PDF 32 `அவனை` / `ஜமீனையே` (`னை`); PDF 34 `அவளை` (`ளை`) and `பஞ்சணை` (`ணை`). These are occurrence-specific character-identity decisions, never global replacements.\n\n## Performance / lyric safeguard\n\nPDF 35–36 / `காட்சி 21` contains the already mapped lyrical block beginning `மணமில்லா மலர் நானம்மா!`. Preserve only the booklet witness. Do not infer an unprinted title, missing lyric body, or authorship from memory, film audio, web text, subtitles or another edition.\n\n## Exact next activity\n\n> **{NEXT}**\n'''
write_if_changed(prompt_path, prompt)

# Root README Naam section.
path = ROOT / "README.md"
text = path.read_text(encoding="utf-8")
section = f'''## நாம் status\n\n`TVA_BOK_0064201_நாம்.pdf` is the **active cinema source**. Intake and the 45-scene structural map are complete; canonical Tamil first-pass transcription is in progress.\n\n- source: **72 PDF pages**, image-only; SHA-256 `{SOURCE_SHA}`;\n- front matter / screenplay / back matter: **PDF 1–4 / 5–71 / 72**;\n- source-numbered scenes: **45 — காட்சி 1–45**, sequential;\n- canonical Tamil first pass: **PDF 5–34 / 30 of 67 pages**;\n- verified pages: **0**; separate visual-fidelity audit: **not-started**;\n- historical-glyph first-pass checked: **30/67**; final glyph-verified: **0/67**;\n- open source uncertainty markers: **2**, both carried from PDF 5/9; PDF 10–34 adds none;\n- newest batch: `works/naam/transcription/parts/pdf-030-034.md`;\n- PDF 31 `தவறான` / `இவனை`, PDF 32 `அவனை` / `ஜமீனையே`, and PDF 34 `அவளை` / `பஞ்சணை` were checked against the historical-glyph families;\n- PDF 30–34 introduces no newly distinct standalone song/lyric block;\n- PDF 35–36 / காட்சி 21 is the next mapped lyrical-block safeguard;\n- downstream derivatives remain blocked pending verified Tamil.\n\n**Next:** {NEXT}\n'''
text = sub_once(text, r'## நாம் status\n.*?(?=\n## ராஜா ராணி status\n)', section.rstrip(), flags=re.S)
write_if_changed(path, text)

# Registry Naam object.
path = ROOT / "data/works.json"
registry = path.read_text(encoding="utf-8")
needle = '"id":"naam"'
pos = registry.find(needle)
if pos < 0:
    pos = registry.find('"id": "naam"')
if pos < 0:
    raise SystemExit("Naam registry object not found")
start = registry.rfind("{", 0, pos)
depth = 0; in_str = False; esc = False; end = None
for i in range(start, len(registry)):
    ch = registry[i]
    if in_str:
        if esc: esc = False
        elif ch == "\\": esc = True
        elif ch == '"': in_str = False
        continue
    if ch == '"': in_str = True
    elif ch == "{": depth += 1
    elif ch == "}":
        depth -= 1
        if depth == 0:
            end = i + 1; break
if end is None:
    raise SystemExit("Naam registry object end not found")
obj = json.loads(registry[start:end])
if obj.get("source_sha256") != SOURCE_SHA:
    raise SystemExit("Naam source SHA mismatch in registry")
obj.update({
    "canonical_tamil_transcription": "partial-first-pass-through-pdf-034",
    "canonical_tamil_first_pass_pages_completed": 30,
    "canonical_tamil_first_pass_pdf_range_completed": "5-34",
    "canonical_tamil_first_pass_current_through_pdf": 34,
    "canonical_tamil_draft_pages": 30,
    "canonical_tamil_verified_pages": 0,
    "canonical_tamil_review_pages": 30,
    "canonical_tamil_open_uncertainty_markers": 2,
    "canonical_tamil_current_batch_path": "works/naam/transcription/parts/pdf-030-034.md",
    "canonical_tamil_current_textual_notes_path": "works/naam/notes/textual-notes-pdf-030-034.md",
    "historical_glyph_audit": "partial-first-pass-through-pdf-034",
    "historical_glyph_pages_checked": 30,
    "historical_glyph_pages_verified": 0,
    "pdf_30_34_new_performance_structures": 0,
    "pdf_31_historical_rraa_decoding": "தவறான",
    "pdf_31_historical_nai_decoding": "இவனை",
    "pdf_32_historical_nai_decoding": "அவனை / ஜமீனையே",
    "pdf_34_historical_llai_decoding": "அவளை",
    "pdf_34_historical_nnai_decoding": "பஞ்சணை",
    "next_action": NEXT,
})
new_obj = json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
registry = registry[:start] + new_obj + registry[end:]
json.loads(registry)
write_if_changed(path, registry)

# Master handover and status audit: bounded textual checkpoint replacements.
path = ROOT / "docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md"
text = path.read_text(encoding="utf-8")
text = re.sub(r'^- \*\*Naam / நாம்\*\* — .*?$', f'- **Naam / நாம்** — active work; intake/map complete; canonical Tamil first pass **PDF 5–34 / 30 of 67**; glyph first-pass **30/67**; verified **0/67**; 2 carried source uncertainties; next PDF 35–39. Source SHA-256 `{SOURCE_SHA}`.', text, count=1, flags=re.M)
text = text.replace("PDF 5–29 / 25 of 67", "PDF 5–34 / 30 of 67")
text = text.replace("25/67 / 0/67", "30/67 / 0/67")
text = text.replace("works/naam/transcription/parts/pdf-025-029.md", "works/naam/transcription/parts/pdf-030-034.md")
text = text.replace("works/naam/notes/textual-notes-pdf-025-029.md", "works/naam/notes/textual-notes-pdf-030-034.md")
text = text.replace("PDF 25–29 adds no new uncertainty marker and no newly distinct standalone lyric/song block", "PDF 30–34 adds no new uncertainty marker and no newly distinct standalone lyric/song block")
text = re.sub(r'\*\*Exact next activity:\*\* .*?\n', f'**Exact next activity:** {NEXT}\n', text, count=1)
write_if_changed(path, text)

path = ROOT / "docs/STATUS_CONSISTENCY_AUDIT.md"
text = path.read_text(encoding="utf-8")
text = re.sub(r'^\| Naam / நாம் \|.*?$', '| Naam / நாம் | intake/map complete; first pass **PDF 5–34 / 30 of 67**, 0 verified | 45 source-numbered scenes mapped; derivatives blocked | not-started | not-started |', text, count=1, flags=re.M)
text = text.replace("PDF 5–29 / 25 of 67 pages", "PDF 5–34 / 30 of 67 pages")
text = text.replace("25 / 0", "30 / 0", 1)
text = text.replace("works/naam/transcription/parts/pdf-025-029.md", "works/naam/transcription/parts/pdf-030-034.md")
text = text.replace("works/naam/notes/textual-notes-pdf-025-029.md", "works/naam/notes/textual-notes-pdf-030-034.md")
text = re.sub(r'\*\*Next production phase:\*\* .*?\n', f'**Next production phase:** {NEXT}\n', text, count=1)
write_if_changed(path, text)

print("Changed files:")
for item in changed:
    print(f"- {item}")
