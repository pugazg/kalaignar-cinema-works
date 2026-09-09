#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
W = REPO / "works" / "naam"
D = W / "dialogues"
C = W / "characters"
N = W / "notes"
S = W / "scenes"
T = W / "transcription" / "parts"

NEXT = (
    "Begin Phase 8 song/performance/authorship gating from the six mapped source-visible performance structures. "
    "Preserve booklet wording, lineation, role cues and source-visible credits; adjudicate authorship only where explicit source evidence supports it. "
    "Keep PDF 16 `ஆயிரம் தெய்வங்கள்` credited to `பாரதியார்` despite the broad PDF 4 Kalaignar `பாடல்` credit, and do not infer authorship for the remaining blocks without source evidence. "
    "Run whole-work song/performance coverage QA before opening English translation. Do not rewrite canonical Tamil, scene text, immutable dialogue records, or character/entity mappings."
)
PHASE7_PREFIX = "Begin Phase 7 character/entity indexing from the complete-verified immutable dialogue layer."

# preferred_name_ta, entity_type, exact dialogue labels, notes
ENTITY_DEFS = {
    "annumalai": (
        "அண்ணுமலை",
        "character",
        ["அண்ணுமலை"],
        "Named recurring character. Scene 3 narrative also prints `அண்ணாமலை`; the immutable dialogue label `அண்ணுமலை` is preserved exactly and is not rewritten.",
    ),
    "meenu": (
        "மீனு",
        "character",
        ["மீனு", "உன்மீனு"],
        "Recurring character. `உன்மீனு` is the source-explicit scene-41 label anomaly and maps here only in the separate entity layer; the dialogue record remains unchanged.",
    ),
    "kandasami": ("கந்தசாமி", "character", ["கந்தசாமி"], "Named recurring character in scenes 14 and 16."),
    "kumaran": ("குமரன்", "character", ["கும", "குமரன்"], "Central character; abbreviated and full labels are continuous across the work."),
    "sanjeevi": ("சஞ்சீவி", "character", ["சஞ்", "சஞ்சீவி"], "Recurring வைத்தியர் character; abbreviated and full labels are continuous."),
    "jeevanandar": ("ஜீவானந்தர்", "character", ["ஜீவா", "ஜீவானந்த", "ஜீவானந்தர்"], "Recurring character; abbreviated/truncated/full source labels are continuous."),
    "gnanam": ("ஞானம்", "character", ["ஞா", "ஞானம்"], "Recurring character identified in scene 3 as the ஜமீன்தார்'s wife; abbreviated/full labels are continuous."),
    "thangaiyan": ("தங்கையன்", "character", ["தங்", "தங்கையன்"], "Scene 4 explicitly establishes the full name before the abbreviated label."),
    "narayani": ("நாராயணி", "character", ["நாரா", "நாராயணி"], "Recurring character; abbreviated/full labels are continuous."),
    "bheemasenan": ("பீமசேனன்", "character", ["பீமசேனன்"], "Named character."),
    "prema": ("பிரேமா", "character", ["பிரே", "பிரேமா"], "Recurring character; scene 4 identifies her as the வைத்தியர்'s daughter; abbreviated/full labels are continuous."),
    "paramasivam": ("பரமசிவம்", "character", ["பரமசிவம்"], "Named character."),
    "mallayappan": (
        "மல்லயப்பன் / மலையப்பன்",
        "character",
        ["மல்", "மல்ல", "மல்லயப்ப", "மல்லயப்பர்", "மல்லயப்பன்", "மலைய", "மலையப்பர்", "மலையப்பன்"],
        "One recurring ஜமீன்தார் character across source abbreviation, honorific and spelling variants. Scene 3 links `மல்ல`, `மல்லயப்பர்` and `மல்லயப்பன்`; later scenes use `மலையப்பர்` / `மலையப்பன்`. No source label is normalized upstream.",
    ),
    "mathirai": ("மாத்திரை", "character", ["மாத்", "மாத்திரை"], "Scene 4 explicitly introduces மாத்திரை as the வைத்தியர்'s worker; abbreviated/full labels are continuous."),
    "oru-role": ("ஒரு", "role", ["ஒரு"], "Generic source role label. Grouping is categorical and does not assert one physical person across turns."),
    "oruvan-role": ("ஒருவன்", "role", ["ஒருவன்"], "Generic male role reused across multiple scenes; entity is a role category, not one continuing individual."),
    "sub-inspector-role": ("சப் இன்ஸ்.", "role", ["சப் இன்ஸ்."], "Unnamed sub-inspector role; no unsupported personal name is supplied."),
    "thief-role": ("திருடன்", "role", ["திருடன்"], "Unnamed thief role/category; grouping does not assert a single person beyond source context."),
    "judge-role": ("நீதிபதி", "role", ["நீதிபதி"], "Unnamed judge role."),
    "poosari-role": ("பூசாரி", "role", ["பூசாரி"], "Unnamed priest role/category."),
    "woman-role": ("பெண்", "role", ["பெண்"], "Unnamed woman role."),
    "elder-role": ("பெரியவர்", "role", ["பெரியவர்"], "Unnamed elder role."),
    "purohithar-role": ("புரோகிதர்", "role", ["புரோகிதர்"], "Unnamed priest/purohit role/category."),
    "mattroru-role": ("மற்றொரு", "role", ["மற்றொரு"], "Source-generic 'another' role; not forced into a named identity."),
    "mattroruvan-role": ("மற்றொருவன்", "role", ["மற்றொருவன்"], "Source-generic 'another man' role; not forced into a named identity."),
    "mattroruvar-role": ("மற்றொருவர்", "role", ["மற்றொருவர்"], "Source-generic 'another person' role; not forced into a named identity."),
    "vanthavar-role": ("வந்தவர்", "role", ["வந்தவர்"], "Unnamed arriving-person role; no identity inference is imposed."),
    "makkal-collective": ("மக்கள்", "collective", ["மக்கள்"], "Collective source label."),
}

