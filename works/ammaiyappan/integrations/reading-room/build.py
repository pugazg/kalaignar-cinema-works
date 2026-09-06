#!/usr/bin/env python3
"""Build and QA the source-linked Ammayappan Reading Room payload."""

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
WORK = ROOT / "works" / "ammaiyappan"
READER_DIR = WORK / "editions" / "en"
READER_JSON = READER_DIR / "reader-edition.json"
READER_MANIFEST = READER_DIR / "manifest.json"
SCENES_DIR = WORK / "scenes"
DIALOGUES_DIR = WORK / "dialogues" / "records"
SUPPLEMENTS_PATH = WORK / "dialogues" / "source-role-resolved-records.json"
SONGS_PATH = WORK / "songs" / "inventory.json"
OUT = WORK / "integrations" / "reading-room"

SOURCE_SHA256 = "eda6468a57022b418f44851a0013b090469bc6f4be44a682487800658771720d"
EXPECTED_SCENES = 63
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
EXPECTED_SPEAKER_ORIGINS = {
    "source-explicit-colon": 1009,
    "source-explicit-noncolon-delimiter": 2,
    "source-context-attributed": 14,
}
PLACEHOLDER_RE = re.compile(r"\b(?:TODO|TBD|FIXME)\b|\[\[\?\]\]|\{\{.+?\}\}", re.I)
COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$")


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


def extract_tamil_scene(path: Path) -> tuple[str, str]:
    raw = path.read_text(encoding="utf-8")
    cleaned = COMMENT_RE.sub("", raw)
    lines = cleaned.splitlines()
    heading = None
    heading_index = None
    for i, line in enumerate(lines):
        match = HEADING_RE.match(line.strip())
        if match:
            heading = match.group(1).strip()
            heading_index = i
            break
    ensure(isinstance(heading, str) and heading, f"Missing Tamil scene heading in {path.relative_to(ROOT)}")
    ensure(isinstance(heading_index, int), f"Missing Tamil scene heading position in {path.relative_to(ROOT)}")
    body_lines = lines[heading_index + 1 :]
    while body_lines and not body_lines[0].strip():
        body_lines.pop(0)
    while body_lines and not body_lines[-1].strip():
        body_lines.pop()
    body = "\n".join(body_lines).strip()
    ensure(body, f"Missing Tamil scene body in {path.relative_to(ROOT)}")
    ensure(not PLACEHOLDER_RE.search(body), f"Editorial placeholder in Tamil scene {path.relative_to(ROOT)}")
    return heading, body


def english_payload(unit: dict[str, Any]) -> tuple[str | None, list[str] | None]:
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


def build_closed_authority() -> tuple[dict[str, dict[str, Any]], set[str], list[Path]]:
    explicit: dict[str, dict[str, Any]] = {}
    authority_paths: list[Path] = []
    for scene in range(1, EXPECTED_SCENES + 1):
        path = DIALOGUES_DIR / f"scene-{scene:03d}.json"
        authority_paths.append(path)
        data = load_json(path)
        records = data if isinstance(data, list) else data.get("records") if isinstance(data, dict) else None
        ensure(isinstance(records, list), f"Malformed dialogue shard {path.relative_to(ROOT)}")
        for rec in records:
            rid = rec.get("id")
            ensure(isinstance(rid, str) and rid not in explicit, f"Bad/duplicate explicit record {rid!r}")
            explicit[rid] = rec
    ensure(len(explicit) == EXPECTED_EXPLICIT, f"Explicit dialogue authority {len(explicit)} != {EXPECTED_EXPLICIT}")

    supplements_data = load_json(SUPPLEMENTS_PATH)
    authority_paths.append(SUPPLEMENTS_PATH)
    ensure(isinstance(supplements_data, list), "Malformed source-role supplement authority")
    supplements: dict[str, dict[str, Any]] = {}
    for rec in supplements_data:
        rid = rec.get("id")
        ensure(isinstance(rid, str) and rid not in explicit and rid not in supplements, f"Bad/duplicate supplement {rid!r}")
        supplements[rid] = rec
    ensure(len(supplements) == EXPECTED_SUPPLEMENTS, f"Supplement authority {len(supplements)} != {EXPECTED_SUPPLEMENTS}")

    songs = load_json(SONGS_PATH)
    authority_paths.append(SONGS_PATH)
    occurrences = songs.get("occurrences") if isinstance(songs, dict) else None
    ensure(isinstance(occurrences, list), "Malformed song/performance occurrence authority")
    occurrence_ids = [x.get("id") for x in occurrences]
    ensure(occurrence_ids == EXPECTED_OCCURRENCES, f"Occurrence authority drifted: {occurrence_ids}")

    return {**explicit, **supplements}, set(occurrence_ids), authority_paths


