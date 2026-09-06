#!/usr/bin/env python3
"""Resolve Ammayappan's reviewed unlabelled source-role residue without normalizing source text.

The 1009 explicit colon-labelled records remain immutable.  This finalizer
classifies every residual block from unlabelled-block-audit.json and emits
a separate source-role-resolved dialogue supplement plus non-dialogue
exclusions.  Contextual speaker attributions are admitted only where the
verified scene text itself supplies the speaker through an immediately
preceding labelled turn or stage-direction actor cue.
"""
from __future__ import annotations
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTES = ROOT / 'notes'
DIALOGUES = ROOT / 'dialogues'

REVIEW = {
    'ammaiyappan-s001-u001': dict(classification='non_dialogue_action_narrative', basis='source prose describes coach arrival and character actions; no speech turn'),
    'ammaiyappan-s005-u001': dict(classification='mixed_action_plus_semicolon_label_exception', speaker='திரு', delimiter=';', basis='block begins with source action prose, then exact source form “திரு; …”; the same scene later prints “திரு : …”; preserve semicolon and do not normalize it'),
    'ammaiyappan-s006-u001': dict(classification='contextual_dialogue_continuation', speaker='சுக', basis='preceding explicit சுக turn continues around the parenthetical sword-fight cue; no intervening speaker is introduced'),
    'ammaiyappan-s006-u002': dict(classification='contextual_dialogue_continuation', speaker='சுக', basis='continues the same sword-practice exchange after “(மீண்டும் சண்டை)”; no intervening speaker is introduced'),
    'ammaiyappan-s006-u003': dict(classification='contextual_dialogue_continuation', speaker='சுக', basis='immediately follows explicit “சுக : டேய்...நீ போ,” and the cue “(முத்தனிடம்)”; the cue identifies the addressee, not a new speaker'),
    'ammaiyappan-s008-u001': dict(classification='contextual_dialogue_continuation', speaker='திரி', basis='preceding explicit திரி turn is interrupted only by the source cue announcing the goat and சுகதேவ் arrival; the unlabelled line continues his invitation'),
    'ammaiyappan-s011-u001': dict(classification='contextual_dialogue_continuation', speaker='முத்தன்', basis='preceding explicit முத்தன் turn is followed by “[சிரிக்கிறாள்]”; the unlabelled question responds directly to that laugh'),
    'ammaiyappan-s011-u002': dict(classification='contextual_dialogue_continuation', speaker='திரிசங்கு', basis='preceding explicit திரிசங்கு turn sends முத்தாயி away; after “[முத்தாயி போகிறாள் கலங்கியபடி]” the prayer/address continues from him'),
    'ammaiyappan-s011-u003': dict(classification='non_dialogue_action_narrative', basis='source prose narrates the fight and embeds quoted words inside narration rather than as a standalone speaker-labelled turn'),
    'ammaiyappan-s014-u001': dict(classification='non_dialogue_action_narrative', basis='source prose describes முத்தன் checking the sword and பூங்காவனம் arriving'),
    'ammaiyappan-s017-u001': dict(classification='contextual_dialogue_continuation', speaker='முத்தன்', basis='preceding explicit முத்தன் political speech is interrupted only by “[நண்பர்கள் சிரிக்கிறார்கள்...]”; the next lines directly address those friends'),
    'ammaiyappan-s017-u002': dict(classification='contextual_dialogue_continuation', speaker='வேதாளம்', basis='preceding explicit வேதாளம் turn sends the others away; after “[போகிறார்கள்]” he immediately addresses முத்தன்'),
    'ammaiyappan-s018-u001': dict(classification='non_dialogue_stage_direction_continuation', basis='this is the second-page continuation of the square-bracket stage direction beginning on PDF 37 and ending with “]” on PDF 38'),
    'ammaiyappan-s027-u001': dict(classification='contextual_dialogue_continuation', speaker='முத்தன்', basis='preceding explicit முத்தன் denunciation is followed by “[சிரிக்கிறார்கள்]”; the unlabelled lines sarcastically answer that laughter and continue his address'),
    'ammaiyappan-s027-u002': dict(classification='contextual_dialogue_stage_cue_attribution', speaker='திரிசங்கு', basis='immediately preceding source cue is “[திரிசங்கு வருகிறான்.]”; the following insult is addressed to his daughter before her labelled response'),
    'ammaiyappan-s030-u001': dict(classification='contextual_dialogue_continuation', speaker='வேல', basis='preceding explicit வேல threat continues after “[இழுத்து உள்ளே தள்ளுகிறான்.]”; the stage-direction subject remains வேலழகன் and no new speaker appears'),
    'ammaiyappan-s035-u001': dict(classification='contextual_dialogue_stage_cue_attribution', speaker='திரிசங்கு', basis='source cue explicitly says திரிசங்கு sees சுகதேவ் arriving; the next unlabelled line is his face-saving remark, not a continuation of the preceding முத்தாயி label'),
    'ammaiyappan-s041-u001': dict(classification='non_dialogue_stage_direction_continuation', basis='this is the PDF 86 continuation of the square-bracket storm/action direction begun on PDF 85'),
    'ammaiyappan-s050-u001': dict(classification='contextual_dialogue_stage_cue_attribution', speaker='சுகதேவ்', basis='immediately preceding source cue says arriving சுகதேவ் sees முத்தாயி leave with வேதாளம்; the following unlabelled monologue is his reaction'),
    'ammaiyappan-s059-u001': dict(classification='contextual_dialogue_continuation', speaker='முத்தன்', basis='verified derivative explicitly records that the PDF 104 speech continues on PDF 105; no new speaker intervenes'),
}

