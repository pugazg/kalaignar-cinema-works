#!/usr/bin/env python3
"""Whole-work diagnostic preflight for the Manohara English reader/export layer."""

import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
WORK = ROOT / "works" / "manohara"
TRANS = WORK / "translations" / "records"
DIALOGUES = WORK / "dialogues" / "records"
SONGS = WORK / "songs" / "inventory.json"
INDEX = WORK / "translations" / "index.json"

EXPECTED_SCENES = 57
EXPECTED_UNITS = 1190
EXPECTED_DIALOGUE_LINKS = 983
EXPECTED_UNLABELLED = 27
EXPECTED_CROSS_PAGE = 17
EXPECTED_SONG_OCCURRENCES = 6
EXPECTED_KINDS = {
    "dialogue": 1009,
    "stage-direction": 173,
    "song-reference": 6,
    "chant": 1,
    "written-text": 1,
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
units = 0
kinds = Counter()
scene_counts = {}
id_errors = []
page_regressions = []
provenance_errors = []
cross_page = []
dialogue_links = []
unlabelled_dialogue = []
song_occurrences = []
synthetic_scene_end = []
structural_star_units = []
status_errors = []
scene_metadata_errors = []

index = json.loads(INDEX.read_text(encoding="utf-8"))

for scene in range(1, EXPECTED_SCENES + 1):
    scene_id = f"manohara-s{scene:03d}"
    path = TRANS / f"scene-{scene:03d}.json"
    if not path.exists():
        errors.append(f"missing translation scene file: {path.relative_to(ROOT)}")
        continue

    data = json.loads(path.read_text(encoding="utf-8"))
    expected_scene_meta = {
        "work_id": "manohara",
        "target_language": "en",
        "scene_id": scene_id,
        "archival_scene_ordinal": scene,
        "source_scene_number": None,
        "scene_status": "verified",
    }
    for key, expected in expected_scene_meta.items():
        if data.get(key) != expected:
            scene_metadata_errors.append((scene, key, data.get(key), expected))

    scene_units = data.get("units", [])
    if data.get("unit_count") != len(scene_units):
        scene_metadata_errors.append((scene, "unit_count", data.get("unit_count"), len(scene_units)))
    scene_counts[scene] = len(scene_units)
    units += len(scene_units)

    prev_page = 0
    for ordinal, unit in enumerate(scene_units, 1):
        uid = unit.get("id")
        expected_uid = f"manohara-en-s{scene:03d}-u{ordinal:03d}"
        if uid != expected_uid:
            id_errors.append((scene, ordinal, uid, expected_uid))

        if unit.get("status") != "verified":
            status_errors.append((uid, unit.get("status")))
        if unit.get("target_language") != "en" or unit.get("scene_id") != scene_id or unit.get("archival_scene_ordinal") != scene:
            scene_metadata_errors.append((scene, "unit-scene-metadata", uid, unit.get("scene_id")))

        kind = unit.get("kind")
        kinds[kind] += 1
        source = unit.get("source", {})
        prov = source.get("page_provenance") or []
        if not prov:
            provenance_errors.append((uid, "missing-page-provenance"))
        else:
            pages = [p.get("pdf_page") for p in prov]
            if any(not isinstance(p, int) for p in pages):
                provenance_errors.append((uid, "invalid-pdf-page", pages))
            else:
                if pages != sorted(pages):
                    provenance_errors.append((uid, "non-monotonic-unit-provenance", pages))
                first_page = pages[0]
                if first_page < prev_page:
                    page_regressions.append((uid, prev_page, first_page))
                prev_page = first_page
                if len(prov) > 1:
                    cross_page.append(uid)

        rid = source.get("source_record_id")
        if rid:
            dialogue_links.append(rid)
            # The source-labelled war proclamation in scene 11 is deliberately
            # classified as a chant while retaining its immutable dialogue link.
            if kind not in {"dialogue", "chant"}:
                errors.append(f"unexpected unit kind carries immutable dialogue record link: {uid} ({kind}) -> {rid}")
        elif kind == "dialogue":
            unlabelled_dialogue.append(uid)
            if source.get("speaker_label") is not None:
                errors.append(f"direct source-unlabelled dialogue has non-null speaker metadata: {uid}")

        occ = source.get("source_occurrence_id")
        if occ:
            song_occurrences.append(occ)
            if kind != "song-reference":
                errors.append(f"non-song-reference unit carries song occurrence link: {uid} -> {occ}")

        locator = source.get("source_locator")
        if isinstance(locator, dict):
            loc_kind = str(locator.get("kind", "")).lower()
            # References such as "after the structural star" in a real stage
            # direction's description are contextual, not translations of the star.
            if loc_kind in STRUCTURAL_LOCATOR_KINDS:
                structural_star_units.append(uid)

        tr = unit.get("translation", {})
        text = tr.get("english_text")
        texts = [text] if isinstance(text, str) else tr.get("english_lines", [])
        for candidate in texts:
            if isinstance(candidate, str) and SYNTH_SCENE_END.match(candidate):
                synthetic_scene_end.append(uid)

immutable_ids = []
for scene in range(1, EXPECTED_SCENES + 1):
    path = DIALOGUES / f"scene-{scene:03d}.json"
    if not path.exists():
        errors.append(f"missing dialogue scene file: {path.relative_to(ROOT)}")
        continue
    data = json.loads(path.read_text(encoding="utf-8"))
    records = data if isinstance(data, list) else data.get("records", [])
    immutable_ids.extend(r["id"] for r in records)

song_data = json.loads(SONGS.read_text(encoding="utf-8"))
song_inventory_ids = [r["id"] for r in song_data.get("records", [])]

link_counts = Counter(dialogue_links)
duplicate_dialogue_links = sorted(rid for rid, count in link_counts.items() if count != 1)
missing_dialogue_links = sorted(set(immutable_ids) - set(dialogue_links))
extra_dialogue_links = sorted(set(dialogue_links) - set(immutable_ids))

song_link_counts = Counter(song_occurrences)
duplicate_song_links = sorted(occ for occ, count in song_link_counts.items() if count != 1)
missing_song_links = sorted(set(song_inventory_ids) - set(song_occurrences))
extra_song_links = sorted(set(song_occurrences) - set(song_inventory_ids))

# Fixed checkpoint assertions established by the completed translation layer.
if units != EXPECTED_UNITS:
    errors.append(f"translation unit total {units} != expected {EXPECTED_UNITS}")
if dict(kinds) != EXPECTED_KINDS:
    errors.append(f"kind counts {dict(kinds)} != expected {EXPECTED_KINDS}")
if len(immutable_ids) != EXPECTED_DIALOGUE_LINKS:
    errors.append(f"immutable dialogue inventory {len(immutable_ids)} != expected {EXPECTED_DIALOGUE_LINKS}")
if len(dialogue_links) != EXPECTED_DIALOGUE_LINKS or len(set(dialogue_links)) != EXPECTED_DIALOGUE_LINKS:
    errors.append(f"dialogue linkage count/unique = {len(dialogue_links)}/{len(set(dialogue_links))}, expected {EXPECTED_DIALOGUE_LINKS}/{EXPECTED_DIALOGUE_LINKS}")
if len(unlabelled_dialogue) != EXPECTED_UNLABELLED:
    errors.append(f"source-unlabelled dialogue count {len(unlabelled_dialogue)} != expected {EXPECTED_UNLABELLED}")
if len(cross_page) != EXPECTED_CROSS_PAGE:
    errors.append(f"cross-page unit count {len(cross_page)} != expected {EXPECTED_CROSS_PAGE}")
if len(song_occurrences) != EXPECTED_SONG_OCCURRENCES or len(set(song_occurrences)) != EXPECTED_SONG_OCCURRENCES:
    errors.append(f"song occurrence links {len(song_occurrences)}/{len(set(song_occurrences))} != expected 6/6")

if id_errors:
    errors.append(f"unit ID errors: {id_errors}")
if status_errors:
    errors.append(f"non-verified units: {status_errors}")
if scene_metadata_errors:
    errors.append(f"scene/unit metadata errors: {scene_metadata_errors}")
if provenance_errors:
    errors.append(f"page provenance errors: {provenance_errors}")
if page_regressions:
    errors.append(f"page-order regressions: {page_regressions}")
if missing_dialogue_links:
    errors.append(f"missing dialogue links: {missing_dialogue_links}")
if extra_dialogue_links:
    errors.append(f"extra dialogue links: {extra_dialogue_links}")
if duplicate_dialogue_links:
    errors.append(f"duplicate dialogue links: {duplicate_dialogue_links}")
if missing_song_links:
    errors.append(f"missing song occurrence links: {missing_song_links}")
if extra_song_links:
    errors.append(f"extra song occurrence links: {extra_song_links}")
if duplicate_song_links:
    errors.append(f"duplicate song occurrence links: {duplicate_song_links}")
if synthetic_scene_end:
    errors.append(f"synthetic scene-end prose units: {synthetic_scene_end}")
if structural_star_units:
    errors.append(f"translation units derived directly from decorative/structural stars: {structural_star_units}")

# Cross-check the stored index rather than trusting it as the source of truth.
if index.get("translation_units") != units:
    errors.append("translations/index.json translation_units does not match files")
if index.get("unit_kind_counts") != dict(kinds):
    errors.append("translations/index.json unit_kind_counts does not match files")
if index.get("dialogue_source_records_linked") != len(dialogue_links):
    errors.append("translations/index.json dialogue link total does not match files")
if index.get("cross_page_translation_units") != cross_page:
    errors.append("translations/index.json cross-page list does not match files in source order")
if index.get("source_linked_unlabelled_spoken_units") != unlabelled_dialogue:
    errors.append("translations/index.json unlabelled-spoken list does not match files in source order")
if index.get("translated_song_occurrences") != song_occurrences:
    errors.append("translations/index.json song occurrence list does not match files in source order")

print("MANOHARA ENGLISH READER PREFLIGHT")
print("status=", "PASS" if not errors else "FAIL")
print("scene_files=", len(scene_counts), "expected=", EXPECTED_SCENES)
print("actual_units=", units)
print("kind_counts=", dict(kinds))
print("scene_counts=", json.dumps(scene_counts, sort_keys=True))
print("dialogue_links_count=", len(dialogue_links), "unique=", len(set(dialogue_links)), "immutable=", len(immutable_ids))
print("missing_dialogue_links=", missing_dialogue_links)
print("extra_dialogue_links=", extra_dialogue_links)
print("duplicate_dialogue_links=", duplicate_dialogue_links)
print("source_unlabelled_spoken_units=", unlabelled_dialogue)
print("cross_page_units=", cross_page)
print("song_occurrence_links=", song_occurrences)
print("missing_song_links=", missing_song_links)
print("extra_song_links=", extra_song_links)
print("synthetic_scene_end_units=", synthetic_scene_end)
print("structural_star_units=", structural_star_units)
print("page_regressions=", page_regressions)
print("id_errors=", id_errors)
print("provenance_errors=", provenance_errors)
print("scene_metadata_errors=", scene_metadata_errors)
print("warnings=", warnings)
if errors:
    print("errors=")
    for err in errors:
        print(" -", err)
    sys.exit(1)
print("errors= []")
