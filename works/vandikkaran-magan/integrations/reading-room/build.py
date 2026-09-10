#!/usr/bin/env python3
"""Build and QA the source-linked Vandikkaran Magan Reading Room payload."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

BUILD_VERSION = 1
ROOT = Path(__file__).resolve().parents[4]
WORK = ROOT / "works" / "vandikkaran-magan"
READER_DIR = WORK / "editions" / "en"
READER_JSON = READER_DIR / "reader-edition.json"
READER_MANIFEST = READER_DIR / "manifest.json"
SCENE_INDEX = WORK / "scenes" / "index.json"
SCENES_DIR = WORK / "scenes"
DIALOGUE_INDEX = WORK / "dialogues" / "index.json"
DIALOGUES_DIR = WORK / "dialogues" / "records"
SONG_INDEX = WORK / "songs" / "index.json"
SONG_INVENTORY = WORK / "songs" / "inventory.json"
OUT = WORK / "integrations" / "reading-room"

SOURCE_SHA256 = "03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253"
EXPECTED_SCENES = 72
EXPECTED_UNITS = 1181
EXPECTED_KINDS = {
    "dialogue": 800,
    "performance-cue": 10,
    "song": 53,
    "stage-direction": 316,
    "written-text": 2,
}
EXPECTED_DIALOGUES = 773
EXPECTED_UNLABELLED = 27
EXPECTED_CROSS_PAGE = 58
EXPECTED_PERFORMANCE_LINKED_UNITS = 66
EXPECTED_PERFORMANCE_IDS = [f"vandikkaran-magan-perf-{n:03d}" for n in range(1, 10)]
EXPECTED_BOUNDED_PERFORMANCES = 6
EXPECTED_CUE_ONLY_PERFORMANCES = 3
EXPECTED_SOURCE_ATTRIBUTED = 0
EXPECTED_UNRESOLVED_AUTHORSHIP = 6
PLACEHOLDER_RE = re.compile(r"\b(?:TODO|TBD|FIXME)\b|\[\[\?\]\]|\{\{.+?\}\}", re.I)
COMMENT_RE = re.compile(r"<!--.*?-->\s*", re.S)
HEADING_RE = re.compile(r"^\s*#{1,6}\s+(.+?)\s*$")


class QAError(RuntimeError):
    pass


def ensure(condition: bool, message: str) -> None:
    if not condition:
        raise QAError(message)


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise QAError(f"Cannot parse {path.relative_to(ROOT)}: {exc}") from exc


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def aggregate_sha256(paths: list[Path]) -> str:
    digest = hashlib.sha256()
    for path in sorted(set(paths), key=lambda p: p.as_posix()):
        ensure(path.exists(), f"Missing integration input {path.relative_to(ROOT)}")
        digest.update(path.relative_to(ROOT).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def translation_payload(unit: dict[str, Any]) -> tuple[str | None, list[str] | None]:
    tr = unit.get("translation")
    ensure(isinstance(tr, dict), f"Malformed translation payload at {unit.get('id')}")
    text = tr.get("english_text")
    lines = tr.get("english_lines")
    ensure(isinstance(text, str) ^ isinstance(lines, list), f"English payload shape differs at {unit.get('id')}")
    if isinstance(text, str):
        ensure(text.strip() and not PLACEHOLDER_RE.search(text), f"Invalid English text at {unit.get('id')}")
        return text, None
    ensure(bool(lines) and all(isinstance(x, str) and x.strip() and not PLACEHOLDER_RE.search(x) for x in lines), f"Invalid English lines at {unit.get('id')}")
    return None, lines


def extract_tamil_scene(path: Path, expected_heading: str) -> str:
    raw = COMMENT_RE.sub("", path.read_text(encoding="utf-8"))
    lines = raw.splitlines()
    heading_index = None
    heading_text = None
    for i, line in enumerate(lines):
        match = HEADING_RE.match(line)
        if match:
            heading_index = i
            heading_text = match.group(1).strip()
            break
    ensure(isinstance(heading_index, int) and isinstance(heading_text, str), f"Missing source heading in {path.relative_to(ROOT)}")
    ensure(heading_text == expected_heading, f"Scene heading drift in {path.relative_to(ROOT)}: {heading_text!r} != {expected_heading!r}")
    body_lines = lines[heading_index + 1 :]
    while body_lines and not body_lines[0].strip():
        body_lines.pop(0)
    while body_lines and not body_lines[-1].strip():
        body_lines.pop()
    body = "\n".join(body_lines).strip()
    ensure(body, f"Empty Tamil scene body in {path.relative_to(ROOT)}")
    ensure(not PLACEHOLDER_RE.search(body), f"Editorial placeholder in Tamil scene {path.relative_to(ROOT)}")
    return body


def dialogue_records(scene: int) -> list[dict[str, Any]]:
    path = DIALOGUES_DIR / f"scene-{scene:03d}.json"
    data = load_json(path)
    records = data if isinstance(data, list) else data.get("records") if isinstance(data, dict) else None
    ensure(isinstance(records, list), f"Malformed dialogue shard {path.relative_to(ROOT)}")
    return records


def load_dialogue_authority() -> tuple[dict[str, dict[str, Any]], list[Path]]:
    authority: dict[str, dict[str, Any]] = {}
    paths = [DIALOGUE_INDEX]
    for scene in range(1, EXPECTED_SCENES + 1):
        path = DIALOGUES_DIR / f"scene-{scene:03d}.json"
        paths.append(path)
        for rec in dialogue_records(scene):
            rid = rec.get("id")
            ensure(isinstance(rid, str) and rid not in authority, f"Bad/duplicate immutable dialogue ID {rid!r}")
            authority[rid] = rec
    ensure(len(authority) == EXPECTED_DIALOGUES, f"Dialogue authority {len(authority)} != {EXPECTED_DIALOGUES}")
    return authority, paths


def validate_and_build() -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, Any], list[Path]]:
    reader = load_json(READER_JSON)
    reader_manifest = load_json(READER_MANIFEST)
    scene_index = load_json(SCENE_INDEX)
    dialogue_index = load_json(DIALOGUE_INDEX)
    song_index = load_json(SONG_INDEX)
    song_inventory = load_json(SONG_INVENTORY)

    ensure(reader.get("work_id") == "vandikkaran-magan", "Reader work id differs")
    ensure(reader.get("status") == "complete-verified", "Reader is not complete-verified")
    ensure(reader.get("source_sha256") == SOURCE_SHA256, "Reader source SHA differs")
    ensure(reader.get("source_numbered_scenes") is True, "Reader lost source-numbered scene semantics")
    ensure(reader.get("archive_scene_count") == EXPECTED_SCENES, "Reader scene total differs")
    ensure(reader.get("translation_units") == EXPECTED_UNITS, "Reader unit total differs")
    ensure(reader.get("unit_kind_counts") == EXPECTED_KINDS, "Reader kind totals differ")
    ensure(reader.get("immutable_dialogue_records_linked") == EXPECTED_DIALOGUES, "Reader dialogue total differs")
    ensure(reader.get("source_unlabelled_spoken_units") == EXPECTED_UNLABELLED, "Reader source-unlabelled total differs")
    ensure(reader.get("cross_page_units") == EXPECTED_CROSS_PAGE, "Reader cross-page total differs")
    ensure(reader.get("performance_linked_units") == EXPECTED_PERFORMANCE_LINKED_UNITS, "Reader performance-linked total differs")
    ensure(reader.get("performance_occurrence_ids_linked") == EXPECTED_PERFORMANCE_IDS, "Reader performance identity list differs")

    ensure(reader_manifest.get("status") == "complete-verified" and reader_manifest.get("qa_status") == "PASS", "Reader manifest is not complete-verified/PASS")
    ensure(reader_manifest.get("source_scan_sha256") == SOURCE_SHA256, "Reader manifest source SHA differs")
    ensure(reader_manifest.get("archive_scenes") == EXPECTED_SCENES, "Reader manifest scene total differs")
    ensure(reader_manifest.get("translation_units") == EXPECTED_UNITS, "Reader manifest unit total differs")
    ensure(reader_manifest.get("immutable_dialogue_records_linked") == EXPECTED_DIALOGUES, "Reader manifest dialogue total differs")
    ensure(reader_manifest.get("source_unlabelled_spoken_units") == EXPECTED_UNLABELLED, "Reader manifest source-unlabelled total differs")
    ensure(reader_manifest.get("cross_page_units") == EXPECTED_CROSS_PAGE, "Reader manifest cross-page total differs")
    ensure(reader_manifest.get("performance_linked_units") == EXPECTED_PERFORMANCE_LINKED_UNITS, "Reader manifest performance-linked total differs")
    ensure(reader_manifest.get("performance_occurrence_ids_linked") == EXPECTED_PERFORMANCE_IDS, "Reader manifest performance identity list differs")

    ensure(scene_index.get("status") == "complete-verified" and scene_index.get("total_scenes") == EXPECTED_SCENES, "Scene authority is not complete-verified 72/72")
    ensure(scene_index.get("source", {}).get("sha256") == SOURCE_SHA256, "Scene authority source SHA differs")
    scene_rows = scene_index.get("scenes")
    ensure(isinstance(scene_rows, list) and len(scene_rows) == EXPECTED_SCENES, "Scene authority must contain 72 rows")
    ensure([int(row.get("ordinal")) for row in scene_rows] == list(range(1, EXPECTED_SCENES + 1)), "Scene authority is unordered")

    ensure(dialogue_index.get("status") == "complete-verified-reconciled" and dialogue_index.get("dialogue_record_count") == EXPECTED_DIALOGUES, "Dialogue authority is not reconciled 773/PASS")
    ensure(song_index.get("status") == "complete-verified-source-only", "Song/performance authority is not closed source-only")
    ensure(song_inventory.get("status") == "complete-verified-source-only" and song_inventory.get("mapped_source_visible_occurrences") == 9, "Song inventory is not closed 9/9")
    ensure(song_inventory.get("full_or_clearly_bounded_tamil_derivatives") == EXPECTED_BOUNDED_PERFORMANCES, "Bounded performance count differs")
    ensure(song_inventory.get("cue_only_non_lyric_records") == EXPECTED_CUE_ONLY_PERFORMANCES, "Cue-only performance count differs")
    ensure(song_inventory.get("source_attributed_authorship_records") == EXPECTED_SOURCE_ATTRIBUTED, "Source-attributed item-level authorship count differs")
    ensure(song_inventory.get("unresolved_item_level_authorship_records") == EXPECTED_UNRESOLVED_AUTHORSHIP, "Unresolved item-level authorship count differs")
    ensure(song_inventory.get("policy", {}).get("item_level_authorship_inferred") is False, "Song inventory permits inferred item-level authorship")

    perf_records = song_inventory.get("records")
    ensure(isinstance(perf_records, list) and [r.get("id") for r in perf_records] == EXPECTED_PERFORMANCE_IDS, "Song/performance identities/order differ")
    performance_ids = set(EXPECTED_PERFORMANCE_IDS)

    dialogue_by_id, dialogue_paths = load_dialogue_authority()
    raw_scenes = reader.get("scenes")
    ensure(isinstance(raw_scenes, list) and len(raw_scenes) == EXPECTED_SCENES, "Reader scene list differs")

    seen_units: set[str] = set()
    dialogue_links: list[str] = []
    unlabelled_units: list[str] = []
    cross_page_units: list[str] = []
    performance_links: list[str] = []
    kinds: Counter[str] = Counter()
    payload_scenes: list[dict[str, Any]] = []
    scene_paths: list[Path] = []

    for ordinal, (reader_scene, meta) in enumerate(zip(raw_scenes, scene_rows), 1):
        source_scene_id = str(meta.get("scene_id"))
        ensure(reader_scene.get("scene_ordinal") == ordinal, f"Reader scene ordinal mismatch at {ordinal}")
        ensure(str(reader_scene.get("source_scene_id")) == source_scene_id, f"Reader/source scene identity mismatch at {ordinal}")
        ensure(reader_scene.get("source_heading") == meta.get("source_heading"), f"Reader/source heading mismatch at {ordinal}")
        ensure(reader_scene.get("location") == meta.get("location"), f"Reader/source location mismatch at {ordinal}")

        scene_id = f"vandikkaran-magan-s{ordinal:03d}"
        scene_path = SCENES_DIR / f"scene-{ordinal:03d}.md"
        scene_paths.append(scene_path)
        tamil_text = extract_tamil_scene(scene_path, str(meta.get("source_heading")))
        units = reader_scene.get("units")
        ensure(isinstance(units, list) and reader_scene.get("unit_count") == len(units), f"Reader unit_count mismatch at scene {ordinal}")

        english_units: list[dict[str, Any]] = []
        scene_pdf_pages: set[int] = set()
        scene_printed_pages: set[int] = set()
        for unit in units:
            uid = unit.get("id")
            ensure(isinstance(uid, str) and uid not in seen_units, f"Bad/duplicate English unit {uid!r}")
            ensure(unit.get("status") == "verified" and unit.get("target_language") == "en", f"Unverified/non-English unit {uid}")
            ensure(unit.get("scene_id") == scene_id and unit.get("scene_ordinal") == ordinal, f"Unit scene identity differs at {uid}")
            ensure(str(unit.get("source_scene_id")) == source_scene_id, f"Unit source scene identity differs at {uid}")
            seen_units.add(uid)

            kind = unit.get("kind")
            ensure(kind in EXPECTED_KINDS, f"Unsupported unit kind {kind!r} at {uid}")
            kinds[kind] += 1
            source = unit.get("source")
            ensure(isinstance(source, dict), f"Malformed source metadata at {uid}")
            provenance = source.get("page_provenance")
            ensure(isinstance(provenance, list) and provenance, f"Missing page provenance at {uid}")
            for page in provenance:
                pdf_page = page.get("pdf_page")
                printed_page = page.get("printed_page")
                ensure(isinstance(pdf_page, int) and 6 <= pdf_page <= 87 and printed_page == pdf_page - 1, f"Invalid page provenance at {uid}: {page}")
                scene_pdf_pages.add(pdf_page)
                scene_printed_pages.add(printed_page)
            if len(provenance) > 1:
                cross_page_units.append(uid)

            rid = source.get("source_record_id")
            if rid is not None:
                ensure(kind == "dialogue", f"Non-dialogue unit carries immutable dialogue ID at {uid}")
                ensure(rid in dialogue_by_id, f"Unknown immutable dialogue ID {rid} at {uid}")
                immutable = dialogue_by_id[rid]
                ensure(immutable.get("scene_id") == scene_id and immutable.get("scene_ordinal") == ordinal, f"Dialogue scene mismatch at {uid}")
                ensure(str(immutable.get("source_scene_id")) == source_scene_id, f"Dialogue source scene mismatch at {uid}")
                ensure(immutable.get("speaker_label") == source.get("speaker_label"), f"Dialogue speaker mismatch at {uid}")
                ensure(immutable.get("source_delimiter") == source.get("source_delimiter"), f"Dialogue delimiter mismatch at {uid}")
                ensure(immutable.get("page_provenance") == provenance, f"Dialogue provenance mismatch at {uid}")
                dialogue_links.append(rid)
            elif kind == "dialogue":
                ensure(source.get("speaker_label") in {None, ""} and source.get("speaker_label_origin") == "source-unlabelled", f"Source-unlabelled speech gained a speaker at {uid}")
                unlabelled_units.append(uid)

            occurrence = source.get("source_occurrence_id")
            if occurrence is not None:
                ensure(occurrence in performance_ids, f"Unknown song/performance occurrence {occurrence} at {uid}")
                performance_links.append(occurrence)

            english_text, english_lines = translation_payload(unit)
            tr = unit.get("translation") or {}
            english_units.append({
                "id": uid,
                "kind": kind,
                "source_record_id": rid,
                "source_occurrence_id": occurrence,
                "source_path": source.get("source_path"),
                "canonical_scene_path": source.get("canonical_scene_path"),
                "source_locator": source.get("source_locator"),
                "speaker_label": source.get("speaker_label"),
                "speaker_label_origin": source.get("speaker_label_origin"),
                "source_delimiter": source.get("source_delimiter"),
                "page_provenance": provenance,
                "english_text": english_text,
                "english_lines": english_lines,
                "english_page_segments": tr.get("english_page_segments"),
                "translation_mode": tr.get("mode"),
                "translation_notes": tr.get("notes") or [],
            })

        expected_pdf_pages = list(meta.get("pdf_pages") or [])
        ensure(set(scene_pdf_pages).issubset(set(expected_pdf_pages)), f"English unit provenance falls outside scene authority at scene {ordinal}")
        payload_scenes.append({
            "scene_id": scene_id,
            "archival_scene_ordinal": ordinal,
            "source_scene_id": source_scene_id,
            "source_scene_numbering_is_printed": True,
            "source_heading_ta": meta.get("source_heading"),
            "source_location_ta": meta.get("location"),
            "source_scene_file": f"works/vandikkaran-magan/scenes/scene-{ordinal:03d}.md",
            "source_pdf_pages": expected_pdf_pages,
            "source_printed_pages": [p - 1 for p in expected_pdf_pages],
            "tamil_text": tamil_text,
            "english_units": english_units,
        })

    ensure(len(seen_units) == EXPECTED_UNITS, f"English unit coverage {len(seen_units)} != {EXPECTED_UNITS}")
    ensure({k: kinds.get(k, 0) for k in EXPECTED_KINDS} == EXPECTED_KINDS and not (set(kinds) - set(EXPECTED_KINDS)), f"English unit-kind counts differ: {dict(kinds)}")
    ensure(len(dialogue_links) == len(set(dialogue_links)) == EXPECTED_DIALOGUES and set(dialogue_links) == set(dialogue_by_id), "Immutable dialogue coverage is not exactly once")
    ensure(len(unlabelled_units) == EXPECTED_UNLABELLED, f"Source-unlabelled spoken unit count {len(unlabelled_units)} != {EXPECTED_UNLABELLED}")
    ensure(len(cross_page_units) == EXPECTED_CROSS_PAGE, f"Cross-page unit count {len(cross_page_units)} != {EXPECTED_CROSS_PAGE}")
    ensure(len(performance_links) == EXPECTED_PERFORMANCE_LINKED_UNITS, f"Performance-linked unit count {len(performance_links)} != {EXPECTED_PERFORMANCE_LINKED_UNITS}")
    ensure(sorted(set(performance_links)) == EXPECTED_PERFORMANCE_IDS, "Performance occurrence coverage is not exact 9/9")

    payload_performances = []
    for rec in perf_records:
        payload_performances.append({
            "id": rec.get("id"),
            "source_scene_id": rec.get("source_scene_id"),
            "archival_scene_ordinal": rec.get("scene_ordinal"),
            "source_pdf_pages": rec.get("source_pdf_pages"),
            "form": rec.get("form"),
            "source_marker": rec.get("source_marker"),
            "source_incipit": rec.get("source_incipit"),
            "source_role_cues": rec.get("source_role_cues") or [],
            "authorship_status": rec.get("authorship_status"),
            "author_as_printed": rec.get("author_as_printed"),
            "full_or_clearly_bounded_body": rec.get("full_or_clearly_bounded_body"),
            "notes": rec.get("notes"),
        })

    stats = {
        "screenplay_scenes": EXPECTED_SCENES,
        "tamil_scene_texts": EXPECTED_SCENES,
        "english_units": EXPECTED_UNITS,
        "dialogue_units": EXPECTED_KINDS["dialogue"],
        "immutable_dialogue_links": EXPECTED_DIALOGUES,
        "source_unlabelled_spoken_units": EXPECTED_UNLABELLED,
        "stage_direction_units": EXPECTED_KINDS["stage-direction"],
        "performance_cue_units": EXPECTED_KINDS["performance-cue"],
        "song_units": EXPECTED_KINDS["song"],
        "written_text_units": EXPECTED_KINDS["written-text"],
        "cross_page_units": EXPECTED_CROSS_PAGE,
        "performance_occurrence_identities": len(EXPECTED_PERFORMANCE_IDS),
        "performance_linked_units": EXPECTED_PERFORMANCE_LINKED_UNITS,
        "bounded_tamil_performance_bodies": EXPECTED_BOUNDED_PERFORMANCES,
        "cue_only_non_lyric_performances": EXPECTED_CUE_ONLY_PERFORMANCES,
        "source_attributed_item_level_lyric_authorships": EXPECTED_SOURCE_ATTRIBUTED,
        "unresolved_item_level_lyric_authorships": EXPECTED_UNRESOLVED_AUTHORSHIP,
    }

    input_paths = [
        READER_JSON,
        READER_MANIFEST,
        SCENE_INDEX,
        DIALOGUE_INDEX,
        SONG_INDEX,
        SONG_INVENTORY,
        *scene_paths,
        *dialogue_paths[1:],
    ]
    return payload_scenes, payload_performances, stats, input_paths


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    scenes, performances, stats, input_paths = validate_and_build()
    payload = {
        "schema_version": 1,
        "integration_target": "Kalaignar Digital Library / Reading Room",
        "preferred_public_surface": "https://nenjukkuneethi.org/read",
        "integration_status": "payload-complete-verified",
        "site_application_status": "not-applied",
        "source_authority": "pugazg/kalaignar-cinema-works verified Vandikkaran Magan source/translation records",
        "work": {
            "id": "vandikkaran-magan",
            "kind": "film-screenplay-dialogue-booklet",
            "title_ta": "வண்டிக்காரன் மகன்",
            "presentation_title_en": "Vandikkaran Magan",
            "presentation_title_en_is_editorial": True,
            "source_identifier": "TVA_BOK_0062961",
            "source_sha256": SOURCE_SHA256,
            "publication_year_as_printed": 1978,
            "status": "complete-verified",
            "languages": ["ta", "en"],
            "counts": stats,
        },
        "navigation": {
            "primary_sections": ["screenplay-scenes"],
            "screenplay_scene_order": "verified printed source-heading order represented by archive ordinals 1-72",
            "screenplay_scene_numbers_are_source_numbers": True,
            "source_scene_ids": [scene["source_scene_id"] for scene in scenes],
            "archival_scene_ordinals_are_stable_order_keys": True,
            "suggested_slug": "vandikkaran-magan",
            "suggested_slug_is_presentation_metadata": True,
        },
        "language_presentation": {
            "default": "ta",
            "available": ["ta", "en", "parallel"],
            "rule": "language switching is presentation only; Tamil source text and verified English text must not be rewritten",
        },
        "search": {
            "recommended_fields": [
                "screenplay_scenes.source_heading_ta",
                "screenplay_scenes.source_location_ta",
                "screenplay_scenes.tamil_text",
                "screenplay_scenes.english_units.speaker_label",
                "screenplay_scenes.english_units.english_text",
                "screenplay_scenes.english_units.english_lines",
                "performance_occurrences.source_marker",
                "performance_occurrences.source_incipit",
            ],
            "normalization_rule": "search normalization may create indexes but must not alter stored source or translation text",
        },
        "provenance_policy": {
            "show_source_pages": True,
            "preserve_source_paths": True,
            "scene_numbering_rule": "the booklet prints scene headings; preserve exact source scene IDs including suffixes and combined heading 45-46, while archive ordinals remain stable ordering keys",
            "speaker_label_rule": "exact Tamil source speaker labels and delimiters remain metadata; source-unlabelled speech remains unassigned",
            "cross_page_rule": "all 58 cross-page English units remain single logical units with all verified PDF/printed page provenance",
            "song_performance_rule": "retain only the nine closed source-visible occurrence identities; six have bounded Tamil bodies and three are cue-only/non-lyric; do not reconstruct absent lyrics",
            "lyric_authorship_rule": "item-level authorship remains 0 source-attributed / 6 unresolved / 3 not-applicable; PDF 88 `பாடல்கள்: கவிஞர் வாலி` remains film-level metadata and is not promoted item-by-item",
        },
        "film_level_credit_context": {
            "songs_credit_as_printed": "பாடல்கள்: கவிஞர் வாலி",
            "songs_credit_scope": "film-level-only",
            "item_level_authorship_inferred": False,
        },
        "performance_occurrences": performances,
        "screenplay_scenes": scenes,
    }

    payload_bytes = (json.dumps(payload, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    payload_sha = sha256_bytes(payload_bytes)
    (OUT / "reading-room.json").write_bytes(payload_bytes)

    qa = f"""# வண்டிக்காரன் மகன் — Reading Room integration payload QA

