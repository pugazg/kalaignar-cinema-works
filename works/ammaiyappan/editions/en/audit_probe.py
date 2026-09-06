#!/usr/bin/env python3
"""Whole-work English reader/export preflight for Ammayappan.

This probe validates the complete verified structured English translation before
publication-facing reader/export files are generated. It is intentionally read-only.
"""

import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
WORK = ROOT / "works" / "ammaiyappan"
TRANS = WORK / "translations" / "records"
DIALOGUES = WORK / "dialogues" / "records"
SUPPLEMENTS = WORK / "dialogues" / "source-role-resolved-records.json"
SONGS = WORK / "songs" / "inventory.json"
INDEX = WORK / "translations" / "index.json"

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
EXPECTED_OCCURRENCE_KINDS = {
    "ammaiyappan-song-001": {"song-reference"},
    "ammaiyappan-song-002": {"dialogue"},
    "ammaiyappan-song-003": {"song-reference"},
    "ammaiyappan-song-004": {"japa", "dialogue"},
    "ammaiyappan-song-005": {"dialogue", "song-reference"},
}

SYNTH_SCENE_END = re.compile(r"^\s*[\[(]?\s*Scene\s+ends?\.?\s*[\])]?\s*$", re.I)
STRUCTURAL_LOCATOR_KINDS = {
    "structural-star",
    "decorative-star",
    "decorative-star-separator",
    "structural-star-separator",
}

errors = []
warnings = []
scene_counts = {}
units_total = 0
kinds = Counter()
id_errors = []
status_errors = []
metadata_errors = []
provenance_errors = []
page_regressions = []
cross_page = []
dialogue_links = []
occurrence_links = []
occurrence_link_kinds = {}
synthetic_scene_end = []
structural_star_units = []

index = json.loads(INDEX.read_text(encoding="utf-8"))

# Build the closed dialogue authority independently of the translation index.
explicit_records = {}
for scene in range(1, EXPECTED_SCENES + 1):
    path = DIALOGUES / f"scene-{scene:03d}.json"
    if not path.exists():
        errors.append(f"missing immutable dialogue shard: {path.relative_to(ROOT)}")
        continue
    data = json.loads(path.read_text(encoding="utf-8"))
    records = data if isinstance(data, list) else data.get("records", [])
    for rec in records:
        rid = rec.get("id")
        if rid in explicit_records:
            errors.append(f"duplicate immutable dialogue record id: {rid}")
        explicit_records[rid] = rec

supplement_records = {}
for rec in json.loads(SUPPLEMENTS.read_text(encoding="utf-8")):
    rid = rec.get("id")
    if rid in supplement_records or rid in explicit_records:
        errors.append(f"duplicate/overlapping source-role record id: {rid}")
    supplement_records[rid] = rec

all_source_records = {**explicit_records, **supplement_records}

# Closed occurrence authority.
song_data = json.loads(SONGS.read_text(encoding="utf-8"))
occurrences = song_data.get("occurrences", [])
occurrence_inventory = [rec.get("id") for rec in occurrences]
occurrence_scene = {rec.get("id"): rec.get("archive_scene_id") for rec in occurrences}