def dump(path: Path, obj) -> None:
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def main() -> None:
    raw = json.loads((NOTES/'unlabelled-block-audit.json').read_text(encoding='utf-8'))
    idx = json.loads((DIALOGUES/'index.json').read_text(encoding='utf-8'))
    blocks = {b['block_id']: b for b in raw['blocks']}
    assert raw['block_count'] == 20
    assert raw['source_line_count'] == 35
    assert set(blocks) == set(REVIEW)
    assert idx['dialogue_record_count'] == 1009
    assert idx['distinct_exact_speaker_labels'] == 62

    reviewed = []
    supplements = []
    exclusions = []
    per_scene = Counter()

    for block_id, b in blocks.items():
        r = REVIEW[block_id]
        reviewed.append({
            'block_id': block_id,
            'archive_scene_id': b['archive_scene_id'],
            'source_scene_file': b['source_scene_file'],
            'page_provenance': b['page_provenance'],
            'classification': r['classification'],
            'speaker_label': r.get('speaker'),
            'source_delimiter': r.get('delimiter'),
            'basis': r['basis'],
            'status': 'source-role-resolved',
        })

        if r['classification'] == 'mixed_action_plus_semicolon_label_exception':
            token = '\n\nதிரு; '
            assert token in b['text']
            action_text, speech_text = b['text'].split(token, 1)
            assert action_text and speech_text
            exclusions.append({
                'source_block_id': block_id,
                'archive_scene_id': b['archive_scene_id'],
                'source_scene_file': b['source_scene_file'],
                'page_provenance': b['page_provenance'],
                'classification': 'non_dialogue_action_narrative',
                'text': action_text,
                'basis': 'action portion of mixed source block before the semicolon-labelled speech',
            })
            per_scene[b['archive_scene_id']] += 1
            supplements.append({
                'id': f"{b['archive_scene_id']}-r{per_scene[b['archive_scene_id']]:03d}",
                'archive_scene_id': b['archive_scene_id'],
                'archive_scene_ordinal': b['archive_scene_ordinal'],
                'source_scene_number': None,
                'source_scene_file': b['source_scene_file'],
                'source_block_id': block_id,
                'speaker_label': r['speaker'],
                'speaker_label_origin': 'source-explicit-noncolon-delimiter',
                'source_delimiter': r['delimiter'],
                'text': speech_text,
                'page_provenance': b['page_provenance'],
                'attribution_basis': r['basis'],
            })
        elif r['classification'].startswith('contextual_dialogue_'):
            per_scene[b['archive_scene_id']] += 1
            supplements.append({
                'id': f"{b['archive_scene_id']}-r{per_scene[b['archive_scene_id']]:03d}",
                'archive_scene_id': b['archive_scene_id'],
                'archive_scene_ordinal': b['archive_scene_ordinal'],
                'source_scene_number': None,
                'source_scene_file': b['source_scene_file'],
                'source_block_id': block_id,
                'speaker_label': r['speaker'],
                'speaker_label_origin': 'source-context-attributed',
                'source_delimiter': None,
                'text': b['text'],
                'page_provenance': b['page_provenance'],
                'attribution_basis': r['basis'],
            })
        else:
            exclusions.append({
                'source_block_id': block_id,
                'archive_scene_id': b['archive_scene_id'],
                'source_scene_file': b['source_scene_file'],
                'page_provenance': b['page_provenance'],
                'classification': r['classification'],
                'text': b['text'],
                'basis': r['basis'],
            })

    assert len(reviewed) == 20
    assert len(supplements) == 15
    assert len(exclusions) == 6
    assert sum(1 for x in supplements if x['source_delimiter'] == ';') == 1
    assert sum(1 for x in supplements if x['speaker_label_origin'] == 'source-context-attributed') == 14

    review_doc = {
        'work_id': 'ammaiyappan',
        'phase': 'unlabelled-source-role-review',
        'status': 'complete',
        'authority': '63 complete-verified scene derivatives plus the raw 20-block unlabelled audit',
        'input_blocks': 20,
        'input_source_lines': 35,
        'resolved_blocks': 20,
        'unresolved_blocks': 0,
        'classification_counts': dict(Counter(x['classification'] for x in reviewed)),
        'review': reviewed,
    }
    dump(NOTES/'unlabelled-source-role-review.json', review_doc)

    md = [
        '# Ammayappan — unlabelled source-role review', '',
        'Status: **COMPLETE — 20/20 blocks resolved**', '',
        'The 1009 explicit colon-labelled dialogue records are not rewritten by this review. Source-role-resolved dialogue that lacks an explicit colon label is emitted separately so that attribution basis remains visible.', '',
        '## Resolution summary', '',
        '- raw residual blocks: **20**',
        '- raw source lines: **35**',
        '- resolved dialogue supplements: **15**',
        '- non-dialogue source units: **6** (the mixed scene-005 block splits into one action unit plus one semicolon-labelled dialogue unit)',
        '- unresolved blocks: **0**',
        '- source punctuation normalized: **0**',
        '- speaker aliases expanded/normalized: **0**', '',
        '## Source exception', '',
        'Scene 005 preserves the exact source form `திரு; ...`. It is classified as dialogue because the verified scene context and later `திரு : ...` turns establish its role, but the semicolon is retained as the source delimiter and is not corrected to a colon.', '',
        '## Decisions', ''
    ]
    for x in reviewed:
        speaker = f" — speaker `{x['speaker_label']}`" if x['speaker_label'] else ''
        md.append(f"- `{x['block_id']}` — **{x['classification']}**{speaker}: {x['basis']}")
    (NOTES/'unlabelled-source-role-review.md').write_text('\n'.join(md) + '\n', encoding='utf-8')

    dump(DIALOGUES/'source-role-resolved-records.json', supplements)
    dump(NOTES/'non-dialogue-source-role-exclusions.json', {
        'work_id': 'ammaiyappan',
        'status': 'complete',
        'unit_count': len(exclusions),
        'units': exclusions,
    })

    final_index = {
        'work_id': 'ammaiyappan',
        'status': 'complete-source-role-resolved',
        'explicit_colon_dialogue_records': 1009,
        'explicit_exact_speaker_labels': 62,
        'source_role_resolved_dialogue_records': 15,
        'total_dialogue_units_for_downstream_indexing': 1024,
        'non_dialogue_resolved_source_units': 6,
        'raw_unlabelled_blocks_reviewed': 20,
        'unresolved_source_role_blocks': 0,
        'source_scene_numbers_invented': 0,
        'speaker_alias_normalizations': 0,
        'source_punctuation_normalizations': 0,
        'explicit_layer_index': 'index.json',
        'source_role_supplement': 'source-role-resolved-records.json',
        'source_role_review': '../notes/unlabelled-source-role-review.json',
        'non_dialogue_exclusions': '../notes/non-dialogue-source-role-exclusions.json',
        'character_entity_gate': 'unlocked',
    }
    dump(DIALOGUES/'final-index.json', final_index)

    final_qa = {
        'work_id': 'ammaiyappan',
        'phase': 'dialogue-final-qa',
        'status': 'pass',
        'explicit_colon_records': 1009,
        'source_role_resolved_dialogue_records': 15,
        'total_dialogue_units': 1024,
        'source_role_blocks_reviewed': '20/20',
        'unresolved_source_role_blocks': 0,
        'non_dialogue_source_units': 6,
        'source_scene_numbers_invented': 0,
        'speaker_alias_normalizations': 0,
        'source_punctuation_normalizations': 0,
        'character_entity_gate': 'unlocked',
    }
    dump(NOTES/'dialogue-final-qa.json', final_qa)
    (NOTES/'dialogue-final-qa.md').write_text(
        '# Ammayappan — dialogue final QA\n\n'
        'Status: **PASS**\n\n'
        '- explicit colon-labelled records: **1009**\n'
        '- source-role-resolved dialogue supplements: **15**\n'
        '- downstream dialogue units: **1024**\n'
        '- residual source-role blocks reviewed: **20/20**\n'
        '- unresolved source-role blocks: **0**\n'
        '- non-dialogue resolved source units: **6**\n'
        '- source scene numbers invented: **0**\n'
        '- speaker aliases normalized: **0**\n'
        '- source punctuation normalized: **0**\n\n'
        '**Character/entity indexing gate: UNLOCKED.**\n',
        encoding='utf-8'
    )

    readme = (DIALOGUES/'README.md').read_text(encoding='utf-8')
    readme = readme.replace('Status: **REVIEW READY**', 'Status: **COMPLETE — FINAL QA PASS**', 1)
    readme = readme.replace('- immutable dialogue records: **1009**', '- explicit immutable colon-labelled records: **1009**\n- source-role-resolved dialogue supplements: **15**\n- downstream dialogue units: **1024**', 1)
    readme = readme.replace('Text that occurs with no active explicit speaker is **not assigned by inference**.  It is preserved separately in `../notes/unlabelled-block-audit.json` for source-role review.\n\nThe character/entity index remains blocked until the unlabelled-block audit and final dialogue QA are closed.',
        'Text that occurs with no active explicit speaker was first preserved separately in `../notes/unlabelled-block-audit.json`. The complete 20/20 source-role review is recorded in `../notes/unlabelled-source-role-review.json`. Fifteen source-supported dialogue supplements are kept in `source-role-resolved-records.json`; six non-dialogue source units are documented in `../notes/non-dialogue-source-role-exclusions.json`. The exact source form `திரு; ...` is retained with `;` as its recorded delimiter.\n\nFinal dialogue QA is **PASS** in `../notes/dialogue-final-qa.json`. The character/entity index gate is **UNLOCKED**.', 1)
    (DIALOGUES/'README.md').write_text(readme, encoding='utf-8')

    handover = (ROOT/'PROJECT_HANDOVER.md').read_text(encoding='utf-8')
    marker = '## Dialogue-index closure — FINAL QA PASS'
    if marker not in handover:
        handover += f'''\n\n{marker}\n\n- explicit colon-labelled records: **1009**;\n- exact source speaker-label strings: **62**;\n- reviewed cross-page continuation candidates: **20/20 PASS**;\n- source-role residual review: **20/20 complete**;\n- source-role-resolved dialogue supplements: **15**;\n- non-dialogue resolved source units: **6**;\n- downstream dialogue units: **1024**;\n- unresolved source-role blocks: **0**;\n- source scene numbers invented: **0**;\n- alias normalization: **0**;\n- source punctuation normalization: **0**;\n- exceptional source delimiter `திரு; ...`: preserved exactly;\n- final QA: `notes/dialogue-final-qa.json` — **PASS**;\n- character/entity index gate: **UNLOCKED**.\n\n### Exact next activity\n\n> **Build the character/entity index from `dialogues/final-index.json`, the 1009 explicit dialogue records, the 15 source-role-resolved dialogue supplements, and the 63 verified scene derivatives. Preserve every exact speaker label as provenance; perform alias/entity reconciliation only in the new character/entity layer, never by rewriting the dialogue records.**\n'''
    (ROOT/'PROJECT_HANDOVER.md').write_text(handover, encoding='utf-8')

    print(json.dumps(final_qa, ensure_ascii=False))

if __name__ == '__main__':
    main()