LABEL_TO_ENTITY: dict[str, str] = {}
for key, (_, _, labels, _) in ENTITY_DEFS.items():
    for label in labels:
        assert label not in LABEL_TO_ENTITY, (label, key, LABEL_TO_ENTITY.get(label))
        LABEL_TO_ENTITY[label] = key


def entity_id(key: str) -> str:
    return f"naam-char-{key}"


def rd(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def wr(path: str, text: str, changed: list[str]) -> None:
    p = REPO / path
    old = p.read_text(encoding="utf-8") if p.exists() else None
    if old != text:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
        changed.append(path)


def load_records() -> list[dict]:
    rows: list[dict] = []
    for p in sorted((D / "records").glob("scene-*.json")):
        rows.extend(json.loads(p.read_text(encoding="utf-8")))
    return rows


def file_hashes(paths: list[Path]) -> dict[str, str]:
    return {str(p.relative_to(REPO)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}


def schema() -> dict:
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "naam-character-entity.schema.json",
        "title": "Naam character/entity record",
        "type": "object",
        "required": [
            "id", "preferred_name_ta", "entity_type", "status", "confidence",
            "source_labels", "scenes", "dialogue_record_count", "notes"
        ],
        "properties": {
            "id": {"type": "string", "pattern": "^naam-char-[a-z0-9-]+$"},
            "preferred_name_ta": {"type": "string", "minLength": 1},
            "entity_type": {"enum": ["character", "role", "collective"]},
            "status": {"const": "verified"},
            "confidence": {"const": "high"},
            "source_labels": {"type": "array", "minItems": 1, "uniqueItems": True, "items": {"type": "string", "minLength": 1}},
            "scenes": {"type": "array", "minItems": 1, "uniqueItems": True, "items": {"type": "integer", "minimum": 1, "maximum": 45}},
            "dialogue_record_count": {"type": "integer", "minimum": 1},
            "supporting_records": {"type": "array", "items": {"type": "string"}},
            "notes": {"type": "string", "minLength": 1},
        },
        "additionalProperties": False,
    }


def main() -> None:
    changed: list[str] = []
    dialogue_index = json.loads((D / "index.json").read_text(encoding="utf-8"))
    dialogue_qa = json.loads((N / "dialogue-index-qa.json").read_text(encoding="utf-8"))
    preflight = json.loads((C / "labels-preflight.json").read_text(encoding="utf-8"))
    assert dialogue_index["status"] == "complete-verified"
    assert dialogue_index["dialogue_record_count"] == 590
    assert dialogue_qa["status"] == "PASS"
    assert preflight["status"] == "review-ready"
    assert preflight["dialogue_units_scanned"] == 590
    assert preflight["distinct_exact_source_labels"] == 45

    protected = sorted(S.glob("scene-*.md")) + sorted((D / "records").glob("scene-*.json")) + [D / "index.json", N / "dialogue-index-qa.json"] + sorted(T.glob("pdf-*.md"))
    before_hashes = file_hashes(protected)

    records = load_records()
    assert len(records) == 590
    assert len({r["id"] for r in records}) == 590
    observed_labels = {r["speaker_label"] for r in records}
    preflight_labels = {x["speaker_label"] for x in preflight["inventory"]}
    assert observed_labels == preflight_labels
    assert observed_labels == set(LABEL_TO_ENTITY), sorted(observed_labels ^ set(LABEL_TO_ENTITY))
    assert len(observed_labels) == 45
    assert len(ENTITY_DEFS) == 28

    by_entity: dict[str, list[dict]] = defaultdict(list)
    by_label: dict[str, list[dict]] = defaultdict(list)
    dispositions = []
    for r in records:
        label = r["speaker_label"]
        key = LABEL_TO_ENTITY[label]
        preferred, etype, _, _ = ENTITY_DEFS[key]
        mapping_mode = "global-alias" if etype == "character" else ("collective-category" if etype == "collective" else "role-category")
        row = {
            "record_id": r["id"],
            "source_speaker_label": label,
            "scene_id": r["scene_id"],
            "scene_ordinal": r["scene_ordinal"],
            "entity_id": entity_id(key),
            "entity_key": key,
            "preferred_name_ta": preferred,
            "entity_type": etype,
            "mapping_mode": mapping_mode,
            "dialogue_record_modified": False,
        }
        dispositions.append(row)
        by_entity[key].append(r)
        by_label[label].append(row)

    assert len(dispositions) == 590
    assert len({x["record_id"] for x in dispositions}) == 590

    label_inventory = []
    for label in sorted(observed_labels):
        ds = by_label[label]
        entity_ids = sorted({x["entity_id"] for x in ds})
        assert len(entity_ids) == 1, (label, entity_ids)
        key = LABEL_TO_ENTITY[label]
        etype = ENTITY_DEFS[key][1]
        label_inventory.append({
            "speaker_label": label,
            "record_count": len(ds),
            "scenes": sorted({x["scene_ordinal"] for x in ds}),
            "entity_id": entity_ids[0],
            "entity_key": key,
            "entity_type": etype,
            "mapping_mode": "global-alias" if etype == "character" else ("collective-category" if etype == "collective" else "role-category"),
            "unresolved_record_count": 0,
        })

    entities = []
    for key, (preferred, etype, source_labels, notes) in ENTITY_DEFS.items():
        rs = by_entity[key]
        assert rs, key
        observed = sorted({r["speaker_label"] for r in rs})
        assert set(observed) == set(source_labels), (key, observed, source_labels)
        entities.append({
            "id": entity_id(key),
            "preferred_name_ta": preferred,
            "entity_type": etype,
            "status": "verified",
            "confidence": "high",
            "source_labels": sorted(source_labels),
            "scenes": sorted({r["scene_ordinal"] for r in rs}),
            "dialogue_record_count": len(rs),
            "supporting_records": [r["id"] for r in rs[:3]],
            "notes": notes,
        })

    type_counts = Counter(x["entity_type"] for x in entities)
    assert type_counts == Counter({"character": 14, "role": 13, "collective": 1}), type_counts
    assert sum(x["dialogue_record_count"] for x in entities) == 590

    wr("works/naam/characters/entities.json", json.dumps(entities, ensure_ascii=False, indent=2) + "\n", changed)
    wr("works/naam/characters/record-dispositions.json", json.dumps(dispositions, ensure_ascii=False, indent=2) + "\n", changed)
    wr("works/naam/characters/labels-inventory.json", json.dumps(label_inventory, ensure_ascii=False, indent=2) + "\n", changed)
    wr("works/naam/characters/schema.json", json.dumps(schema(), ensure_ascii=False, indent=2) + "\n", changed)

    index = {
        "work_id": "naam",
        "status": "complete-verified",
        "dialogue_index": "../dialogues/index.json",
        "schema": "schema.json",
        "label_preflight": "labels-preflight.json",
        "label_inventory": "labels-inventory.json",
        "record_dispositions": "record-dispositions.json",
        "entities": "entities.json",
        "dialogue_records_source": 590,
        "distinct_source_labels": 45,
        "entity_count": len(entities),
        "entity_type_counts": dict(sorted(type_counts.items())),
        "verified_entities": len(entities),
        "review_entities": 0,
        "unresolved_entities": 0,
        "verified_labels": 45,
        "review_labels": 0,
        "unresolved_labels": 0,
        "label_coverage": "45/45",
        "dialogue_record_coverage": "590/590",
        "remaining_unmapped_labels": 0,
        "remaining_unmapped_records": 0,
        "record_aware_labels": [],
        "dialogue_records_modified": False,
        "source_anomaly_labels_preserved": ["உன்மீனு"],
        "next_activity": NEXT,
    }
    wr("works/naam/characters/index.json", json.dumps(index, ensure_ascii=False, indent=2) + "\n", changed)

    readme = f'''# நாம் — character/entity layer

Status: **COMPLETE-VERIFIED**

Authority: `../dialogues/index.json` — **590 immutable dialogue records / QA PASS**.

## Coverage

- exact source speaker labels: **45/45 mapped**;
- dialogue records: **590/590 mapped exactly once**;
- entity records: **{len(entities)}**;
- named characters: **{type_counts['character']}**;
- generic role categories: **{type_counts['role']}**;
- collectives: **{type_counts['collective']}**;
- unresolved labels / records: **0 / 0**;
- dialogue records modified: **0**.

Exact source labels remain immutable provenance. Named abbreviations/spelling variants are reconciled only in this separate layer. Generic labels such as `ஒருவன்`, `திருடன்`, `பூசாரி`, `பெண்`, `மற்றொரு` and `வந்தவர்` are retained as role categories and do **not** assert that all occurrences are one physical person.

The scene-41 source anomaly `உன்மீனு` remains unchanged in the dialogue layer and maps to the `மீனு` entity only here. Likewise, the recurring ஜமீன்தார் is represented as `மல்லயப்பன் / மலையப்பன்` while all eight observed source-label variants remain preserved.

## QA

See `../notes/character-entity-qa.json` and `../notes/character-entity-qa.md`.

## Next activity

{NEXT}
'''
    wr("works/naam/characters/README.md", readme, changed)

    qa = {
        "work_id": "naam",
        "phase": "character-entity-qa",
        "status": "PASS",
        "dialogue_records_expected": 590,
        "dialogue_records_mapped": 590,
        "dialogue_record_coverage": "590/590 exactly once",
        "distinct_source_labels_expected": 45,
        "distinct_source_labels_mapped": 45,
        "source_label_coverage": "45/45",
        "entity_count": len(entities),
        "entity_type_counts": dict(sorted(type_counts.items())),
        "unresolved_labels": 0,
        "unresolved_records": 0,
        "named_alias_groups": {
            "குமரன்": ["கும", "குமரன்"],
            "சஞ்சீவி": ["சஞ்", "சஞ்சீவி"],
            "மீனு": ["மீனு", "உன்மீனு"],
            "மல்லயப்பன் / மலையப்பன்": ["மல்", "மல்ல", "மல்லயப்ப", "மல்லயப்பர்", "மல்லயப்பன்", "மலைய", "மலையப்பர்", "மலையப்பன்"],
            "நாராயணி": ["நாரா", "நாராயணி"],
            "பிரேமா": ["பிரே", "பிரேமா"],
            "மாத்திரை": ["மாத்", "மாத்திரை"],
            "ஞானம்": ["ஞா", "ஞானம்"],
            "ஜீவானந்தர்": ["ஜீவா", "ஜீவானந்த", "ஜீவானந்தர்"],
            "தங்கையன்": ["தங்", "தங்கையன்"],
        },
        "generic_role_policy": "Role-category mappings preserve source labels without asserting one continuing physical person across generic occurrences.",
        "source_anomaly_labels_preserved": ["உன்மீனு"],
        "record_aware_dispositions_required": 0,
        "dialogue_records_modified": 0,
        "scene_text_modified": 0,
        "canonical_tamil_modified": 0,
        "next_gate": "song/performance/authorship gate ready",
    }
    wr("works/naam/notes/character-entity-qa.json", json.dumps(qa, ensure_ascii=False, indent=2) + "\n", changed)
    qmd = f'''# நாம் — character/entity QA

Result: **PASS**

- immutable dialogue records mapped exactly once: **590/590**;
- exact source speaker labels mapped: **45/45**;
- entity records: **{len(entities)}** — {type_counts['character']} named characters, {type_counts['role']} role categories, {type_counts['collective']} collective;
- unresolved labels / records: **0 / 0**;
- record-aware split labels required: **0**;
- source-label normalization in dialogue layer: **0**;
- dialogue / scene / canonical Tamil modifications: **0 / 0 / 0**.

Named abbreviations and spelling variants are reconciled only in the separate entity layer. Generic labels remain role categories rather than unsupported named identities. Scene-41 `உன்மீனு` is preserved as the exact source label and maps to `மீனு` only in this downstream alias layer.

## Gate result

**Character/entity indexing CLOSED / COMPLETE-VERIFIED.** The song/performance/authorship gate may now begin.

## Next activity

{NEXT}
'''
    wr("works/naam/notes/character-entity-qa.md", qmd, changed)

    # Work-local metadata/status.
    p = "works/naam/metadata.yaml"
    s = rd(p)
    if "  character_entity_index_path:" not in s:
        s = s.replace(
            '  dialogue_qa_path: "notes/dialogue-index-qa.json"',
            '  dialogue_qa_path: "notes/dialogue-index-qa.json"\n'
            '  character_entity_index: complete-verified\n'
            '  character_entity_index_path: "characters/index.json"\n'
            f'  character_entity_count: {len(entities)}\n'
            '  character_entity_label_coverage: "45/45"\n'
            '  character_entity_record_coverage: "590/590"\n'
            '  character_entity_qa_path: "notes/character-entity-qa.json"',
        )
    s = s.replace("  character_entity_index: ready-next", f"  character_entity_index: complete-verified-{len(entities)}-entities")
    s = s.replace("  song_authorship_gate: blocked-pending-character-layer", "  song_authorship_gate: ready-next")
    s = re.sub(r'next_action:\s*".*"\s*$', 'next_action: ' + json.dumps(NEXT, ensure_ascii=False), s, count=1, flags=re.M)
    wr(p, s, changed)

    # Work README.
    p = "works/naam/README.md"
    s = rd(p)
    s = s.replace("- character/entity index: **ready-next**; song derivatives remain downstream;", f"- character/entity index: **{len(entities)} entities / 45/45 labels / 590/590 records / COMPLETE-VERIFIED / QA PASS**;\n- song/performance/authorship gate: **ready-next**;")
    if "## Character/entity closure checkpoint" not in s:
        marker = "## Source-visible publication / credit evidence\n"
        block = f'''## Character/entity closure checkpoint\n\n- immutable dialogue authority: **590 records / QA PASS**;\n- exact source labels mapped: **45/45**;\n- dialogue records mapped exactly once: **590/590**;\n- entities: **{len(entities)}** — {type_counts['character']} named / {type_counts['role']} role / {type_counts['collective']} collective;\n- unresolved labels / records: **0 / 0**;\n- source anomaly `உன்மீனு`: preserved upstream, mapped to `மீனு` only here;\n- QA: `notes/character-entity-qa.json` — **PASS**;\n- upstream text/dialogue modifications: **0**.\n\n**Next:** {NEXT}\n\n'''
        s = s.replace(marker, block + marker, 1)
    s = re.sub(r'\*\*Next:\*\* Begin Phase 7 character/entity indexing[^\n]*', "**Next:** " + NEXT, s)
    wr(p, s, changed)

    # Project handover and fresh prompt.
    p = "works/naam/PROJECT_HANDOVER.md"
    s = rd(p)
    s = re.sub(r'> \*\*Begin Phase 7 character/entity indexing[^\n]*', "> **" + NEXT + "**", s)
    if "## Character/entity closure checkpoint" not in s:
        s += f'''\n\n## Character/entity closure checkpoint\n\n- character/entity index: **COMPLETE-VERIFIED**;\n- source labels: **45/45 mapped**;\n- dialogue records: **590/590 mapped exactly once**;\n- entities: **{len(entities)}** — {type_counts['character']} named / {type_counts['role']} role / {type_counts['collective']} collective;\n- unresolved labels / records: **0 / 0**;\n- generic labels remain role categories; no unsupported identity merge;\n- `உன்மீனு` remains unchanged in the dialogue layer and maps to `மீனு` only downstream;\n- QA: `notes/character-entity-qa.json` — **PASS**;\n- canonical Tamil / scene / dialogue modifications: **0 / 0 / 0**.\n\n## Exact next activity\n\n> **{NEXT}**\n'''
    wr(p, s, changed)
    wr("works/naam/NEXT_CHAT_PROMPT.md", f'''# Next Chat Prompt — நாம்\n\nContinue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/naam/`. Live `main` is authoritative.\n\nCanonical Tamil is **67/67 COMPLETE-VERIFIED**. Scene-text derivatives are **45/45 COMPLETE-VERIFIED**. Immutable dialogue indexing is **590 records / COMPLETE-VERIFIED / QA PASS**. Character/entity indexing is now **COMPLETE-VERIFIED: 45/45 exact source labels and 590/590 dialogue records mapped into {len(entities)} entities ({type_counts['character']} named characters, {type_counts['role']} role categories, {type_counts['collective']} collective), with 0 unresolved labels/records and 0 upstream rewrites**.\n\nCharacter index: `works/naam/characters/index.json`. QA: `works/naam/notes/character-entity-qa.json`. Exact source labels remain immutable in `works/naam/dialogues/`; generic labels are only role categories, and scene-41 `உன்மீனு` remains preserved upstream.\n\nDo not alter canonical Tamil, scenes, immutable dialogue records, or completed character/entity mappings except for later source-supported corrections.\n\n## Exact next activity\n\n> **{NEXT}**\n''', changed)

    # Repository data mirror.
    p = "data/works.json"
    data = json.loads(rd(p))
    naam = next(x for x in data if x.get("id") == "naam")
    sd = naam.setdefault("structured_derivatives", {})
    sd.update({
        "character_entity_index": "complete-verified",
        "character_entity_index_path": "works/naam/characters/index.json",
        "character_entity_count": len(entities),
        "character_entity_type_counts": dict(sorted(type_counts.items())),
        "character_entity_label_coverage": "45/45",
        "character_entity_dialogue_record_coverage": "590/590",
        "character_entity_qa": "PASS",
        "character_entity_qa_path": "works/naam/notes/character-entity-qa.json",
        "song_authorship_gate": "ready-next",
        "next_structured_derivative": "song-performance-authorship-gate",
    })
    naam["next_action"] = NEXT
    wr(p, json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n", changed)

    # Root mirrors: use conservative replacements and next-action regex.
    p = "README.md"
    s = rd(p)
    if "character/entity index: **28 entities" not in s:
        s = s.replace(
            "- dialogue index: **590 immutable records / COMPLETE-VERIFIED / QA PASS**;",
            "- dialogue index: **590 immutable records / COMPLETE-VERIFIED / QA PASS**;\n- character/entity index: **28 entities / 45/45 labels / 590/590 records / COMPLETE-VERIFIED / QA PASS**;",
        )
    s = re.sub(r'\*\*Next:\*\* Begin Phase 7 character/entity indexing[^\n]*', "**Next:** " + NEXT, s)
    wr(p, s, changed)

    p = "docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md"
    s = rd(p)
    s = s.replace(
        "- **Naam / நாம்** — canonical Tamil **67/67 COMPLETE-VERIFIED**; scenes **45/45 COMPLETE-VERIFIED**; dialogue index **590 records COMPLETE-VERIFIED / QA PASS**; character/entity index next.",
        "- **Naam / நாம்** — canonical Tamil **67/67 COMPLETE-VERIFIED**; scenes **45/45 COMPLETE-VERIFIED**; dialogue **590 records COMPLETE-VERIFIED / QA PASS**; character/entity **28 entities / 45/45 labels / 590/590 records COMPLETE-VERIFIED / QA PASS**; song/authorship gate next.",
    )
    s = re.sub(r'\*\*Exact next activity:\*\* Begin Phase 7 character/entity indexing[^\n]*', "**Exact next activity:** " + NEXT, s)
    wr(p, s, changed)

    p = "docs/STATUS_CONSISTENCY_AUDIT.md"
    s = rd(p)
    s = s.replace(
        "| Naam / நாம் | canonical Tamil 67/67 complete-verified; 0 unresolved | **45/45 scenes; 590 dialogue records; dialogue QA PASS** | character/entity index next | not-started |",
        "| Naam / நாம் | canonical Tamil 67/67 complete-verified; 0 unresolved | **45/45 scenes; 590 dialogues; 28 character/entities; all QA PASS** | song/authorship gate next | not-started |",
    )
    s = re.sub(r'\*\*Next production phase:\*\* Begin Phase 7 character/entity indexing[^\n]*', "**Next production phase:** " + NEXT, s)
    wr(p, s, changed)

    after_hashes = file_hashes(protected)
    assert before_hashes == after_hashes, "Upstream canonical/scene/dialogue files changed during character/entity build"

    print(json.dumps({
        "changed": changed,
        "dialogue_records_mapped": len(dispositions),
        "source_labels_mapped": len(label_inventory),
        "entities": len(entities),
        "entity_type_counts": dict(sorted(type_counts.items())),
        "unresolved_labels": 0,
        "unresolved_records": 0,
        "next_action": NEXT,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
