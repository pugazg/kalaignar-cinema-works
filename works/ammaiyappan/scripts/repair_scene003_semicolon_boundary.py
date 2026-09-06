#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "dialogues"
C = ROOT / "characters"
N = ROOT / "notes"
T = ROOT / "translations"
S = ROOT / "scripts"


def dump(path: Path, obj) -> None:
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    # Restore the source-visible scene-3 speaker boundary.
    p = D / "records/scene-003.json"
    rows = json.loads(p.read_text(encoding="utf-8"))
    assert len(rows) == 10 and rows[0]["id"] == "ammaiyappan-s003-d001"
    bad = "பூங்காவனம்-பூங்காவனம்.......\n\nபூங் ; என்ன அண்ணா...என்ன விசேஷம்......."
    assert rows[0]["text"] == bad
    rows[0]["text"] = "பூங்காவனம்-பூங்காவனம்......."
    dump(p, rows)

    sp = D / "source-role-resolved-records.json"
    supp = json.loads(sp.read_text(encoding="utf-8"))
    assert len(supp) == 15
    assert not any(x["id"] == "ammaiyappan-s003-r001" for x in supp)
    supp.append({
        "id": "ammaiyappan-s003-r001",
        "archive_scene_id": "ammaiyappan-s003",
        "archive_scene_ordinal": 3,
        "source_scene_number": None,
        "source_scene_file": "scene-003.md",
        "source_block_id": "ammaiyappan-s003-semicolon-001",
        "speaker_label": "பூங்",
        "speaker_label_origin": "source-explicit-noncolon-delimiter",
        "source_delimiter": ";",
        "text": "என்ன அண்ணா...என்ன விசேஷம்.......",
        "page_provenance": [{"pdf_page": 9, "printed_page": 7}],
        "attribution_basis": "verified scene text prints exact source form `பூங் ; என்ன அண்ணா...என்ன விசேஷம்.......`; preserve semicolon and separate it from preceding Baladevar utterance",
    })
    supp.sort(key=lambda x: (x["archive_scene_ordinal"], x["id"]))
    dump(sp, supp)

    fi = D / "final-index.json"
    f = json.loads(fi.read_text(encoding="utf-8"))
    assert f["explicit_colon_dialogue_records"] == 1009
    assert f["source_role_resolved_dialogue_records"] == 15
    assert f["total_dialogue_units_for_downstream_indexing"] == 1024
    f["source_role_resolved_dialogue_records"] = 16
    f["total_dialogue_units_for_downstream_indexing"] = 1025
    f["semicolon_boundary_correction"] = "scene-003 `பூங் ;` separated from preceding Baladevar record; source delimiter preserved"
    dump(fi, f)

    q = N / "dialogue-final-qa.json"
    x = json.loads(q.read_text(encoding="utf-8"))
    assert x["source_role_resolved_dialogue_records"] == 15 and x["total_dialogue_units"] == 1024
    x["source_role_resolved_dialogue_records"] = 16
    x["total_dialogue_units"] = 1025
    x["post_closure_boundary_corrections"] = 1
    x["post_closure_boundary_correction"] = "scene 3 `பூங் ;` source speaker boundary restored; canonical Tamil unchanged"
    dump(q, x)

    qmd = N / "dialogue-final-qa.md"
    s = qmd.read_text(encoding="utf-8")
    s = s.replace("source-role-resolved dialogue supplements: **15**", "source-role-resolved dialogue supplements: **16**")
    s = s.replace("downstream dialogue units: **1024**", "downstream dialogue units: **1025**")
    s += "\n## Post-closure source-role correction\n\n- scene 3 exact source form `பூங் ; ...` is a distinct source-explicit non-colon dialogue unit; it is no longer swallowed into Baladevar `d001`.\n- canonical Tamil changed: **no**.\n- source delimiter normalized: **no**.\n"
    qmd.write_text(s, encoding="utf-8")

    # Make character builders use the current dialogue authority rather than stale 15/1024 constants.
    bp = S / "build_character_preflight.py"
    s = bp.read_text(encoding="utf-8")
    s = s.replace(
        "    assert len(supp)==15\n    assert fi['total_dialogue_units_for_downstream_indexing']==1024\n",
        "    assert len(supp)==fi['source_role_resolved_dialogue_records']\n    assert len(explicit)+len(supp)==fi['total_dialogue_units_for_downstream_indexing']\n",
    )
    s = s.replace("    assert len(rows)==1024\n", "    assert len(rows)==fi['total_dialogue_units_for_downstream_indexing']\n")
    bp.write_text(s, encoding="utf-8")

    be = S / "build_character_entities.py"
    s = be.read_text(encoding="utf-8")
    s = s.replace(
        "    assert len(supplements) == 15\n    rows = explicit + supplements\n    assert len(rows) == 1024\n    assert len({r[\"id\"] for r in rows}) == 1024\n    assert final_index[\"total_dialogue_units_for_downstream_indexing\"] == 1024\n",
        "    assert len(supplements) == final_index['source_role_resolved_dialogue_records']\n    rows = explicit + supplements\n    expected_total = final_index['total_dialogue_units_for_downstream_indexing']\n    assert len(rows) == expected_total\n    assert len({r['id'] for r in rows}) == expected_total\n",
    )
    s = s.replace(
        "    assert len(dispositions) == 1024\n    assert len({x[\"record_id\"] for x in dispositions}) == 1024\n",
        "    assert len(dispositions) == expected_total\n    assert len({x['record_id'] for x in dispositions}) == expected_total\n",
    )
    be.write_text(s, encoding="utf-8")

    subprocess.run(["python", str(bp)], check=True)
    subprocess.run(["python", str(be)], check=True)
    ci = json.loads((C / "index.json").read_text(encoding="utf-8"))
    assert ci["dialogue_records_source"] == 1025
    assert ci["dialogue_unit_coverage"] == "1025/1025"
    assert ci["remaining_unmapped_records"] == 0
    assert ci["distinct_source_labels"] == 62 and ci["entity_count"] == 26

    # Pilot remains valid; only its authority count changes.
    pre = T / "preflight.json"
    e = json.loads(pre.read_text(encoding="utf-8"))
    e["authority"]["dialogue_final_index"] = "1025-downstream-units-complete-source-role-resolved"
    dump(pre, e)
    pilot = json.loads((T / "records/scene-001.json").read_text(encoding="utf-8"))
    assert pilot["unit_count"] == 34
    assert sum(1 for u in pilot["units"] if u["kind"] == "dialogue") == 31

    ep = S / "build_english_translation_pilot.py"
    s = ep.read_text(encoding="utf-8")
    old = '"dialogue_final_index": "1024-downstream-units-complete-source-role-resolved",'
    new = '"dialogue_final_index": f"{json.loads((DIALOGUES / \'final-index.json\').read_text(encoding=\'utf-8\'))[\'total_dialogue_units_for_downstream_indexing\']}-downstream-units-complete-source-role-resolved",'
    assert old in s
    ep.write_text(s.replace(old, new), encoding="utf-8")

    audit = {
        "work_id": "ammaiyappan",
        "status": "complete-pass",
        "scope": "all 63 verified scene derivatives",
        "semicolon_candidates_scanned": 46,
        "true_source_speaker_semicolon_forms": ["scene-003 `பூங் ;`", "scene-005 `திரு;`"],
        "already_correct_before_audit": ["scene-005 `திரு;`"],
        "corrected_by_this_pass": ["scene-003 `பூங் ;`"],
        "canonical_tamil_modified": False,
        "source_punctuation_normalized": False,
        "dialogue_explicit_colon_records": 1009,
        "source_role_supplements": 16,
        "downstream_dialogue_units": 1025,
        "character_coverage": "1025/1025",
        "remaining_unresolved": 0,
    }
    dump(N / "semicolon-speaker-boundary-audit.json", audit)
    print("AMMAYAPPAN SCENE-003 SEMICOLON REPAIR PASS — 1025/1025")


if __name__ == "__main__":
    main()