**Status:** PASS  
**Site application:** not-applied  
**Source scan SHA-256:** `{SOURCE_SHA256}`  
**Reader authority:** `works/vandikkaran-magan/editions/en/reader-edition.json`

## Verified payload checks

- source-numbered screenplay navigation: **72/72 scenes** in verified printed-heading order;
- Tamil scene texts: **72/72**, generated from verified scene derivatives without provenance comments;
- verified English units: **1,181/1,181 exactly once**;
- unit kinds: **800 dialogue / 316 stage-direction / 10 performance-cue / 53 song / 2 written-text**;
- immutable labelled dialogue links: **773/773 exactly once**;
- source-unlabelled spoken units: **27/27**, retained with no invented speaker/dialogue ID;
- cross-page English units: **58/58**, preserving all PDF/printed page provenance;
- verified song/performance identities: **9/9**, represented across **66** linked English units;
- performance source forms: **6 bounded Tamil bodies + 3 cue-only/non-lyric records**;
- item-level lyric authorship: **0 source-attributed / 6 unresolved / 3 not-applicable**;
- PDF 88 `பாடல்கள்: கவிஞர் வாலி` remains film-level metadata only and is not promoted item-by-item;
- source page provenance remains within screenplay PDF **6–87** / printed **5–86**, with `printed = PDF - 1`;
- exact source scene IDs, including suffixes and combined `45-46`, are preserved;
- structural `★` separators are not manufactured into English prose;
- editorial placeholder tokens in payload source/translation text: **0**;
- closed Tamil/dialogue/character/song/translation/reader evidence modified by payload generation: **0**.

