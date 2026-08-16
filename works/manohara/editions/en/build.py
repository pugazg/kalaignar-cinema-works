#!/usr/bin/env python3
"""Build and QA the provenance-safe Manohara English reader/export edition."""

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
WORK = ROOT / "works" / "manohara"
TRANSLATIONS = WORK / "translations"
INDEX_PATH = TRANSLATIONS / "index.json"
DIALOGUES = WORK / "dialogues" / "records"
SONG_INVENTORY_PATH = WORK / "songs" / "inventory.json"
OUT_DIR = WORK / "editions" / "en"

SCENES = list(range(1, 58))
EXPECTED_UNITS = 1190
EXPECTED_KINDS = {
    "dialogue": 1009,
    "stage-direction": 173,
    "song-reference": 6,
    "chant": 1,
    "written-text": 1,
}
EXPECTED_DIALOGUE_RECORDS = 983
EXPECTED_DIRECT_UNLABELLED = 27
EXPECTED_CROSS_PAGE = 17
EXPECTED_SONG_OCCURRENCES = 6
SOURCE_SHA256 = "87518fd8c290d7880aa2ddd9f2b5999c9d421d48fe1f02d61cf8e254393236a9"
UNIT_RE = re.compile(r"^manohara-en-s\d{3}-u\d{3}$")
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


def dialogue_records(scene: int) -> list[dict[str, Any]]:
    path = DIALOGUES / f"scene-{scene:03d}.json"
    ensure(path.exists(), f"Missing dialogue shard {path.relative_to(ROOT)}")
    data = load_json(path)
    records = data if isinstance(data, list) else data.get("records") if isinstance(data, dict) else None
    ensure(isinstance(records, list), f"Malformed dialogue shard {path.relative_to(ROOT)}")
    return records


def render_markdown(records: list[dict[str, Any]]) -> str:
    out = [
        "# Manohara — English Reader Edition", "",
        "**Tamil title:** மனோகரா  ",
        "**Status:** complete-verified source-linked English derivative  ",
        "**English authority:** `works/manohara/translations/records/`  ",
        f"**Source scan SHA-256:** `{SOURCE_SHA256}`", "",
        "> Editorial note: The source booklet prints no scene numbers. The 57 headings below are archival navigation segments only. This edition concatenates the 1,190 verified English units without rewriting them. Exact Tamil speaker labels remain visible for source-labelled speech; source-unlabelled speech remains unlabelled. Decorative structural stars are not converted into invented prose.", "",
        "## Contents", "",
        *[f"- [Archival scene {scene}](#archival-scene-{scene})" for scene in SCENES], "", "---", "",
    ]
    labels = {
        "song-reference": "Song / performance reference",
        "chant": "Chant / proclamation",
        "written-text": "Written text",
    }
    for record in records:
        scene = record["archival_scene_ordinal"]
        out.extend([f"## Archival scene {scene}", ""])
        for unit in record["units"]:
            uid, kind, source = unit["id"], unit["kind"], unit["source"]
            text, lines = translation_payload(unit)
            out.append(f"<!-- unit:{uid}; source:{page_label(source['page_provenance'])} -->")
            if kind == "dialogue":
                if source.get("speaker_label"):
                    out.append(f"**{source['speaker_label']}**  ")
                out.extend([text, ""])
            elif kind == "stage-direction":
                out.extend([f"*{text}*", ""])
            else:
                out.append(f"*{labels[kind]}*  ")
                if lines:
                    out.extend([*(f"> {line}  " for line in lines), ""])
                else:
                    out.extend([f"> {text}", ""])
        out.extend(["---", ""])
    return "\n".join(out).rstrip() + "\n"


