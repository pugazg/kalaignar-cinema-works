#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "dialogues"
C = ROOT / "characters"

ENTITY_DEFS = {
    "muthan": ("முத்தன்", "character", ["(திகிலுடன்) முத்", "முத்தன்"], "Central character. Exact label `முத்` is record-aware because the same shorthand is also used for முத்தாயி."),
    "muthayi": ("முத்தாயி", "character", ["முத்தா", "முத்தாயி"], "Central character. Scene 63 establishes source label `முத்தா` as முத்தாயி; exact label `முத்` is record-aware."),
    "sukhadev": ("சுகதேவ்", "character", ["சுக", "சுகதேவ்"], "Recurring prince character; abbreviated and full labels are contextually continuous."),
    "sumathi": ("சுமதி", "character", ["சும", "சுமதி"], "Recurring named character; abbreviated and full labels are contextually continuous."),
    "thanapathi": ("தனபதி", "character", ["தனபதி"], "Recurring named/title character. Exact label `தன` is record-aware because it is also reused for தனவணிகர்."),
    "thanavanigar": ("தனவணிகர்", "character", ["தனவணிகர்", "வணி", "வணிகர்"], "The same merchant with the child recurs across scenes 36, 42, 43 and 45. Exact label `தன` is record-aware because scene 36 also uses it once for தனபதி."),
    "tirisangu": ("திரிசங்கு", "character", ["திரி", "திரிசங்கு", "திரு", "திருசங்கு"], "Recurring character. The source varies abbreviation/spelling and includes the exceptional `திரு; ...` delimiter; dialogue evidence remains unchanged."),
    "baladevar": ("பலதேவர்", "character", ["பல", "பலதேவர்"], "Recurring pாளையக்காரர் character; abbreviated/full labels are continuous."),
    "poongavanam": ("பூங்காவனம்", "character", ["பூங்", "பூங்காவனம்"], "Recurring named character; abbreviated/full labels are continuous."),
    "poobathi": ("பூபதி", "character", ["பூப", "பூபதி"], "Recurring physician character; abbreviated/full labels are continuous."),
    "maykainathar": ("மாய்கைநாதர் / மாப்பிள்ளைதாசு", "character", ["சாமி", "சாமியார்", "மாப்பிள்ளை", "மாய்", "மாய்கை", "மாய்கைநாதர்", "மாய்க்கை", "மாய்க்கை நாதர்"], "One recurring ascetic character across source spelling/abbreviation forms. Scenes 61–62 identify the later மாப்பிள்ளைதாசு/மாப்பிள்ளை form as the same சாமியார்; no dialogue label is rewritten."),
    "vedalam": ("வேதாளம்", "character", ["வே", "வேதா", "வேதாளம்"], "Recurring character; source contexts establish `வே` here as வேதாளம்."),
    "velazhagan": ("வேலழகன்", "character", ["தள", "வேல", "வேலழ", "வேலழகன்"], "Recurring commander character. Scene 49 establishes `தள` as the தளபதி வேலழகன்."),
    "kurumban": ("குறும்பன்", "character", ["குறு", "குறும்பன்"], "Recurring subordinate character; abbreviated/full labels are continuous."),
    "vengai-king": ("வேங்கை நாட்டு மன்னன்", "character", ["அர", "அரச", "சக்கரவர்த்தி"], "Unnamed Vengai ruler. Scene 55 uses `சக்கரவர்த்தி`; scene 60 uses `அரச`/`அர` for the same ruler."),
    "queen": ("பலதேவர் மனைவி / ராணி", "character", ["ராணி"], "Unnamed recurring wife of பலதேவர் and mother of சுகதேவ்; source scene 13 explicitly identifies this relationship."),
    "recruit-man-role": ("ஆள்", "role", ["ஆள்"], "Generic recruit/man label reused for more than one person in the enlistment scene; this is a role category, not one continuing individual."),
    "voice-role": ("குரல்", "role", ["குரல்"], "Source-visible voice/performance label; no unsupported human identity is imposed."),
    "friend-role": ("நண்பன்", "role", ["நண்", "நண்பன்"], "Generic friend label/category across Muthan's friend groups; grouping does not assert one physical person."),
    "comrade-1-role": ("தோழன் 1", "role", ["தோழன் 1"], "Source-numbered unnamed comrade role."),
    "comrade-2-role": ("தோழன் 2", "role", ["தோழ 2", "தோழன் 2"], "Source-numbered unnamed comrade role; `தோழ 2` is the same numbered role within scene 39."),
    "comrade-3-role": ("தோழன் 3", "role", ["தோழன் 3"], "Source-numbered unnamed comrade role."),
    "drummer-role": ("பறையடிப்பவன்", "role", ["பறையடிப்பவன்"], "Unnamed public-announcement/drummer role."),
    "warrior-role": ("வீரன்", "role", ["வீர", "வீரன்", "வீரன் 1", "வீரன் 2", "வீரன் 3", "வீரன் 4"], "Generic/numbered warrior labels grouped as a role category; this does not assert that every occurrence is one soldier."),
    "people-collective": ("மக்கள்", "collective", ["மக்கள்"], "Collective source label."),
    "warriors-collective": ("வீரர்கள்", "collective", ["வீரர்கள்"], "Collective source label, kept distinct from singular warrior-role records."),
}

