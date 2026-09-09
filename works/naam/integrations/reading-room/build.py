#!/usr/bin/env python3
"""Build and QA the source-linked Reading Room payload for நாம்."""

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
WORK = ROOT / "works" / "naam"
READER_DIR = WORK / "editions" / "en"
READER_JSON = READER_DIR / "reader-edition.json"
READER_MANIFEST = READER_DIR / "manifest.json"
SCENES_DIR = WORK / "scenes"
SONGS_PATH = WORK / "songs" / "inventory.json"
OUT = WORK / "integrations" / "reading-room"

SOURCE_SHA256 = "0f7a54882eb6a5a8f83b29060c771ef18dee2b9e108c8797184de2b97c30b7ad"
EXPECTED_SCENES = 45
EXPECTED_UNITS = 797
EXPECTED_KINDS = {
    "dialogue": 610,
    "narrative": 35,
    "performance-cue": 6,
    "song": 6,
    "stage-direction": 137,
    "written-text": 2,
    "chant": 1,
}
EXPECTED_DIALOGUE_LINKS = 590
EXPECTED_UNLABELLED = 20
EXPECTED_PERFORMANCES = [
    "naam-perf-007",
    "naam-perf-001",
    "naam-perf-002",
    "naam-perf-003",
    "naam-perf-004",
    "naam-perf-005",
    "naam-perf-006",
]
EXPECTED_PERFORMANCE_MAPS = 138
EXPECTED_CHANT_UNIT = "naam-en-s034-u002"
EXPECTED_CHANT_MAPS = 16
EXPECTED_WRITTEN = ["naam-en-s041-u012", "naam-en-s045-u025"]
EXPECTED_CROSS_PAGE = [
    "naam-en-s001-u021",
    "naam-en-s008-u009",
    "naam-en-s017-u011",
    "naam-en-s020-u003",
    "naam-en-s021-u002",
    "naam-en-s030-u016",
    "naam-en-s031-u002",
    "naam-en-s036-u007",
    "naam-en-s039-u017",
    "naam-en-s041-u002",
    "naam-en-s045-u013",
    "naam-en-s045-u022",
]
COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$")
PLACEHOLDER_RE = re.compile(r"\b(?:TODO|TBD|FIXME|PLACEHOLDER|TRANSLATE(?:\s+ME)?)\b|\[\[\?\]\]|\{\{.+?\}\}", re.I)


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


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def aggregate_sha256(paths: list[Path]) -> str:
    h = hashlib.sha256()
    for path in sorted(set(paths), key=lambda p: p.as_posix()):
        ensure(path.exists(), f"Missing input {path.relative_to(ROOT)}")
        h.update(path.relative_to(ROOT).as_posix().encode("utf-8"))
        h.update(b"\0")
        h.update(path.read_bytes())
        h.update(b"\0")
    return h.hexdigest()