def render_html(records: list[dict[str, Any]]) -> str:
    nav = " ".join(f'<a href="#archival-scene-{scene}">{scene}</a>' for scene in SCENES)
    sections: list[str] = []
    labels = {
        "song-reference": "Song / performance reference",
        "chant": "Chant / proclamation",
        "written-text": "Written text",
    }
    for record in records:
        scene = record["archival_scene_ordinal"]
        body = [f'<section class="scene" id="archival-scene-{scene}"><h2>Archival scene {scene}</h2>']
        for unit in record["units"]:
            uid, kind, source = unit["id"], unit["kind"], unit["source"]
            text, _ = translation_payload(unit)
            content = html.escape(text).replace("\n", "<br>")
            attrs = f'data-unit-id="{html.escape(uid, quote=True)}" data-source-page="{html.escape(page_label(source["page_provenance"]), quote=True)}"'
            if kind == "dialogue":
                speaker = source.get("speaker_label")
                lead = f'<span class="speaker">{html.escape(speaker)}</span>' if isinstance(speaker, str) and speaker else ""
                body.append(f'<p class="unit dialogue" {attrs}>{lead}<span>{content}</span></p>')
            elif kind == "stage-direction":
                body.append(f'<p class="unit stage" {attrs}>{content}</p>')
            else:
                body.append(f'<div class="unit special" {attrs}><strong>{html.escape(labels[kind])}</strong><p>{content}</p></div>')
        body.append('<p class="back"><a href="#contents">Back to contents</a></p></section>')
        sections.append("\n".join(body))
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Manohara — English Reader Edition</title>
<style>body{{font-family:ui-serif,Georgia,"Times New Roman",serif;max-width:56rem;margin:auto;padding:2rem 1.25rem 5rem;line-height:1.65}}nav{{display:flex;flex-wrap:wrap;gap:.5rem;margin:1.5rem 0}}.scene{{border-top:1px solid;margin-top:2.5rem;padding-top:1rem}}.dialogue{{display:grid;grid-template-columns:minmax(5rem,8rem) 1fr;gap:.75rem}}.dialogue:not(:has(.speaker)){{display:block}}.speaker{{font-weight:700}}.stage{{font-style:italic}}.special{{margin:1rem 0 1rem 1rem;border-left:2px solid;padding-left:1rem}}@media(max-width:36rem){{.dialogue{{display:block}}.speaker{{display:block}}}}@media print{{nav,.back{{display:none}}.scene{{break-before:page}}}}</style>
</head><body><h1>Manohara — English Reader Edition</h1><p><strong>Tamil title:</strong> மனோகரா</p><p><strong>Status:</strong> complete-verified source-linked English derivative</p><p><strong>Editorial note:</strong> The source booklet prints no scene numbers. These 57 headings are archival navigation segments only. This edition concatenates the {EXPECTED_UNITS:,} verified English units without rewriting them. Exact Tamil speaker labels remain visible for source-labelled speech; source-unlabelled speech remains unlabelled.</p><h2 id="contents">Contents</h2><nav>{nav}</nav>{''.join(sections)}</body></html>\n'''


def main() -> int:
    index = load_json(INDEX_PATH)
    ensure(index.get("status") == "complete-verified", "Translation index is not complete-verified")
    ensure(index.get("translation_units") == EXPECTED_UNITS, "Translation unit total differs from reader checkpoint")
    ensure(index.get("unit_status_counts") == {"draft": 0, "review": 0, "verified": EXPECTED_UNITS}, "Translation status totals differ")
    ensure(index.get("unit_kind_counts") == EXPECTED_KINDS, "Translation kind totals differ")
    ensure(index.get("scenes_started") == SCENES and index.get("scenes_verified") == SCENES, "Scene coverage differs from 1-57")
    ensure(index.get("scenes_in_review") == [], "A scene remains in review")
    meta = index.get("scene_records")
    ensure(isinstance(meta, list) and [x.get("archival_scene_ordinal") for x in meta] == SCENES, "Scene record index is incomplete or unordered")

    dialogue_by_id: dict[str, dict[str, Any]] = {}
    dialogue_paths: list[Path] = []
    for scene in SCENES:
        path = DIALOGUES / f"scene-{scene:03d}.json"
        dialogue_paths.append(path)
        for rec in dialogue_records(scene):
            rid = rec.get("id")
            ensure(isinstance(rid, str) and rid not in dialogue_by_id, f"Bad or duplicate dialogue id {rid!r}")
            dialogue_by_id[rid] = rec
    ensure(len(dialogue_by_id) == EXPECTED_DIALOGUE_RECORDS, f"Expected {EXPECTED_DIALOGUE_RECORDS} immutable dialogue records")

    song_inventory = load_json(SONG_INVENTORY_PATH)
    song_ids = {r.get("id") for r in song_inventory.get("records", []) if isinstance(r, dict) and isinstance(r.get("id"), str)}
    direct_expected = index.get("source_linked_unlabelled_spoken_units")
    ensure(isinstance(direct_expected, list) and len(direct_expected) == EXPECTED_DIRECT_UNLABELLED, "Source-unlabelled spoken-unit index differs")

    units_seen: set[str] = set()
    dialogue_links: list[str] = []
    occurrence_links: list[str] = []
    direct_seen: list[str] = []
    cross_page: list[str] = []
    synthetic_end: list[str] = []
    kinds: Counter[str] = Counter()
    records: list[dict[str, Any]] = []
    translation_paths = [INDEX_PATH]
    previous_scene_page = 0

    for item in meta:
        scene = item["archival_scene_ordinal"]
        path = TRANSLATIONS / item["path"]
        translation_paths.append(path)
        record = load_json(path)
        records.append(record)
        ensure(record.get("scene_id") == f"manohara-s{scene:03d}" and record.get("archival_scene_ordinal") == scene and record.get("scene_status") == "verified", f"Scene {scene} record mismatch")
        units = record.get("units")
        ensure(isinstance(units, list) and record.get("unit_count") == len(units) == item.get("unit_count"), f"Scene {scene} unit_count mismatch")
        first_page = min(p["pdf_page"] for unit in units for p in unit["source"]["page_provenance"])
        ensure(first_page >= previous_scene_page, f"Scene {scene} regresses in source-page order")
        previous_scene_page = first_page
        previous_unit_page = 0

        for ordinal, unit in enumerate(units, 1):
            uid = unit.get("id")
            expected_uid = f"manohara-en-s{scene:03d}-u{ordinal:03d}"
            ensure(uid == expected_uid and isinstance(uid, str) and UNIT_RE.match(uid), f"Scene {scene} unit {ordinal} id mismatch")
            ensure(uid not in units_seen and unit.get("status") == "verified", f"Duplicate or unverified unit {uid}")
            units_seen.add(uid)
            kind = unit.get("kind")
            ensure(kind in EXPECTED_KINDS, f"Unsupported kind {kind!r} at {uid}")
            kinds[kind] += 1

            source = unit.get("source")
            ensure(isinstance(source, dict), f"Malformed source metadata at {uid}")
            provenance = source.get("page_provenance")
            ensure(isinstance(provenance, list) and provenance, f"No page provenance at {uid}")
            ensure(provenance[0]["pdf_page"] >= previous_unit_page, f"Page order regression at {uid}")
            previous_unit_page = provenance[0]["pdf_page"]
            for page in provenance:
                ensure(7 <= page.get("pdf_page", 0) <= 88 and page.get("printed_page") == page.get("pdf_page") - 1, f"Invalid page provenance at {uid}")
            if len(provenance) > 1:
                cross_page.append(uid)

            record_id = source.get("source_record_id")
            if record_id is not None:
                ensure(record_id in dialogue_by_id, f"Unknown dialogue link {record_id} at {uid}")
                immutable = dialogue_by_id[record_id]
                ensure(immutable.get("scene_id") == f"manohara-s{scene:03d}", f"Dialogue scene mismatch at {uid}")
                ensure(immutable.get("speaker_label") == source.get("speaker_label"), f"Speaker-label mismatch at {uid}")
                ensure(immutable.get("page_provenance") == provenance, f"Dialogue provenance mismatch at {uid}")
                dialogue_links.append(record_id)
            elif kind == "dialogue":
                ensure(uid in direct_expected and source.get("speaker_label") is None, f"Unindexed or labelled source-unlabelled speech at {uid}")
                direct_seen.append(uid)

            occurrence = source.get("source_occurrence_id")
            if occurrence is not None:
                ensure(occurrence in song_ids, f"Unknown song occurrence {occurrence} at {uid}")
                ensure(kind == "song-reference", f"Non-song-reference occurrence link at {uid}")
                occurrence_links.append(occurrence)

            text, _ = translation_payload(unit)
            ensure(not PLACEHOLDER_RE.search(text), f"Editorial placeholder at {uid}")
            if SYNTHETIC_END_RE.match(text):
                synthetic_end.append(uid)

    ensure(len(units_seen) == EXPECTED_UNITS, f"Expected {EXPECTED_UNITS} unique units")
    ensure(dict(kinds) == EXPECTED_KINDS, f"Kind counts differ: {dict(kinds)}")
    ensure(len(dialogue_links) == EXPECTED_DIALOGUE_RECORDS and len(set(dialogue_links)) == EXPECTED_DIALOGUE_RECORDS and set(dialogue_links) == set(dialogue_by_id), "Immutable dialogue linkage is not exactly once")
    ensure(direct_seen == direct_expected and len(direct_seen) == EXPECTED_DIRECT_UNLABELLED, "Source-unlabelled spoken units differ from index")
    ensure(cross_page == index.get("cross_page_translation_units") and len(cross_page) == EXPECTED_CROSS_PAGE, "Cross-page unit list differs from index")
    ensure(occurrence_links == index.get("translated_song_occurrences") and len(occurrence_links) == EXPECTED_SONG_OCCURRENCES and len(set(occurrence_links)) == EXPECTED_SONG_OCCURRENCES, "Song occurrence linkage differs")
    ensure(not synthetic_end, f"Synthetic scene-end units found: {synthetic_end}")

    reader = {
        "work_id": "manohara",
        "edition": "english-reader",
        "status": "complete-verified",
        "build_version": BUILD_VERSION,
        "title_ta": "மனோகரா",
        "title_en": "Manohara",
        "source_scan_sha256": SOURCE_SHA256,
        "source_scene_numbering": "none-printed",
        "archival_scene_numbering": "derivative-navigation-only",
        "translation_authority": "works/manohara/translations/records",
        "scene_count": 57,
        "translation_units": EXPECTED_UNITS,
        "unit_kind_counts": EXPECTED_KINDS,
        "immutable_dialogue_records_linked": EXPECTED_DIALOGUE_RECORDS,
        "source_unlabelled_spoken_units": direct_seen,
        "cross_page_units": cross_page,
        "song_occurrence_links": occurrence_links,
        "scenes": records,
    }

    md = render_markdown(records)
    html_text = render_html(records)
    json_text = json.dumps(reader, ensure_ascii=False, indent=2) + "\n"

    # Generated-output QA: every source-linked English unit must occur exactly once in every export.
    unit_ids = sorted(units_seen)
    md_ids = re.findall(r"<!-- unit:(manohara-en-s\d{3}-u\d{3});", md)
    html_ids = re.findall(r'data-unit-id="(manohara-en-s\d{3}-u\d{3})"', html_text)
    json_ids = [unit["id"] for scene in reader["scenes"] for unit in scene["units"]]
    ensure(len(md_ids) == EXPECTED_UNITS and len(set(md_ids)) == EXPECTED_UNITS and sorted(md_ids) == unit_ids, "Markdown unit coverage is not exact")
    ensure(len(html_ids) == EXPECTED_UNITS and len(set(html_ids)) == EXPECTED_UNITS and sorted(html_ids) == unit_ids, "HTML unit coverage is not exact")
    ensure(len(json_ids) == EXPECTED_UNITS and len(set(json_ids)) == EXPECTED_UNITS and sorted(json_ids) == unit_ids, "JSON unit coverage is not exact")
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

    qa = f"""# Manohara English Reader Edition — Whole-work QA

**Status:** PASS  
**English authority:** `works/manohara/translations/records/`  
**Source scan SHA-256:** `{SOURCE_SHA256}`

## Verified checks

- archival navigation scenes: **57/57** in source order; the booklet itself prints no scene numbers;
- English units: **1,190/1,190 unique, sequential and verified**;
- status counts: **1,190 verified / 0 review / 0 draft**;
- kind counts: **1,009 dialogue / 173 stage direction / 6 song-reference / 1 chant / 1 written-text**;
- immutable labelled dialogue records linked exactly once: **983/983**;
- source-visible unlabelled spoken units retained without invented speakers/dialogue IDs: **27**;
- song/performance occurrence links cross-checked exactly once: **6/6**;
- cross-page English units: **17**, exactly matching `translations/index.json`;
- all provenance lies inside PDF **7–88** / printed **6–87**, with `printed = PDF - 1`;
- source-only decorative stars do not survive as synthetic `(Scene ends.)` units;
- reader Markdown, standalone HTML and machine-readable JSON each contain every verified English unit exactly once;
- exact Tamil `speaker_label` values remain presentation labels only for source-labelled speech;
- no editorial placeholder token appears in reader text.

## Source-sensitive safeguards retained

Scene numbering is explicitly labelled archival rather than source numbering. Scene 11 retains its source-labelled war proclamation as a `chant` while preserving the immutable dialogue-source link. Scene 55 retains all four genuine page crossings. Scene 56 keeps four source-empty speaker lines unlabelled. Scene 57 keeps the unlabelled `Padma! Queen of my heart...` continuation inside the preceding king's source-linked unit. All six song/performance references remain limited to what the booklet prints; no absent lyric is reconstructed.

The generator writes only inside `works/manohara/editions/en/` and does not modify canonical Tamil or structured source layers.
"""
    qa_bytes = qa.encode("utf-8")
    (OUT_DIR / "QA_REPORT.md").write_bytes(qa_bytes)

    translation_input_paths = translation_paths
    validation_paths = translation_paths + dialogue_paths + [SONG_INVENTORY_PATH]
    manifest_outputs = {**outputs, "QA_REPORT.md": qa_bytes}
    manifest = {
        "work_id": "manohara",
        "edition": "english-reader",
        "status": "complete-verified",
        "build_version": BUILD_VERSION,
        "generator": "works/manohara/editions/en/build.py",
        "source_scan_sha256": SOURCE_SHA256,
        "translation_authority": "works/manohara/translations/records",
        "source_scene_numbering": "none-printed",
        "archival_scene_numbering": "derivative-navigation-only",
        "translation_input_files": len(translation_input_paths),
        "translation_input_aggregate_sha256": aggregate_sha256(translation_input_paths),
        "validation_input_files": len(validation_paths),
        "validation_input_aggregate_sha256": aggregate_sha256(validation_paths),
        "archival_scenes": SCENES,
        "translation_units": EXPECTED_UNITS,
        "unit_kind_counts": EXPECTED_KINDS,
        "immutable_dialogue_records_linked": EXPECTED_DIALOGUE_RECORDS,
        "source_unlabelled_spoken_units": direct_seen,
        "cross_page_units": cross_page,
        "song_occurrence_links": occurrence_links,
        "qa_status": "PASS",
        "outputs": {
            name: {"sha256": sha256(data), "bytes": len(data)}
            for name, data in manifest_outputs.items()
        },
    }
    (OUT_DIR / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("MANOHARA ENGLISH READER BUILD")
    print("status= PASS")
    print("scenes= 57")
    print("units= 1190")
    print("dialogue_links= 983/983 exactly once")
    print("source_unlabelled_spoken_units= 27")
    print("cross_page_units= 17")
    print("song_occurrence_links= 6/6")
    print("outputs= reader-edition.md, reader-edition.html, reader-edition.json, QA_REPORT.md, manifest.json")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except QAError as exc:
        print(f"MANOHARA ENGLISH READER BUILD\nstatus= FAIL\nerror= {exc}", file=sys.stderr)
        raise SystemExit(1)
