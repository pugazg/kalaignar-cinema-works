#!/usr/bin/env python3
"""Synchronize the Vandikkaran Magan intake/mapping checkpoint across repository status surfaces."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / "works" / "vandikkaran-magan"

NEXT = (
    "Begin canonical Tamil first-pass transcription from PDF 4 onward in source order, preserving front matter and screenplay exactly with stable PDF/printed-page anchors. "
    "Use the historical-glyph guide prospectively on every page, keep uncertain readings explicit, and do not call pages verified during first pass. "
    "No structured derivative work begins until the later separate visual-fidelity + historical-glyph verification gate closes."
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def load_json(path: Path):
    return json.loads(read(path))


def dump_json(path: Path, obj) -> None:
    write(path, json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


def upsert_marker(path: Path, marker: str, block: str) -> None:
    text = read(path)
    pattern = re.escape(marker) + r".*?(?=\n<!-- |\Z)"
    replacement = marker + "\n" + block.rstrip() + "\n"
    if marker in text:
        text, n = re.subn(pattern, replacement, text, count=1, flags=re.S)
        if not n:
            text += "\n\n" + replacement
    else:
        text += "\n\n" + replacement
    write(path, text)


def main() -> None:
    for rel in [
        "README.md",
        "metadata.yaml",
        "mapping.md",
        "notes/scene-heading-audit.md",
        "PROJECT_HANDOVER.md",
        "NEXT_CHAT_PROMPT.md",
    ]:
        assert (WORK / rel).exists(), rel

    # Structured work registry.
    path = ROOT / "data" / "works.json"
    works = load_json(path)
    entry = {
        "id": "vandikkaran-magan",
        "title_ta": "வண்டிக்காரன் மகன்",
        "source_title_ta": "வண்டிக்காரன் மகன்",
        "work_type": "film",
        "source_type": "printed_screenplay_dialogue_booklet",
        "source_identifier": "TVA_BOK_0062961",
        "source_pdf_pages": 90,
        "source_byte_size": 26391039,
        "source_sha256": "03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253",
        "original_story_credit_as_printed": "மூலக்கதை அண்ணா",
        "screenplay_dialogue_credit_as_printed": "திரைக்கதை-வசனம் கலைஞர்",
        "publisher_as_printed": "கனி பதிப்பகம் / சென்னை-34.",
        "edition_statement_as_printed": "முதற் பதிப்பு : 1978",
        "publication_year_as_printed": 1978,
        "price_as_printed": "விலை ரூ. 1-50",
        "printer_as_printed": "அச்சிட்டோர்: முரசொலி அச்சகம் சென்னை - 600 034.",
        "front_cover_pdf_page": 1,
        "title_credit_pdf_page": 2,
        "edition_price_printer_pdf_page": 3,
        "front_matter_pdf_pages": "4-5",
        "main_text_pdf_pages": "6-87",
        "main_text_printed_pages": "5-86",
        "film_credit_pdf_pages": "88-89",
        "back_cover_pdf_page": 90,
        "screenplay_pagination_formula": "printed=pdf-1",
        "film_level_song_credit_as_printed": "பாடல்கள்: கவிஞர் வாலி",
        "film_level_music_credit_as_printed": "இசை: எம். எஸ். விஸ்வநாதன்",
        "structural_mapping": "complete-verified",
        "mapping_path": "works/vandikkaran-magan/mapping.md",
        "source_numbered_scene_headings": True,
        "scene_heading_occurrences_observed": 70,
        "scene_heading_audit_path": "works/vandikkaran-magan/notes/scene-heading-audit.md",
        "scene_base_number_range": "1-56",
        "scene_combined_heading": "45-46",
        "scene_suffix_insertions": [
            "10-எ", "14-எ", "16-எ", "20-எ", "22-எ",
            "24-எ", "24-பி", "24-சி", "24-டி", "29-எ",
            "33-எ", "42-எ", "53-எ", "53-பி", "53-சி",
        ],
        "historical_glyph_guide_path": "docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md",
        "canonical_tamil_first_pass": "not-started",
        "visual_fidelity_audit": "not-started",
        "historical_glyph_audit": "not-started",
        "structured_derivatives": {
            "scene_text_derivatives": "blocked",
            "dialogue_index": "blocked",
            "character_entity_index": "blocked",
            "song_performance_authorship_gate": "not-started",
            "english_translation": "not-started",
            "reader_export": "not-started",
            "reading_room_integration": "not-started",
            "next_structured_derivative": None,
        },
        "next_action": NEXT,
    }
    existing = next((i for i, x in enumerate(works) if x.get("id") == "vandikkaran-magan"), None)
    if existing is None:
        works.append(entry)
    else:
        works[existing] = entry
    dump_json(path, works)
    assert len({x.get('id') for x in works}) == len(works)
    assert len(works) == 9, f"expected 9 registered works, got {len(works)}"

    # Root README: place the new active work before the closed Naam status when possible.
    path = ROOT / "README.md"
    text = read(path)
    section = f"""## வண்டிக்காரன் மகன் status

`TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` is the new active cinema-work source.