for scene in range(1, EXPECTED_SCENES + 1):
    scene_id = f"ammaiyappan-s{scene:03d}"
    path = TRANS / f"scene-{scene:03d}.json"
    if not path.exists():
        errors.append(f"missing translation scene file: {path.relative_to(ROOT)}")
        continue

    data = json.loads(path.read_text(encoding="utf-8"))
    expected_scene_meta = {
        "work_id": "ammaiyappan",
        "target_language": "en",
        "scene_id": scene_id,
        "archival_scene_ordinal": scene,
        "source_scene_number": None,
        "scene_status": "verified",
    }
    for key, expected in expected_scene_meta.items():
        if data.get(key) != expected:
            metadata_errors.append((scene, key, data.get(key), expected))

    scene_units = data.get("units", [])
    if data.get("unit_count") != len(scene_units):
        metadata_errors.append((scene, "unit_count", data.get("unit_count"), len(scene_units)))
    scene_counts[scene] = len(scene_units)
    units_total += len(scene_units)

    prev_first_page = 0
    for ordinal, unit in enumerate(scene_units, 1):
        uid = unit.get("id")
        expected_uid = f"ammaiyappan-en-s{scene:03d}-u{ordinal:03d}"
        if uid != expected_uid:
            id_errors.append((scene, ordinal, uid, expected_uid))

        if unit.get("status") != "verified":
            status_errors.append((uid, unit.get("status")))
        if unit.get("target_language") != "en" or unit.get("scene_id") != scene_id or unit.get("archival_scene_ordinal") != scene:
            metadata_errors.append((scene, "unit-scene-metadata", uid, unit.get("scene_id"), unit.get("archival_scene_ordinal")))

        kind = unit.get("kind")
        kinds[kind] += 1
        source = unit.get("source", {})
        canonical_scene_path = f"works/ammaiyappan/scenes/scene-{scene:03d}.md"
        if source.get("canonical_scene_path") != canonical_scene_path:
            metadata_errors.append((uid, "canonical_scene_path", source.get("canonical_scene_path"), canonical_scene_path))

        prov = source.get("page_provenance") or []
        if not prov:
            provenance_errors.append((uid, "missing-page-provenance"))
        else:
            pages = [p.get("pdf_page") for p in prov]
            printed = [p.get("printed_page") for p in prov]
            if any(not isinstance(p, int) for p in pages + printed):
                provenance_errors.append((uid, "invalid-page-provenance", prov))
            else:
                if pages != sorted(pages):
                    provenance_errors.append((uid, "non-monotonic-unit-provenance", pages))
                first_page = pages[0]
                if first_page < prev_first_page:
                    page_regressions.append((uid, prev_first_page, first_page))
                prev_first_page = first_page
                if len(prov) > 1:
                    cross_page.append(uid)
                    segments = unit.get("translation", {}).get("english_page_segments")
                    if not isinstance(segments, list) or len(segments) != len(prov):
                        provenance_errors.append((uid, "cross-page-segments-missing-or-count-mismatch"))
                    else:
                        segment_pairs = [(p.get("pdf_page"), p.get("printed_page")) for p in segments]
                        provenance_pairs = [(p.get("pdf_page"), p.get("printed_page")) for p in prov]
                        if segment_pairs != provenance_pairs:
                            provenance_errors.append((uid, "cross-page-segment-pages-do-not-match-provenance", segment_pairs, provenance_pairs))

        rid = source.get("source_record_id")
        if kind == "dialogue" and not rid:
            errors.append(f"dialogue unit lacks closed source record link: {uid}")
        if rid:
            dialogue_links.append(rid)
            if kind != "dialogue":
                errors.append(f"non-dialogue unit carries dialogue source record link: {uid} ({kind}) -> {rid}")
            rec = all_source_records.get(rid)
            if rec is None:
                errors.append(f"translation links unknown dialogue/source-role record: {uid} -> {rid}")
            else:
                if rec.get("archive_scene_id") != scene_id:
                    errors.append(f"source record scene mismatch: {uid} -> {rid}")
                if source.get("speaker_label") != rec.get("speaker_label"):
                    errors.append(f"speaker label provenance mismatch: {uid} -> {rid}")
                expected_origin = rec.get("speaker_label_origin") if rid in supplement_records else "source-explicit-colon"
                if source.get("speaker_label_origin") != expected_origin:
                    errors.append(f"speaker label origin mismatch: {uid} -> {rid}: {source.get('speaker_label_origin')} != {expected_origin}")
                if source.get("page_provenance") != rec.get("page_provenance"):
                    errors.append(f"dialogue page provenance mismatch: {uid} -> {rid}")
                expected_path = (
                    "works/ammaiyappan/dialogues/source-role-resolved-records.json"
                    if rid in supplement_records
                    else f"works/ammaiyappan/dialogues/records/scene-{scene:03d}.json"
                )
                if source.get("source_path") != expected_path:
                    errors.append(f"dialogue source_path mismatch: {uid} -> {rid}")

        occ = source.get("source_occurrence_id")
        if occ:
            occurrence_links.append(occ)
            occurrence_link_kinds.setdefault(occ, set()).add(kind)
            if occ not in occurrence_scene:
                errors.append(f"translation links unknown occurrence: {uid} -> {occ}")
            elif occurrence_scene[occ] != scene_id:
                errors.append(f"occurrence scene mismatch: {uid} -> {occ}")

        locator = source.get("source_locator")
        if isinstance(locator, dict) and str(locator.get("kind", "")).lower() in STRUCTURAL_LOCATOR_KINDS:
            structural_star_units.append(uid)

        tr = unit.get("translation", {})
        text_candidates = []
        if isinstance(tr.get("english_text"), str):
            text_candidates.append(tr["english_text"])
        if isinstance(tr.get("english_lines"), list):
            text_candidates.extend(x for x in tr["english_lines"] if isinstance(x, str))
        if not text_candidates:
            errors.append(f"translation text missing: {uid}")
        for candidate in text_candidates:
            if SYNTH_SCENE_END.match(candidate):
                synthetic_scene_end.append(uid)

