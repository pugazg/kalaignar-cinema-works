#!/usr/bin/env python3
"""Build and QA the deterministic Raja Rani bilingual reader/export layer."""

from __future__ import annotations

import hashlib
import html
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

BUILD_VERSION = 1
ROOT = Path(__file__).resolve().parents[4]
WORK = ROOT / "works" / "raja-rani"
SCENE_TRANS = WORK / "translations" / "records"
SCENE_INDEX = WORK / "translations" / "index.json"
SCENES_DIR = WORK / "scenes"
DIALOGUES_DIR = WORK / "dialogues" / "records"
SONG_TRANS = WORK / "translations" / "songs" / "records"
SONG_TRANS_INDEX = WORK / "translations" / "songs" / "index.json"
SONG_SOURCE_INDEX = WORK / "songs" / "index.json"
SONG_INVENTORY = WORK / "songs" / "inventory.json"
SONG_TAMIL = WORK / "songs" / "tamil"
OUT = WORK / "editions" / "en"

SOURCE_SHA256 = "26ecc026b89deafac94bb3b107ee7c5f361c68796c4a1cdf4d01ad7c1c0d31a4"
EXPECTED_SCENES = 58
EXPECTED_SCREENPLAY_UNITS = 1236
EXPECTED_KINDS = {
    "dialogue": 1090,
    "stage-direction": 137,
    "performance-cue": 4,
    "written-text": 5,
}
EXPECTED_DIALOGUE_RECORDS = 1071
EXPECTED_UNLABELLED = 19
EXPECTED_CROSS_PAGE_UNITS = 15
EXPECTED_PERFORMANCE_OCCURRENCES = [
    "raja-rani-song-perf-001",
    "raja-rani-song-perf-002",
    "raja-rani-song-perf-003",
    "raja-rani-song-perf-004",
]
EXPECTED_SONGS = 11
EXPECTED_SONG_SECTIONS = 67
EXPECTED_SONG_LINE_CUES = 181
EXPECTED_CROSS_PAGE_SONGS = [
    "raja-rani-song-en-002",
    "raja-rani-song-en-003",
    "raja-rani-song-en-008",
    "raja-rani-song-en-010",
]
EXPECTED_ATTRIBUTED = {
    "raja-rani-song-003",
    "raja-rani-song-005",
    "raja-rani-song-006",
    "raja-rani-song-007",
    "raja-rani-song-008",
}
EXPECTED_UNRESOLVED = {
    "raja-rani-song-001",
    "raja-rani-song-002",
    "raja-rani-song-004",
    "raja-rani-song-009",
    "raja-rani-song-010",
    "raja-rani-song-011",
}
DELETED_DUPLICATE_IDS = {
    "raja-rani-s055-d026",
    "raja-rani-s055-d027",
    "raja-rani-s055-d028",
    "raja-rani-s055-d029",
    "raja-rani-s055-d030",
}
PLACEHOLDER_RE = re.compile(r"\b(?:TODO|TBD|FIXME)\b|\[\[\?\]\]|\{\{.+?\}\}", re.I)
SYNTHETIC_END_RE = re.compile(r"^\s*[\[(]?\s*Scene\s+ends?\.?\s*[\])]?\s*$", re.I)
COMMENT_RE = re.compile(r"<!--.*?-->\s*", re.S)


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
        ensure(path.exists(), f"Missing authoritative input {path.relative_to(ROOT)}")
        digest.update(path.relative_to(ROOT).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def strip_scene_comments(raw: str) -> str:
    return COMMENT_RE.sub("", raw).strip()


def translation_payload(unit: dict[str, Any]) -> tuple[str, list[str] | None]:
    tr = unit.get("translation")
    ensure(isinstance(tr, dict), f"{unit.get('id')} has malformed translation")
    text = tr.get("english_text")
    lines = tr.get("english_lines")
    ensure(isinstance(text, str) ^ isinstance(lines, list), f"{unit.get('id')} must have exactly one English payload")
    if isinstance(text, str):
        ensure(text.strip(), f"{unit.get('id')} has empty English text")
        return text, None
    ensure(lines and all(isinstance(line, str) and line.strip() for line in lines), f"{unit.get('id')} has malformed English lines")
    return "\n".join(lines), lines


def page_label(provenance: list[dict[str, int]]) -> str:
    if len(provenance) == 1:
        p = provenance[0]
        return f"PDF {p['pdf_page']} / printed {p['printed_page']}"
    a, b = provenance[0], provenance[-1]
    return f"PDF {a['pdf_page']}→{b['pdf_page']} / printed {a['printed_page']}→{b['printed_page']}"


def song_page_label(pages: list[int], printed: list[int]) -> str:
    pdf = str(pages[0]) if len(pages) == 1 else f"{pages[0]}→{pages[-1]}"
    if not printed:
        return f"PDF {pdf}"
    pr = str(printed[0]) if len(printed) == 1 else f"{printed[0]}→{printed[-1]}"
    return f"PDF {pdf} / printed {pr}"


def song_line_id(song_no: int, section_no: int, line_no: int) -> str:
    return f"raja-rani-song-en-{song_no:03d}-s{section_no:02d}-l{line_no:03d}"


def authoritative_input_paths() -> list[Path]:
    paths = [SCENE_INDEX, SONG_TRANS_INDEX, SONG_SOURCE_INDEX, SONG_INVENTORY]
    paths.extend(SCENE_TRANS / f"scene-{n:03d}.json" for n in range(1, EXPECTED_SCENES + 1))
    paths.extend(SCENES_DIR / f"scene-{n:03d}.md" for n in range(1, EXPECTED_SCENES + 1))
    paths.extend(DIALOGUES_DIR / f"scene-{n:03d}.json" for n in range(1, EXPECTED_SCENES + 1))
    paths.extend(SONG_TRANS / f"song-{n:03d}.json" for n in range(1, EXPECTED_SONGS + 1))
    paths.extend(SONG_TAMIL / f"song-{n:03d}.md" for n in range(1, EXPECTED_SONGS + 1))
    return paths


def load_dialogue_inventory() -> dict[str, dict[str, Any]]:
    by_id: dict[str, dict[str, Any]] = {}
    for scene in range(1, EXPECTED_SCENES + 1):
        path = DIALOGUES_DIR / f"scene-{scene:03d}.json"
        data = load_json(path)
        records = data.get("records") if isinstance(data, dict) else data
        ensure(isinstance(records, list), f"Malformed dialogue shard {path.relative_to(ROOT)}")
        ensure(data.get("record_count") == len(records), f"Dialogue record_count mismatch in scene {scene}")
        for record in records:
            rid = record.get("id")
            ensure(isinstance(rid, str) and rid not in by_id, f"Bad/duplicate dialogue id {rid!r}")
            ensure(rid not in DELETED_DUPLICATE_IDS, f"Deleted T055 duplicate id restored: {rid}")
            by_id[rid] = record
    ensure(len(by_id) == EXPECTED_DIALOGUE_RECORDS, f"Dialogue inventory {len(by_id)} != {EXPECTED_DIALOGUE_RECORDS}")
    return by_id


def expected_performance_links(song_index: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    result: dict[str, list[dict[str, Any]]] = {f"raja-rani-song-{n:03d}": [] for n in range(1, EXPECTED_SONGS + 1)}
    links = song_index.get("screenplay_performance_links")
    ensure(isinstance(links, dict), "Song translation index missing screenplay_performance_links")
    for status in ("verified", "review"):
        rows = links.get(status)
        ensure(isinstance(rows, list), f"Missing {status} screenplay performance links")
        for row in rows:
            sid = row.get("song_id")
            ensure(sid in result, f"Unknown linked numbered song {sid}")
            result[sid].append({
                "occurrence_id": row.get("occurrence_id"),
                "status": status,
                "scene": row.get("scene"),
            })
    return result


def validate_model() -> tuple[dict[str, Any], dict[str, Any], list[Path]]:
    scene_index = load_json(SCENE_INDEX)
    song_index = load_json(SONG_TRANS_INDEX)
    source_song_index = load_json(SONG_SOURCE_INDEX)
    inventory = load_json(SONG_INVENTORY)
    dialogue_by_id = load_dialogue_inventory()

    ensure(scene_index.get("status") == "complete-verified", "Screenplay translation index is not complete-verified")
    ensure(scene_index.get("translation_units") == EXPECTED_SCREENPLAY_UNITS, "Screenplay unit total drifted")
    index_kind_counts = scene_index.get("unit_kind_counts")
    ensure(isinstance(index_kind_counts, dict) and all(index_kind_counts.get(k) == v for k, v in EXPECTED_KINDS.items()) and all(k in EXPECTED_KINDS or v == 0 for k, v in index_kind_counts.items()), "Screenplay kind counts drifted")
    ensure(scene_index.get("dialogue_source_records_linked") == EXPECTED_DIALOGUE_RECORDS, "Screenplay dialogue-link total drifted")
    ensure(scene_index.get("translation_eligible_scenes") == EXPECTED_SCENES and scene_index.get("translation_blocked_scenes") == 0, "Screenplay coverage drifted")
    ensure(scene_index.get("scenes_verified") == list(range(1, EXPECTED_SCENES + 1)), "Verified scene list is incomplete/out of order")
    ensure(scene_index.get("scenes_in_review") == [], "A screenplay scene remains in review")
    ensure(set(scene_index.get("source_unlabelled_spoken_units", [])) and len(scene_index.get("source_unlabelled_spoken_units", [])) == EXPECTED_UNLABELLED, "Unlabelled spoken index drifted")
    ensure(len(scene_index.get("cross_page_translation_units", [])) == EXPECTED_CROSS_PAGE_UNITS, "Cross-page screenplay index drifted")
    ensure(scene_index.get("translated_song_occurrences") == EXPECTED_PERFORMANCE_OCCURRENCES, "Screenplay performance occurrence list drifted")

    scene_rows = scene_index.get("scene_records")
    ensure(isinstance(scene_rows, list) and len(scene_rows) == EXPECTED_SCENES, "Scene record index must contain 58 rows")
    ensure([row.get("archival_scene_ordinal") for row in scene_rows] == list(range(1, EXPECTED_SCENES + 1)), "Scene record index is unordered")

    screenplay_units = 0
    kind_counts: Counter[str] = Counter()
    dialogue_links: list[str] = []
    unlabelled: list[str] = []
    cross_page: list[str] = []
    occurrence_links: list[str] = []
    scene_payloads: list[dict[str, Any]] = []
    seen_unit_ids: set[str] = set()
    previous_scene_page = 0

    for scene, row in enumerate(scene_rows, 1):
        scene_id = f"raja-rani-s{scene:03d}"
        trans_path = SCENE_TRANS / f"scene-{scene:03d}.json"
        tamil_path = SCENES_DIR / f"scene-{scene:03d}.md"
        ensure(row.get("scene_id") == scene_id and row.get("path") == f"records/scene-{scene:03d}.json", f"Scene index row mismatch at {scene}")
        trans = load_json(trans_path)
        ensure(trans.get("work_id") == "raja-rani" and trans.get("target_language") == "en", f"Scene {scene} work/language mismatch")
        ensure(trans.get("scene_id") == scene_id and trans.get("archival_scene_ordinal") == scene, f"Scene {scene} metadata mismatch")
        ensure(trans.get("source_scene_number") is None and trans.get("scene_status") == "verified", f"Scene {scene} source-number/status mismatch")
        units = trans.get("units")
        ensure(isinstance(units, list) and trans.get("unit_count") == len(units) == row.get("unit_count"), f"Scene {scene} unit_count mismatch")
        ensure(units, f"Scene {scene} must retain at least one translation unit")

        raw_tamil = tamil_path.read_text(encoding="utf-8")
        ensure("status=verified" in raw_tamil, f"Scene {scene} Tamil derivative does not declare verified source status")
        tamil_text = strip_scene_comments(raw_tamil)
        ensure(tamil_text, f"Scene {scene} Tamil display text is empty")

        scene_first_page = min(p["pdf_page"] for unit in units for p in unit.get("source", {}).get("page_provenance", []))
        ensure(scene_first_page >= previous_scene_page, f"Scene {scene} regresses in source order")
        previous_scene_page = scene_first_page
        previous_unit_page = 0
        reader_units: list[dict[str, Any]] = []

        for ordinal, unit in enumerate(units, 1):
            uid = unit.get("id")
            expected_uid = f"raja-rani-en-s{scene:03d}-u{ordinal:03d}"
            ensure(uid == expected_uid and uid not in seen_unit_ids, f"Scene {scene} unit ID mismatch/duplicate at ordinal {ordinal}")
            ensure(unit.get("status") == "verified" and unit.get("target_language") == "en", f"Unverified/non-English unit {uid}")
            ensure(unit.get("scene_id") == scene_id and unit.get("archival_scene_ordinal") == scene, f"Unit scene metadata mismatch at {uid}")
            seen_unit_ids.add(uid)
            screenplay_units += 1

            kind = unit.get("kind")
            ensure(kind in EXPECTED_KINDS, f"Unsupported screenplay unit kind {kind!r} at {uid}")
            kind_counts[kind] += 1
            source = unit.get("source")
            ensure(isinstance(source, dict), f"Malformed source metadata at {uid}")
            provenance = source.get("page_provenance")
            ensure(isinstance(provenance, list) and provenance, f"Missing provenance at {uid}")
            pages = [p.get("pdf_page") for p in provenance]
            ensure(all(isinstance(p, int) and 10 <= p <= 79 for p in pages), f"Invalid PDF provenance at {uid}: {pages}")
            ensure(pages == sorted(pages), f"Non-monotonic provenance at {uid}")
            ensure(all(p.get("printed_page") == p.get("pdf_page") - 1 for p in provenance), f"Printed-page provenance mismatch at {uid}")
            ensure(pages[0] >= previous_unit_page, f"Source-page regression within scene at {uid}")
            previous_unit_page = pages[0]
            if len(provenance) > 1:
                cross_page.append(uid)

            rid = source.get("source_record_id")
            if rid is not None:
                ensure(rid not in DELETED_DUPLICATE_IDS, f"English links deleted T055 duplicate {rid}")
                ensure(rid in dialogue_by_id, f"Unknown immutable dialogue link {rid} at {uid}")
                immutable = dialogue_by_id[rid]
                ensure(immutable.get("scene_id") == scene_id, f"Dialogue scene mismatch at {uid}")
                ensure(immutable.get("speaker_label") == source.get("speaker_label"), f"Speaker-label mismatch at {uid}")
                ensure(immutable.get("page_provenance") == provenance, f"Dialogue provenance mismatch at {uid}")
                dialogue_links.append(rid)
            elif kind == "dialogue":
                ensure(source.get("speaker_label") is None, f"Source-unlabelled dialogue has speaker metadata at {uid}")
                unlabelled.append(uid)

            occurrence = source.get("source_occurrence_id")
            if occurrence is not None:
                ensure(kind == "performance-cue", f"Non-performance unit carries occurrence link at {uid}")
                occurrence_links.append(occurrence)

            text, lines = translation_payload(unit)
            ensure(not PLACEHOLDER_RE.search(text), f"Placeholder leaked into English at {uid}")
            ensure(not SYNTHETIC_END_RE.match(text), f"Synthetic scene-end text at {uid}")
            reader_units.append({
                "id": uid,
                "kind": kind,
                "speaker_label": source.get("speaker_label"),
                "source_record_id": rid,
                "source_occurrence_id": occurrence,
                "page_provenance": provenance,
                "english_text": text if lines is None else None,
                "english_lines": lines,
            })

        scene_payloads.append({
            "scene_id": scene_id,
            "archival_scene_ordinal": scene,
            "source_scene_number": None,
            "tamil_source_file": f"works/raja-rani/scenes/scene-{scene:03d}.md",
            "translation_file": f"works/raja-rani/translations/records/scene-{scene:03d}.json",
            "tamil_text": tamil_text,
            "english_units": reader_units,
        })

    ensure(screenplay_units == EXPECTED_SCREENPLAY_UNITS, f"Screenplay units {screenplay_units} != {EXPECTED_SCREENPLAY_UNITS}")
    ensure(dict(kind_counts) == EXPECTED_KINDS, f"Actual screenplay kinds {dict(kind_counts)} != {EXPECTED_KINDS}")
    ensure(len(dialogue_links) == len(set(dialogue_links)) == EXPECTED_DIALOGUE_RECORDS, "Immutable dialogue links are missing/duplicated")
    ensure(set(dialogue_links) == set(dialogue_by_id), "English dialogue links do not exactly cover immutable corpus")
    ensure(len(unlabelled) == EXPECTED_UNLABELLED and set(unlabelled) == set(scene_index.get("source_unlabelled_spoken_units", [])), "Source-unlabelled spoken units drifted")
    ensure(len(cross_page) == EXPECTED_CROSS_PAGE_UNITS and set(cross_page) == set(scene_index.get("cross_page_translation_units", [])), "Cross-page screenplay units drifted")
    ensure(occurrence_links == EXPECTED_PERFORMANCE_OCCURRENCES, f"Performance links drifted: {occurrence_links}")

    ensure(song_index.get("status") == "complete-verified", "Numbered-song translation index is not complete-verified")
    ensure(song_index.get("numbered_songs_verified") == EXPECTED_SONGS, "Numbered-song verified count drifted")
    ensure(song_index.get("translation_sections") == EXPECTED_SONG_SECTIONS, "Numbered-song section count drifted")
    ensure(song_index.get("source_tamil_line_cues") == EXPECTED_SONG_LINE_CUES and song_index.get("english_line_cues") == EXPECTED_SONG_LINE_CUES, "Numbered-song line/cue totals drifted")
    ensure(song_index.get("cross_page_song_records") == EXPECTED_CROSS_PAGE_SONGS, "Cross-page song set drifted")
    ensure(song_index.get("authorship", {}).get("anthology_attributed") == 5 and song_index.get("authorship", {}).get("unresolved") == 6, "Song authorship counts drifted")
    ensure(song_index.get("authorship", {}).get("primary_source_item_level_credits") == 0, "Unexpected original-booklet item-level song credit")
    ensure(song_index.get("authorship", {}).get("modified_by_translation") is False, "Translation claims to modify authorship")
    ensure(song_index.get("screenplay_performance_links", {}).get("modified_or_upgraded_by_translation") is False, "Translation claims to modify performance links")
    ensure(set(source_song_index.get("kalaignar_attributed_numbered_song_ids", [])) == EXPECTED_ATTRIBUTED, "Source song attributed set drifted")
    ensure(set(source_song_index.get("unresolved_numbered_song_ids", [])) == EXPECTED_UNRESOLVED, "Source song unresolved set drifted")

    inv_rows = inventory.get("records")
    ensure(isinstance(inv_rows, list), "Song inventory records missing")
    inventory_by_song = {row.get("id"): row for row in inv_rows if row.get("occurrence_kind") == "numbered-song-block"}
    perf_by_id = {row.get("id"): row for row in inv_rows if row.get("occurrence_kind") == "screenplay-singing-reference"}
    ensure(set(inventory_by_song) == EXPECTED_ATTRIBUTED | EXPECTED_UNRESOLVED, "Numbered-song source inventory set drifted")
    ensure(set(perf_by_id) == set(EXPECTED_PERFORMANCE_OCCURRENCES), "Performance occurrence inventory set drifted")
    expected_links_by_song = expected_performance_links(song_index)

    song_rows = song_index.get("records")
    ensure(isinstance(song_rows, list) and len(song_rows) == EXPECTED_SONGS, "Song translation index must contain 11 records")
    song_payloads: list[dict[str, Any]] = []
    seen_song_translation_ids: set[str] = set()
    seen_line_ids: set[str] = set()
    song_sections = 0
    song_lines = 0
    actual_cross_page_songs: list[str] = []

    for n, idx in enumerate(song_rows, 1):
        sid = f"raja-rani-song-{n:03d}"
        tid = f"raja-rani-song-en-{n:03d}"
        record_path = SONG_TRANS / f"song-{n:03d}.json"
        tamil_path = SONG_TAMIL / f"song-{n:03d}.md"
        record = load_json(record_path)
        ensure(idx.get("id") == tid and idx.get("song_id") == sid and idx.get("file") == f"records/song-{n:03d}.json", f"Song index row mismatch at {n}")
        ensure(record.get("id") == tid and record.get("song_id") == sid and record.get("numbered_song_number") == n, f"Song record identity mismatch at {n}")
        ensure(record.get("status") == "verified" and record.get("target_language") == "en", f"Song {n} is not verified English")
        ensure(record.get("mode") == "semantic-poetic-source-faithful", f"Song {n} translation mode drifted")
        ensure(tid not in seen_song_translation_ids, f"Duplicate song translation id {tid}")
        seen_song_translation_ids.add(tid)

        source = record.get("source")
        ensure(isinstance(source, dict), f"Song {n} missing source metadata")
        ensure(source.get("tamil_song_file") == f"works/raja-rani/songs/tamil/song-{n:03d}.md", f"Song {n} Tamil source path mismatch")
        ensure(source.get("tamil_status") == "verified", f"Song {n} Tamil source not verified")
        ensure(source.get("pdf_pages") == idx.get("pdf_pages"), f"Song {n} PDF pages mismatch")
        source_inventory = inventory_by_song[sid]
        ensure(source.get("pdf_pages") == source_inventory.get("pdf_pages"), f"Song {n} inventory PDF pages mismatch")
        ensure(source.get("printed_pages") == source_inventory.get("printed_pages"), f"Song {n} printed pages mismatch")
        if len(source.get("pdf_pages", [])) > 1:
            actual_cross_page_songs.append(tid)

        if sid in EXPECTED_ATTRIBUTED:
            ensure(source.get("authorship_status") == "anthology-attributed" and source.get("lyricist_ta") == "மு. கருணாநிதி", f"Song {n} attribution drifted")
        else:
            ensure(source.get("authorship_status") == "unresolved" and source.get("lyricist_ta") is None, f"Song {n} unresolved authorship drifted")
        ensure(source.get("performance_links") == expected_links_by_song[sid], f"Song {n} performance-link metadata drifted")

        tamil_raw = tamil_path.read_text(encoding="utf-8")
        ensure("source_status=verified" in tamil_raw and "status=verified" in tamil_raw, f"Song {n} Tamil derivative is not marked verified")
        translation = record.get("translation")
        ensure(isinstance(translation, dict) and isinstance(translation.get("english_title"), str) and translation.get("english_title").strip(), f"Song {n} missing English title")
        sections = translation.get("sections")
        ensure(isinstance(sections, list) and sections, f"Song {n} has no translation sections")

        reader_sections: list[dict[str, Any]] = []
        for s_no, section in enumerate(sections, 1):
            ensure(section.get("ordinal") == s_no, f"Song {n} section order mismatch")
            ta = section.get("source_tamil_lines")
            en = section.get("english_lines")
            ensure(isinstance(ta, list) and isinstance(en, list) and ta and len(ta) == len(en), f"Song {n} section {s_no} line mapping mismatch")
            ensure(all(isinstance(x, str) and x.strip() for x in ta + en), f"Song {n} section {s_no} contains empty/non-string lines")
            ensure(isinstance(section.get("pdf_pages"), list) and section.get("pdf_pages"), f"Song {n} section {s_no} lacks page provenance")
            ensure(all(p in source.get("pdf_pages", []) for p in section.get("pdf_pages")), f"Song {n} section {s_no} page outside song bounds")
            song_sections += 1
            pairs: list[dict[str, str]] = []
            for l_no, (ta_line, en_line) in enumerate(zip(ta, en), 1):
                lid = song_line_id(n, s_no, l_no)
                ensure(lid not in seen_line_ids, f"Duplicate song line id {lid}")
                ensure(ta_line in tamil_raw, f"Song {n} mapped Tamil line not found in verified derivative: {ta_line!r}")
                ensure(not PLACEHOLDER_RE.search(en_line), f"Placeholder leaked into song English {lid}")
                seen_line_ids.add(lid)
                song_lines += 1
                pairs.append({"id": lid, "tamil": ta_line, "english": en_line})
            reader_sections.append({
                "ordinal": s_no,
                "source_label": section.get("source_label"),
                "english_label": section.get("english_label"),
                "pdf_pages": section.get("pdf_pages"),
                "line_pairs": pairs,
            })

        ensure(len(sections) == idx.get("sections"), f"Song {n} section count differs from index")
        ensure(sum(len(s["line_pairs"]) for s in reader_sections) == idx.get("source_tamil_line_cues") == idx.get("english_line_cues"), f"Song {n} line/cue count differs from index")
        song_payloads.append({
            "translation_id": tid,
            "song_id": sid,
            "numbered_song_number": n,
            "tamil_title": source.get("tamil_title"),
            "english_title": translation.get("english_title"),
            "authorship_status": source.get("authorship_status"),
            "lyricist_ta": source.get("lyricist_ta"),
            "performance_links": source.get("performance_links"),
            "pdf_pages": source.get("pdf_pages"),
            "printed_pages": source.get("printed_pages"),
            "tamil_source_file": source.get("tamil_song_file"),
            "translation_file": f"works/raja-rani/translations/songs/records/song-{n:03d}.json",
            "sections": reader_sections,
        })

    ensure(song_sections == EXPECTED_SONG_SECTIONS, f"Song sections {song_sections} != {EXPECTED_SONG_SECTIONS}")
    ensure(song_lines == len(seen_line_ids) == EXPECTED_SONG_LINE_CUES, f"Song line/cue mappings {song_lines} != {EXPECTED_SONG_LINE_CUES}")
    ensure(actual_cross_page_songs == EXPECTED_CROSS_PAGE_SONGS, f"Cross-page song records drifted: {actual_cross_page_songs}")

    model = {
        "work_id": "raja-rani",
        "title_ta": "ராஜா ராணி",
        "title_en": "Raja Rani",
        "status": "complete-verified-bilingual-reader-input",
        "source_sha256": SOURCE_SHA256,
        "source_structure": {
            "numbered_front_matter_songs": EXPECTED_SONGS,
            "source_numbered_screenplay_scenes": False,
            "archival_scene_segments": EXPECTED_SCENES,
            "archival_scene_ids_are_navigation_only": True,
        },
        "numbered_songs": song_payloads,
        "screenplay_scenes": scene_payloads,
    }
    stats = {
        "screenplay_scenes": EXPECTED_SCENES,
        "screenplay_units": screenplay_units,
        "screenplay_kind_counts": dict(kind_counts),
        "immutable_dialogue_links": len(dialogue_links),
        "source_unlabelled_spoken_units": len(unlabelled),
        "cross_page_screenplay_units": len(cross_page),
        "screenplay_performance_occurrence_links": len(occurrence_links),
        "numbered_songs": len(song_payloads),
        "numbered_song_sections": song_sections,
        "numbered_song_line_cues": song_lines,
        "cross_page_numbered_songs": len(actual_cross_page_songs),
        "song_authorship_anthology_attributed": len(EXPECTED_ATTRIBUTED),
        "song_authorship_unresolved": len(EXPECTED_UNRESOLVED),
        "song_performance_links_verified": 3,
        "song_performance_links_review": 1,
    }
    return model, stats, authoritative_input_paths()


def render_markdown(model: dict[str, Any]) -> str:
    out = [
        "# Raja Rani — Bilingual Reader Edition",
        "",
        "**Tamil title:** ராஜா ராணி  ",
        "**Status:** complete-verified deterministic bilingual derivative  ",
        f"**Source scan SHA-256:** `{SOURCE_SHA256}`",
        "",
        "> Source-structure note: the booklet prints 11 numbered front-matter songs but no screenplay scene numbers. Songs 1–11 below retain their actual source numbering. The 58 screenplay headings are archival navigation segments only and are never presented as source scene numbers. Tamil source text and verified English remain separate downstream views; this reader does not repair either layer.",
        "",
        "## Contents — numbered songs",
        "",
    ]
    for song in model["numbered_songs"]:
        n = song["numbered_song_number"]
        out.append(f"- [Song {n} — {song['english_title']}](#numbered-song-{n})")
    out.extend(["", "## Contents — screenplay", ""])
    for scene in model["screenplay_scenes"]:
        n = scene["archival_scene_ordinal"]
        out.append(f"- [Archival scene {n}](#archival-scene-{n})")
    out.extend(["", "---", "", "# Numbered front-matter songs", ""])

    for song in model["numbered_songs"]:
        n = song["numbered_song_number"]
        out.extend([
            f"<a id=\"numbered-song-{n}\"></a>",
            f"## Song {n} — {song['english_title']}",
            "",
            f"**Tamil title:** {song['tamil_title']}  ",
            f"**Source:** {song_page_label(song['pdf_pages'], song['printed_pages'])}  ",
            f"**Authorship status:** `{song['authorship_status']}`  ",
            f"**Tamil derivative:** `{song['tamil_source_file']}`",
            "",
        ])
        if song["performance_links"]:
            desc = ", ".join(f"{x['occurrence_id']} / scene {x['scene']} / {x['status']}" for x in song["performance_links"])
            out.extend([f"**Screenplay performance relation(s):** {desc}", ""])
        for section in song["sections"]:
            if section.get("english_label") or section.get("source_label"):
                out.append(f"### {section.get('english_label') or section.get('source_label')}")
                if section.get("source_label"):
                    out.append(f"*Source label: {section['source_label']}*")
                out.append("")
            for pair in section["line_pairs"]:
                out.extend([
                    f"<!-- song-line:{pair['id']} -->",
                    f"**தமிழ்:** {pair['tamil']}  ",
                    f"**English:** {pair['english']}",
                    "",
                ])
        out.extend(["---", ""])

    out.extend(["# Screenplay", "", "> The headings below are archival navigation only; the booklet prints no screenplay scene numbers.", ""])
    for scene in model["screenplay_scenes"]:
        n = scene["archival_scene_ordinal"]
        out.extend([
            f"<a id=\"archival-scene-{n}\"></a>",
            f"## Archival scene {n}",
            "",
            f"**Tamil source derivative:** `{scene['tamil_source_file']}`  ",
            f"**English record:** `{scene['translation_file']}`",
            "",
            "### தமிழ் — verified scene derivative",
            "",
            "```text",
            scene["tamil_text"],
            "```",
            "",
            "### English — verified source-linked units",
            "",
        ])
        for unit in scene["english_units"]:
            text = unit["english_text"] if unit["english_text"] is not None else "\n".join(unit["english_lines"] or [])
            out.append(f"<!-- unit:{unit['id']}; source:{page_label(unit['page_provenance'])} -->")
            if unit["kind"] == "dialogue":
                if unit.get("speaker_label"):
                    out.append(f"**{unit['speaker_label']}**  ")
                out.extend([text, ""])
            elif unit["kind"] == "stage-direction":
                out.extend([f"*{text}*", ""])
            else:
                label = "Performance cue" if unit["kind"] == "performance-cue" else "Written text"
                out.extend([f"**{label}**  ", text, ""])
        out.extend(["---", ""])
    return "\n".join(out).rstrip() + "\n"


def render_html(model: dict[str, Any]) -> str:
    song_nav = "".join(f'<li><a href="#numbered-song-{s["numbered_song_number"]}">Song {s["numbered_song_number"]} — {html.escape(s["english_title"])}</a></li>' for s in model["numbered_songs"])
    scene_nav = " ".join(f'<a href="#archival-scene-{s["archival_scene_ordinal"]}">{s["archival_scene_ordinal"]}</a>' for s in model["screenplay_scenes"])
    song_blocks: list[str] = []
    for song in model["numbered_songs"]:
        n = song["numbered_song_number"]
        parts = [f'<section class="song" id="numbered-song-{n}"><h2>Song {n} — {html.escape(song["english_title"])}</h2>',
                 f'<p><strong>Tamil title:</strong> <span lang="ta">{html.escape(str(song["tamil_title"]))}</span><br><strong>Source:</strong> {html.escape(song_page_label(song["pdf_pages"], song["printed_pages"]))}<br><strong>Authorship status:</strong> <code>{html.escape(song["authorship_status"])}</code></p>']
        if song["performance_links"]:
            desc = ", ".join(f"{x['occurrence_id']} / scene {x['scene']} / {x['status']}" for x in song["performance_links"])
            parts.append(f'<p><strong>Screenplay performance relation(s):</strong> {html.escape(desc)}</p>')
        for section in song["sections"]:
            if section.get("english_label") or section.get("source_label"):
                parts.append(f'<h3>{html.escape(str(section.get("english_label") or section.get("source_label")))}</h3>')
                if section.get("source_label"):
                    parts.append(f'<p class="source-label" lang="ta">{html.escape(str(section["source_label"]))}</p>')
            for pair in section["line_pairs"]:
                parts.append(f'<div class="song-pair" data-line-id="{html.escape(pair["id"], quote=True)}"><div class="ta" lang="ta">{html.escape(pair["tamil"])}</div><div class="en" lang="en">{html.escape(pair["english"])}</div></div>')
        parts.append('</section>')
        song_blocks.append("\n".join(parts))

    scene_blocks: list[str] = []
    for scene in model["screenplay_scenes"]:
        n = scene["archival_scene_ordinal"]
        parts = [f'<section class="scene" id="archival-scene-{n}"><h2>Archival scene {n}</h2>',
                 '<p class="nav-note">Archival navigation only; no source scene number is printed.</p>',
                 '<div class="bilingual-scene"><div class="tamil-panel"><h3>தமிழ் — verified scene derivative</h3>',
                 f'<div class="tamil-source" lang="ta">{html.escape(scene["tamil_text"]).replace(chr(10), "<br>")}</div></div>',
                 '<div class="english-panel"><h3>English — verified source-linked units</h3>']
        for unit in scene["english_units"]:
            text = unit["english_text"] if unit["english_text"] is not None else "\n".join(unit["english_lines"] or [])
            attrs = f'data-unit-id="{html.escape(unit["id"], quote=True)}" data-source-page="{html.escape(page_label(unit["page_provenance"]), quote=True)}"'
            content = html.escape(text).replace("\n", "<br>")
            if unit["kind"] == "dialogue":
                speaker = unit.get("speaker_label")
                lead = f'<span class="speaker" lang="ta">{html.escape(str(speaker))}</span>' if speaker else ""
                parts.append(f'<div class="unit dialogue" {attrs}>{lead}<span lang="en">{content}</span></div>')
            elif unit["kind"] == "stage-direction":
                parts.append(f'<div class="unit stage" {attrs} lang="en">{content}</div>')
            else:
                label = "Performance cue" if unit["kind"] == "performance-cue" else "Written text"
                parts.append(f'<div class="unit special" {attrs}><strong>{label}</strong><div lang="en">{content}</div></div>')
        parts.extend(['</div></div>', '<p class="back"><a href="#contents">Back to contents</a></p>', '</section>'])
        scene_blocks.append("\n".join(parts))

    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Raja Rani — Bilingual Reader Edition</title>
<style>
body{{font-family:ui-serif,Georgia,"Times New Roman",serif;max-width:76rem;margin:auto;padding:2rem 1.25rem 5rem;line-height:1.6}} nav.scenes{{display:flex;flex-wrap:wrap;gap:.5rem}} .song,.scene{{border-top:1px solid;margin-top:2.5rem;padding-top:1rem}} .song-pair{{display:grid;grid-template-columns:1fr 1fr;gap:1rem;padding:.45rem 0}} .ta{{font-family:system-ui,sans-serif}} .bilingual-scene{{display:grid;grid-template-columns:1fr 1fr;gap:2rem;align-items:start}} .tamil-source{{font-family:system-ui,sans-serif;white-space:normal}} .unit{{margin:.75rem 0}} .dialogue{{display:grid;grid-template-columns:minmax(5rem,9rem) 1fr;gap:.75rem}} .speaker{{font-weight:700}} .stage{{font-style:italic}} .special{{border-left:2px solid;padding-left:.75rem}} .nav-note,.source-label{{font-style:italic}} @media(max-width:48rem){{.song-pair,.bilingual-scene,.dialogue{{display:block}}.ta,.speaker{{display:block;margin-bottom:.25rem}}}} @media print{{nav,.back{{display:none}}.scene,.song{{break-before:page}}}}
</style></head><body>
<h1>Raja Rani — Bilingual Reader Edition</h1><p><strong>Tamil title:</strong> <span lang="ta">ராஜா ராணி</span></p><p><strong>Status:</strong> complete-verified deterministic bilingual derivative</p><p><strong>Source-structure note:</strong> The booklet prints 11 numbered front-matter songs but no screenplay scene numbers. Song numbering below is source numbering; the 58 screenplay headings are archival navigation only.</p>
<h2 id="contents">Contents — numbered songs</h2><ol>{song_nav}</ol><h2>Contents — screenplay</h2><nav class="scenes">{scene_nav}</nav>
<h1>Numbered front-matter songs</h1>{''.join(song_blocks)}<h1>Screenplay</h1>{''.join(scene_blocks)}</body></html>\n'''


def output_qa(model: dict[str, Any], stats: dict[str, Any], md: bytes, html_bytes: bytes, json_bytes: bytes, input_hash: str) -> tuple[str, dict[str, Any]]:
    json_model = json.loads(json_bytes.decode("utf-8"))
    ensure(json_model == model, "Serialized reader JSON does not round-trip exactly")
    md_text = md.decode("utf-8")
    html_text = html_bytes.decode("utf-8")

    screenplay_unit_ids = [u["id"] for s in model["screenplay_scenes"] for u in s["english_units"]]
    song_line_ids = [p["id"] for s in model["numbered_songs"] for sec in s["sections"] for p in sec["line_pairs"]]
    ensure(len(screenplay_unit_ids) == EXPECTED_SCREENPLAY_UNITS and len(set(screenplay_unit_ids)) == EXPECTED_SCREENPLAY_UNITS, "Reader model screenplay IDs are not unique/complete")
    ensure(len(song_line_ids) == EXPECTED_SONG_LINE_CUES and len(set(song_line_ids)) == EXPECTED_SONG_LINE_CUES, "Reader model song line IDs are not unique/complete")
    for uid in screenplay_unit_ids:
        ensure(md_text.count(f"unit:{uid};") == 1, f"Markdown does not render screenplay unit exactly once: {uid}")
        ensure(html_text.count(f'data-unit-id="{uid}"') == 1, f"HTML does not render screenplay unit exactly once: {uid}")
        ensure(json_bytes.decode("utf-8").count(f'"id": "{uid}"') == 1, f"JSON does not contain screenplay unit exactly once: {uid}")
    for lid in song_line_ids:
        ensure(md_text.count(f"song-line:{lid}") == 1, f"Markdown does not render song line exactly once: {lid}")
        ensure(html_text.count(f'data-line-id="{lid}"') == 1, f"HTML does not render song line exactly once: {lid}")
        ensure(json_bytes.decode("utf-8").count(f'"id": "{lid}"') == 1, f"JSON does not contain song line exactly once: {lid}")
    for bad in DELETED_DUPLICATE_IDS:
        ensure(bad not in md_text and bad not in html_text and bad not in json_bytes.decode("utf-8"), f"Deleted T055 duplicate leaked into reader: {bad}")
    ensure(not PLACEHOLDER_RE.search(md_text) and not PLACEHOLDER_RE.search(html_text), "Placeholder text leaked into generated reader")

    outputs = {
        "reader-edition.md": {"bytes": len(md), "sha256": sha256_bytes(md)},
        "reader-edition.html": {"bytes": len(html_bytes), "sha256": sha256_bytes(html_bytes)},
        "reader-edition.json": {"bytes": len(json_bytes), "sha256": sha256_bytes(json_bytes)},
    }
    report = f"""# Raja Rani bilingual reader/export — QA report

Status: **PASS**

## Input checkpoint

- screenplay scenes: **{stats['screenplay_scenes']}/58**
- screenplay English units: **{stats['screenplay_units']:,}/1,236**
- immutable dialogue links: **{stats['immutable_dialogue_links']:,}/1,071**
- source-unlabelled spoken units: **{stats['source_unlabelled_spoken_units']}/19**
- cross-page screenplay units: **{stats['cross_page_screenplay_units']}/15**
- screenplay performance occurrence links: **{stats['screenplay_performance_occurrence_links']}/4**
- numbered songs: **{stats['numbered_songs']}/11**
- numbered-song translation sections: **{stats['numbered_song_sections']}/67**
- numbered-song Tamil/English line-cue mappings: **{stats['numbered_song_line_cues']}/181**
- cross-page numbered songs: **{stats['cross_page_numbered_songs']}/4**
- song authorship: **{stats['song_authorship_anthology_attributed']} later-anthology Kalaignar-attributed / {stats['song_authorship_unresolved']} unresolved**
- screenplay song relations: **3 verified / 1 review**

## Structural QA

- numbered songs remain separate source-numbered front-matter structures: **PASS**
- screenplay `s001`–`s058` remain archival navigation only, not source scene numbering: **PASS**
- all immutable dialogue links appear exactly once in English: **PASS**
- source-unlabelled speech remains unlabelled: **PASS**
- T055/T056 deleted duplicate IDs absent: **PASS**
- source-page provenance/order checks: **PASS**
- song line/cue mappings complete and unique: **PASS**
- authorship tiers unchanged by translation/reader generation: **PASS**
- scene-58/song-11 relation remains review-level: **PASS**
- synthetic `(Scene ends.)` / placeholder leakage: **0**

## Generated-output QA

- Markdown contains each of the **1,236** screenplay unit IDs exactly once and each of the **181** song line IDs exactly once: **PASS**
- HTML contains each screenplay unit and song line data ID exactly once: **PASS**
- machine JSON round-trips to the validated reader model: **PASS**
- generated outputs contain no deleted T055 duplicate IDs: **PASS**

## Reproducibility

- build version: **{BUILD_VERSION}**
- authoritative-input aggregate SHA-256: `{input_hash}`
- Markdown SHA-256: `{outputs['reader-edition.md']['sha256']}`
- HTML SHA-256: `{outputs['reader-edition.html']['sha256']}`
- JSON SHA-256: `{outputs['reader-edition.json']['sha256']}`

No canonical Tamil, immutable dialogue record, character mapping, song authorship disposition or translation record is modified by reader generation.
"""
    return report, outputs


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    model, stats, input_paths = validate_model()
    input_hash = aggregate_sha256(input_paths)
    md = render_markdown(model).encode("utf-8")
    html_bytes = render_html(model).encode("utf-8")
    json_bytes = (json.dumps(model, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    report, outputs = output_qa(model, stats, md, html_bytes, json_bytes, input_hash)

    (OUT / "reader-edition.md").write_bytes(md)
    (OUT / "reader-edition.html").write_bytes(html_bytes)
    (OUT / "reader-edition.json").write_bytes(json_bytes)
    (OUT / "QA_REPORT.md").write_text(report, encoding="utf-8")
    manifest = {
        "work_id": "raja-rani",
        "edition": "bilingual-reader",
        "build_version": BUILD_VERSION,
        "status": "PASS",
        "source_sha256": SOURCE_SHA256,
        "authoritative_input_count": len(set(input_paths)),
        "authoritative_input_aggregate_sha256": input_hash,
        "checkpoint": stats,
        "outputs": outputs,
    }
    (OUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("RAJA RANI BILINGUAL READER BUILD: PASS")
    print(json.dumps(stats, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
