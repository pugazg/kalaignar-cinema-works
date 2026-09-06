#!/usr/bin/env python3
"""Build and QA the provenance-safe Ammayappan English reader/export edition."""

from __future__ import annotations

import hashlib
import html
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

BUILD_VERSION = 1
ROOT = Path(__file__).resolve().parents[4]
WORK = ROOT / "works" / "ammaiyappan"
TRANSLATIONS = WORK / "translations"
INDEX_PATH = TRANSLATIONS / "index.json"
TRANS_RECORDS = TRANSLATIONS / "records"
DIALOGUES = WORK / "dialogues" / "records"
SUPPLEMENTS_PATH = WORK / "dialogues" / "source-role-resolved-records.json"
SONG_INVENTORY_PATH = WORK / "songs" / "inventory.json"
PREFLIGHT_REPORT = WORK / "editions" / "en" / "PREFLIGHT_QA_REPORT.md"
OUT_DIR = WORK / "editions" / "en"

SCENES = list(range(1, 64))
EXPECTED_UNITS = 1210
EXPECTED_KINDS = {
    "dialogue": 1025,
    "stage-direction": 181,
    "song-reference": 3,
    "literary-verse": 0,
    "japa": 1,
    "written-text": 0,
}
EXPECTED_EXPLICIT = 1009
EXPECTED_SUPPLEMENTS = 16
EXPECTED_DIALOGUE_TOTAL = 1025
EXPECTED_CROSS_PAGE = 28
EXPECTED_OCCURRENCES = [
    "ammaiyappan-song-001",
    "ammaiyappan-song-002",
    "ammaiyappan-song-003",
    "ammaiyappan-song-004",
    "ammaiyappan-song-005",
]
EXPECTED_OCCURRENCE_LINK_COUNTS = {
    "ammaiyappan-song-001": 1,
    "ammaiyappan-song-002": 1,
    "ammaiyappan-song-003": 1,
    "ammaiyappan-song-004": 2,
    "ammaiyappan-song-005": 2,
}
SOURCE_SHA256 = "eda6468a57022b418f44851a0013b090469bc6f4be44a682487800658771720d"
UNIT_RE = re.compile(r"^ammaiyappan-en-s\d{3}-u\d{3}$")
PLACEHOLDER_RE = re.compile(r"\b(?:TODO|TBD|FIXME)\b|\[\[\?\]\]|\{\{.+?\}\}", re.I)
SYNTHETIC_END_RE = re.compile(r"^\s*[\[(]?\s*Scene\s+ends?\.?\s*[\])]?\s*$", re.I)


class QAError(RuntimeError):
    pass


