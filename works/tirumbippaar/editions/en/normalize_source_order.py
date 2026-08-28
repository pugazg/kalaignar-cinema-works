#!/usr/bin/env python3
"""Synchronize Tirumbippaar English source metadata without changing unit IDs/text.

The corrected Tamil dialogue shards are the immutable source-metadata authority.
This helper repairs only downstream metadata/ordering drift:

* exact speaker-label spacing/forms for units linked to immutable dialogue IDs;
* two source-proven carry-over stage directions whose higher stable English IDs
  must appear at the beginning of scenes 37 and 39.

Page-provenance disagreements are never auto-repaired. They are all reported in
one pass so each can be adjudicated against the corrected scene/source before a
manual repository correction. No files are written while such mismatches remain.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
WORK = ROOT / "works" / "tirumbippaar"
TRANSLATIONS = WORK / "translations" / "records"
DIALOGUES = WORK / "dialogues" / "records"
SCENES = range(1, 94)

SOURCE_ORDER_MOVES = {
    37: "tirumbippaar-en-s037-u051",
    39: "tirumbippaar-en-s039-u026",
}

loaded: dict[int, tuple[Path, dict]] = {}
provenance_mismatches: list[dict] = []
speaker_repairs = 0
order_repairs = 0

for scene in SCENES:
    translation_path = TRANSLATIONS / f"scene-{scene:02d}.json"
    dialogue_path = DIALOGUES / f"scene-{scene:02d}.json"

    translation = json.loads(translation_path.read_text(encoding="utf-8"))
    dialogue_data = json.loads(dialogue_path.read_text(encoding="utf-8"))
    dialogue_records = dialogue_data if isinstance(dialogue_data, list) else dialogue_data.get("records", [])
    dialogue_by_id = {record["id"]: record for record in dialogue_records}

    units = translation.get("units")
    if not isinstance(units, list):
        raise SystemExit(f"Malformed units array: {translation_path.relative_to(ROOT)}")

    for unit in units:
        source = unit.get("source")
        if not isinstance(source, dict):
            raise SystemExit(f"Malformed source metadata in {translation_path.relative_to(ROOT)}: {unit.get('id')}")
        record_id = source.get("source_record_id")
        if record_id is None:
            continue
        immutable = dialogue_by_id.get(record_id)
        if immutable is None:
            raise SystemExit(f"Unknown dialogue source_record_id {record_id} in {translation_path.relative_to(ROOT)}")

        if source.get("page_provenance") != immutable.get("page_provenance"):
            provenance_mismatches.append({
                "scene": scene,
                "unit_id": unit.get("id"),
                "source_record_id": record_id,
                "translation": source.get("page_provenance"),
                "dialogue": immutable.get("page_provenance"),
            })

        exact_label = immutable.get("speaker_label")
        if source.get("speaker_label") != exact_label:
            source["speaker_label"] = exact_label
            speaker_repairs += 1

    move_id = SOURCE_ORDER_MOVES.get(scene)
    if move_id is not None:
        positions = [index for index, unit in enumerate(units) if unit.get("id") == move_id]
        if len(positions) != 1:
            raise SystemExit(f"Expected exactly one {move_id} in {translation_path.relative_to(ROOT)}")
        position = positions[0]
        if position != 0:
            unit = units.pop(position)
            units.insert(0, unit)
            order_repairs += 1

    if translation.get("unit_count") != len(units):
        raise SystemExit(f"unit_count changed unexpectedly in {translation_path.relative_to(ROOT)}")

    loaded[scene] = (translation_path, translation)

if provenance_mismatches:
    print(f"PAGE_PROVENANCE_MISMATCHES={len(provenance_mismatches)}")
    for mismatch in provenance_mismatches:
        print(json.dumps(mismatch, ensure_ascii=False, separators=(",", ":")))
    raise SystemExit("Page provenance mismatches require manual source review; no translation files were rewritten")

changed_scenes: list[int] = []
for scene, (translation_path, translation) in loaded.items():
    units = translation["units"]
    pages = [unit["source"]["page_provenance"][0]["pdf_page"] for unit in units]
    if pages != sorted(pages):
        raise SystemExit(f"Source-page order still regresses in {translation_path.relative_to(ROOT)}: {pages}")

    original = json.loads(translation_path.read_text(encoding="utf-8"))
    if translation != original:
        translation_path.write_text(
            json.dumps(translation, ensure_ascii=False, separators=(",", ":")) + "\n",
            encoding="utf-8",
        )
        changed_scenes.append(scene)

print(
    "Synchronized Tirumbippaar English source metadata: "
    f"speaker_repairs={speaker_repairs}, order_repairs={order_repairs}, changed_scenes={changed_scenes}"
)
