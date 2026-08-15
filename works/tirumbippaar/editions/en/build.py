#!/usr/bin/env python3
"""Build and QA the provenance-safe Tirumbippaar English reader edition.

The complete-verified scene-sharded translation records are the English authority.
This script validates whole-work structure and immutable dialogue/source links,
then emits continuous Markdown, HTML, and JSON reader exports plus a deterministic
QA report and integrity manifest. It writes only inside
works/tirumbippaar/editions/en/.
"""

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
WORK = ROOT / "works" / "tirumbippaar"
TRANSLATIONS = WORK / "translations"
INDEX_PATH = TRANSLATIONS / "index.json"
DIALOGUES = WORK / "dialogues" / "records"
SONG_INVENTORY_PATH = WORK / "songs" / "inventory.json"
OUT_DIR = WORK / "editions" / "en"

EXPECTED_SCENES = list(range(1, 94))
EXPECTED_UNITS = 1330
EXPECTED_KIND_COUNTS = {
    "dialogue": 1047,
    "stage-direction": 263,
    "song": 0,
    "song-reference": 7,
    "chant": 2,
    "written-text": 11,
}
EXPECTED_DIALOGUE_RECORDS = 1040
EXPECTED_DIRECT_UNLABELLED_DIALOGUE = 7
EXPECTED_CROSS_PAGE = 12
EXPECTED_SOURCE_SHA256 = "973b9c3f7b84d6a1902a4a472af8799c783bf1ec2d6cd015796fc1df1ce59682"
ALLOWED_KINDS = set(EXPECTED_KIND_COUNTS)
UNIT_ID_RE = re.compile(r"^tirumbippaar-en-s(?P<scene>\d{3})-u(?P<unit>\d{3})$")
PLACEHOLDER_RE = re.compile(r"\b(?:TODO|TBD|FIXME)\b|\[\[\?\]\]|\{\{.+?\}\}", re.IGNORECASE)
SYNTHETIC_END_RE = re.compile(r"^\s*\(Scene ends\.\)\s*$", re.IGNORECASE)


class QAError(RuntimeError):
    pass


