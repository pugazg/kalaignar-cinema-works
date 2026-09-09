#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIALOGUES = ROOT / "dialogues"
CHARACTERS = ROOT / "characters"


def load_records() -> list[dict]:
    rows: list[dict] = []
    for path in sorted((DIALOGUES / "records").glob("scene-*.json")):
        rows.extend(json.loads(path.read_text(encoding="utf-8")))
    return rows


def main() -> None:
    idx = json.loads((DIALOGUES / "index.json").read_text(encoding="utf-8"))
    qa = json.loads((ROOT / "notes" / "dialogue-index-qa.json").read_text(encoding="utf-8"))
    assert idx["status"] == "complete-verified"
    assert idx["dialogue_record_count"] == 590
    assert idx["distinct_exact_speaker_labels"] == 45
    assert qa["status"] == "PASS"
    assert qa["explicit_label_ownership"] == "590/590 exactly once"

    records = load_records()
    assert len(records) == 590
    assert len({r["id"] for r in records}) == 590

    by_label: dict[str, list[dict]] = defaultdict(list)
    for r in records:
        by_label[r["speaker_label"]].append(r)
    assert len(by_label) == 45

    inventory = []
    for label in sorted(by_label):
        rs = by_label[label]
        inventory.append({
            "speaker_label": label,
            "record_count": len(rs),
            "scene_count": len({r["scene_ordinal"] for r in rs}),
            "scenes": sorted({r["scene_ordinal"] for r in rs}),
            "delimiter_distribution": dict(sorted(Counter(r["source_delimiter"] for r in rs).items())),
            "sample_records": [r["id"] for r in rs[:5]],
            "samples": [
                {
                    "record_id": r["id"],
                    "scene": r["scene_ordinal"],
                    "source_heading": r["source_heading"],
                    "pdf_pages": [p["pdf_page"] for p in r["page_provenance"]],
                    "text_preview": r["text"][:180],
                }
                for r in rs[:3]
            ],
        })

    doc = {
        "work_id": "naam",
        "phase": "character-entity-preflight",
        "status": "review-ready",
        "dialogue_authority": "../dialogues/index.json",
        "dialogue_units_scanned": len(records),
        "distinct_exact_source_labels": len(by_label),
        "inventory": inventory,
        "policy": {
            "dialogue_records_modified": False,
            "source_speaker_labels_immutable": True,
            "alias_mapping_separate_from_dialogue_layer": True,
            "global_named_label_merge_requires_identity_continuity": True,
            "generic_roles_must_not_be_forced_into_named_characters": True,
            "role_categories_do_not_assert_one_physical_person_across_occurrences": True,
            "source_anomalies_remain_visible": True,
        },
        "next_action": "Review all 45 exact source labels, map supported named-label variants only in a separate entity layer, retain generic/collective labels as role entities, and require 590/590 record coverage with zero dialogue rewrites.",
    }

    CHARACTERS.mkdir(exist_ok=True)
    (CHARACTERS / "labels-preflight.json").write_text(
        json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    md = [
        "# நாம் — character/entity preflight",
        "",
        "Status: **REVIEW READY**",
        "",
        f"- immutable dialogue records scanned: **{len(records)}**",
        f"- distinct exact source speaker labels: **{len(by_label)}**",
        "- dialogue records modified: **0**",
        "",
        "## Exact label inventory",
        "",
    ]
    for x in inventory:
        md.append(
            f"- `{x['speaker_label']}` — {x['record_count']} records / {x['scene_count']} scenes — scenes {x['scenes']}"
        )
    md += [
        "",
        "## Mapping rule",
        "",
        "Named-label variants may share an entity only where scene/dialogue continuity supports identity. Generic labels remain role or collective entities and do not assert one physical person across occurrences. Exact source speaker labels remain unchanged in the immutable dialogue layer.",
        "",
    ]
    (CHARACTERS / "labels-preflight.md").write_text("\n".join(md), encoding="utf-8")

    print(json.dumps({
        "dialogue_units": len(records),
        "distinct_labels": len(by_label),
        "labels": [
            {"label": x["speaker_label"], "count": x["record_count"], "scenes": x["scenes"]}
            for x in inventory
        ],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
