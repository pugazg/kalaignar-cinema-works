#!/usr/bin/env python3
"""Restore corrected source order for stable-ID Tirumbippaar translation units.

The English reconciliation preserves historical unit IDs. Two source-proven
carry-over stage directions were added after the historical pass and therefore
have higher IDs even though they belong at the beginning of their scenes.
This helper moves only those known units into printed source order; it never
renumbers, rewrites or translates unit content.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RECORDS = ROOT / "works" / "tirumbippaar" / "translations" / "records"

MOVES = {
    37: "tirumbippaar-en-s037-u051",
    39: "tirumbippaar-en-s039-u026",
}


def normalize(scene: int, unit_id: str) -> None:
    path = RECORDS / f"scene-{scene:02d}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    units = data.get("units")
    if not isinstance(units, list):
        raise SystemExit(f"Malformed units array: {path.relative_to(ROOT)}")

    matches = [unit for unit in units if unit.get("id") == unit_id]
    if len(matches) != 1:
        raise SystemExit(f"Expected exactly one {unit_id} in {path.relative_to(ROOT)}")

    unit = matches[0]
    units = [item for item in units if item.get("id") != unit_id]
    units.insert(0, unit)
    data["units"] = units

    pages = [item["source"]["page_provenance"][0]["pdf_page"] for item in units]
    if pages != sorted(pages):
        raise SystemExit(f"Source-page order still regresses in {path.relative_to(ROOT)}: {pages}")

    if data.get("unit_count") != len(units):
        raise SystemExit(f"unit_count changed unexpectedly in {path.relative_to(ROOT)}")

    path.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    print(f"Normalized source order without renumbering: scene {scene} / {unit_id}")


for scene, unit_id in MOVES.items():
    normalize(scene, unit_id)