# Reconcile dialogue authority exactly once.
link_counts = Counter(dialogue_links)
expected_dialogue_ids = set(all_source_records)
missing_dialogue_links = sorted(expected_dialogue_ids - set(dialogue_links))
extra_dialogue_links = sorted(set(dialogue_links) - expected_dialogue_ids)
duplicate_dialogue_links = sorted(rid for rid, count in link_counts.items() if count != 1)

# Reconcile occurrence identities and their intentional multi-span links.
occ_counts = Counter(occurrence_links)
first_seen_occurrences = list(dict.fromkeys(occurrence_links))
missing_occurrences = [x for x in EXPECTED_OCCURRENCES if x not in occ_counts]
extra_occurrences = sorted(set(occ_counts) - set(EXPECTED_OCCURRENCES))
occurrence_count_mismatches = {
    occ: (occ_counts.get(occ, 0), expected)
    for occ, expected in EXPECTED_OCCURRENCE_LINK_COUNTS.items()
    if occ_counts.get(occ, 0) != expected
}
occurrence_kind_mismatches = {
    occ: (sorted(occurrence_link_kinds.get(occ, set())), sorted(expected))
    for occ, expected in EXPECTED_OCCURRENCE_KINDS.items()
    if occurrence_link_kinds.get(occ, set()) != expected
}

# Fixed closed-checkpoint assertions.
if len(explicit_records) != EXPECTED_EXPLICIT:
    errors.append(f"immutable explicit dialogue inventory {len(explicit_records)} != {EXPECTED_EXPLICIT}")
if len(supplement_records) != EXPECTED_SUPPLEMENTS:
    errors.append(f"source-role supplement inventory {len(supplement_records)} != {EXPECTED_SUPPLEMENTS}")
if len(all_source_records) != EXPECTED_DIALOGUE_TOTAL:
    errors.append(f"closed dialogue authority {len(all_source_records)} != {EXPECTED_DIALOGUE_TOTAL}")
if units_total != EXPECTED_UNITS:
    errors.append(f"translation unit total {units_total} != {EXPECTED_UNITS}")
if {k: kinds.get(k, 0) for k in EXPECTED_KINDS} != EXPECTED_KINDS or set(kinds) - set(EXPECTED_KINDS):
    errors.append(f"kind counts {dict(kinds)} != expected {EXPECTED_KINDS}")
if len(dialogue_links) != EXPECTED_DIALOGUE_TOTAL or len(set(dialogue_links)) != EXPECTED_DIALOGUE_TOTAL:
    errors.append(f"dialogue links total/unique {len(dialogue_links)}/{len(set(dialogue_links))} != {EXPECTED_DIALOGUE_TOTAL}/{EXPECTED_DIALOGUE_TOTAL}")
if len(cross_page) != EXPECTED_CROSS_PAGE:
    errors.append(f"cross-page unit count {len(cross_page)} != {EXPECTED_CROSS_PAGE}")
if occurrence_inventory != EXPECTED_OCCURRENCES:
    errors.append(f"closed occurrence inventory {occurrence_inventory} != expected {EXPECTED_OCCURRENCES}")
if missing_dialogue_links:
    errors.append(f"missing dialogue/source-role links: {missing_dialogue_links}")
