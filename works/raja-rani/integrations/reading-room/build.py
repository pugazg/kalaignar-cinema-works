#!/usr/bin/env python3
"""Build and QA the Raja Rani Reading Room integration payload."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

BUILD_VERSION = 1
ROOT = Path(__file__).resolve().parents[4]
WORK = ROOT / "works" / "raja-rani"
READER_DIR = WORK / "editions" / "en"
READER_JSON = READER_DIR / "reader-edition.json"
READER_MANIFEST = READER_DIR / "manifest.json"
OUT = WORK / "integrations" / "reading-room"

SOURCE_SHA256 = "26ecc026b89deafac94bb3b107ee7c5f361c68796c4a1cdf4d01ad7c1c0d31a4"
EXPECTED_SCENES = 58
EXPECTED_UNITS = 1236
EXPECTED_DIALOGUE_LINKS = 1071
EXPECTED_UNLABELLED = 19
EXPECTED_CROSS_PAGE = 15
EXPECTED_PERFORMANCE_LINKS = 4
EXPECTED_SONGS = 11
EXPECTED_SONG_SECTIONS = 67
EXPECTED_SONG_LINES = 181
EXPECTED_CROSS_PAGE_SONGS = 4
DELETED_DUPLICATE_IDS = {
    "raja-rani-s055-d026",
    "raja-rani-s055-d027",
    "raja-rani-s055-d028",
    "raja-rani-s055-d029",
    "raja-rani-s055-d030",
}
PLACEHOLDER_RE = re.compile(r"\b(?:TODO|TBD|FIXME)\b|\[\[\?\]\]|\{\{.+?\}\}", re.I)


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
    for path in sorted(paths, key=lambda p: p.as_posix()):
        ensure(path.exists(), f"Missing integration input {path.relative_to(ROOT)}")
        digest.update(path.relative_to(ROOT).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def validate_reader() -> tuple[dict[str, Any], dict[str, Any]]:
    reader = load_json(READER_JSON)
    manifest = load_json(READER_MANIFEST)
    ensure(manifest.get("status") == "PASS", "Reader manifest is not PASS")
    ensure(manifest.get("source_sha256") == SOURCE_SHA256, "Reader source SHA drifted")
    checkpoint = manifest.get("checkpoint")
    ensure(isinstance(checkpoint, dict), "Reader manifest checkpoint missing")
    expected_checkpoint = {
        "screenplay_scenes": EXPECTED_SCENES,
        "screenplay_units": EXPECTED_UNITS,
        "immutable_dialogue_links": EXPECTED_DIALOGUE_LINKS,
        "source_unlabelled_spoken_units": EXPECTED_UNLABELLED,
        "cross_page_screenplay_units": EXPECTED_CROSS_PAGE,
        "screenplay_performance_occurrence_links": EXPECTED_PERFORMANCE_LINKS,
        "numbered_songs": EXPECTED_SONGS,
        "numbered_song_sections": EXPECTED_SONG_SECTIONS,
        "numbered_song_line_cues": EXPECTED_SONG_LINES,
        "cross_page_numbered_songs": EXPECTED_CROSS_PAGE_SONGS,
        "song_authorship_anthology_attributed": 5,
        "song_authorship_unresolved": 6,
        "song_performance_links_verified": 3,
        "song_performance_links_review": 1,
    }
    for key, value in expected_checkpoint.items():
        ensure(checkpoint.get(key) == value, f"Reader manifest checkpoint drifted for {key}")

    ensure(reader.get("work_id") == "raja-rani" and reader.get("source_sha256") == SOURCE_SHA256, "Reader work/source identity mismatch")
    structure = reader.get("source_structure")
    ensure(isinstance(structure, dict), "Reader source_structure missing")
    ensure(structure.get("numbered_front_matter_songs") == EXPECTED_SONGS, "Reader numbered-song structure drifted")
    ensure(structure.get("source_numbered_screenplay_scenes") is False, "Reader incorrectly claims source-numbered screenplay scenes")
    ensure(structure.get("archival_scene_segments") == EXPECTED_SCENES and structure.get("archival_scene_ids_are_navigation_only") is True, "Reader archival scene semantics drifted")

    songs = reader.get("numbered_songs")
    scenes = reader.get("screenplay_scenes")
    ensure(isinstance(songs, list) and len(songs) == EXPECTED_SONGS, "Reader must contain 11 numbered songs")
    ensure(isinstance(scenes, list) and len(scenes) == EXPECTED_SCENES, "Reader must contain 58 screenplay scenes")

    seen_song_ids: set[str] = set()
    seen_song_line_ids: set[str] = set()
    song_sections = 0
    song_lines = 0
    cross_page_songs = 0
    attributed = 0
    unresolved = 0
    verified_perf = 0
    review_perf = 0
    for n, song in enumerate(songs, 1):
        sid = f"raja-rani-song-{n:03d}"
        tid = f"raja-rani-song-en-{n:03d}"
        ensure(song.get("song_id") == sid and song.get("translation_id") == tid and song.get("numbered_song_number") == n, f"Reader song identity/order mismatch at {n}")
        ensure(sid not in seen_song_ids, f"Duplicate reader song id {sid}")
        seen_song_ids.add(sid)
        pages = song.get("pdf_pages")
        ensure(isinstance(pages, list) and pages and all(isinstance(p, int) and 4 <= p <= 9 for p in pages), f"Invalid song page provenance for {sid}")
        if len(pages) > 1:
            cross_page_songs += 1
        status = song.get("authorship_status")
        if status == "anthology-attributed":
            attributed += 1
            ensure(song.get("lyricist_ta") == "மு. கருணாநிதி", f"Attributed song lyricist mismatch at {sid}")
        elif status == "unresolved":
            unresolved += 1
            ensure(song.get("lyricist_ta") is None, f"Unresolved song has lyricist at {sid}")
        else:
            raise QAError(f"Unexpected authorship status {status!r} at {sid}")
        links = song.get("performance_links")
        ensure(isinstance(links, list), f"Song performance links malformed at {sid}")
        for link in links:
            if link.get("status") == "verified":
                verified_perf += 1
            elif link.get("status") == "review":
                review_perf += 1
            else:
                raise QAError(f"Unexpected performance-link status at {sid}: {link}")
        sections = song.get("sections")
        ensure(isinstance(sections, list) and sections, f"Reader song sections missing at {sid}")
        for s_no, section in enumerate(sections, 1):
            ensure(section.get("ordinal") == s_no, f"Reader song section order mismatch at {sid}/{s_no}")
            pairs = section.get("line_pairs")
            ensure(isinstance(pairs, list) and pairs, f"Reader song line pairs missing at {sid}/{s_no}")
            song_sections += 1
            for pair in pairs:
                lid = pair.get("id")
                ensure(isinstance(lid, str) and lid not in seen_song_line_ids, f"Bad/duplicate song line id {lid!r}")
                ensure(isinstance(pair.get("tamil"), str) and pair.get("tamil").strip(), f"Missing Tamil song line at {lid}")
                ensure(isinstance(pair.get("english"), str) and pair.get("english").strip(), f"Missing English song line at {lid}")
                ensure(not PLACEHOLDER_RE.search(pair["tamil"]) and not PLACEHOLDER_RE.search(pair["english"]), f"Placeholder in song line {lid}")
                seen_song_line_ids.add(lid)
                song_lines += 1

    ensure(song_sections == EXPECTED_SONG_SECTIONS, f"Reader song sections {song_sections} != {EXPECTED_SONG_SECTIONS}")
    ensure(song_lines == EXPECTED_SONG_LINES, f"Reader song line/cues {song_lines} != {EXPECTED_SONG_LINES}")
    ensure(cross_page_songs == EXPECTED_CROSS_PAGE_SONGS, "Reader cross-page song count drifted")
    ensure((attributed, unresolved) == (5, 6), "Reader authorship distribution drifted")
    ensure((verified_perf, review_perf) == (3, 1), "Reader performance-link distribution drifted")

    seen_scene_ids: set[str] = set()
    seen_unit_ids: set[str] = set()
    dialogue_links: list[str] = []
    unlabelled = 0
    cross_page_units = 0
    occurrence_links: list[str] = []
    total_units = 0
    for n, scene in enumerate(scenes, 1):
        scene_id = f"raja-rani-s{n:03d}"
        ensure(scene.get("scene_id") == scene_id and scene.get("archival_scene_ordinal") == n, f"Reader scene identity/order mismatch at {n}")
        ensure(scene.get("source_scene_number") is None, f"Reader scene {n} incorrectly has a source scene number")
        ensure(scene_id not in seen_scene_ids, f"Duplicate reader scene id {scene_id}")
        seen_scene_ids.add(scene_id)
        ensure(isinstance(scene.get("tamil_text"), str) and scene.get("tamil_text").strip(), f"Reader scene {n} missing Tamil text")
        units = scene.get("english_units")
        ensure(isinstance(units, list) and units, f"Reader scene {n} missing English units")
        for unit in units:
            uid = unit.get("id")
            ensure(isinstance(uid, str) and uid not in seen_unit_ids, f"Bad/duplicate reader unit id {uid!r}")
            seen_unit_ids.add(uid)
            total_units += 1
            rid = unit.get("source_record_id")
            if rid:
                ensure(rid not in DELETED_DUPLICATE_IDS, f"Deleted T055 duplicate leaked into reader input: {rid}")
                dialogue_links.append(rid)
            elif unit.get("kind") == "dialogue":
                ensure(unit.get("speaker_label") is None, f"Source-unlabelled dialogue has speaker metadata at {uid}")
                unlabelled += 1
            provenance = unit.get("page_provenance")
            ensure(isinstance(provenance, list) and provenance, f"Reader unit lacks provenance at {uid}")
            if len(provenance) > 1:
                cross_page_units += 1
            occ = unit.get("source_occurrence_id")
            if occ:
                occurrence_links.append(occ)
            payload = unit.get("english_text") if unit.get("english_text") is not None else "\n".join(unit.get("english_lines") or [])
            ensure(isinstance(payload, str) and payload.strip() and not PLACEHOLDER_RE.search(payload), f"Invalid English payload at {uid}")

    ensure(total_units == EXPECTED_UNITS, f"Reader screenplay units {total_units} != {EXPECTED_UNITS}")
    ensure(len(dialogue_links) == len(set(dialogue_links)) == EXPECTED_DIALOGUE_LINKS, "Reader immutable dialogue-link coverage drifted")
    ensure(unlabelled == EXPECTED_UNLABELLED, "Reader source-unlabelled spoken count drifted")
    ensure(cross_page_units == EXPECTED_CROSS_PAGE, "Reader cross-page screenplay count drifted")
    ensure(len(occurrence_links) == len(set(occurrence_links)) == EXPECTED_PERFORMANCE_LINKS, "Reader screenplay performance-link count drifted")

    stats = {
        "screenplay_scenes": len(scenes),
        "screenplay_units": total_units,
        "immutable_dialogue_links": len(dialogue_links),
        "source_unlabelled_spoken_units": unlabelled,
        "cross_page_screenplay_units": cross_page_units,
        "screenplay_performance_occurrence_links": len(occurrence_links),
        "numbered_songs": len(songs),
        "numbered_song_sections": song_sections,
        "numbered_song_line_cues": song_lines,
        "cross_page_numbered_songs": cross_page_songs,
        "song_authorship_anthology_attributed": attributed,
        "song_authorship_unresolved": unresolved,
        "song_performance_links_verified": verified_perf,
        "song_performance_links_review": review_perf,
    }
    return reader, stats


def build_payload(reader: dict[str, Any], stats: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "integration_target": "Kalaignar Digital Library / Reading Room",
        "preferred_public_surface": "https://nenjukkuneethi.org/read",
        "integration_status": "payload-complete-verified",
        "site_application_status": "not-applied",
        "source_authority": "pugazg/kalaignar-cinema-works verified Raja Rani structured records",
        "work": {
            "id": "raja-rani",
            "kind": "film-screenplay-with-numbered-front-matter-songs",
            "title_ta": "ராஜா ராணி",
            "presentation_title_en": "Raja Rani",
            "presentation_title_en_is_editorial": True,
            "source_sha256": SOURCE_SHA256,
            "status": "complete-verified",
            "languages": ["ta", "en"],
            "counts": stats,
        },
        "navigation": {
            "primary_sections": ["numbered-songs", "screenplay-scenes"],
            "numbered_song_order": "source numbering 1-11",
            "screenplay_scene_order": "archival navigation 1-58",
            "screenplay_scene_numbers_are_source_numbers": False,
            "screenplay_scene_navigation_is_editorial": True,
            "suggested_slug": "raja-rani",
            "suggested_slug_is_presentation_metadata": True,
        },
        "language_presentation": {
            "default": "ta",
            "available": ["ta", "en", "parallel"],
            "rule": "language switching is presentation only; Tamil and English stored text must not be rewritten",
        },
        "search": {
            "recommended_fields": [
                "numbered_songs.tamil_title",
                "numbered_songs.english_title",
                "numbered_songs.sections.line_pairs.tamil",
                "numbered_songs.sections.line_pairs.english",
                "screenplay_scenes.tamil_text",
                "screenplay_scenes.english_units.speaker_label",
                "screenplay_scenes.english_units.english_text",
                "screenplay_scenes.english_units.english_lines",
            ],
            "normalization_rule": "search normalization may create indexes but must not alter stored source or translation text",
        },
        "provenance_policy": {
            "show_source_pages": True,
            "preserve_source_paths": True,
            "scene_numbering_rule": "archival scene ordinals are navigation only because the source prints no screenplay scene numbers",
            "song_numbering_rule": "numbered songs 1-11 are actual source numbering",
            "song_authorship_rule": "five songs remain later-anthology Kalaignar-attributed; six remain unresolved; reader/site must not upgrade these tiers",
            "performance_link_rule": "scene 58 to song 11 remains review-level",
        },
        "numbered_songs": reader["numbered_songs"],
        "screenplay_scenes": reader["screenplay_scenes"],
    }


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    reader, stats = validate_reader()
    payload = build_payload(reader, stats)
    payload_bytes = (json.dumps(payload, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    payload_text = payload_bytes.decode("utf-8")
    for bad in DELETED_DUPLICATE_IDS:
        ensure(bad not in payload_text, f"Deleted T055 duplicate leaked into payload: {bad}")
    ensure(not PLACEHOLDER_RE.search(payload_text), "Placeholder leaked into Reading Room payload")

    input_paths = [READER_JSON, READER_MANIFEST]
    input_hash = aggregate_sha256(input_paths)
    payload_hash = sha256_bytes(payload_bytes)
    (OUT / "reading-room.json").write_bytes(payload_bytes)

    report = f"""# Raja Rani Reading Room payload — QA report

