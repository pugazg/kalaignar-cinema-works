#!/usr/bin/env python3
"""Diagnostic-only preflight for Tirumbippaar English reader export."""
import json, re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
WORK = ROOT / "works" / "tirumbippaar"
TRANS = WORK / "translations" / "records"
DIALOGUES = WORK / "dialogues" / "records"
SYNTH = re.compile(r"^\s*\(Scene ends\.\)\s*$", re.I)

units = 0
kinds = Counter()
synthetic = []
page_regressions = []
id_errors = []
dialogue_links = []
cross_page = []
direct_dialogue = []
occurrences = []
scene_counts = {}

for scene in range(1, 94):
    path = TRANS / f"scene-{scene:02d}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    scene_units = data["units"]
    scene_counts[scene] = len(scene_units)
    units += len(scene_units)
    prev_page = 0
    for ordinal, unit in enumerate(scene_units, 1):
        uid = unit["id"]
        if uid != f"tirumbippaar-en-s{scene:03d}-u{ordinal:03d}":
            id_errors.append((scene, ordinal, uid))
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

immutable_ids = []
for scene in range(1, 94):
    data = json.loads((DIALOGUES / f"scene-{scene:02d}.json").read_text(encoding="utf-8"))
    records = data if isinstance(data, list) else data.get("records", [])
    immutable_ids.extend(r["id"] for r in records)

print("TIRUMBIPPAAR READER PREFLIGHT")
print("actual_units=", units)
print("kind_counts=", dict(kinds))
print("scene_counts=", json.dumps(scene_counts, sort_keys=True))
print("synthetic_scene_end_units=", synthetic)
print("page_regressions=", page_regressions)
print("id_errors=", id_errors)
print("cross_page_units=", cross_page)
print("direct_unlabelled_dialogue_units=", direct_dialogue)
print("song_occurrence_links=", occurrences)
print("dialogue_links_count=", len(dialogue_links), "unique=", len(set(dialogue_links)), "immutable=", len(immutable_ids))
print("missing_dialogue_links=", sorted(set(immutable_ids) - set(dialogue_links)))
print("extra_dialogue_links=", sorted(set(dialogue_links) - set(immutable_ids)))