## Output

- `reading-room.json` — SHA-256 `{payload_sha}` — **{len(payload_bytes):,} bytes**.

This payload is a deterministic data derivative for the separate Kalaignar Digital Library / Reading Room implementation. The public-site repository has **not** been modified or deployed by this step.
"""
    qa_bytes = qa.encode("utf-8")
    (OUT / "QA_REPORT.md").write_bytes(qa_bytes)

    readme = f"""# வண்டிக்காரன் மகன் — Reading Room integration payload

This directory contains the deterministic **source-linked data payload** prepared for the Kalaignar Digital Library / Reading Room.

It does **not** modify or deploy the separate public-site implementation repository.

## Authority

Direct inputs are the complete-verified `வண்டிக்காரன் மகன்` reader/export, the 72 verified source-numbered scene derivatives, the reconciled 773-record immutable dialogue authority, and the closed nine-occurrence song/performance inventory. This integration layer does not become textual authority.

## Navigation semantics

The booklet **does print scene headings**. The payload therefore preserves the exact source scene IDs (`1`, suffix forms such as `4-எ`, and combined `45-46`) while retaining archive ordinals 1–72 only as stable ordering keys.

## Language model

Tamil and English are both available. `ta`, `en`, and parallel display are presentation modes only; stored source/translation text must not be rewritten by the site.