GLOBAL_LABEL_TO_ENTITY = {}
for key, (_, _, labels, _) in ENTITY_DEFS.items():
    for label in labels:
        if label in GLOBAL_LABEL_TO_ENTITY:
            raise AssertionError((label, key, GLOBAL_LABEL_TO_ENTITY[label]))
        GLOBAL_LABEL_TO_ENTITY[label] = key

RECORD_AWARE_LABELS = {"முத்", "தன"}


def load_records():
    explicit = []
    for p in sorted((D / "records").glob("scene-*.json")):
        explicit.extend(json.loads(p.read_text(encoding="utf-8")))
    supplements = json.loads((D / "source-role-resolved-records.json").read_text(encoding="utf-8"))
    return explicit, supplements


def entity_id(key: str) -> str:
    return f"ammaiyappan-char-{key}"


def main():
    C.mkdir(exist_ok=True)
    final_index = json.loads((D / "final-index.json").read_text(encoding="utf-8"))
    preflight = json.loads((C / "labels-preflight.json").read_text(encoding="utf-8"))
    muth_doc = json.loads((C / "muth-record-dispositions.json").read_text(encoding="utf-8"))

    explicit, supplements = load_records()
    assert len(explicit) == 1009
    assert len(supplements) == final_index['source_role_resolved_dialogue_records']
    rows = explicit + supplements
    expected_total = final_index['total_dialogue_units_for_downstream_indexing']
    assert len(rows) == expected_total
    assert len({r['id'] for r in rows}) == expected_total

    observed_labels = {r["speaker_label"] for r in rows}
    preflight_labels = {x["speaker_label"] for x in preflight["inventory"]}
    assert observed_labels == preflight_labels
    assert len(observed_labels) == 62
    assert set(GLOBAL_LABEL_TO_ENTITY) | RECORD_AWARE_LABELS == observed_labels

    muth_map = {x["record_id"]: x for x in muth_doc["dispositions"]}
    assert len(muth_map) == 177
    assert Counter(x["entity_key"] for x in muth_map.values()) == Counter({"muthan": 80, "muthayi": 97})

    dispositions = []
    by_entity = defaultdict(list)
    by_label = defaultdict(list)

    for r in rows:
        rid = r["id"]
        label = r["speaker_label"]
        if label == "முத்":
            d = muth_map.get(rid)
            assert d is not None, rid
            key = d["entity_key"]
            basis = d["basis"]
            mode = "record-aware"
        elif label == "தன":
            key = "thanapathi" if rid == "ammaiyappan-s036-d006" else "thanavanigar"
            basis = "scene-36 turn context before merchant transition" if key == "thanapathi" else "merchant continuity across scenes 36/43/45"
            mode = "record-aware"
        else:
            key = GLOBAL_LABEL_TO_ENTITY[label]
            basis = "verified global label/entity continuity" if ENTITY_DEFS[key][1] == "character" else "verified role/collective disposition"
            mode = "global"

        assert key in ENTITY_DEFS
        row = {
            "record_id": rid,
            "source_speaker_label": label,
            "archive_scene_id": r["archive_scene_id"],
            "archive_scene_ordinal": r["archive_scene_ordinal"],
            "entity_id": entity_id(key),
            "entity_key": key,
            "mapping_mode": mode,
            "basis": basis,
            "dialogue_record_modified": False,
        }
        dispositions.append(row)
        by_entity[key].append((r, row))
        by_label[label].append(row)

    assert len(dispositions) == expected_total
    assert len({x['record_id'] for x in dispositions}) == expected_total

    muth_counts = Counter(x["entity_key"] for x in dispositions if x["source_speaker_label"] == "முத்")
    assert muth_counts == Counter({"muthan": 80, "muthayi": 97}), muth_counts
    than_rows = [x for x in dispositions if x["source_speaker_label"] == "தன"]
    assert len(than_rows) == 10
    than_counts = Counter(x["entity_key"] for x in than_rows)
    assert than_counts == Counter({"thanavanigar": 9, "thanapathi": 1}), than_counts
    assert {x["record_id"] for x in than_rows if x["entity_key"] == "thanapathi"} == {"ammaiyappan-s036-d006"}

    label_inventory = []
    for label in sorted(observed_labels):
        ds = by_label[label]
        entity_ids = sorted({x["entity_id"] for x in ds})
        mode = "record-aware" if label in RECORD_AWARE_LABELS else "global"
        if mode == "global":
            assert len(entity_ids) == 1, (label, entity_ids)
        else:
            assert len(entity_ids) == 2, (label, entity_ids)
        label_inventory.append({
            "speaker_label": label,
            "record_count": len(ds),
            "scenes": sorted({x["archive_scene_ordinal"] for x in ds}),
            "mapping_mode": mode,
            "entity_ids": entity_ids,
            "unresolved_record_count": 0,
        })

    entities = []
    for key, (preferred, etype, safe_labels, notes) in ENTITY_DEFS.items():
        rs = by_entity[key]
        assert rs, key
        observed = sorted({r["speaker_label"] for r, _ in rs})
        record_aware = sorted(set(observed) & RECORD_AWARE_LABELS)
        global_observed = sorted(set(observed) - RECORD_AWARE_LABELS)
        assert set(global_observed) == set(safe_labels), (key, global_observed, safe_labels)
        entities.append({
            "id": entity_id(key),
            "preferred_name_ta": preferred,
            "entity_type": etype,
            "status": "verified",
            "confidence": "high",
            "global_source_labels": sorted(safe_labels),
            "record_aware_source_labels": record_aware,
            "observed_source_labels": observed,
            "scenes": sorted({r["archive_scene_ordinal"] for r, _ in rs}),
            "dialogue_record_count": len(rs),
            "record_aware_record_count": sum(1 for r, _ in rs if r["speaker_label"] in RECORD_AWARE_LABELS),
            "supporting_records": [r["id"] for r, _ in rs[:3]],
            "notes": notes,
        })

    assert len(entities) == 26
    assert sum(x["dialogue_record_count"] for x in entities) == expected_total

    shared = {
        label: sorted({x["entity_id"] for x in by_label[label]})
        for label in sorted(RECORD_AWARE_LABELS)
    }
    assert shared["முத்"] == sorted([entity_id("muthan"), entity_id("muthayi")])
    assert shared["தன"] == sorted([entity_id("thanapathi"), entity_id("thanavanigar")])

    record_aware = {
        "work_id": "ammaiyappan",
        "status": "complete-verified",
        "record_aware_labels": ["முத்", "தன"],
        "record_aware_record_count": sum(1 for x in dispositions if x["mapping_mode"] == "record-aware"),
        "unresolved_record_count": 0,
        "label_entity_counts": {
            "முத்": dict(sorted(muth_counts.items())),
            "தன": dict(sorted(than_counts.items())),
        },
        "policy": "Dialogue speaker labels remain immutable. Only this derivative assigns reused exact labels to entities by record context.",
        "dispositions": [x for x in dispositions if x["mapping_mode"] == "record-aware"],
    }
    assert record_aware["record_aware_record_count"] == 187

    entities_doc = {
        "work_id": "ammaiyappan",
        "status": "complete-verified-reconciled",
        "source_label_inventory": "labels-inventory.json",
        "dialogue_index": "../dialogues/final-index.json",
        "record_aware_dispositions": "record-aware-dispositions.json",
        "dialogue_records_source": expected_total,
        "distinct_source_labels": 62,
        "entity_count": 26,
        "verified_entity_count": 26,
        "review_entity_count": 0,
        "unresolved_entity_count": 0,
        "verified_label_count": 62,
        "review_label_count": 0,
        "unresolved_label_count": 0,
        "record_aware_label_count": 2,
        "record_aware_record_count": 187,
        "coverage_note": f"All {expected_total:,} downstream dialogue units and all 62 exact source speaker labels have a verified disposition. `முத்` and `தன` are record-aware; no dialogue evidence is rewritten.",
        "entities": entities,
    }

    schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "ammaiyappan-character-index-schema",
        "title": "Ammayappan character/entity derivative",
        "description": "Verified derivative mapping exact dialogue labels and record-aware reused shorthands to stable entities/role categories. Dialogue records remain immutable.",
        "type": "object",
        "required": ["work_id", "status", "entities"],
        "properties": {
            "work_id": {"const": "ammaiyappan"},
            "status": {"enum": ["in-progress", "complete-verified-reconciled"]},
            "entities": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["id", "preferred_name_ta", "entity_type", "status", "confidence", "global_source_labels", "record_aware_source_labels", "scenes", "dialogue_record_count", "notes"],
                    "properties": {
                        "id": {"type": "string", "pattern": "^ammaiyappan-char-[a-z0-9-]+$"},
                        "preferred_name_ta": {"type": "string", "minLength": 1},
                        "entity_type": {"enum": ["character", "role", "collective", "unresolved"]},
                        "status": {"enum": ["verified", "review", "unresolved"]},
                        "confidence": {"enum": ["high", "medium", "low"]},
                        "global_source_labels": {"type": "array", "uniqueItems": True, "items": {"type": "string"}},
                        "record_aware_source_labels": {"type": "array", "uniqueItems": True, "items": {"type": "string"}},
                        "scenes": {"type": "array", "uniqueItems": True, "items": {"type": "integer", "minimum": 1, "maximum": 63}},
                        "dialogue_record_count": {"type": "integer", "minimum": 1},
                        "notes": {"type": "string"},
                    },
                    "additionalProperties": True,
                },
            },
        },
        "additionalProperties": True,
    }

    index = {
        "work_id": "ammaiyappan",
        "status": "complete-verified-reconciled",
        "dialogue_index": "../dialogues/final-index.json",
        "schema": "schema.json",
        "label_inventory": "labels-inventory.json",
        "record_aware_dispositions": "record-aware-dispositions.json",
        "entities": "entities.json",
        "dialogue_records_source": expected_total,
        "distinct_source_labels": 62,
        "entity_count": 26,
        "verified_entities": 26,
        "review_entities": 0,
        "unresolved_entities": 0,
        "verified_labels": 62,
        "review_labels": 0,
        "unresolved_labels": 0,
        "record_aware_labels": ["முத்", "தன"],
        "record_aware_records": 187,
        "label_coverage": "62/62",
        "dialogue_unit_coverage": f"{expected_total}/{expected_total}",
        "remaining_unmapped_labels": 0,
        "remaining_unmapped_records": 0,
        "dialogue_records_modified": False,
        "next_activity": "Open English translation/reconciliation only after synchronizing work-level handover/status to this completed character/entity layer.",
    }

    readme = """# அம்மையப்பன் — character/entity index

**Stage:** structured derivatives  
**Canonical authority:** 105/105 dual-gate verified Tamil, 63/63 verified scene derivatives, and the complete 1,024-unit dialogue layer  
**Character/entity status:** **COMPLETE VERIFIED RECONCILED — 62/62 exact labels, 1,024/1,024 dialogue units**

This directory maps the immutable dialogue evidence to stable characters, unnamed roles, or collective categories. It never rewrites, normalizes, or relabels dialogue records.

## Completion summary

- downstream dialogue units: **1,024**
- exact source speaker labels: **62**
- stable entities / role categories: **26**
- verified entities: **26**
- unresolved entities: **0**
- verified label coverage: **62/62**
- dialogue-unit coverage: **1,024/1,024**
- record-aware exact labels: **2** — `முத்`, `தன`
- record-aware units: **187**
- unresolved record dispositions: **0**
- dialogue records modified by this layer: **no**

## Record-aware cases

`முத்` cannot be globally normalized: the source uses it for both **முத்தன்** and **முத்தாயி**. The verified split is **80 → முத்தன் / 97 → முத்தாயி** and is preserved in `muth-record-dispositions.json` and the consolidated `record-aware-dispositions.json`.

`தன` also cannot be globally normalized. In scene 36 record `ammaiyappan-s036-d006` it is **தனபதி**; the remaining nine `தன` records belong to the recurring **தனவணிகர்**. This split is stored only in the derivative identity layer.

## Other important reconciliations

- `திரி / திரிசங்கு / திரு / திருசங்கு` → **திரிசங்கு**; the exceptional source semicolon form remains untouched in dialogue evidence.
- `வே / வேதா / வேதாளம்` → **வேதாளம்**.
- `தள / வேல / வேலழ / வேலழகன்` → **வேலழகன்**.
- `அர / அரச / சக்கரவர்த்தி` → the unnamed **வேங்கை நாட்டு மன்னன்**.
- `முத்தா` in scene 63 → **முத்தாயி**.
- `சாமி / சாமியார் / மாய் / மாய்கை* / மாப்பிள்ளை` → the same ascetic character, represented here as **மாய்கைநாதர் / மாப்பிள்ளைதாசு**.
- generic `ஆள்`, `நண்பன்`, and singular `வீரன்` variants are role categories; grouping them does **not** assert that every occurrence is one physical person.
- `வீரர்கள்` and `மக்கள்` remain collectives.

## Files

- `schema.json` — character/entity derivative schema.
- `labels-inventory.json` — all 62 exact labels with global vs record-aware disposition.
- `record-aware-dispositions.json` — all 187 record-level assignments for reused labels.
- `muth-record-dispositions.json` — detailed earlier `முத்` audit/disposition authority.
- `entities.json` — complete 26-entity mapping.
- `index.json` — compact completion checkpoint.

## Next activity

Synchronize the work-level handover/status to this closure, then open the English translation/reconciliation layer. Tamil dialogue evidence remains frozen unless a new source-backed correction is independently established.
"""

    readme = readme.replace("1,024", f"{expected_total:,}")

    (C / "schema.json").write_text(json.dumps(schema, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (C / "labels-inventory.json").write_text(json.dumps({"work_id": "ammaiyappan", "status": "complete-verified", "distinct_source_labels": 62, "labels": label_inventory}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (C / "record-aware-dispositions.json").write_text(json.dumps(record_aware, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (C / "entities.json").write_text(json.dumps(entities_doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (C / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (C / "README.md").write_text(readme, encoding="utf-8")

    print(json.dumps({
        "dialogue_units": expected_total,
        "labels": 62,
        "entities": 26,
        "record_aware_records": 187,
        "muth": dict(sorted(muth_counts.items())),
        "than": dict(sorted(than_counts.items())),
        "unresolved": 0,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