if extra_dialogue_links:
    errors.append(f"extra dialogue/source-role links: {extra_dialogue_links}")
if duplicate_dialogue_links:
    errors.append(f"duplicate dialogue/source-role links: {duplicate_dialogue_links}")
if missing_occurrences:
    errors.append(f"missing retained occurrence identities: {missing_occurrences}")
if extra_occurrences:
    errors.append(f"extra retained occurrence identities: {extra_occurrences}")
if occurrence_count_mismatches:
    errors.append(f"occurrence link-count mismatches: {occurrence_count_mismatches}")
if occurrence_kind_mismatches:
    errors.append(f"occurrence kind mismatches: {occurrence_kind_mismatches}")
if id_errors:
    errors.append(f"unit ID errors: {id_errors}")
if status_errors:
    errors.append(f"non-verified units: {status_errors}")
if metadata_errors:
    errors.append(f"scene/unit metadata errors: {metadata_errors}")
if provenance_errors:
    errors.append(f"page provenance errors: {provenance_errors}")
if page_regressions:
    errors.append(f"page-order regressions: {page_regressions}")
if synthetic_scene_end:
    errors.append(f"synthetic scene-end prose units: {synthetic_scene_end}")
if structural_star_units:
    errors.append(f"units derived directly from structural/decorative stars: {structural_star_units}")

# Cross-check the stored translation index instead of trusting it as authority.
if index.get("status") != "complete-verified":
    errors.append("translations/index.json status is not complete-verified")
if index.get("translation_units") != units_total:
    errors.append("translations/index.json translation_units does not match scene files")
if index.get("unit_kind_counts") != EXPECTED_KINDS:
    errors.append("translations/index.json unit_kind_counts does not match closed totals")
if index.get("dialogue_source_records_linked") != EXPECTED_EXPLICIT:
    errors.append("translations/index.json explicit dialogue link total mismatch")
if index.get("source_role_supplement_records_linked") != EXPECTED_SUPPLEMENTS:
    errors.append("translations/index.json source-role supplement total mismatch")
if index.get("cross_page_translation_units") != cross_page:
    errors.append("translations/index.json cross-page list does not match records in source order")
if index.get("translated_song_performance_occurrences") != first_seen_occurrences:
    errors.append("translations/index.json unique occurrence list does not match first-seen record order")
if index.get("source_visible_structural_stars_translated") != 0:
    errors.append("translations/index.json reports structural stars translated as prose")
if index.get("canonical_tamil_modified") is not False or index.get("scene_files_modified") is not False or index.get("dialogue_records_modified") is not False or index.get("character_index_modified") is not False or index.get("song_inventory_modified") is not False:
    errors.append("translations/index.json reports a frozen source layer modified by English")

print("AMMAYAPPAN ENGLISH READER PREFLIGHT")
print("status=", "PASS" if not errors else "FAIL")
print("scene_files=", len(scene_counts), "expected=", EXPECTED_SCENES)
print("translation_units=", units_total)
print("kind_counts=", dict(kinds))
print("explicit_dialogue_records=", len(explicit_records))
print("source_role_supplements=", len(supplement_records))
print("dialogue_links_total=", len(dialogue_links), "unique=", len(set(dialogue_links)))
print("missing_dialogue_links=", missing_dialogue_links)
print("extra_dialogue_links=", extra_dialogue_links)
print("duplicate_dialogue_links=", duplicate_dialogue_links)
print("cross_page_units_count=", len(cross_page))
print("cross_page_units=", cross_page)
print("occurrence_inventory=", occurrence_inventory)
print("occurrence_links_total=", len(occurrence_links), "counts=", dict(occ_counts))
print("occurrence_link_kinds=", {k: sorted(v) for k, v in occurrence_link_kinds.items()})
print("synthetic_scene_end_units=", synthetic_scene_end)
print("structural_star_units=", structural_star_units)
print("page_regressions=", page_regressions)
print("id_errors=", id_errors)
print("provenance_errors=", provenance_errors)
print("metadata_errors=", metadata_errors)
print("warnings=", warnings)
if errors:
    print("errors=")
    for err in errors:
        print(" -", err)
    sys.exit(1)
print("errors= []")