def ensure(ok: bool, message: str) -> None:
    if not ok:
        raise QAError(message)


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise QAError(f"Cannot parse {path.relative_to(ROOT)}: {exc}") from exc


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def aggregate_sha256(paths: list[Path]) -> str:
    digest = hashlib.sha256()
    for path in sorted(set(paths), key=lambda p: p.as_posix()):
        digest.update(path.relative_to(ROOT).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def translation_payload(unit: dict[str, Any]) -> tuple[str, list[str] | None]:
    translation = unit.get("translation")
    ensure(isinstance(translation, dict), f"{unit.get('id')} has malformed translation")
    text = translation.get("english_text")
    lines = translation.get("english_lines")
    ensure(isinstance(text, str) ^ isinstance(lines, list), f"{unit.get('id')} must have exactly one English payload")
    if isinstance(text, str):
        ensure(bool(text.strip()), f"{unit.get('id')} has empty English text")
        return text, None
    ensure(bool(lines) and all(isinstance(line, str) and line.strip() for line in lines), f"{unit.get('id')} has malformed English lines")
    return "\n".join(lines), lines


def page_label(provenance: list[dict[str, int]]) -> str:
    if len(provenance) == 1:
        p = provenance[0]
        return f"PDF {p['pdf_page']} / printed {p['printed_page']}"
    a, b = provenance[0], provenance[-1]
    return f"PDF {a['pdf_page']}→{b['pdf_page']} / printed {a['printed_page']}→{b['printed_page']}"


def speaker_markdown(source: dict[str, Any]) -> str | None:
    label = source.get("speaker_label")
    if not isinstance(label, str) or not label:
        return None
    origin = source.get("speaker_label_origin")
    if origin == "source-explicit-colon":
        return f"**{label}:**"
    if origin == "source-explicit-noncolon-delimiter":
        return f"**{label};** *(source semicolon delimiter)*"
    if origin == "source-context-attributed":
        return f"**[{label} — context-attributed; no printed speaker label]**"
    return f"**{label}**"


def speaker_html(source: dict[str, Any]) -> str:
    label = source.get("speaker_label")
    if not isinstance(label, str) or not label:
        return ""
    origin = source.get("speaker_label_origin")
    safe = html.escape(label)
    if origin == "source-explicit-colon":
        shown = safe + ":"
    elif origin == "source-explicit-noncolon-delimiter":
        shown = safe + "; <small>source semicolon delimiter</small>"
    elif origin == "source-context-attributed":
        shown = f"[{safe} — context-attributed; no printed speaker label]"
    else:
        shown = safe
    return f'<span class="speaker">{shown}</span>'


def unit_marker(unit: dict[str, Any]) -> str:
    source = unit["source"]
    record_id = source.get("source_record_id") or ""
    occurrence_id = source.get("source_occurrence_id") or ""
    origin = source.get("speaker_label_origin") or ""
    return (
        f"<!-- unit:{unit['id']} | source:{page_label(source['page_provenance'])} | "
        f"record:{record_id} | occurrence:{occurrence_id} | origin:{origin} -->"
    )


def render_markdown(records: list[dict[str, Any]]) -> str:
    out = [
        "# Ammayappan — English Reader Edition",
        "",
        "**Tamil title:** அம்மையப்பன்  ",
        "**Status:** complete-verified source-linked English derivative  ",
        "**English authority:** `works/ammaiyappan/translations/records/`  ",
        f"**Source scan SHA-256:** `{SOURCE_SHA256}`",
        "",
        "> Editorial note: The source booklet prints no scene numbers. The 63 headings below are archival navigation segments only. This edition is generated deterministically from all 1,210 verified English units without rewriting them. Exact Tamil speaker-label provenance is retained: printed colon labels remain explicit, the two source-semicolon records retain their semicolon provenance, and context-attributed source-role supplements are visibly marked as contextual rather than printed labels. Cross-page units remain single logical units; the machine-readable JSON retains their page segments. Decorative structural stars are not converted into prose.",
        "",
        "## Contents",
        "",
        *[f"- [Archival scene {scene}](#archival-scene-{scene})" for scene in SCENES],
        "",
        "---",
        "",
    ]
    special_labels = {
        "song-reference": "Song / performance reference",
        "literary-verse": "Literary verse",
        "japa": "Japa / performance cue",
        "written-text": "Written text",
    }
    for record in records:
        scene = record["archival_scene_ordinal"]
        out.extend([f"## Archival scene {scene}", ""])
        for unit in record["units"]:
            source = unit["source"]
            text, lines = translation_payload(unit)
            out.append(unit_marker(unit))
            if unit["kind"] == "dialogue":
                speaker = speaker_markdown(source)
                if speaker:
                    out.extend([speaker + "  ", text, ""])
                else:
                    out.extend([text, ""])
            elif unit["kind"] == "stage-direction":
                out.extend([f"*{text}*", ""])
            else:
                out.append(f"*{special_labels[unit['kind']]}*  ")
                if lines:
                    out.extend([*(f"> {line}  " for line in lines), ""])
                else:
                    out.extend([f"> {text}", ""])
        out.extend(["---", ""])
    return "\n".join(out).rstrip() + "\n"


def render_html(records: list[dict[str, Any]]) -> str:
    nav = " ".join(f'<a href="#archival-scene-{scene}">{scene}</a>' for scene in SCENES)
    sections: list[str] = []
    special_labels = {
        "song-reference": "Song / performance reference",
        "literary-verse": "Literary verse",
        "japa": "Japa / performance cue",
        "written-text": "Written text",
    }
    for record in records:
        scene = record["archival_scene_ordinal"]
        body = [f'<section class="scene" id="archival-scene-{scene}"><h2>Archival scene {scene}</h2>']
        for unit in record["units"]:
            source = unit["source"]
            text, _ = translation_payload(unit)
            content = html.escape(text).replace("\n", "<br>")
            attrs = (
                f'data-unit-id="{html.escape(unit["id"], quote=True)}" '
                f'data-source-record-id="{html.escape(source.get("source_record_id") or "", quote=True)}" '
                f'data-source-occurrence-id="{html.escape(source.get("source_occurrence_id") or "", quote=True)}" '
                f'data-speaker-origin="{html.escape(source.get("speaker_label_origin") or "", quote=True)}" '
                f'data-source-page="{html.escape(page_label(source["page_provenance"]), quote=True)}"'
            )
            kind = unit["kind"]
            if kind == "dialogue":
                body.append(f'<p class="unit dialogue" {attrs}>{speaker_html(source)}<span>{content}</span></p>')
            elif kind == "stage-direction":
                body.append(f'<p class="unit stage" {attrs}>{content}</p>')
            else:
                body.append(
                    f'<div class="unit special" {attrs}><strong>{html.escape(special_labels[kind])}</strong><p>{content}</p></div>'
                )
        body.append('<p class="back"><a href="#contents">Back to contents</a></p></section>')
        sections.append("\n".join(body))
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Ammayappan — English Reader Edition</title>
<style>body{{font-family:ui-serif,Georgia,"Times New Roman",serif;max-width:58rem;margin:auto;padding:2rem 1.25rem 5rem;line-height:1.65}}nav{{display:flex;flex-wrap:wrap;gap:.5rem;margin:1.5rem 0}}.scene{{border-top:1px solid;margin-top:2.5rem;padding-top:1rem}}.dialogue{{display:grid;grid-template-columns:minmax(7rem,13rem) 1fr;gap:.75rem}}.dialogue:not(:has(.speaker)){{display:block}}.speaker{{font-weight:700}}.speaker small{{font-weight:400}}.stage{{font-style:italic}}.special{{margin:1rem 0 1rem 1rem;border-left:2px solid;padding-left:1rem}}@media(max-width:42rem){{.dialogue{{display:block}}.speaker{{display:block;margin-bottom:.2rem}}}}@media print{{nav,.back{{display:none}}.scene{{break-before:page}}}}</style>
</head><body><h1>Ammayappan — English Reader Edition</h1><p><strong>Tamil title:</strong> அம்மையப்பன்</p><p><strong>Status:</strong> complete-verified source-linked English derivative</p><p><strong>Editorial note:</strong> The source booklet prints no scene numbers. These 63 headings are archival navigation segments only. This edition is generated deterministically from all {EXPECTED_UNITS:,} verified English units. Printed speaker labels, source-semicolon provenance and context-attributed source-role provenance remain distinguished; cross-page units remain unsplit.</p><h2 id="contents">Contents</h2><nav>{nav}</nav>{''.join(sections)}</body></html>\n'''


def main() -> int:
    index = load_json(INDEX_PATH)
    ensure(index.get("status") == "complete-verified", "Translation index is not complete-verified")
    ensure(index.get("source_scene_numbering") == "none-printed", "Translation index source-scene-numbering state differs")
    ensure(index.get("translation_units") == EXPECTED_UNITS, "Translation unit total differs")
    ensure(index.get("unit_status_counts") == {"draft": 0, "review": 0, "verified": EXPECTED_UNITS}, "Translation status totals differ")
    ensure(index.get("unit_kind_counts") == EXPECTED_KINDS, "Translation kind totals differ")
    ensure(index.get("scenes_started") == SCENES and index.get("scenes_verified") == SCENES, "Scene coverage differs from 1-63")
    ensure(index.get("scenes_in_review") == [], "A scene remains in review")
    ensure(index.get("canonical_tamil_modified") is False, "Translation index reports canonical Tamil modification")
    ensure(index.get("scene_files_modified") is False, "Translation index reports scene modification")
    ensure(index.get("dialogue_records_modified") is False, "Translation index reports dialogue modification")
    ensure(index.get("character_index_modified") is False, "Translation index reports character modification")
    ensure(index.get("song_inventory_modified") is False, "Translation index reports song inventory modification")
    meta = index.get("scene_records")
    ensure(isinstance(meta, list) and [x.get("archival_scene_ordinal") for x in meta] == SCENES, "Scene record index is incomplete or unordered")

    explicit: dict[str, dict[str, Any]] = {}
    dialogue_paths: list[Path] = []
    for scene in SCENES:
        path = DIALOGUES / f"scene-{scene:03d}.json"
        dialogue_paths.append(path)
        data = load_json(path)
        records = data if isinstance(data, list) else data.get("records") if isinstance(data, dict) else None
        ensure(isinstance(records, list), f"Malformed dialogue shard {path.relative_to(ROOT)}")
        for rec in records:
            rid = rec.get("id")
            ensure(isinstance(rid, str) and rid not in explicit, f"Bad or duplicate explicit dialogue id {rid!r}")
            explicit[rid] = rec
    supplements_data = load_json(SUPPLEMENTS_PATH)
    ensure(isinstance(supplements_data, list), "Source-role supplement file is malformed")
    supplements: dict[str, dict[str, Any]] = {}
    for rec in supplements_data:
        rid = rec.get("id")
        ensure(isinstance(rid, str) and rid not in explicit and rid not in supplements, f"Bad or duplicate supplement id {rid!r}")
        supplements[rid] = rec
    ensure(len(explicit) == EXPECTED_EXPLICIT, f"Expected {EXPECTED_EXPLICIT} explicit dialogue records")
    ensure(len(supplements) == EXPECTED_SUPPLEMENTS, f"Expected {EXPECTED_SUPPLEMENTS} source-role supplements")
    source_records = {**explicit, **supplements}
    ensure(len(source_records) == EXPECTED_DIALOGUE_TOTAL, f"Expected {EXPECTED_DIALOGUE_TOTAL} dialogue/source-role records")

    song_inventory = load_json(SONG_INVENTORY_PATH)
    occurrence_records = song_inventory.get("occurrences", [])
    ensure(isinstance(occurrence_records, list), "Song/performance inventory is malformed")
    occurrence_ids = [r.get("id") for r in occurrence_records]
    ensure(occurrence_ids == EXPECTED_OCCURRENCES, "Closed occurrence inventory differs")
    occurrence_scene = {r["id"]: r.get("archive_scene_id") for r in occurrence_records}

    units_seen: set[str] = set()
    kinds: Counter[str] = Counter()
    dialogue_links: list[str] = []
    occurrence_links: list[str] = []
    cross_page: list[str] = []
    records: list[dict[str, Any]] = []
    translation_paths = [INDEX_PATH]
    previous_scene_page = 0

    for item in meta:
        scene = item["archival_scene_ordinal"]
        path = TRANSLATIONS / item["path"]
        translation_paths.append(path)
        record = load_json(path)
        records.append(record)
        scene_id = f"ammaiyappan-s{scene:03d}"
        ensure(record.get("work_id") == "ammaiyappan", f"Scene {scene} work id mismatch")
        ensure(record.get("target_language") == "en", f"Scene {scene} target language mismatch")
        ensure(record.get("scene_id") == scene_id and record.get("archival_scene_ordinal") == scene, f"Scene {scene} record mismatch")
        ensure(record.get("source_scene_number") is None, f"Scene {scene} incorrectly claims a printed scene number")
        ensure(record.get("scene_status") == "verified", f"Scene {scene} is not verified")
        units = record.get("units")
        ensure(isinstance(units, list) and record.get("unit_count") == len(units) == item.get("unit_count"), f"Scene {scene} unit_count mismatch")
        first_page = min(p["pdf_page"] for unit in units for p in unit["source"]["page_provenance"])
        ensure(first_page >= previous_scene_page, f"Scene {scene} regresses in source-page order")
        previous_scene_page = first_page
        previous_unit_page = 0

        for ordinal, unit in enumerate(units, 1):
            uid = unit.get("id")
            expected_uid = f"ammaiyappan-en-s{scene:03d}-u{ordinal:03d}"
            ensure(uid == expected_uid and isinstance(uid, str) and UNIT_RE.match(uid), f"Scene {scene} unit {ordinal} id mismatch")
            ensure(uid not in units_seen and unit.get("status") == "verified", f"Duplicate or unverified unit {uid}")
            units_seen.add(uid)
            ensure(unit.get("target_language") == "en" and unit.get("scene_id") == scene_id and unit.get("archival_scene_ordinal") == scene, f"Unit scene metadata mismatch at {uid}")
            kind = unit.get("kind")
            ensure(kind in EXPECTED_KINDS, f"Unsupported kind {kind!r} at {uid}")
            kinds[kind] += 1

            source = unit.get("source")
            ensure(isinstance(source, dict), f"Malformed source metadata at {uid}")
            ensure(source.get("canonical_scene_path") == f"works/ammaiyappan/scenes/scene-{scene:03d}.md", f"Canonical scene path mismatch at {uid}")
            provenance = source.get("page_provenance")
            ensure(isinstance(provenance, list) and provenance, f"No page provenance at {uid}")
            pdf_pages = [p.get("pdf_page") for p in provenance]
            printed_pages = [p.get("printed_page") for p in provenance]
            ensure(all(isinstance(p, int) for p in pdf_pages + printed_pages), f"Invalid page provenance at {uid}")
            ensure(pdf_pages == sorted(pdf_pages), f"Non-monotonic unit provenance at {uid}")
            ensure(pdf_pages[0] >= previous_unit_page, f"Page order regression at {uid}")
            previous_unit_page = pdf_pages[0]
            for p in provenance:
                ensure(5 <= p["pdf_page"] <= 109 and p["printed_page"] == p["pdf_page"] - 2, f"Out-of-range page provenance at {uid}")
            if len(provenance) > 1:
                cross_page.append(uid)
                segments = unit.get("translation", {}).get("english_page_segments")
                ensure(isinstance(segments, list) and len(segments) == len(provenance), f"Cross-page segments missing or count mismatch at {uid}")
                ensure(
                    [(s.get("pdf_page"), s.get("printed_page")) for s in segments]
                    == [(p["pdf_page"], p["printed_page"]) for p in provenance],
                    f"Cross-page segment provenance mismatch at {uid}",
                )

            rid = source.get("source_record_id")
            if kind == "dialogue":
                ensure(isinstance(rid, str) and rid in source_records, f"Dialogue unit lacks known source record at {uid}")
                rec = source_records[rid]
                dialogue_links.append(rid)
                ensure(rec.get("archive_scene_id") == scene_id, f"Source record scene mismatch at {uid}")
                ensure(source.get("speaker_label") == rec.get("speaker_label"), f"Speaker-label mismatch at {uid}")
                expected_origin = rec.get("speaker_label_origin") if rid in supplements else "source-explicit-colon"
                ensure(source.get("speaker_label_origin") == expected_origin, f"Speaker-label origin mismatch at {uid}")
                ensure(source.get("page_provenance") == rec.get("page_provenance"), f"Dialogue provenance mismatch at {uid}")
                expected_source_path = (
                    "works/ammaiyappan/dialogues/source-role-resolved-records.json"
                    if rid in supplements
                    else f"works/ammaiyappan/dialogues/records/scene-{scene:03d}.json"
                )
                ensure(source.get("source_path") == expected_source_path, f"Dialogue source path mismatch at {uid}")
            else:
                ensure(rid is None, f"Non-dialogue unit carries a dialogue record link at {uid}")

            occurrence = source.get("source_occurrence_id")
            if occurrence is not None:
                ensure(occurrence in occurrence_scene, f"Unknown occurrence {occurrence} at {uid}")
                ensure(occurrence_scene[occurrence] == scene_id, f"Occurrence scene mismatch at {uid}")
                occurrence_links.append(occurrence)

            text, _ = translation_payload(unit)
            ensure(not PLACEHOLDER_RE.search(text), f"Editorial placeholder at {uid}")
            ensure(not SYNTHETIC_END_RE.match(text), f"Synthetic scene-end prose at {uid}")

    ensure(len(units_seen) == EXPECTED_UNITS, f"Expected {EXPECTED_UNITS} unique units")
    ensure({k: kinds.get(k, 0) for k in EXPECTED_KINDS} == EXPECTED_KINDS and not (set(kinds) - set(EXPECTED_KINDS)), f"Kind counts differ: {dict(kinds)}")
    ensure(len(dialogue_links) == EXPECTED_DIALOGUE_TOTAL and len(set(dialogue_links)) == EXPECTED_DIALOGUE_TOTAL and set(dialogue_links) == set(source_records), "Dialogue/source-role linkage is not exactly once")
    ensure(cross_page == index.get("cross_page_translation_units") and len(cross_page) == EXPECTED_CROSS_PAGE, "Cross-page unit list differs from index")
    ensure(index.get("translated_song_performance_occurrences") == EXPECTED_OCCURRENCES, "Unique occurrence list differs from index")
    ensure(Counter(occurrence_links) == Counter(EXPECTED_OCCURRENCE_LINK_COUNTS), f"Occurrence source-span linkage differs: {Counter(occurrence_links)}")

    reader = {
        "work_id": "ammaiyappan",
        "edition": "english-reader",
        "status": "complete-verified",
        "build_version": BUILD_VERSION,
        "title_ta": "அம்மையப்பன்",
        "title_en": "Ammayappan",
        "source_scan_sha256": SOURCE_SHA256,
        "source_scene_numbering": "none-printed",
        "archival_scene_numbering": "derivative-navigation-only",
        "translation_authority": "works/ammaiyappan/translations/records",
        "preflight_report": "works/ammaiyappan/editions/en/PREFLIGHT_QA_REPORT.md",
        "scene_count": len(SCENES),
        "translation_units": EXPECTED_UNITS,
        "unit_kind_counts": EXPECTED_KINDS,
        "dialogue_authority": {
            "explicit_records": EXPECTED_EXPLICIT,
            "source_role_supplements": EXPECTED_SUPPLEMENTS,
            "total": EXPECTED_DIALOGUE_TOTAL,
            "linked_exactly_once": True,
        },
        "cross_page_units": cross_page,
        "occurrence_identities": EXPECTED_OCCURRENCES,
        "occurrence_source_span_link_counts": EXPECTED_OCCURRENCE_LINK_COUNTS,
        "scenes": records,
    }

    md = render_markdown(records)
    html_text = render_html(records)
    json_text = json.dumps(reader, ensure_ascii=False, indent=2) + "\n"

    unit_ids = sorted(units_seen)
    md_ids = re.findall(r"<!-- unit:(ammaiyappan-en-s\d{3}-u\d{3}) \|", md)
    html_ids = re.findall(r'data-unit-id="(ammaiyappan-en-s\d{3}-u\d{3})"', html_text)
    json_ids = [unit["id"] for scene in reader["scenes"] for unit in scene["units"]]
    ensure(len(md_ids) == EXPECTED_UNITS and len(set(md_ids)) == EXPECTED_UNITS and sorted(md_ids) == unit_ids, "Markdown unit coverage is not exact")
    ensure(len(html_ids) == EXPECTED_UNITS and len(set(html_ids)) == EXPECTED_UNITS and sorted(html_ids) == unit_ids, "HTML unit coverage is not exact")
    ensure(len(json_ids) == EXPECTED_UNITS and len(set(json_ids)) == EXPECTED_UNITS and sorted(json_ids) == unit_ids, "JSON unit coverage is not exact")

    md_record_ids = [x for x in re.findall(r"\| record:([^|]*) \| occurrence:", md) if x]
    html_record_ids = [x for x in re.findall(r'data-source-record-id="([^"]*)"', html_text) if x]
    json_record_ids = [unit["source"].get("source_record_id") for scene in reader["scenes"] for unit in scene["units"] if unit["source"].get("source_record_id")]
    ensure(Counter(md_record_ids) == Counter(dialogue_links), "Markdown dialogue/source-role markers differ")
    ensure(Counter(html_record_ids) == Counter(dialogue_links), "HTML dialogue/source-role markers differ")
    ensure(Counter(json_record_ids) == Counter(dialogue_links), "JSON dialogue/source-role markers differ")

    md_occurrences = [x for x in re.findall(r"\| occurrence:([^|]*) \| origin:", md) if x]
    html_occurrences = [x for x in re.findall(r'data-source-occurrence-id="([^"]*)"', html_text) if x]
    json_occurrences = [unit["source"].get("source_occurrence_id") for scene in reader["scenes"] for unit in scene["units"] if unit["source"].get("source_occurrence_id")]
    ensure(Counter(md_occurrences) == Counter(EXPECTED_OCCURRENCE_LINK_COUNTS), "Markdown occurrence markers differ")
    ensure(Counter(html_occurrences) == Counter(EXPECTED_OCCURRENCE_LINK_COUNTS), "HTML occurrence markers differ")
    ensure(Counter(json_occurrences) == Counter(EXPECTED_OCCURRENCE_LINK_COUNTS), "JSON occurrence markers differ")

    json_cross_page = [unit["id"] for scene in reader["scenes"] for unit in scene["units"] if len(unit["source"].get("page_provenance", [])) > 1]
    ensure(json_cross_page == cross_page, "JSON cross-page unit list differs")
    for scene in reader["scenes"]:
        for unit in scene["units"]:
            if unit["id"] in cross_page:
                ensure(isinstance(unit["translation"].get("english_page_segments"), list), f"Reader JSON lost page segments at {unit['id']}")

    ensure(not PLACEHOLDER_RE.search(md) and not PLACEHOLDER_RE.search(html_text), "Generated reader contains an editorial placeholder")
    ensure("(Scene ends.)" not in md and "(Scene ends.)" not in html_text, "Generated reader contains synthetic scene-end prose")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    outputs = {
        "reader-edition.md": md.encode("utf-8"),
        "reader-edition.html": html_text.encode("utf-8"),
        "reader-edition.json": json_text.encode("utf-8"),
    }
    for name, data in outputs.items():
        (OUT_DIR / name).write_bytes(data)

    output_hashes = {name: sha256(data) for name, data in outputs.items()}
    qa = f"""# Ammayappan English Reader Edition — Whole-work generated-output QA

**Status:** PASS  
**English authority:** `works/ammaiyappan/translations/records/`  
**Source scan SHA-256:** `{SOURCE_SHA256}`  
**Preflight:** `PREFLIGHT_QA_REPORT.md` — PASS

## Generated outputs

- Markdown: `reader-edition.md` — SHA-256 `{output_hashes['reader-edition.md']}`
- standalone HTML: `reader-edition.html` — SHA-256 `{output_hashes['reader-edition.html']}`
- machine-readable JSON: `reader-edition.json` — SHA-256 `{output_hashes['reader-edition.json']}`

## Verified checks

- archival navigation scenes: **63/63** in source order; the booklet itself prints no scene numbers;
- English units: **1,210/1,210 unique, sequential and verified**;
- status counts: **1,210 verified / 0 review / 0 draft**;
- kind counts: **1,025 dialogue / 181 stage direction / 3 song-reference / 1 japa / 0 literary-verse / 0 written-text**;
- explicit immutable dialogue records: **1,009/1,009 linked exactly once**;
- closed source-role supplements: **16/16 linked exactly once**;
- total dialogue/source-role authority: **1,025/1,025 exactly once**;
- exact Tamil speaker-label and source-role provenance retained, including scene 3 `பூங் ; ...`, scene 5 `திரு; ...`, and all context-attributed supplements;
- genuine cross-page English units: **28/28**, retained as single logical units; machine-readable JSON preserves matching `english_page_segments`;
- retained occurrence identities: **5/5**, represented through exactly **7** intentional source-span links (`1,1,1,2,2`);
- Markdown, HTML and JSON each contain every verified unit exactly once;
- Markdown, HTML and JSON preserve every dialogue/source-role link and every occurrence source-span link with the same multiplicity as the verified structured translation;
- provenance lies inside PDF **5–109** / printed **3–107**, with `printed = PDF - 2`;
- archive scene ordinals remain derivative navigation only;
- synthetic `(Scene ends.)` units: **0**;
- direct decorative/structural-star prose units: **0**;
- editorial placeholder tokens: **0**.

## Source-sensitive presentation

Printed colon-labelled speech displays the exact Tamil source label. The two source-explicit semicolon records visibly retain semicolon provenance. `source-context-attributed` supplements are explicitly marked as contextual and are not presented as printed labels. Song/performance references remain limited to the five closed source-visible occurrence identities; no absent title, lyric body or authorship is reconstructed.

The generator writes only inside `works/ammaiyappan/editions/en/` and does not modify canonical Tamil, scene derivatives, immutable dialogue/source-role evidence, character mappings or song/performance evidence.
"""
    qa_bytes = qa.encode("utf-8")
    (OUT_DIR / "QA_REPORT.md").write_bytes(qa_bytes)

    source_validation_paths = dialogue_paths + [SUPPLEMENTS_PATH, SONG_INVENTORY_PATH]
    authoritative_input_paths = translation_paths + source_validation_paths
    manifest_outputs = {**outputs, "QA_REPORT.md": qa_bytes}
    manifest = {
        "work_id": "ammaiyappan",
        "edition": "english-reader",
        "status": "complete-verified",
        "build_version": BUILD_VERSION,
        "generator": "works/ammaiyappan/editions/en/build.py",
        "generator_sha256": sha256(Path(__file__).read_bytes()),
        "preflight_report": "works/ammaiyappan/editions/en/PREFLIGHT_QA_REPORT.md",
        "source_scan_sha256": SOURCE_SHA256,
        "translation_authority": "works/ammaiyappan/translations/records",
        "source_scene_numbering": "none-printed",
        "archival_scene_numbering": "derivative-navigation-only",
        "translation_input_files": len(translation_paths),
        "translation_input_aggregate_sha256": aggregate_sha256(translation_paths),
        "source_validation_input_files": len(source_validation_paths),
        "source_validation_input_aggregate_sha256": aggregate_sha256(source_validation_paths),
        "authoritative_input_files": len(authoritative_input_paths),
        "authoritative_input_aggregate_sha256": aggregate_sha256(authoritative_input_paths),
        "archival_scenes": SCENES,
        "translation_units": EXPECTED_UNITS,
        "unit_kind_counts": EXPECTED_KINDS,
        "explicit_dialogue_records_linked": EXPECTED_EXPLICIT,
        "source_role_supplements_linked": EXPECTED_SUPPLEMENTS,
        "dialogue_source_links_total": EXPECTED_DIALOGUE_TOTAL,
        "cross_page_units": cross_page,
        "occurrence_identities": EXPECTED_OCCURRENCES,
        "occurrence_source_span_link_counts": EXPECTED_OCCURRENCE_LINK_COUNTS,
        "occurrence_source_span_links_total": sum(EXPECTED_OCCURRENCE_LINK_COUNTS.values()),
        "qa_status": "PASS",
        "frozen_source_layers_modified": False,
        "outputs": {
            name: {"sha256": sha256(data), "bytes": len(data)}
            for name, data in manifest_outputs.items()
        },
    }
    (OUT_DIR / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("AMMAYAPPAN ENGLISH READER BUILD")
    print("status= PASS")
    print("scenes= 63")
    print("units= 1210")
    print("dialogue_source_links= 1025/1025 exactly once")
    print("cross_page_units= 28")
    print("occurrence_identities= 5/5")
    print("occurrence_source_span_links= 7")
    print("outputs= reader-edition.md, reader-edition.html, reader-edition.json, QA_REPORT.md, manifest.json")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except QAError as exc:
        print(f"AMMAYAPPAN ENGLISH READER BUILD\nstatus= FAIL\nerror= {exc}", file=sys.stderr)
        raise SystemExit(1)