## Completion checkpoint

Status: **payload-complete-verified — QA PASS**.

- payload: `reading-room.json`;
- payload bytes: **{len(payload_bytes):,}**;
- payload SHA-256: `{payload_sha}`;
- scenes / Tamil scene texts: **72 / 72**;
- English units: **1,181**;
- immutable dialogue links: **773**;
- source-unlabelled spoken units: **27**;
- cross-page units: **58**;
- performance occurrence identities / linked English units: **9 / 66**;
- item-level lyric authorship remains **0 source-attributed / 6 unresolved / 3 not-applicable**;
- QA: `QA_REPORT.md` — **PASS**;
- site application: **not-applied**.

The payload is ready for the separate public-site implementation repository only when that repository is explicitly authorized for modification.

## Outputs

- `build.py` — deterministic payload builder and validator;
- `reading-room.json` — machine-readable integration payload;
- `QA_REPORT.md` — payload QA checkpoint;
- `manifest.json` — reproducibility/integrity hashes.
"""
    readme_bytes = readme.encode("utf-8")
    (OUT / "README.md").write_bytes(readme_bytes)

    manifest = {
        "work_id": "vandikkaran-magan",
        "integration": "reading-room",
        "build_version": BUILD_VERSION,
        "status": "PASS",
        "site_application_status": "not-applied",
        "source_sha256": SOURCE_SHA256,
        "reader_input_paths": [
            "works/vandikkaran-magan/editions/en/reader-edition.json",
            "works/vandikkaran-magan/editions/en/manifest.json",
        ],
        "authoritative_input_files": len(set(input_paths)),
        "authoritative_input_aggregate_sha256": aggregate_sha256(input_paths),
        "checkpoint": stats,
        "output": {
            "path": "works/vandikkaran-magan/integrations/reading-room/reading-room.json",
            "bytes": len(payload_bytes),
            "sha256": payload_sha,
        },
        "qa_report": {
            "path": "works/vandikkaran-magan/integrations/reading-room/QA_REPORT.md",
            "bytes": len(qa_bytes),
            "sha256": sha256_bytes(qa_bytes),
        },
        "readme": {
            "path": "works/vandikkaran-magan/integrations/reading-room/README.md",
            "bytes": len(readme_bytes),
            "sha256": sha256_bytes(readme_bytes),
        },
    }
    (OUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("VANDIKKARAN MAGAN READING ROOM PAYLOAD BUILD")
    print("status= PASS")
    print("scenes= 72")
    print("english_units= 1181")
    print("immutable_dialogue_links= 773/773 exactly once")
    print("source_unlabelled_spoken_units= 27")
    print("cross_page_units= 58")
    print("performance_occurrence_identities= 9/9")
    print("performance_linked_units= 66")
    print(f"payload_sha256= {payload_sha}")
    print("site_application_status= not-applied")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except QAError as exc:
        print(f"VANDIKKARAN MAGAN READING ROOM PAYLOAD BUILD\nstatus= FAIL\nerror= {exc}", file=sys.stderr)
        raise SystemExit(1)
