#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
D = ROOT / 'dialogues'
C = ROOT / 'characters'
N = ROOT / 'notes'
T = ROOT / 'translations'
SCRIPTS = ROOT / 'scripts'

OLD_COMBINED = 'பூங்காவனம்-பூங்காவனம்.......\n\nபூங் ; என்ன அண்ணா...என்ன விசேஷம்.......'
BALA_TEXT = 'பூங்காவனம்-பூங்காவனம்.......'
POONG_TEXT = 'என்ன அண்ணா...என்ன விசேஷம்.......'
NEW_SUPPLEMENT_ID = 'ammaiyappan-s003-r001'


def replace_exact(text: str, old: str, new: str, label: str, expected: int = 1) -> str:
    count = text.count(old)
    if count != expected:
        raise AssertionError(f'{label}: expected {expected} matches, found {count}')
    return text.replace(old, new, expected)


def dump(path: Path, obj) -> None:
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def main() -> None:
    # Source/scene lock: the verified scene must contain the exact semicolon form.
    scene3 = (ROOT / 'scenes/scene-003.md').read_text(encoding='utf-8')
    assert 'பல : பூங்காவனம்-பூங்காவனம்.......' in scene3
    assert 'பூங் ; என்ன அண்ணா...என்ன விசேஷம்.......' in scene3

    # 1) Repair only the wrongly fused explicit-colon record; keep its immutable ID.
    p = D / 'records/scene-003.json'
    rows = json.loads(p.read_text(encoding='utf-8'))
    assert len(rows) == 10
    assert rows[0]['id'] == 'ammaiyappan-s003-d001'
    assert rows[0]['speaker_label'] == 'பல'
    assert rows[0]['text'] == OLD_COMBINED, rows[0]['text']
    rows[0]['text'] = BALA_TEXT
    dump(p, rows)

    # 2) Add the source-explicit semicolon turn as a supplemental dialogue record.
    p = D / 'source-role-resolved-records.json'
    supplements = json.loads(p.read_text(encoding='utf-8'))
    assert len(supplements) == 15
    assert not any(x['id'] == NEW_SUPPLEMENT_ID for x in supplements)
    assert any(x['id'] == 'ammaiyappan-s005-r001' and x.get('source_delimiter') == ';' for x in supplements)
    new_row = {
        'id': NEW_SUPPLEMENT_ID,
        'archive_scene_id': 'ammaiyappan-s003',
        'archive_scene_ordinal': 3,
        'source_scene_number': None,
        'source_scene_file': 'scene-003.md',
        'source_block_id': 'ammaiyappan-s003-semicolon-001',
        'speaker_label': 'பூங்',
        'speaker_label_origin': 'source-explicit-noncolon-delimiter',
        'source_delimiter': ';',
        'text': POONG_TEXT,
        'page_provenance': [{'pdf_page': 9, 'printed_page': 7}],
        'attribution_basis': 'verified scene text prints exact source form “பூங் ; …”; preserve the semicolon delimiter and do not normalize it to a colon',
    }
    supplements.insert(0, new_row)
    assert len({x['id'] for x in supplements}) == 16
    dump(p, supplements)

    # 3) Dialogue closure/index QA: explicit-colon layer is unchanged; supplements become 16.
    p = D / 'final-index.json'
    fi = json.loads(p.read_text(encoding='utf-8'))
    assert fi['explicit_colon_dialogue_records'] == 1009
    assert fi['source_role_resolved_dialogue_records'] == 15
    assert fi['total_dialogue_units_for_downstream_indexing'] == 1024
    assert fi['explicit_exact_speaker_labels'] == 62
    fi['source_role_resolved_dialogue_records'] = 16
    fi['total_dialogue_units_for_downstream_indexing'] = 1025
    fi['post_translation_delimiter_reconciliations'] = 1
    fi['delimiter_reconciliation_audit'] = '../notes/dialogue-semicolon-delimiter-reconciliation.json'
    fi['next_activity'] = 'Continue source-linked English translation/reconciliation from the reconciled 1,025-unit dialogue layer.'
    dump(p, fi)

    p = N / 'dialogue-final-qa.json'
    qa = json.loads(p.read_text(encoding='utf-8'))
    assert qa['status'] == 'pass'
    assert qa['explicit_colon_records'] == 1009
    assert qa['source_role_resolved_dialogue_records'] == 15
    assert qa['total_dialogue_units'] == 1024
    qa['source_role_resolved_dialogue_records'] = 16
    qa['total_dialogue_units'] = 1025
    qa['post_translation_delimiter_reconciliations'] = 1
    qa['delimiter_reconciliation_audit'] = 'dialogue-semicolon-delimiter-reconciliation.json'
    dump(p, qa)

    audit = {
        'work_id': 'ammaiyappan',
        'phase': 'post-dialogue-source-delimiter-reconciliation',
        'status': 'complete-pass',
        'trigger': 'English batch preflight for archival scene 3 exposed a semicolon-delimited source speaker turn fused into the preceding colon record.',
        'source_scene_file': 'scenes/scene-003.md',
        'source_pdf_page': 9,
        'logical_printed_page': 7,
        'source_form': 'பூங் ; என்ன அண்ணா...என்ன விசேஷம்.......',
        'affected_explicit_record': 'ammaiyappan-s003-d001',
        'affected_explicit_record_action': 'retain ID and speaker label பல; remove only the wrongly absorbed பூங் semicolon turn from its text',
        'new_source_role_record': NEW_SUPPLEMENT_ID,
        'new_source_role_label': 'பூங்',
        'new_source_role_origin': 'source-explicit-noncolon-delimiter',
        'new_source_delimiter': ';',
        'explicit_colon_records_before_after': [1009, 1009],
        'source_role_supplements_before_after': [15, 16],
        'downstream_dialogue_units_before_after': [1024, 1025],
        'distinct_source_labels_before_after': [62, 62],
        'canonical_tamil_changed': False,
        'scene_derivative_changed': False,
        'existing_dialogue_record_ids_renumbered': False,
        'speaker_label_normalized': False,
        'related_existing_semicolon_precedent': 'ammaiyappan-s005-r001 (`திரு; ...`)',
        'source_wide_semicolon_diagnostic': {
            'workflow_run_id': 34003725210,
            'raw_semicolon_candidates': 46,
            'speaker_delimiter_cases_after_label/context review': 2,
            'already_handled_cases': ['திரு; ... — scene 5'],
            'newly_reconciled_cases': ['பூங் ; ... — scene 3'],
        },
    }
    dump(N / 'dialogue-semicolon-delimiter-reconciliation.json', audit)

    p = D / 'README.md'
    text = p.read_text(encoding='utf-8')
    text = replace_exact(text, '- source-role-resolved dialogue supplements: **15**', '- source-role-resolved dialogue supplements: **16**', 'dialogue README supplement')
    text = replace_exact(text, '- downstream dialogue units: **1024**', '- downstream dialogue units: **1025**', 'dialogue README total')
    text = replace_exact(
        text,
        'Fifteen source-supported dialogue supplements are kept in `source-role-resolved-records.json`; six non-dialogue source units are documented in `../notes/non-dialogue-source-role-exclusions.json`. The exact source form `திரு; ...` is retained with `;` as its recorded delimiter.',
        'Sixteen source-supported dialogue supplements are kept in `source-role-resolved-records.json`; six non-dialogue source units are documented in `../notes/non-dialogue-source-role-exclusions.json`. The exact source forms `பூங் ; ...` (scene 3) and `திரு; ...` (scene 5) are retained with `;` as their recorded delimiter. The late scene-3 boundary reconciliation is recorded in `../notes/dialogue-semicolon-delimiter-reconciliation.json`.',
        'dialogue README delimiter paragraph',
    )
    p.write_text(text, encoding='utf-8')

    # 4) Make character-preflight builder consume final-index counts rather than stale constants, then regenerate.
    p = SCRIPTS / 'build_character_preflight.py'
    text = p.read_text(encoding='utf-8')
    text = replace_exact(text, 'assert len(supp)==15', "assert len(supp)==fi['source_role_resolved_dialogue_records']", 'character preflight supplement assert')
    text = replace_exact(text, "assert fi['total_dialogue_units_for_downstream_indexing']==1024", "assert fi['total_dialogue_units_for_downstream_indexing']==len(explicit)+len(supp)", 'character preflight total assert')
    text = replace_exact(text, 'assert len(rows)==1024', "assert len(rows)==fi['total_dialogue_units_for_downstream_indexing']", 'character preflight row assert')
    p.write_text(text, encoding='utf-8')

    # 5) Make character-entity builder consume the reconciled total dynamically, then regenerate.
    p = SCRIPTS / 'build_character_entities.py'
    text = p.read_text(encoding='utf-8')
    text = replace_exact(text, 'assert len(supplements) == 15', 'assert len(supplements) == final_index["source_role_resolved_dialogue_records"]', 'entity builder supplement assert')
    old = '''    rows = explicit + supplements\n    assert len(rows) == 1024\n    assert len({r["id"] for r in rows}) == 1024\n    assert final_index["total_dialogue_units_for_downstream_indexing"] == 1024'''
    new = '''    rows = explicit + supplements\n    expected_total = final_index["total_dialogue_units_for_downstream_indexing"]\n    assert expected_total == len(explicit) + len(supplements)\n    assert len(rows) == expected_total\n    assert len({r["id"] for r in rows}) == expected_total'''
    text = replace_exact(text, old, new, 'entity builder total block')
    text = replace_exact(text, 'assert len(dispositions) == 1024', 'assert len(dispositions) == expected_total', 'entity builder dispositions count')
    text = replace_exact(text, 'assert len({x["record_id"] for x in dispositions}) == 1024', 'assert len({x["record_id"] for x in dispositions}) == expected_total', 'entity builder disposition IDs')
    text = replace_exact(text, 'assert sum(x["dialogue_record_count"] for x in entities) == 1024', 'assert sum(x["dialogue_record_count"] for x in entities) == expected_total', 'entity builder entity sum')
    text = replace_exact(text, '"dialogue_records_source": 1024,', '"dialogue_records_source": expected_total,', 'entity builder dialogue source', expected=2)
    text = replace_exact(text, '"coverage_note": "All 1,024 downstream dialogue units and all 62 exact source speaker labels have a verified disposition. `முத்` and `தன` are record-aware; no dialogue evidence is rewritten.",', '"coverage_note": f"All {expected_total:,} downstream dialogue units and all 62 exact source speaker labels have a verified disposition. `முத்` and `தன` are record-aware; no dialogue evidence is rewritten.",', 'entity builder coverage note')
    text = replace_exact(text, '"dialogue_unit_coverage": "1024/1024",', '"dialogue_unit_coverage": f"{expected_total}/{expected_total}",', 'entity builder coverage')
    text = text.replace('1,024-unit dialogue layer', '1,025-unit dialogue layer')
    text = text.replace('1,024/1,024 dialogue units', '1,025/1,025 dialogue units')
    text = text.replace('downstream dialogue units: **1,024**', 'downstream dialogue units: **1,025**')
    text = text.replace('dialogue-unit coverage: **1,024/1,024**', 'dialogue-unit coverage: **1,025/1,025**')
    text = replace_exact(text, '"dialogue_units": 1024,', '"dialogue_units": expected_total,', 'entity builder print total')
    p.write_text(text, encoding='utf-8')

    # Run the now-current deterministic character builders.
    import subprocess
    subprocess.run(['python', str(SCRIPTS / 'build_character_preflight.py')], check=True)
    subprocess.run(['python', str(SCRIPTS / 'build_character_entities.py')], check=True)

    # Verify the new Poongavanam record is represented by both generated layers.
    pre = json.loads((C / 'labels-preflight.json').read_text(encoding='utf-8'))
    assert pre['dialogue_units_scanned'] == 1025
    assert pre['source_role_supplement_units'] == 16
    poong_pre = next(x for x in pre['inventory'] if x['speaker_label'] == 'பூங்')
    assert poong_pre['record_count'] == 35
    assert poong_pre['record_origins'].get('source-explicit-noncolon-delimiter') == 1

    ci = json.loads((C / 'index.json').read_text(encoding='utf-8'))
    assert ci['dialogue_records_source'] == 1025
    assert ci['dialogue_unit_coverage'] == '1025/1025'
    assert ci['distinct_source_labels'] == 62
    assert ci['entity_count'] == 26
    ent = json.loads((C / 'entities.json').read_text(encoding='utf-8'))
    poong = next(x for x in ent['entities'] if x['id'] == 'ammaiyappan-char-poongavanam')
    assert poong['dialogue_record_count'] == 41

    # 6) Refresh the English pilot's authority metadata; the scene-1 translation itself remains unchanged.
    p = SCRIPTS / 'build_english_translation_pilot.py'
    text = p.read_text(encoding='utf-8')
    text = replace_exact(text, '1024-downstream-units-complete-source-role-resolved', '1025-downstream-units-complete-source-role-resolved', 'English pilot dialogue authority')
    p.write_text(text, encoding='utf-8')
    subprocess.run(['python', str(p)], check=True)
    pilot = json.loads((T / 'index.json').read_text(encoding='utf-8'))
    assert pilot['status'] == 'pilot-verified'
    assert pilot['translation_units'] == 34
    assert pilot['dialogue_source_records_linked'] == 31

    # 7) Work-local status mirrors.
    p = ROOT / 'README.md'
    text = p.read_text(encoding='utf-8')
    text = replace_exact(text, '| Dialogue index | **complete-source-role-resolved — 1,024/1,024 downstream units** |', '| Dialogue index | **complete-source-role-resolved — 1,025/1,025 downstream units** |', 'work README dialogue')
    text = replace_exact(text, '| Character/entity index | **complete-verified-reconciled — 26 entities / 62 labels / 1,024 units** |', '| Character/entity index | **complete-verified-reconciled — 26 entities / 62 labels / 1,025 units** |', 'work README character')
    text = replace_exact(text, '| English translation / reader | **READY — next phase** |', '| English translation / reader | **pilot-verified — scene 1/63, 34/34 pilot units** |', 'work README English')
    text = replace_exact(text, '**Begin source-linked English translation/reconciliation from the frozen 105/105 Tamil source plus the completed scene, dialogue, character/entity, and song/performance evidence layers.** Preserve source structure and exact Tamil linkage; translate only source-visible song/performance material and do not reconstruct absent lyrics.', '**Continue source-linked English translation with archival scenes 2–5 using the verified scene-1 pilot.** Use the reconciled 1,025-unit dialogue layer; preserve exact Tamil/source-role provenance and do not reconstruct absent lyrics.', 'work README next action')
    p.write_text(text, encoding='utf-8')

    p = ROOT / 'PROJECT_HANDOVER.md'
    text = p.read_text(encoding='utf-8')
    text = text.replace('source-role-resolved dialogue supplements: **15**;', 'source-role-resolved dialogue supplements: **16**;')
    text = text.replace('downstream dialogue units: **1024**;', 'downstream dialogue units: **1025**;')
    text = text.replace('downstream dialogue units dispositioned: **1,024/1,024**;', 'downstream dialogue units dispositioned: **1,025/1,025**;')
    recon_section = '''\n\n## Late dialogue-delimiter reconciliation — PASS\n\nDuring English scene-3 preflight, the verified scene exposed source form `பூங் ; என்ன அண்ணா...என்ன விசேஷம்.......`. The earlier colon parser had fused that Poongavanam turn into `ammaiyappan-s003-d001` (Baladevar). The fix preserves the existing `d001` ID and Baladevar text, adds `ammaiyappan-s003-r001` as a source-explicit non-colon `;` turn, and does not change canonical Tamil or scene text.\n\n- explicit colon records: **1009 unchanged**;\n- source-role supplements: **15 → 16**;\n- downstream dialogue units: **1024 → 1025**;\n- exact labels: **62 unchanged**;\n- character entities: **26 unchanged**;\n- Poongavanam dialogue units: **40 → 41**;\n- reconciliation audit: `notes/dialogue-semicolon-delimiter-reconciliation.json`;\n- existing `திரு; ...` precedent remains preserved.\n\n## English translation — PILOT VERIFIED\n\n- pilot: archive scene **1 / 63** (`மடாலய வெளிப்புறம்`);\n- source: PDF **5–7** / logical pp. **3–5**;\n- verified pilot units: **34/34**;\n- immutable explicit dialogue links: **31/31**;\n- stage-direction/action units: **3**;\n- source-role supplements in pilot: **0**;\n- song/performance links in pilot: **0**;\n- canonical Tamil / dialogue evidence modified by translation: **no**;\n- translation index: `translations/index.json`;\n- pilot review: `translations/PILOT_REVIEW.md`.\n\n### Exact next activity\n\n> **Translate and source-review archival scenes 2–5 using the verified scene-1 voice template and the reconciled 1,025-unit dialogue authority.**\n'''
    if '## Late dialogue-delimiter reconciliation — PASS' not in text:
        text = text.rstrip() + recon_section + '\n'
    p.write_text(text, encoding='utf-8')

    p = ROOT / 'metadata.yaml'
    text = p.read_text(encoding='utf-8')
    text = text.replace('complete-source-role-resolved-1024-of-1024', 'complete-source-role-resolved-1025-of-1025')
    text = replace_exact(text, '  source_role_supplements: 15', '  source_role_supplements: 16', 'metadata supplement count')
    text = text.replace('complete-verified-reconciled-26-entities-62-labels-1024-units', 'complete-verified-reconciled-26-entities-62-labels-1025-units')
    text = replace_exact(
        text,
        '  english_translation: ready-next-phase\n  reader_export: blocked-pending-english',
        '  english_translation: pilot-verified-scene-1-of-63-34-units\n  translation_index_path: "translations/index.json"\n  translation_scenes_verified: 1\n  translation_units_verified: 34\n  reader_export: blocked-pending-english',
        'metadata structured English',
    )
    text = replace_exact(text, '  english_translation: ready-next-phase\n  reader_export: blocked-pending-english', '  english_translation: pilot-verified-scene-1-of-63-34-units\n  reader_export: blocked-pending-english', 'metadata status English')
    text = replace_exact(text, 'next_action: "Begin source-linked English translation/reconciliation from the frozen verified Tamil plus completed scene/dialogue/character/song-performance evidence layers; do not reconstruct absent lyrics."', 'next_action: "Translate and source-review archival scenes 2-5 using the verified scene-1 English pilot and reconciled 1,025-unit dialogue layer; do not reconstruct absent lyrics."', 'metadata next action')
    p.write_text(text, encoding='utf-8')

    # Shared work registry: add/update explicit current fields without guessing older field names.
    p = REPO / 'data/works.json'
    works = json.loads(p.read_text(encoding='utf-8'))
    matches = [w for w in works if w.get('id') == 'ammaiyappan']
    assert len(matches) == 1
    w = matches[0]
    sd = w.setdefault('structured_derivatives', {})
    sd.update({
        'dialogue_index': 'complete-source-role-resolved-1025-of-1025',
        'dialogue_index_path': 'works/ammaiyappan/dialogues/final-index.json',
        'explicit_colon_records': 1009,
        'source_role_supplements': 16,
        'dialogue_units': 1025,
        'character_entity_index': 'complete-verified-reconciled',
        'character_entity_index_path': 'works/ammaiyappan/characters/index.json',
        'character_dialogue_units': 1025,
        'character_distinct_source_labels': 62,
        'character_entities': 26,
        'english_translation': 'pilot-verified',
        'translation_index_path': 'works/ammaiyappan/translations/index.json',
        'translation_scenes_verified': 1,
        'translation_units': 34,
        'translation_verified_units': 34,
        'translation_next_batch': '2-5',
        'next_structured_derivative': 'english-translation',
    })
    w['next_action'] = 'Translate and source-review Ammayappan archival scenes 2-5 from the verified Tamil/structured source layers.'
    dump(p, works)

    print(json.dumps({
        'explicit_colon_records': 1009,
        'source_role_supplements': 16,
        'downstream_dialogue_units': 1025,
        'source_labels': 62,
        'entities': 26,
        'poongavanam_units': 41,
        'english_pilot_scenes_verified': 1,
        'english_pilot_units': 34,
        'next_batch': '2-5',
    }, ensure_ascii=False))


if __name__ == '__main__':
    main()
