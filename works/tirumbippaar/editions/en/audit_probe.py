#!/usr/bin/env python3
"""Diagnostic preflight for the reconciled Tirumbippaar English reader export."""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
WORK = ROOT / "works" / "tirumbippaar"
TRANS = WORK / "translations" / "records"
DIALOGUES = WORK / "dialogues" / "records"
UNIT_RE = re.compile(r"^tirumbippaar-en-s(\d{3})-u\d{3}$")
SYNTH = re.compile(r"^\s*\(Scene ends\.\)\s*$", re.I)

units = 0
kinds: Counter[str] = Counter()
synthetic: list[str] = []
page_regressions: list[tuple[str, int, int]] = []
id_errors: list[tuple[int, str]] = []
duplicate_ids: list[str] = []
dialogue_links: list[str] = []
cross_page: list[str] = []
direct_dialogue: list[str] = []
occurrences: list[str] = []
scene_counts: dict[int, int] = {}
seen_ids: set[str] = set()
parse_errors: list[str] = []

for scene in range(1, 94):
    path = TRANS / f"scene-{scene:02d}.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        msg = f"scene={scene} path={path.relative_to(ROOT)} error={exc}"
        print("TRANSLATION_JSON_PARSE_ERROR", msg)
        parse_errors.append(msg)
        continue
    scene_units = data["units"]
    scene_counts[scene] = len(scene_units)
    units += len(scene_units)
    prev_page = 0
    for unit in scene_units:
        uid = unit["id"]
        match = UNIT_RE.match(uid)
        if not match or int(match.group(1)) != scene:
            id_errors.append((scene, uid))
        if uid in seen_ids:
            duplicate_ids.append(uid)
        seen_ids.add(uid)
        kinds[unit["kind"]] += 1
        prov = unit["source"]["page_provenance"]
        page = prov[0]["pdf_page"]
        if page < prev_page:
            page_regressions.append((uid, prev_page, page))
        prev_page = page
        if len(prov) > 1:
            cross_page.append(uid)
        rid = unit["source"].get("source_record_id")
        if rid:
            dialogue_links.append(rid)
        elif unit["kind"] == "dialogue":
            direct_dialogue.append(uid)
        occ = unit["source"].get("source_occurrence_id")
        if occ:
            occurrences.append(occ)
        tr = unit.get("translation", {})
        text = tr.get("english_text")
        if isinstance(text, str) and SYNTH.match(text):
            synthetic.append(uid)

immutable_ids: list[str] = []
for scene in range(1, 94):
    path = DIALOGUES / f"scene-{scene:02d}.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        msg = f"scene={scene} path={path.relative_to(ROOT)} error={exc}"
        print("DIALOGUE_JSON_PARSE_ERROR", msg)
        parse_errors.append(msg)
        continue
    records = data if isinstance(data, list) else data.get("records", [])
    immutable_ids.extend(r["id"] for r in records)

print("TIRUMBIPPAAR READER PREFLIGHT")
print("actual_units=", units)
print("kind_counts=", dict(kinds))
print("scene_counts=", json.dumps(scene_counts, sort_keys=True))
print("synthetic_scene_end_units=", synthetic)
print("page_regressions=", page_regressions)
print("id_errors=", id_errors)
print("duplicate_unit_ids=", duplicate_ids)
print("cross_page_units=", cross_page)
print("direct_unlabelled_dialogue_units=", direct_dialogue)
print("song_occurrence_links=", occurrences)
print("dialogue_links_count=", len(dialogue_links), "unique=", len(set(dialogue_links)), "immutable=", len(immutable_ids))
print("missing_dialogue_links=", sorted(set(immutable_ids) - set(dialogue_links)))
print("extra_dialogue_links=", sorted(set(dialogue_links) - set(immutable_ids)))
if parse_errors:
    raise SystemExit(f"JSON parse errors: {len(parse_errors)}")