def extract_tamil_scene(path: Path) -> tuple[str, str]:
    raw = COMMENT_RE.sub("", path.read_text(encoding="utf-8"))
    lines = raw.splitlines()
    heading = None
    idx = None
    for i, line in enumerate(lines):
        m = HEADING_RE.match(line.strip())
        if m:
            heading = m.group(1).strip()
            idx = i
            break
    ensure(isinstance(heading, str) and isinstance(idx, int), f"Missing source heading in {path.relative_to(ROOT)}")
    body = lines[idx + 1 :]
    while body and not body[0].strip():
        body.pop(0)
    while body and not body[-1].strip():
        body.pop()
    text = "\n".join(body)
    ensure(text.strip(), f"Empty Tamil scene body in {path.relative_to(ROOT)}")
    return heading, text


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    reader = load_json(READER_JSON)
    rmanifest = load_json(READER_MANIFEST)
    songs = load_json(SONGS_PATH)

    ensure(reader.get("work_id") == "naam" and reader.get("status") == "complete-verified", "Reader is not complete-verified")
    ensure(reader.get("source_scan_sha256") == SOURCE_SHA256, "Reader source scan SHA drifted")
    ensure(reader.get("source_scene_numbering") == "printed-1-45" and reader.get("scene_navigation_is_source_numbering") is True, "Reader scene-number semantics drifted")
    ensure(reader.get("scene_count") == EXPECTED_SCENES and reader.get("translation_units") == EXPECTED_UNITS, "Reader totals drifted")
    ensure(reader.get("unit_kind_counts") == EXPECTED_KINDS, "Reader kind counts drifted")
    ensure(rmanifest.get("status") == "complete-verified" and rmanifest.get("qa_status") == "PASS", "Reader manifest is not PASS")
    ensure(rmanifest.get("translation_units") == EXPECTED_UNITS and rmanifest.get("immutable_dialogue_links") == EXPECTED_DIALOGUE_LINKS, "Reader manifest totals drifted")
    ensure(rmanifest.get("reading_room_gate") == "READY-NEXT", "Reader manifest has not opened Reading Room gate")

    song_records = songs.get("records")
    ensure(isinstance(song_records, list) and [x.get("id") for x in song_records] == EXPECTED_PERFORMANCES, "Performance inventory drifted")
    ensure(next(x for x in song_records if x["id"] == "naam-perf-001").get("author_as_printed") == "பாரதியார்", "Specific Bharathiyar source credit drifted")
    for x in song_records:
        if x["id"] != "naam-perf-001":
            ensure(x.get("authorship_status") == "unresolved-item-level" and x.get("author_as_printed") is None, f"Unsupported item-level authorship at {x['id']}")

    raw_scenes = reader.get("scenes")
    ensure(isinstance(raw_scenes, list) and len(raw_scenes) == EXPECTED_SCENES, "Reader scene list drifted")
    payload_scenes: list[dict[str, Any]] = []
    scene_paths: list[Path] = []
    seen_units: list[str] = []
    kinds: Counter[str] = Counter()
    dialogue_links: list[str] = []
    unlabelled: list[str] = []
    occurrence_order: list[str] = []
    occurrence_maps: Counter[str] = Counter()
    chant_units: list[str] = []
    chant_maps = 0
    written: list[str] = []
    cross_page: list[str] = []
    provenance_failures: list[str] = []

    for n, scene in enumerate(raw_scenes, 1):
        ensure(scene.get("scene_id") == f"naam-s{n:03d}" and scene.get("source_scene_number") == n, f"Reader scene order/identity drifted at {n}")
        scene_path = SCENES_DIR / f"scene-{n:03d}.md"
        scene_paths.append(scene_path)
        heading, tamil_text = extract_tamil_scene(scene_path)
        ensure(heading == scene.get("source_heading_ta"), f"Tamil heading differs from reader at scene {n}")
        units = scene.get("units")
        ensure(isinstance(units, list) and len(units) == scene.get("unit_count"), f"Reader unit count differs at scene {n}")
        scene_pages = set(scene.get("pdf_pages") or [])
        english_units: list[dict[str, Any]] = []

        for unit in units:
            uid = unit.get("id")
            ensure(isinstance(uid, str) and uid not in seen_units, f"Bad/duplicate reader unit {uid!r}")
            seen_units.append(uid)
            kind = unit.get("kind")
            ensure(kind in EXPECTED_KINDS, f"Unsupported unit kind {kind!r} at {uid}")
            kinds[kind] += 1
            source = unit.get("source")
            ensure(isinstance(source, dict), f"Malformed source metadata at {uid}")
            prov = source.get("page_provenance")
            ensure(isinstance(prov, list) and prov, f"Missing provenance at {uid}")
            pages = [x.get("pdf_page") for x in prov]
            if any(not isinstance(p, int) or p not in scene_pages for p in pages):
                provenance_failures.append(uid)
            if len(prov) > 1:
                cross_page.append(uid)

            rid = source.get("source_record_id")
            if rid:
                dialogue_links.append(rid)
            elif kind == "dialogue":
                ensure(source.get("speaker_label") is None and source.get("source_delimiter") is None and source.get("speaker_label_origin") is None, f"Unlabelled speech acquired speaker metadata at {uid}")
                unlabelled.append(uid)
            if kind == "written-text":
                written.append(uid)
            occ = source.get("source_occurrence_id")
            if occ:
                ensure(occ in EXPECTED_PERFORMANCES, f"Unknown performance occurrence {occ} at {uid}")
                if occ not in occurrence_order:
                    occurrence_order.append(occ)
                occurrence_maps[occ] += len(unit.get("translation", {}).get("line_map") or [])
            if kind == "chant":
                chant_units.append(uid)
                ensure(occ is None, "Scene-local chant was promoted to retained performance inventory")
                chant_maps += len(unit.get("translation", {}).get("line_map") or [])

            tr = unit.get("translation")
            ensure(isinstance(tr, dict), f"Malformed translation at {uid}")
            english_text = tr.get("english_text")
            english_lines = tr.get("english_lines")
            ensure(isinstance(english_text, str) ^ isinstance(english_lines, list), f"English payload shape drifted at {uid}")
            if isinstance(english_text, str):
                ensure(english_text.strip() and not PLACEHOLDER_RE.search(english_text), f"Invalid English text at {uid}")
            else:
                ensure(bool(english_lines) and all(isinstance(x, str) and x.strip() and not PLACEHOLDER_RE.search(x) for x in english_lines), f"Invalid English lines at {uid}")

            english_units.append({
                "id": uid,
                "kind": kind,
                "source_record_id": rid,
                "source_occurrence_id": occ,
                "source_path": source.get("source_path"),
                "canonical_scene_path": source.get("canonical_scene_path"),
                "source_locator": source.get("source_locator"),
                "speaker_label": source.get("speaker_label"),
                "speaker_label_origin": source.get("speaker_label_origin"),
                "source_delimiter": source.get("source_delimiter"),
                "page_provenance": prov,
                "english_text": english_text if isinstance(english_text, str) else None,
                "english_lines": english_lines if isinstance(english_lines, list) else None,
                "line_map": tr.get("line_map") or [],
                "translation_mode": tr.get("mode"),
                "translation_notes": tr.get("notes") or [],
            })

        payload_scenes.append({
            "scene_id": f"naam-s{n:03d}",
            "source_scene_number": n,
            "source_heading_ta": heading,
            "source_scene_file": f"works/naam/scenes/scene-{n:03d}.md",
            "pdf_pages": scene.get("pdf_pages"),
            "start_pdf": scene.get("start_pdf"),
            "start_printed": scene.get("start_printed"),
            "end_pdf": scene.get("end_pdf"),
            "end_printed": scene.get("end_printed"),
            "tamil_text": tamil_text,
            "english_units": english_units,
        })

    ensure(len(seen_units) == len(set(seen_units)) == EXPECTED_UNITS, "Reading Room English unit coverage is not exactly once")
    ensure({k: kinds.get(k, 0) for k in EXPECTED_KINDS} == EXPECTED_KINDS and not (set(kinds) - set(EXPECTED_KINDS)), f"Reading Room kind counts drifted: {dict(kinds)}")
    ensure(len(dialogue_links) == len(set(dialogue_links)) == EXPECTED_DIALOGUE_LINKS, "Reading Room dialogue links are not exactly once")
    ensure(len(unlabelled) == EXPECTED_UNLABELLED, f"Reading Room unlabelled speech total drifted: {len(unlabelled)}")
    ensure(occurrence_order == EXPECTED_PERFORMANCES, f"Reading Room performance order drifted: {occurrence_order}")
    ensure(sum(occurrence_maps.values()) == EXPECTED_PERFORMANCE_MAPS, f"Reading Room performance mapping total drifted: {dict(occurrence_maps)}")
    ensure(chant_units == [EXPECTED_CHANT_UNIT] and chant_maps == EXPECTED_CHANT_MAPS, "Reading Room chant state drifted")
    ensure(written == EXPECTED_WRITTEN, f"Reading Room written-text state drifted: {written}")
    ensure(cross_page == EXPECTED_CROSS_PAGE, f"Reading Room cross-page list drifted: {cross_page}")
    ensure(provenance_failures == [], f"Reading Room provenance outside scene bounds: {provenance_failures}")

    performances = []
    for x in song_records:
        performances.append({
            "id": x["id"],
            "source_pdf_pages": x.get("source_pdf_pages"),
            "source_scene_number": x.get("source_scene_number"),
            "scene_relation": x.get("scene_relation"),
            "form": x.get("form"),
            "source_marker": x.get("source_marker"),
            "source_title": x.get("source_title"),
            "source_role_cues": x.get("source_role_cues") or [],
            "performance_cue": x.get("performance_cue"),
            "authorship_status": x.get("authorship_status"),
            "author_as_printed": x.get("author_as_printed"),
        })

    payload = {
        "schema_version": 1,
        "integration_target": "kalaignar-digital-library-reading-room",
        "preferred_public_surface": "https://nenjukkuneethi.org/read",
        "integration_status": "payload-complete-verified",
        "site_application_status": "not-applied",
        "work": {
            "id": "naam",
            "title_ta": "நாம்",
            "title_en": "Naam",
            "kind": "film-screenplay-dialogue-booklet",
            "status": "complete-verified",
            "source_scan_sha256": SOURCE_SHA256,
            "languages": ["ta", "en"],
            "source_scene_count": EXPECTED_SCENES,
            "english_unit_count": EXPECTED_UNITS,
            "immutable_dialogue_links": EXPECTED_DIALOGUE_LINKS,
            "retained_performance_records": 7,
        },
        "navigation": {
            "primary": "screenplay-scenes",
            "scene_numbers": list(range(1, 46)),
            "scene_numbering_origin": "printed-source",
            "screenplay_scene_numbers_are_source_numbers": True,
            "screenplay_scene_navigation_is_editorial": False,
            "separate_performance_inventory_count": 7,
            "scene_34_chant_is_separate_performance_inventory_item": False,
        },
        "language_presentation": {
            "default": "ta",
            "available": ["ta", "en", "parallel"],
            "switching_is_presentation_only": True,
        },
        "provenance_policy": {
            "source_pages_available_per_scene_and_unit": True,
            "source_unlabelled_speech_remains_unassigned": True,
            "speaker_labels_are_source_exact_metadata": True,
            "source_delimiters_are_preserved_metadata": True,
            "search_normalization_may_not_rewrite_stored_text": True,
        },
        "authorship": {
            "source_attributed": {"naam-perf-001": "பாரதியார்"},
            "unresolved_item_level": [x for x in EXPECTED_PERFORMANCES if x != "naam-perf-001"],
            "unsupported_downstream_upgrades": 0,
        },
        "performance_inventory": performances,
        "source_local_chant": {
            "unit_id": EXPECTED_CHANT_UNIT,
            "line_cue_mappings": EXPECTED_CHANT_MAPS,
            "promoted_to_performance_inventory": False,
        },
        "scenes": payload_scenes,
    }

    payload_path = OUT / "reading-room.json"
    write_json(payload_path, payload)
    # Reparse and assert exact generated ownership.
    reparsed = load_json(payload_path)
    ids = [u["id"] for s in reparsed["scenes"] for u in s["english_units"]]
    ensure(ids == seen_units and len(set(ids)) == EXPECTED_UNITS, "Serialized Reading Room unit coverage drifted")
    ensure([s["source_scene_number"] for s in reparsed["scenes"]] == list(range(1, 46)), "Serialized source scene order drifted")

    qa_path = OUT / "QA_REPORT.md"
    qa_path.write_text(
        "# நாம் — Reading Room payload QA\n\n"
        "**Status:** **PASS / PAYLOAD-COMPLETE-VERIFIED**\n\n"
        "- source-numbered screenplay scenes: **45/45 exactly once / source order 1–45**;\n"
        f"- Tamil scene bodies: **45/45** from verified source scene derivatives;\n"
        f"- English units: **{EXPECTED_UNITS}/{EXPECTED_UNITS} exactly once**;\n"
        f"- immutable dialogue links: **{EXPECTED_DIALOGUE_LINKS}/{EXPECTED_DIALOGUE_LINKS} unique**;\n"
        f"- source-unlabelled speech: **{EXPECTED_UNLABELLED} / inferred speakers 0**;\n"
        f"- retained performance identities: **7/7 / {EXPECTED_PERFORMANCE_MAPS} line-cue mappings**;\n"
        f"- scene-34 chant: **1 / {EXPECTED_CHANT_MAPS} mappings / remains outside performance inventory**;\n"
        f"- written-text units: **2**; cross-page units: **{len(EXPECTED_CROSS_PAGE)}**;\n"
        "- provenance outside mapped scene bounds: **0**;\n"
        "- unsupported authorship upgrades: **0**;\n"
        "- scene numbers are explicitly marked as **printed source numbering**, not editorial navigation;\n"
        "- public-site application: **NOT APPLIED**.\n\n"
        "The payload supports Tamil, English and parallel presentation without rewriting either stored language layer. The separate Reading Room implementation repository must be explicitly authorized before site application.\n",
        encoding="utf-8",
    )
    (OUT / "README.md").write_text(
        "# நாம் — Reading Room integration payload\n\n"
        "Source-linked bilingual payload prepared for the Kalaignar Digital Library / Reading Room.\n\n"
        "- `reading-room.json` — verified Tamil/English scene payload with source provenance;\n"
        "- `QA_REPORT.md` — whole-payload QA;\n"
        "- `manifest.json` — reader/input and payload integrity hashes;\n"
        "- `build.py` — deterministic fail-closed payload builder.\n\n"
        "Status: **PAYLOAD-COMPLETE-VERIFIED / QA PASS**. Site application is intentionally **not-applied** in this repository. Scene 1–45 numbering is printed source numbering, not invented reader navigation.\n",
        encoding="utf-8",
    )

    input_paths = [READER_JSON, READER_MANIFEST, SONGS_PATH, *scene_paths]
    manifest = {
        "schema_version": 1,
        "work_id": "naam",
        "build_version": BUILD_VERSION,
        "status": "payload-complete-verified",
        "qa_status": "PASS",
        "site_application_status": "not-applied",
        "source_scan_sha256": SOURCE_SHA256,
        "reader_manifest_sha256": sha256_bytes(READER_MANIFEST.read_bytes()),
        "reader_json_sha256": sha256_bytes(READER_JSON.read_bytes()),
        "authoritative_input_file_count": len(set(input_paths)),
        "authoritative_input_aggregate_sha256": aggregate_sha256(input_paths),
        "scene_count": EXPECTED_SCENES,
        "english_units": EXPECTED_UNITS,
        "immutable_dialogue_links": EXPECTED_DIALOGUE_LINKS,
        "source_unlabelled_speech_units": EXPECTED_UNLABELLED,
        "retained_performance_records": EXPECTED_PERFORMANCES,
        "performance_line_cue_mappings": EXPECTED_PERFORMANCE_MAPS,
        "source_local_chant_line_cue_mappings": EXPECTED_CHANT_MAPS,
        "written_text_units": EXPECTED_WRITTEN,
        "cross_page_units": EXPECTED_CROSS_PAGE,
        "payload": {
            "path": "works/naam/integrations/reading-room/reading-room.json",
            "sha256": sha256_bytes(payload_path.read_bytes()),
            "bytes": payload_path.stat().st_size,
        },
        "qa_report": {
            "sha256": sha256_bytes(qa_path.read_bytes()),
            "bytes": qa_path.stat().st_size,
        },
    }
    write_json(OUT / "manifest.json", manifest)

    print(json.dumps({
        "status": "PASS",
        "scenes": EXPECTED_SCENES,
        "english_units": EXPECTED_UNITS,
        "dialogue_links": EXPECTED_DIALOGUE_LINKS,
        "performances": 7,
        "performance_mappings": EXPECTED_PERFORMANCE_MAPS,
        "chant_mappings": EXPECTED_CHANT_MAPS,
        "site_application": "not-applied",
        "payload_sha256": manifest["payload"]["sha256"],
        "payload_bytes": manifest["payload"]["bytes"],
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except QAError as exc:
        print(f"QA FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