def validate_reader_and_build_scenes() -> tuple[list[dict[str, Any]], dict[str, Any], list[Path]]:
    reader = load_json(READER_JSON)
    manifest = load_json(READER_MANIFEST)
    ensure(reader.get("work_id") == "ammaiyappan", "Reader work id differs")
    ensure(reader.get("status") == "complete-verified", "Reader is not complete-verified")
    ensure(reader.get("source_scan_sha256") == SOURCE_SHA256, "Reader source SHA differs")
    ensure(reader.get("source_scene_numbering") == "none-printed", "Reader incorrectly claims source scene numbering")
    ensure(reader.get("archival_scene_numbering") == "derivative-navigation-only", "Reader archival numbering semantics differ")
    ensure(reader.get("scene_count") == EXPECTED_SCENES and reader.get("translation_units") == EXPECTED_UNITS, "Reader totals differ")
    ensure(reader.get("unit_kind_counts") == EXPECTED_KINDS, "Reader unit-kind totals differ")
    ensure(manifest.get("status") == "complete-verified" and manifest.get("qa_status") == "PASS", "Reader manifest is not complete-verified/PASS")
    ensure(manifest.get("source_scan_sha256") == SOURCE_SHA256, "Reader manifest source SHA differs")
    ensure(manifest.get("translation_units") == EXPECTED_UNITS, "Reader manifest unit total differs")
    ensure(manifest.get("dialogue_source_links_total") == EXPECTED_DIALOGUE_TOTAL, "Reader manifest dialogue total differs")
    ensure(len(manifest.get("cross_page_units") or []) == EXPECTED_CROSS_PAGE, "Reader manifest cross-page total differs")
    ensure(manifest.get("occurrence_source_span_links_total") == 7, "Reader manifest occurrence-span total differs")

    closed_records, occurrence_ids, authority_paths = build_closed_authority()
    raw_scenes = reader.get("scenes")
    ensure(isinstance(raw_scenes, list) and len(raw_scenes) == EXPECTED_SCENES, "Reader scene list differs")

    payload_scenes: list[dict[str, Any]] = []
    scene_paths: list[Path] = []
    seen_units: set[str] = set()
    dialogue_links: list[str] = []
    occurrence_links: list[str] = []
    cross_page: list[str] = []
    kinds: Counter[str] = Counter()
    speaker_origins: Counter[str] = Counter()

    for ordinal, scene in enumerate(raw_scenes, 1):
        scene_id = f"ammaiyappan-s{ordinal:03d}"
        ensure(scene.get("scene_id") == scene_id and scene.get("archival_scene_ordinal") == ordinal, f"Reader scene identity/order mismatch at {ordinal}")
        ensure(scene.get("source_scene_number") is None, f"Scene {ordinal} has a source scene number")
        source_scene_path = SCENES_DIR / f"scene-{ordinal:03d}.md"
        scene_paths.append(source_scene_path)
        heading, tamil_text = extract_tamil_scene(source_scene_path)
        units = scene.get("units")
        ensure(isinstance(units, list) and len(units) == scene.get("unit_count"), f"Scene {ordinal} unit count differs")

        english_units: list[dict[str, Any]] = []
        scene_pdf_pages: set[int] = set()
        scene_printed_pages: set[int] = set()
        for unit in units:
            uid = unit.get("id")
            ensure(isinstance(uid, str) and uid not in seen_units, f"Bad/duplicate reader unit {uid!r}")
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
                ensure(isinstance(pdf_page, int) and isinstance(printed_page, int), f"Bad provenance at {uid}")
                ensure(5 <= pdf_page <= 109 and printed_page == pdf_page - 2, f"Out-of-range provenance at {uid}")
                scene_pdf_pages.add(pdf_page)
                scene_printed_pages.add(printed_page)
            if len(provenance) > 1:
                cross_page.append(uid)
                segments = unit.get("translation", {}).get("english_page_segments")
                ensure(isinstance(segments, list) and len(segments) == len(provenance), f"Cross-page segments differ at {uid}")
                ensure(
                    [(x.get("pdf_page"), x.get("printed_page")) for x in segments]
                    == [(x.get("pdf_page"), x.get("printed_page")) for x in provenance],
                    f"Cross-page segment provenance differs at {uid}",
                )

            rid = source.get("source_record_id")
            if kind == "dialogue":
                ensure(isinstance(rid, str) and rid in closed_records, f"Dialogue source link missing/unknown at {uid}")
                rec = closed_records[rid]
                ensure(rec.get("archive_scene_id") == scene_id, f"Dialogue source scene differs at {uid}")
                ensure(source.get("speaker_label") == rec.get("speaker_label"), f"Speaker label differs at {uid}")
                expected_origin = rec.get("speaker_label_origin") or "source-explicit-colon"
                ensure(source.get("speaker_label_origin") == expected_origin, f"Speaker origin differs at {uid}")
                ensure(source.get("page_provenance") == rec.get("page_provenance"), f"Dialogue provenance differs at {uid}")
                dialogue_links.append(rid)
                speaker_origins[expected_origin] += 1
            else:
                ensure(rid is None, f"Non-dialogue unit carries dialogue source link at {uid}")

            occ = source.get("source_occurrence_id")
            if occ is not None:
                ensure(occ in occurrence_ids, f"Unknown occurrence id {occ} at {uid}")
                occurrence_links.append(occ)

            english_text, english_lines = english_payload(unit)
            tr = unit["translation"]
            flat = {
                "id": uid,
                "kind": kind,
                "source_record_id": rid,
                "source_occurrence_id": occ,
                "source_path": source.get("source_path"),
                "canonical_scene_path": source.get("canonical_scene_path"),
                "source_locator": source.get("source_locator"),
                "speaker_label": source.get("speaker_label"),
                "speaker_label_origin": source.get("speaker_label_origin"),
                "page_provenance": provenance,
                "english_text": english_text,
                "english_lines": english_lines,
                "english_page_segments": tr.get("english_page_segments"),
                "translation_mode": tr.get("mode"),
                "translation_notes": tr.get("notes") or [],
            }
            english_units.append(flat)

        payload_scenes.append({
            "scene_id": scene_id,
            "archival_scene_ordinal": ordinal,
            "source_scene_number": None,
            "archival_navigation_only": True,
            "source_heading_ta": heading,
            "source_scene_file": f"works/ammaiyappan/scenes/scene-{ordinal:03d}.md",
            "pdf_pages": sorted(scene_pdf_pages),
            "printed_pages": sorted(scene_printed_pages),
            "tamil_text": tamil_text,
            "english_units": english_units,
        })

    ensure(len(seen_units) == EXPECTED_UNITS, f"Reader units {len(seen_units)} != {EXPECTED_UNITS}")
    ensure({k: kinds.get(k, 0) for k in EXPECTED_KINDS} == EXPECTED_KINDS and not (set(kinds) - set(EXPECTED_KINDS)), f"Unit kinds differ: {dict(kinds)}")
    ensure(len(dialogue_links) == EXPECTED_DIALOGUE_TOTAL and len(set(dialogue_links)) == EXPECTED_DIALOGUE_TOTAL and set(dialogue_links) == set(closed_records), "Dialogue/source-role coverage is not exactly once")
    ensure(dict(speaker_origins) == EXPECTED_SPEAKER_ORIGINS, f"Speaker-origin counts differ: {dict(speaker_origins)}")
    ensure(cross_page == manifest.get("cross_page_units") and len(cross_page) == EXPECTED_CROSS_PAGE, "Cross-page list differs from reader manifest")
    ensure(Counter(occurrence_links) == Counter(EXPECTED_OCCURRENCE_LINK_COUNTS), f"Occurrence source-span links differ: {Counter(occurrence_links)}")

    stats = {
        "screenplay_scenes": EXPECTED_SCENES,
        "tamil_scene_texts": EXPECTED_SCENES,
        "english_units": EXPECTED_UNITS,
        "dialogue_source_links": EXPECTED_DIALOGUE_TOTAL,
        "explicit_dialogue_records": EXPECTED_EXPLICIT,
        "source_role_supplements": EXPECTED_SUPPLEMENTS,
        "stage_action_units": EXPECTED_KINDS["stage-direction"],
        "song_reference_units": EXPECTED_KINDS["song-reference"],
        "japa_units": EXPECTED_KINDS["japa"],
        "cross_page_units": EXPECTED_CROSS_PAGE,
        "occurrence_identities": len(EXPECTED_OCCURRENCES),
        "occurrence_source_span_links": sum(EXPECTED_OCCURRENCE_LINK_COUNTS.values()),
        "speaker_origin_source_explicit_colon": EXPECTED_SPEAKER_ORIGINS["source-explicit-colon"],
        "speaker_origin_source_explicit_noncolon_delimiter": EXPECTED_SPEAKER_ORIGINS["source-explicit-noncolon-delimiter"],
        "speaker_origin_source_context_attributed": EXPECTED_SPEAKER_ORIGINS["source-context-attributed"],
    }
    return payload_scenes, stats, [READER_JSON, READER_MANIFEST, *scene_paths, *authority_paths]


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    scenes, stats, input_paths = validate_reader_and_build_scenes()
    payload = {
        "schema_version": 1,
        "integration_target": "Kalaignar Digital Library / Reading Room",
        "preferred_public_surface": "https://nenjukkuneethi.org/read",
        "integration_status": "payload-complete-verified",
        "site_application_status": "not-applied",
        "source_authority": "pugazg/kalaignar-cinema-works verified Ammayappan source/translation records",
        "work": {
            "id": "ammaiyappan",
            "kind": "film-screenplay",
            "title_ta": "அம்மையப்பன்",
            "presentation_title_en": "Ammayappan",
            "presentation_title_en_is_editorial": True,
            "source_sha256": SOURCE_SHA256,
            "status": "complete-verified",
            "languages": ["ta", "en"],
            "counts": stats,
        },
        "navigation": {
            "primary_sections": ["screenplay-scenes"],
            "screenplay_scene_order": "archival navigation 1-63",
            "screenplay_scene_numbers_are_source_numbers": False,
            "screenplay_scene_navigation_is_editorial": True,
            "suggested_slug": "ammaiyappan",
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
            "scene_numbering_rule": "archival scene ordinals are navigation only because the source booklet prints no scene numbers",
            "speaker_label_rule": "exact Tamil speaker labels and source-role origins must remain distinct; context-attributed supplements are not printed labels",
            "source_delimiter_rule": "scene 3 பூங் ; and scene 5 திரு; retain source-explicit semicolon provenance and must not be normalized to printed-colon labels",
            "cross_page_rule": "all 28 cross-page English units remain single logical units with their verified page segments",
            "song_performance_rule": "retain only the five closed source-visible occurrence identities across seven source spans; do not reconstruct absent lyrics, titles or authorship",
        },
        "screenplay_scenes": scenes,
    }

    payload_bytes = (json.dumps(payload, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    payload_sha = sha256_bytes(payload_bytes)
    (OUT / "reading-room.json").write_bytes(payload_bytes)

    qa = f"""# Ammayappan — Reading Room integration payload QA

**Status:** PASS  
**Site application:** not-applied  
**Source scan SHA-256:** `{SOURCE_SHA256}`  
**Reader authority:** `works/ammaiyappan/editions/en/reader-edition.json`

## Verified payload checks

- archival screenplay navigation: **63/63 scenes**, in source order; the booklet prints no scene numbers;
- Tamil scene texts: **63/63**, generated from the verified scene derivatives without provenance comments;
- verified English units: **1,210/1,210 exactly once**;
- dialogue/source-role links: **1,025/1,025 exactly once** = **1,009 explicit colon-labelled records + 16 closed supplements**;
- speaker-label provenance: **1,009 source-explicit-colon + 2 source-explicit-noncolon-delimiter + 14 source-context-attributed**;
- stage/action units: **181**;
- song-reference units: **3**; japa units: **1**;
- cross-page English units: **28/28**, with matching `english_page_segments` preserved;
- retained occurrence identities: **5/5**, represented through **7** intentional source-span links (`1,1,1,2,2`);
- source page provenance remains within PDF **5–109** / printed **3–107** with `printed = PDF - 2`;
- scene 3 `பூங் ; ...` and scene 5 `திரு; ...` retain non-colon source provenance;
- context-attributed supplements remain explicitly contextual and are not promoted into printed labels;
- absent song titles, lyric bodies and authorship are **not reconstructed**;
- payload editorial placeholder tokens: **0**;
- canonical Tamil/dialogue/character/song evidence modified by payload generation: **0**.

## Output

- `reading-room.json` — SHA-256 `{payload_sha}` — **{len(payload_bytes):,} bytes**.

This payload is a deterministic data derivative for the separate Kalaignar Digital Library / Reading Room implementation. The public-site repository has **not** been modified or deployed by this step.
"""
    qa_bytes = qa.encode("utf-8")
    (OUT / "QA_REPORT.md").write_bytes(qa_bytes)

    readme = f"""# Ammayappan — Reading Room integration payload

This directory contains the deterministic **source-linked data payload** prepared for the Kalaignar Digital Library / Reading Room.

It does **not** modify or deploy the separate public-site implementation repository.

## Authority

Direct inputs are the complete-verified Ammayappan reader/export, all 63 verified scene derivatives, the closed 1,025-record dialogue/source-role authority and the five-occurrence song/performance inventory. The integration layer does not become textual authority.

## Navigation semantics

The source booklet prints **no scene numbers**. All 63 `ammaiyappan-sNNN` ordinals are archival navigation only and must never be presented as printed source scene numbering.

## Language model

Tamil and English are both available. `ta`, `en`, and parallel display are presentation modes only; stored source/translation text must not be rewritten by the site.

## Completion checkpoint

Status: **payload-complete-verified — QA PASS**.

- payload: `reading-room.json`;
- payload bytes: **{len(payload_bytes):,}**;
- payload SHA-256: `{payload_sha}`;
- scenes: **63**;
- English units: **1,210**;
- dialogue/source-role links: **1,025**;
- cross-page units: **28**;
- occurrence identities / source-span links: **5 / 7**;
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
        "work_id": "ammaiyappan",
        "integration": "reading-room",
        "build_version": BUILD_VERSION,
        "status": "PASS",
        "site_application_status": "not-applied",
        "source_sha256": SOURCE_SHA256,
        "reader_input_paths": [
            "works/ammaiyappan/editions/en/reader-edition.json",
            "works/ammaiyappan/editions/en/manifest.json",
        ],
        "authoritative_input_files": len(set(input_paths)),
        "authoritative_input_aggregate_sha256": aggregate_sha256(input_paths),
        "checkpoint": stats,
        "output": {
            "path": "works/ammaiyappan/integrations/reading-room/reading-room.json",
            "bytes": len(payload_bytes),
            "sha256": payload_sha,
        },
        "qa_report": {
            "path": "works/ammaiyappan/integrations/reading-room/QA_REPORT.md",
            "bytes": len(qa_bytes),
            "sha256": sha256_bytes(qa_bytes),
        },
        "readme": {
            "path": "works/ammaiyappan/integrations/reading-room/README.md",
            "bytes": len(readme_bytes),
            "sha256": sha256_bytes(readme_bytes),
        },
    }
    (OUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("AMMAYAPPAN READING ROOM PAYLOAD BUILD")
    print("status= PASS")
    print("scenes= 63")
    print("english_units= 1210")
    print("dialogue_source_links= 1025/1025 exactly once")
    print("cross_page_units= 28")
    print("occurrence_identities= 5/5")
    print("occurrence_source_span_links= 7")
    print(f"payload_sha256= {payload_sha}")
    print("site_application_status= not-applied")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except QAError as exc:
        print(f"AMMAYAPPAN READING ROOM PAYLOAD BUILD\nstatus= FAIL\nerror= {exc}", file=sys.stderr)
        raise SystemExit(1)