Status: **PASS**

## Input authority

- reader manifest status: **PASS**
- reader input files: **2** (`reader-edition.json`, `manifest.json`)
- reader-input aggregate SHA-256: `{input_hash}`
- upstream source scan SHA-256: `{SOURCE_SHA256}`

## Payload checkpoint

- numbered source songs: **{stats['numbered_songs']}/11**
- numbered-song sections: **{stats['numbered_song_sections']}/67**
- Tamil/English song line-cues: **{stats['numbered_song_line_cues']}/181**
- archival screenplay scenes: **{stats['screenplay_scenes']}/58**
- screenplay English units: **{stats['screenplay_units']:,}/1,236**
- immutable dialogue links: **{stats['immutable_dialogue_links']:,}/1,071**
- source-unlabelled spoken units: **{stats['source_unlabelled_spoken_units']}/19**
- cross-page screenplay units: **{stats['cross_page_screenplay_units']}/15**
- screenplay performance occurrence links: **{stats['screenplay_performance_occurrence_links']}/4**
- song authorship: **5 later-anthology Kalaignar-attributed / 6 unresolved**
- song-performance relations: **3 verified / 1 review**

## Semantic safeguards

- source-numbered songs remain songs 1–11: **PASS**
- screenplay scene ordinals are explicitly archival/editorial navigation only: **PASS**
- Tamil/English switching is presentation-only metadata: **PASS**
- page/source provenance retained: **PASS**
- deleted T055 duplicate dialogue IDs absent: **PASS**
- scene-58/song-11 relation remains review-level: **PASS**
- authorship tiers are not upgraded: **PASS**
- placeholder leakage: **0**
- site application status: **not-applied**

## Output integrity

- `reading-room.json` bytes: **{len(payload_bytes):,}**
- `reading-room.json` SHA-256: `{payload_hash}`

The payload is ready for use by the separate Reading Room implementation repository when that repository is explicitly authorized for modification. This repository-only step does not deploy or change the public site.
"""
    (OUT / "QA_REPORT.md").write_text(report, encoding="utf-8")
    manifest = {
        "work_id": "raja-rani",
        "integration": "reading-room",
        "build_version": BUILD_VERSION,
        "status": "PASS",
        "site_application_status": "not-applied",
        "source_sha256": SOURCE_SHA256,
        "reader_input_aggregate_sha256": input_hash,
        "checkpoint": stats,
        "output": {
            "path": "works/raja-rani/integrations/reading-room/reading-room.json",
            "bytes": len(payload_bytes),
            "sha256": payload_hash,
        },
    }
    (OUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("RAJA RANI READING ROOM PAYLOAD: PASS")
    print(json.dumps(stats, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