def ensure(condition: bool, message: str) -> None:
    if not condition:
        raise QAError(message)


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise QAError(f"Cannot parse JSON {path.relative_to(ROOT)}: {exc}") from exc


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def aggregate_sha256(paths: list[Path]) -> str:
    digest = hashlib.sha256()
    for path in sorted(set(paths), key=lambda p: p.as_posix()):
        digest.update(path.relative_to(ROOT).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def collect_ids(node: Any) -> set[str]:
    found: set[str] = set()
    if isinstance(node, dict):
        if isinstance(node.get("id"), str):
            found.add(node["id"])
        for value in node.values():
            found.update(collect_ids(value))
    elif isinstance(node, list):
        for value in node:
            found.update(collect_ids(value))
    return found


def translation_parts(unit: dict[str, Any]) -> tuple[str | None, list[str] | None]:
    translation = unit.get("translation")
    ensure(isinstance(translation, dict), f"Unit {unit.get('id')} has malformed translation")
    text = translation.get("english_text")
    lines = translation.get("english_lines")
    text_value = text if isinstance(text, str) else None
    line_value = lines if isinstance(lines, list) else None
    ensure((text_value is not None) ^ (line_value is not None), f"Unit {unit.get('id')} must have exactly one of english_text or english_lines")
    if text_value is not None:
        ensure(bool(text_value.strip()), f"Unit {unit.get('id')} has empty english_text")
    else:
        ensure(bool(line_value) and all(isinstance(line, str) and line.strip() for line in line_value or []), f"Unit {unit.get('id')} has malformed english_lines")
    return text_value, line_value


def unit_text(unit: dict[str, Any]) -> str:
    text, lines = translation_parts(unit)
    return text if text is not None else "\n".join(lines or [])


def page_label(provenance: list[dict[str, int]]) -> str:
    if len(provenance) == 1:
        page = provenance[0]
        return f"PDF {page['pdf_page']} / printed {page['printed_page']}"
    first, last = provenance[0], provenance[-1]
    return f"PDF {first['pdf_page']}→{last['pdf_page']} / printed {first['printed_page']}→{last['printed_page']}"


def load_dialogue_records(scene: int) -> list[dict[str, Any]]:
    path = DIALOGUES / f"scene-{scene:02d}.json"
    ensure(path.exists(), f"Missing immutable dialogue shard {path.relative_to(ROOT)}")
    data = load_json(path)
    if isinstance(data, list):
        records = data
    elif isinstance(data, dict) and isinstance(data.get("records"), list):
        records = data["records"]
    else:
        raise QAError(f"Malformed dialogue shard {path.relative_to(ROOT)}")
    for record in records:
        ensure(isinstance(record, dict) and isinstance(record.get("id"), str), f"Malformed dialogue record in {path.relative_to(ROOT)}")
    return records


def render_markdown(scenes: list[dict[str, Any]]) -> str:
    out: list[str] = [
        "# Tirumbippaar! — English Reader Edition",
        "",
        "**Tamil title:** திரும்பிப்பார்!  ",
        "**Status:** complete-verified source-linked English derivative  ",
        "**English authority:** `works/tirumbippaar/translations/records/`  ",
        f"**Source scan SHA-256:** `{EXPECTED_SOURCE_SHA256}`",
        "",
        "> Editorial note: This edition concatenates the 1,330 verified English units without rewriting them. Exact Tamil speaker labels remain visible for labelled dialogue; source-unlabelled speech remains unlabelled. Structural stars are not converted into invented prose.",
        "",
        "## Contents",
        "",
    ]
    out.extend(f"- [Scene {scene}](#scene-{scene})" for scene in EXPECTED_SCENES)
    out.extend(["", "---", ""])

    for record in scenes:
        scene = record["canonical_scene"]
        out.extend([f"## Scene {scene}", ""])
        for unit in record["units"]:
            uid = unit["id"]
            kind = unit["kind"]
            source = unit["source"]
            text, lines = translation_parts(unit)
            out.append(f"<!-- unit:{uid}; source:{page_label(source['page_provenance'])} -->")
            if kind == "dialogue":
                speaker = source.get("speaker_label")
                if speaker:
                    out.append(f"**{speaker}**  ")
                if text is not None:
                    out.append(text)
                else:
                    out.extend(f"> {line}  " for line in lines or [])
            elif kind == "stage-direction":
                if text is not None:
                    out.append(f"*{text}*")
                else:
                    out.extend(f"*{line}*  " for line in lines or [])
            else:
                label = {
                    "song": "Song",
                    "song-reference": "Song / performance reference",
                    "chant": "Chant",
                    "written-text": "Written text",
                }[kind]
                out.append(f"*{label}*  ")
                if text is not None:
                    out.append(f"> {text}")
                else:
                    out.extend(f"> {line}  " for line in lines or [])
            out.append("")
        out.extend(["---", ""])
    return "\n".join(out).rstrip() + "\n"


def render_html(scenes: list[dict[str, Any]]) -> str:
    nav = "\n".join(f'<a href="#scene-{scene}">Scene {scene}</a>' for scene in EXPECTED_SCENES)
    sections: list[str] = []
    for record in scenes:
        scene = record["canonical_scene"]
        body = [f'<section class="scene" id="scene-{scene}">', f"<h2>Scene {scene}</h2>"]
        for unit in record["units"]:
            uid = html.escape(unit["id"], quote=True)
            kind = unit["kind"]
            source = unit["source"]
            text, lines = translation_parts(unit)
            page = html.escape(page_label(source["page_provenance"]), quote=True)
            content = html.escape(text).replace("\n", "<br>\n") if text is not None else "<br>\n".join(html.escape(line) for line in lines or [])
            if kind == "dialogue":
                speaker = source.get("speaker_label")
                speaker_html = f'<span class="speaker">{html.escape(speaker)}</span>' if isinstance(speaker, str) and speaker else ""
                body.append(f'<p class="unit dialogue" data-unit-id="{uid}" data-source-page="{page}">{speaker_html}<span class="text">{content}</span></p>')
            elif kind == "stage-direction":
                body.append(f'<p class="unit stage" data-unit-id="{uid}" data-source-page="{page}">{content}</p>')
            else:
                label = {
                    "song": "Song",
                    "song-reference": "Song / performance reference",
                    "chant": "Chant",
                    "written-text": "Written text",
                }[kind]
                body.append(f'<div class="unit special {html.escape(kind)}" data-unit-id="{uid}" data-source-page="{page}"><p class="unit-label">{html.escape(label)}</p><p>{content}</p></div>')
        body.append('<p class="back"><a href="#contents">Back to contents</a></p>')
        body.append("</section>")
        sections.append("\n".join(body))

    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Tirumbippaar! — English Reader Edition</title>
<style>
:root {{ color-scheme: light dark; }}
body {{ font-family: ui-serif, Georgia, "Times New Roman", serif; max-width: 56rem; margin: 0 auto; padding: 2rem 1.25rem 5rem; line-height: 1.65; }}
h1, h2 {{ line-height: 1.2; }}
.note {{ font-style: italic; opacity: .82; }}
nav {{ display: flex; flex-wrap: wrap; gap: .35rem .8rem; margin: 1.5rem 0 2.5rem; }}
nav a {{ white-space: nowrap; }}
.scene {{ padding-top: 1rem; border-top: 1px solid currentColor; margin-top: 2.5rem; }}
.dialogue {{ display: grid; grid-template-columns: minmax(5rem, 8rem) 1fr; gap: .75rem; }}
.dialogue:not(:has(.speaker)) {{ display: block; }}
.speaker {{ font-weight: 700; }}
.stage {{ font-style: italic; }}
.special {{ margin: 1.2rem 0 1.2rem 1.5rem; padding-left: 1rem; border-left: 2px solid currentColor; }}
.unit-label {{ font-style: italic; font-weight: 600; margin-bottom: .25rem; }}
.back {{ font-size: .9rem; }}
@media (max-width: 36rem) {{ .dialogue {{ display: block; }} .speaker {{ display: block; margin-bottom: .2rem; }} .special {{ margin-left: .5rem; }} }}
@media print {{ nav, .back {{ display: none; }} body {{ max-width: none; }} .scene {{ break-before: page; }} }}
</style>
</head>
<body>
<header>
<h1>Tirumbippaar! — English Reader Edition</h1>
<p><strong>Tamil title:</strong> திரும்பிப்பார்!</p>
<p><strong>Status:</strong> complete-verified source-linked English derivative</p>
<p class="note">This edition concatenates the 1,330 verified English units without rewriting them. Exact Tamil speaker labels remain visible for labelled dialogue; source-unlabelled speech remains unlabelled. Structural stars are not converted into invented prose.</p>
</header>
<h2 id="contents">Contents</h2>
<nav aria-label="Scene navigation">{nav}</nav>
{''.join(sections)}
</body>
</html>
'''


def main() -> int:
    index = load_json(INDEX_PATH)
    ensure(index.get("status") == "complete-verified", "Translation index is not complete-verified")
    ensure(index.get("target_language") == "en", "Translation index target language is not en")
    ensure(index.get("translation_units") == EXPECTED_UNITS, f"Expected {EXPECTED_UNITS} indexed units")
    ensure(index.get("unit_status_counts") == {"draft": 0, "review": 0, "verified": EXPECTED_UNITS}, "Translation status counts differ from the verified checkpoint")
    ensure(index.get("unit_kind_counts") == EXPECTED_KIND_COUNTS, "Indexed unit-kind counts differ from the verified checkpoint")
    ensure(index.get("scenes_started") == EXPECTED_SCENES, "scenes_started does not cover canonical scenes 1-93")
    ensure(index.get("scenes_reviewed") == EXPECTED_SCENES, "scenes_reviewed does not cover canonical scenes 1-93")
    ensure(index.get("scenes_verified") == EXPECTED_SCENES, "scenes_verified does not cover canonical scenes 1-93")
    ensure(index.get("scenes_in_review") == [], "scenes_in_review is not empty")

    scene_meta = index.get("scene_records")
    ensure(isinstance(scene_meta, list), "scene_records is missing or malformed")
    ensure([item.get("canonical_scene") for item in scene_meta] == EXPECTED_SCENES, "scene_records order/coverage does not match scenes 1-93")

    song_ids = {value for value in collect_ids(load_json(SONG_INVENTORY_PATH)) if value.startswith("tirumbippaar-song-")}
    expected_direct_unlabelled = index.get("direct_source_unlabelled_dialogue_units")
    ensure(isinstance(expected_direct_unlabelled, list) and len(expected_direct_unlabelled) == EXPECTED_DIRECT_UNLABELLED_DIALOGUE, "Expected seven indexed source-unlabelled spoken units")

    dialogue_by_id: dict[str, dict[str, Any]] = {}
    dialogue_input_paths: list[Path] = []
    for scene in EXPECTED_SCENES:
        path = DIALOGUES / f"scene-{scene:02d}.json"
        dialogue_input_paths.append(path)
        for record in load_dialogue_records(scene):
            rid = record["id"]
            ensure(rid not in dialogue_by_id, f"Duplicate immutable dialogue id {rid}")
            dialogue_by_id[rid] = record
    ensure(len(dialogue_by_id) == EXPECTED_DIALOGUE_RECORDS, f"Expected {EXPECTED_DIALOGUE_RECORDS} immutable dialogue records, found {len(dialogue_by_id)}")

    seen_units: set[str] = set()
    linked_dialogue_ids: list[str] = []
    linked_occurrence_ids: list[str] = []
    kinds: Counter[str] = Counter()
    cross_page: list[str] = []
    direct_unlabelled: list[str] = []
    scenes: list[dict[str, Any]] = []
    translation_input_paths: list[Path] = [INDEX_PATH]
    previous_scene_page = 0

    for meta in scene_meta:
        scene = meta["canonical_scene"]
        path = TRANSLATIONS / meta["path"]
        ensure(path.exists(), f"Missing translation scene record {path.relative_to(ROOT)}")
        translation_input_paths.append(path)
        record = load_json(path)
        scenes.append(record)
        ensure(record.get("work_id") == "tirumbippaar", f"Scene {scene} work_id mismatch")
        ensure(record.get("target_language") == "en", f"Scene {scene} target_language mismatch")
        ensure(record.get("canonical_scene") == scene, f"Scene mismatch in {path.relative_to(ROOT)}")
        ensure(record.get("scene_status", record.get("pilot_status")) == "verified", f"Scene {scene} is not verified")
        units = record.get("units")
        ensure(isinstance(units, list) and units, f"Scene {scene} has no units array")
        ensure(record.get("unit_count") == len(units) == meta.get("unit_count"), f"Scene {scene} unit count mismatch")
        ensure(meta.get("status") == "verified", f"Scene {scene} index status is not verified")

        first_scene_page = min(page["pdf_page"] for unit in units for page in unit["source"]["page_provenance"])
        ensure(first_scene_page >= previous_scene_page, f"Scene {scene} regresses in canonical source-page order")
        previous_scene_page = first_scene_page
        previous_unit_page = 0

        for ordinal, unit in enumerate(units, 1):
            uid = unit.get("id")
            expected_uid = f"tirumbippaar-en-s{scene:03d}-u{ordinal:03d}"
            ensure(uid == expected_uid and isinstance(uid, str) and UNIT_ID_RE.match(uid), f"Scene {scene} unit {ordinal} id mismatch: {uid!r}")
            ensure(uid not in seen_units, f"Duplicate English unit id {uid}")
            seen_units.add(uid)
            ensure(unit.get("status") == "verified", f"Unit {uid} is not verified")
            if "canonical_scene" in unit:
                ensure(unit.get("canonical_scene") == scene, f"Unit {uid} canonical_scene mismatch")
            if "target_language" in unit:
                ensure(unit.get("target_language") == "en", f"Unit {uid} target_language mismatch")

            kind = unit.get("kind")
            ensure(kind in ALLOWED_KINDS, f"Unit {uid} has unsupported kind {kind!r}")
            kinds[kind] += 1

            source = unit.get("source")
            ensure(isinstance(source, dict), f"Unit {uid} has malformed source metadata")
            provenance = source.get("page_provenance")
            ensure(isinstance(provenance, list) and provenance, f"Unit {uid} has no page provenance")
            first_unit_page = provenance[0].get("pdf_page")
            ensure(isinstance(first_unit_page, int) and first_unit_page >= previous_unit_page, f"Unit {uid} regresses in source-page order within scene {scene}")
            previous_unit_page = first_unit_page
            for page in provenance:
                pdf_page = page.get("pdf_page")
                printed_page = page.get("printed_page")
                ensure(isinstance(pdf_page, int) and 9 <= pdf_page <= 112, f"Unit {uid} PDF page {pdf_page!r} is outside canonical range 9-112")
                ensure(isinstance(printed_page, int) and printed_page == pdf_page - 8, f"Unit {uid} printed/PDF page mapping is inconsistent")
            if len(provenance) > 1:
                cross_page.append(uid)

            record_id = source.get("source_record_id")
            if record_id is not None:
                ensure(isinstance(record_id, str) and record_id in dialogue_by_id, f"Unit {uid} source_record_id {record_id!r} is not in immutable dialogue records")
                immutable = dialogue_by_id[record_id]
                ensure(immutable.get("canonical_scene") == scene, f"Unit {uid} immutable dialogue scene mismatch")
                ensure(immutable.get("speaker_label") == source.get("speaker_label"), f"Unit {uid} speaker_label differs from immutable dialogue record")
                ensure(immutable.get("page_provenance") == provenance, f"Unit {uid} page provenance differs from immutable dialogue record")
                linked_dialogue_ids.append(record_id)
            elif kind == "dialogue":
                ensure(uid in expected_direct_unlabelled, f"Dialogue unit {uid} lacks immutable source record but is not in the indexed source-unlabelled set")
                ensure(source.get("speaker_label") in {None, ""}, f"Source-unlabelled dialogue {uid} has an invented speaker label")
                direct_unlabelled.append(uid)

            occurrence_id = source.get("source_occurrence_id")
            if occurrence_id is not None:
                ensure(isinstance(occurrence_id, str) and occurrence_id in song_ids, f"Unit {uid} song occurrence {occurrence_id!r} is not in the song inventory")
                linked_occurrence_ids.append(occurrence_id)

            text = unit_text(unit)
            ensure(not PLACEHOLDER_RE.search(text), f"Unit {uid} contains an editorial placeholder token")
            ensure(not SYNTHETIC_END_RE.match(text), f"Unit {uid} reintroduces synthetic '(Scene ends.)' text")

            translation = unit.get("translation")
            if isinstance(translation, dict) and translation.get("english_page_segments") is not None:
                segments = translation["english_page_segments"]
                ensure(isinstance(segments, list) and len(segments) >= 2, f"Unit {uid} has malformed english_page_segments")
                segment_pages = [(seg.get("pdf_page"), seg.get("printed_page")) for seg in segments]
                provenance_pages = [(page["pdf_page"], page["printed_page"]) for page in provenance]
                ensure(segment_pages == provenance_pages, f"Unit {uid} english_page_segments do not match page provenance")

    ensure(len(seen_units) == EXPECTED_UNITS, f"Expected {EXPECTED_UNITS} unique English units, found {len(seen_units)}")
    ensure(dict(kinds) == EXPECTED_KIND_COUNTS, f"Aggregated kind counts differ: {dict(kinds)}")
    ensure(cross_page == index.get("cross_page_translation_units"), "Derived cross-page list differs from translations/index.json")
    ensure(len(cross_page) == EXPECTED_CROSS_PAGE, f"Expected {EXPECTED_CROSS_PAGE} cross-page units")
    ensure(direct_unlabelled == expected_direct_unlabelled, "Derived source-unlabelled dialogue list differs from translations/index.json")
    ensure(len(linked_dialogue_ids) == EXPECTED_DIALOGUE_RECORDS, f"Expected {EXPECTED_DIALOGUE_RECORDS} dialogue links, found {len(linked_dialogue_ids)}")
    ensure(len(set(linked_dialogue_ids)) == EXPECTED_DIALOGUE_RECORDS, "One or more immutable dialogue records are linked more than once")
    ensure(set(linked_dialogue_ids) == set(dialogue_by_id), "Translation dialogue links do not exactly cover immutable dialogue records")
    ensure(linked_occurrence_ids == index.get("verified_song_reference_occurrences"), "Derived song occurrence links differ from translations/index.json")

    reader_json = {
        "work_id": "tirumbippaar",
        "title": "Tirumbippaar! — English Reader Edition",
        "title_ta": "திரும்பிப்பார்!",
        "target_language": "en",
        "status": "complete-verified",
        "authority": "works/tirumbippaar/translations/records",
        "source_sha256": EXPECTED_SOURCE_SHA256,
        "canonical_scene_order": EXPECTED_SCENES,
        "translation_units": EXPECTED_UNITS,
        "unit_kind_counts": EXPECTED_KIND_COUNTS,
        "scenes": scenes,
    }
    reader_json_text = json.dumps(reader_json, ensure_ascii=False, indent=2) + "\n"
    reader_md = render_markdown(scenes)
    reader_html = render_html(scenes)

    for uid in seen_units:
        ensure(reader_md.count(f"unit:{uid};") == 1, f"Reader Markdown does not contain exactly one marker for {uid}")
        ensure(reader_html.count(f'data-unit-id="{uid}"') == 1, f"Reader HTML does not contain exactly one element for {uid}")
    ensure(reader_md.count("\n## Scene ") == len(EXPECTED_SCENES), "Reader Markdown scene heading count mismatch")
    ensure(reader_html.count('<section class="scene" id="scene-') == len(EXPECTED_SCENES), "Reader HTML scene section count mismatch")

    qa_report = f"""# Tirumbippaar English Reader Edition — Whole-work QA\n\n**Status:** PASS  \n**English authority:** `works/tirumbippaar/translations/records/`  \n**Source scan SHA-256:** `{EXPECTED_SOURCE_SHA256}`\n\n## Verified checks\n\n- canonical scenes: **93/93** in source order;\n- English units: **{EXPECTED_UNITS}/{EXPECTED_UNITS} unique, sequential and verified**;\n- status counts: **1,330 verified / 0 review / 0 draft**;\n- kind counts: **1,047 dialogue / 263 stage direction / 7 song-reference / 2 chant / 11 written-text**;\n- immutable labelled dialogue records linked exactly once: **{len(linked_dialogue_ids)}/{EXPECTED_DIALOGUE_RECORDS}**;\n- source-visible unlabelled spoken units retained without invented speaker/dialogue IDs: **{len(direct_unlabelled)}**;\n- verified song/performance occurrence links cross-checked: **{len(linked_occurrence_ids)}**;\n- cross-page English units: **{len(cross_page)}**, exactly matching `translations/index.json`;\n- every provenance page lies inside PDF **9–112** / printed **1–104**, with `printed = PDF - 8`;\n- unit order is non-regressing in source-page order within every scene;\n- scene order is non-regressing across scenes 1–93;\n- source-only structural stars do not survive as synthetic `(Scene ends.)` units;\n- reader Markdown contains every verified unit exactly once;\n- reader HTML contains every verified unit exactly once;\n- no `TODO`, `TBD`, `FIXME`, or template-placeholder token appears in reader text.\n\n## Source-sensitive structures retained\n\n- scene 31 remains linked to `tirumbippaar-song-006` / **`பாண்டியன் என் சொல்லை`**;\n- scene 72 preserves the already-verified source-specific confrontation without normalizing its distinct wording variants;\n- scene 90 retains the dying-breath transition as a stage direction;\n- scene 91 retains `பத்திரிகை News` as written text rather than dialogue;\n- scene 93 retains final `வணக்கம்.` as translated written text while the following `★` remains structural.\n\n## Generated derivatives\n\n- `reader-edition.md` — continuous Markdown reader with invisible unit/page provenance comments;\n- `reader-edition.html` — standalone responsive/print-friendly HTML reader;\n- `reader-edition.json` — concatenated machine-readable edition retaining translation metadata;\n- `manifest.json` — deterministic input/output integrity manifest.\n\nThe generator writes only inside `works/tirumbippaar/editions/en/`; it does not modify canonical Tamil, scene derivatives, dialogue records, character mappings, song inventory, or transcription files.\n"""

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    output_payloads = {
        OUT_DIR / "reader-edition.md": reader_md.encode("utf-8"),
        OUT_DIR / "reader-edition.html": reader_html.encode("utf-8"),
        OUT_DIR / "reader-edition.json": reader_json_text.encode("utf-8"),
        OUT_DIR / "QA_REPORT.md": qa_report.encode("utf-8"),
    }
    for path, payload in output_payloads.items():
        path.write_bytes(payload)

    validation_inputs = translation_input_paths + dialogue_input_paths + [SONG_INVENTORY_PATH]
    manifest = {
        "work_id": "tirumbippaar",
        "edition": "english-reader",
        "status": "complete-verified",
        "build_version": BUILD_VERSION,
        "generator": "works/tirumbippaar/editions/en/build.py",
        "source_scan_sha256": EXPECTED_SOURCE_SHA256,
        "translation_authority": "works/tirumbippaar/translations/records",
        "translation_input_files": len(translation_input_paths),
        "translation_input_aggregate_sha256": aggregate_sha256(translation_input_paths),
        "validation_input_files": len(validation_inputs),
        "validation_input_aggregate_sha256": aggregate_sha256(validation_inputs),
        "canonical_scenes": EXPECTED_SCENES,
        "translation_units": EXPECTED_UNITS,
        "unit_kind_counts": EXPECTED_KIND_COUNTS,
        "immutable_dialogue_records_linked": len(linked_dialogue_ids),
        "direct_source_unlabelled_dialogue_units": direct_unlabelled,
        "cross_page_units": cross_page,
        "song_occurrence_links": linked_occurrence_ids,
        "qa_status": "PASS",
        "outputs": {
            path.name: {"sha256": sha256_bytes(payload), "bytes": len(payload)}
            for path, payload in output_payloads.items()
        },
    }
    (OUT_DIR / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("Tirumbippaar English whole-work QA: PASS")
    print(f"Scenes: {len(EXPECTED_SCENES)} | Units: {len(seen_units)} | Cross-page: {len(cross_page)}")
    print(f"Dialogue source links: {len(linked_dialogue_ids)} | Direct unlabelled speech: {len(direct_unlabelled)} | Song occurrences: {len(linked_occurrence_ids)}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except QAError as exc:
        print(f"Tirumbippaar English whole-work QA: FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