- source: **90 PDF pages / 26,391,039 bytes / SHA-256 `03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253`**;
- source credits: **`மூலக்கதை அண்ணா` / `திரைக்கதை-வசனம் கலைஞர்`**;
- publisher / edition: **`கனி பதிப்பகம்`, `சென்னை-34.` / `முதற் பதிப்பு : 1978`**;
- source boundaries: **PDF 4–5 foreword / PDF 6–87 screenplay-dialogue / PDF 88–89 film credits**;
- screenplay pagination: **printed = PDF − 1 / printed pp.5–86**;
- scene-heading mapping: **70 observed occurrences / COMPLETE-VERIFIED**;
- numbering structure: base **1–56**, **15 suffix insertions**, combined printed **`45-46`**;
- canonical Tamil / fidelity / structured derivatives: **NOT-STARTED / NOT-STARTED / BLOCKED**;
- historical-glyph workflow: **mandatory prospectively from first pass**.

**Next:** {NEXT}

"""
    if "## வண்டிக்காரன் மகன் status" in text:
        text = re.sub(r"## வண்டிக்காரன் மகன் status\n.*?(?=\n## |\Z)", section.rstrip() + "\n", text, count=1, flags=re.S)
    elif "## நாம் status" in text:
        text = text.replace("## நாம் status", section + "## நாம் status", 1)
    else:
        text += "\n\n" + section
    write(path, text)

    # Master handover: add a durable active checkpoint and correct the old active-work sentence if present.
    path = ROOT / "docs" / "HANDOVER_KALAIGNAR_CINEMA_WORKS.md"
    text = read(path)
    text = text.replace(
        "The current active production work is **Naam / நாம்**, beginning canonical Tamil only after its completed source-intake and structural-mapping gate.",
        "**Naam / நாம் is closed through reader/export and Reading Room payload QA PASS. The current active production work is வண்டிக்காரன் மகன், whose source intake and structural-mapping gate are now complete-verified; canonical Tamil is next.**",
    )
    if "- **Vandikkaran Magan / வண்டிக்காரன் மகன்**" not in text:
        anchor = "- **Naam / நாம்**"
        pos = text.find(anchor)
        if pos >= 0:
            line_end = text.find("\n", pos)
            text = text[:line_end+1] + "- **Vandikkaran Magan / வண்டிக்காரன் மகன்** — 90-page 1978 first-edition source; intake + structural map complete-verified; 70 source scene-heading occurrences mapped; canonical Tamil not started.\n" + text[line_end+1:]
    write(path, text)
    upsert_marker(
        path,
        "<!-- Vandikkaran Magan intake current -->",
        f"""## வண்டிக்காரன் மகன் active checkpoint

- source: `TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` — **90 pages / 26,391,039 bytes / SHA-256 `03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253`**;
- printed source roles: **`மூலக்கதை அண்ணா` / `திரைக்கதை-வசனம் கலைஞர்`**;
- first edition: **1978**; publisher: **கனி பதிப்பகம், சென்னை-34.**;
- structure: PDF 4–5 foreword; PDF 6–87 screenplay/dialogue; PDF 88–89 film credits; PDF 90 back cover;
- scene-heading mapping: **70/70 observed occurrences**, including 15 suffix insertions and combined `45-46`;
- canonical Tamil: **NOT-STARTED**; later derivatives: **BLOCKED**;
- source film credits include `பாடல்கள்: கவிஞர் வாலி`; item-level occurrence mapping remains deferred to the song gate.

**Exact next activity:** {NEXT}
""",
    )

    # Status consistency audit: register ninth work and add a current matrix row / durable current marker.
    path = ROOT / "docs" / "STATUS_CONSISTENCY_AUDIT.md"
    text = read(path)
    text = text.replace("all **eight registered works**", "all **nine registered works**")
    if "| Vandikkaran Magan / வண்டிக்காரன் மகன் |" not in text:
        matrix_row = "| Vandikkaran Magan / வண்டிக்காரன் மகன் | intake + structural map **complete-verified**; canonical Tamil not started | 70 observed source scene headings mapped; derivatives blocked | not-started | not-started |\n"
        naam_row = re.search(r"^\| Naam / நாம் \|.*$", text, flags=re.M)
        if naam_row:
            text = text[:naam_row.end()] + "\n" + matrix_row.rstrip() + text[naam_row.end():]
    write(path, text)
    upsert_marker(
        path,
        "<!-- Vandikkaran Magan intake current -->",
        f"""**Current active work:** **வண்டிக்காரன் மகன்**. Source intake and structural mapping are synchronized **COMPLETE-VERIFIED**: 90-page image-only 1978 first-edition source, screenplay PDF 6–87 / printed pp.5–86, and **70 observed source scene-heading occurrences** including suffix insertions and combined `45-46`. Canonical Tamil is **NOT-STARTED** and every downstream derivative remains blocked/not-started. The source-visible film-level lyric credit `பாடல்கள்: கவிஞர் வாலி` is metadata only until the item-level song/performance gate. **Next:** {NEXT}
""",
    )

    print(json.dumps({
        "status": "PASS",
        "registered_works": len(works),
        "active_work": "vandikkaran-magan",
        "source_intake": "complete",
        "structural_mapping": "complete-verified",
        "scene_heading_occurrences": 70,
        "canonical_tamil": "not-started",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
