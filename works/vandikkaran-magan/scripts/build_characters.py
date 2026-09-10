#!/usr/bin/env python3
from pathlib import Path
from collections import Counter, defaultdict
import json

W = Path(__file__).resolve().parents[1]
D = W / 'dialogues'
C = W / 'characters'
N = W / 'notes'
C.mkdir(exist_ok=True)
N.mkdir(exist_ok=True)

NEXT = (
    'Begin the song/performance authorship gate from the closed source, scene, dialogue and character/entity layers. '
    'Inventory source-visible song, verse and performance occurrences first; preserve exact source wording, lineation, cues and provenance; '
    'do not infer item-level lyric authorship from the film-level `பாடல்கள்: கவிஞர் வாலி` credit alone; assign authorship only where item-level evidence supports it; '
    'run whole-work occurrence/authorship coverage QA before English translation. Do not rewrite canonical Tamil, scenes, immutable dialogue records or character/entity mappings.'
)

# Exact-label -> interpretive entity mapping. The keys are immutable source labels.
M = {
    'ஆட்கள்': ('aadkal-collective', 'ஆட்கள்', 'collective', 'collective-category', 'Generic source collective; grouping is categorical and does not assert one fixed group across scenes.'),
    'இன்னொருவன்': ('innoruvan-role', 'இன்னொருவன்', 'role', 'role-category', 'Generic source role; no named identity is inferred.'),
    'உமா': ('uma', 'உமா', 'character', 'global-alias', 'Named recurring character; exact source label is retained.'),
    'ஊர்ப்பெரியவர்': ('oorperiyavar-role', 'ஊர்ப்பெரியவர்', 'role', 'role-category', 'Generic source community-elder role; no personal name is inferred.'),
    'எல்லோரும்': ('ellorum-collective', 'எல்லோரும்', 'collective', 'collective-category', 'Generic source collective; no individual identities are inferred.'),
    'ஒரு சிறுமி': ('oru-sirumi-role', 'ஒரு சிறுமி', 'role', 'role-category', 'Generic source role; preserved separately from `சிறுமி`.'),
    'ஒருத்தி': ('oruthi-role', 'ஒருத்தி', 'role', 'role-category', 'Generic source female role; no personal identity is inferred.'),
    'ஒருவர்': ('oruvar-role', 'ஒருவர்', 'role', 'role-category', 'Generic source role; no personal identity is inferred.'),
    'ஒருவன்': ('oruvan-role', 'ஒருவன்', 'role', 'role-category', 'Generic source male role reused contextually; entity is a role category, not one continuing individual.'),
    'கடைக்': ('kadaikaran-role', 'கடைக்காரன்', 'role', 'role-category', 'Source abbreviation `கடைக்` is retained in dialogue; scene 40 context explicitly identifies the role as `கடைக்காரன்`.'),
    'கண்ணாயிரம்': ('kannayiram', 'கண்ணாயிரம்', 'character', 'global-alias', 'Named recurring character.'),
    'கண்ணாயிரத்தின் குரல்': ('kannayiram', 'கண்ணாயிரம்', 'character', 'source-explicit-voice-alias', 'Source label explicitly identifies this as கண்ணாயிரம்’s voice; the voice label remains unchanged upstream.'),
    'காளிங்': ('kalingarayan', 'காளிங்கராயன்', 'character', 'global-alias', 'Scene 1 names `காளிங்கராயன்` in the stage direction and addresses him as `காளிங்கராயா`; abbreviated source label `காளிங்` is retained.'),
    'காளிங்க': ('kalingarayan', 'காளிங்கராயன்', 'character', 'global-alias', 'Later source label variant for the same காளிங்கராயன் established in scene 1; exact source label is retained.'),
    'காவலன்': ('kaavalan-role', 'காவலன்', 'role', 'role-category', 'Generic guard role; no named identity is inferred.'),
    'கோகிலா': ('kokila', 'கோகிலா', 'character', 'global-alias', 'Named recurring character.'),
    'சடையன்': ('sadaiyan', 'சடையன்', 'character', 'global-alias', 'Named recurring character.'),
    'சடையன் குரல்': ('sadaiyan', 'சடையன்', 'character', 'source-explicit-voice-alias', 'Source label explicitly identifies this as சடையன்’s voice; the voice label remains unchanged upstream.'),
    'சிறுமி': ('sirumi-role', 'சிறுமி', 'role', 'role-category', 'Generic source role; preserved separately from `ஒரு சிறுமி`.'),
    'சொக்': ('sokkalingam', 'சொக்கலிங்கம்', 'character', 'global-alias', 'Scene 5 stage direction names சிறுவன் சொக்கலிங்கம் and `சொக்` self-identifies as `சொக்கலிங்கம்`; exact abbreviated label is retained.'),
    'சொக்க': ('sokkalingam', 'சொக்கலிங்கம்', 'character', 'global-alias', 'Scene 6 stage direction identifies the child as சொக்கலிங்கம் while dialogue uses `சொக்க`; exact source label is retained.'),
    'சொர்ணம்': ('sornam', 'சொர்ணம்', 'character', 'global-alias', 'Named recurring character.'),
    'ஜம்பு': ('jambu', 'ஜம்பு', 'character', 'global-alias', 'Named character at டேவிட் துரை’s bungalow; kept distinct from ஜம்புலிங்க பூபதி.'),
    'ஜமீன்': ('jambulingam-boopathi', 'ஜம்புலிங்க பூபதி', 'character', 'global-alias', 'Scene 38 uses source label `ஜமீன்` for the same father addressed by உமா as `அப்பா`; scene 1 supplies the full name `ஜமீன்தார் ஜம்புலிங்க பூபதி`.'),
    'ஜமீன்தார்': ('jambulingam-boopathi', 'ஜம்புலிங்க பூபதி', 'character', 'global-alias', 'Scene 1 explicitly prints `ஜமீன்தார் ஜம்புலிங்க பூபதி`; the role-form speaker label remains immutable in dialogue.'),
    'டேவிட்': ('david', 'டேவிட்', 'character', 'global-alias', 'Named character; scene 5 stage direction identifies டேவிட்துரை.'),
    'தரகர்': ('tharagar-role', 'தரகர்', 'role', 'role-category', 'Generic broker role; no personal name is inferred.'),
    'புலவர்': ('pulavar-role', 'புலவர்', 'role', 'role-category', 'Recurring unnamed poet/father role; no personal name is supplied by the source dialogue layer.'),
    'புரோகிதர்': ('purohithar-role', 'புரோகிதர்', 'role', 'role-category', 'Generic priest role; no personal name is inferred.'),
    'பெண்': ('pen-role', 'பெண்', 'role', 'role-category', 'Generic source female role; no personal identity is inferred.'),
    'மக்கள்': ('makkal-collective', 'மக்கள்', 'collective', 'collective-category', 'Generic source collective; no individual identities are inferred.'),
    'மற்றொரு சிறுவன்': ('mattroru-siruvan-role', 'மற்றொரு சிறுவன்', 'role', 'role-category', 'Generic source child role; kept separate from other generic child labels.'),
    'மரகதம்': ('maragatham', 'மரகதம்', 'character', 'global-alias', 'Named recurring character.'),
    'முனியன்': ('muniyan', 'முனியன்', 'character', 'global-alias', 'Named character.'),
    'லிங்கன்': ('lingan', 'லிங்கன்', 'character', 'global-alias', 'Named recurring character; source context treats லிங்கன் as distinct from விங்கன், so the two are not collapsed.'),
    'லீனா': ('leena', 'லீனா', 'character', 'global-alias', 'Named recurring character.'),
    'விங்கன்': ('vingan', 'விங்கன்', 'character', 'global-alias', 'Named recurring character.'),
    'விங்கன் குரல்': ('vingan', 'விங்கன்', 'character', 'source-explicit-voice-alias', 'Source label explicitly identifies this as விங்கன்’s voice; the voice label remains unchanged upstream.'),
}

idx = json.loads((D / 'index.json').read_text(encoding='utf-8'))
assert idx['status'] in {'complete-verified','complete-verified-reconciled'}
assert idx['dialogue_record_count'] == 773
assert idx['distinct_exact_speaker_labels'] == 38

records = []
for path in sorted((D / 'records').glob('scene-*.json')):
    rows = json.loads(path.read_text(encoding='utf-8'))
    records.extend(rows)
assert len(records) == 773
assert len({r['id'] for r in records}) == 773
labels = sorted({r['speaker_label'] for r in records})
assert len(labels) == 38
assert set(labels) == set(M), (set(labels)-set(M), set(M)-set(labels))

by_label = defaultdict(list)
for r in records:
    by_label[r['speaker_label']].append(r)

entity_rows = defaultdict(list)
label_inventory = []
record_dispositions = []
for label in labels:
    key, preferred, typ, mode, note = M[label]
    entity_id = f'vandikkaran-magan-char-{key}'
    rows = by_label[label]
    scene_ordinals = sorted({r['scene_ordinal'] for r in rows})
    source_scene_ids = []
    for r in rows:
        if r['source_scene_id'] not in source_scene_ids:
            source_scene_ids.append(r['source_scene_id'])
    label_inventory.append({
        'speaker_label': label,
        'record_count': len(rows),
        'scenes': scene_ordinals,
        'source_scene_ids': source_scene_ids,
        'entity_id': entity_id,
        'entity_key': key,
        'entity_type': typ,
        'mapping_mode': mode,
        'status': 'verified',
        'confidence': 'high',
        'unresolved_record_count': 0,
        'mapping_note': note,
    })
    for r in rows:
        entity_rows[entity_id].append(r)
        record_dispositions.append({
            'record_id': r['id'],
            'source_speaker_label': label,
            'scene_id': r['scene_id'],
            'scene_ordinal': r['scene_ordinal'],
            'source_scene_id': r['source_scene_id'],
            'entity_id': entity_id,
            'entity_key': key,
            'preferred_name_ta': preferred,
            'entity_type': typ,
            'mapping_mode': mode,
            'status': 'verified',
            'dialogue_record_modified': False,
        })

entities = []
for entity_id in sorted(entity_rows):
    rows = entity_rows[entity_id]
    source_labels = []
    for r in rows:
        if r['speaker_label'] not in source_labels:
            source_labels.append(r['speaker_label'])
    source_labels = sorted(source_labels)
    first = M[source_labels[0]]
    # All labels mapped to one entity must agree on preferred name/type.
    preferreds = {M[x][1] for x in source_labels}
    types = {M[x][2] for x in source_labels}
    assert len(preferreds) == 1 and len(types) == 1
    preferred = next(iter(preferreds)); typ = next(iter(types))
    scenes = sorted({r['scene_ordinal'] for r in rows})
    source_scene_ids = []
    for r in rows:
        if r['source_scene_id'] not in source_scene_ids:
            source_scene_ids.append(r['source_scene_id'])
    notes = []
    for label in source_labels:
        n = M[label][4]
        if n not in notes:
            notes.append(n)
    entities.append({
        'id': entity_id,
        'preferred_name_ta': preferred,
        'entity_type': typ,
        'status': 'verified',
        'confidence': 'high',
        'source_labels': source_labels,
        'scenes': scenes,
        'source_scene_ids': source_scene_ids,
        'dialogue_record_count': len(rows),
        'supporting_records': [r['id'] for r in rows[:3]],
        'notes': ' '.join(notes),
    })

assert len(entities) == 32
entity_type_counts = dict(Counter(e['entity_type'] for e in entities))
assert entity_type_counts == {'character': 15, 'collective': 3, 'role': 14}, entity_type_counts
assert sum(e['dialogue_record_count'] for e in entities) == 773
assert len(record_dispositions) == 773
assert len({x['record_id'] for x in record_dispositions}) == 773
assert all(x['dialogue_record_modified'] is False for x in record_dispositions)
assert all(x['status'] == 'verified' for x in label_inventory)

schema = {
  '$schema': 'https://json-schema.org/draft/2020-12/schema',
  '$id': 'vandikkaran-magan-character-entity.schema.json',
  'title': 'Vandikkaran Magan character/entity record',
  'type': 'object',
  'required': ['id','preferred_name_ta','entity_type','status','confidence','source_labels','scenes','source_scene_ids','dialogue_record_count','notes'],
  'properties': {
    'id': {'type':'string','pattern':'^vandikkaran-magan-char-[a-z0-9-]+$'},
    'preferred_name_ta': {'type':'string','minLength':1},
    'entity_type': {'enum':['character','role','collective']},
    'status': {'enum':['verified','review','unresolved']},
    'confidence': {'enum':['high','medium','low']},
    'source_labels': {'type':'array','minItems':1,'uniqueItems':True,'items':{'type':'string','minLength':1}},
    'scenes': {'type':'array','minItems':1,'uniqueItems':True,'items':{'type':'integer','minimum':1,'maximum':72}},
    'source_scene_ids': {'type':'array','minItems':1,'uniqueItems':True,'items':{'type':'string','minLength':1}},
    'dialogue_record_count': {'type':'integer','minimum':1},
    'supporting_records': {'type':'array','items':{'type':'string'}},
    'notes': {'type':'string','minLength':1},
  },
  'additionalProperties': False,
}

index = {
    'work_id': 'vandikkaran-magan',
    'status': 'complete-verified',
    'dialogue_index': '../dialogues/index.json',
    'schema': 'schema.json',
    'label_preflight': 'labels-preflight.json',
    'label_inventory': 'labels-inventory.json',
    'record_dispositions': 'record-dispositions.json',
    'entities': 'entities.json',
    'qa': '../notes/character-index-qa.json',
    'dialogue_records_source': 773,
    'distinct_source_labels': 38,
    'entity_count': 32,
    'entity_type_counts': entity_type_counts,
    'verified_entities': 32,
    'review_entities': 0,
    'unresolved_entities': 0,
    'verified_labels': 38,
    'review_labels': 0,
    'unresolved_labels': 0,
    'label_coverage': '38/38',
    'dialogue_record_coverage': '773/773',
    'remaining_unmapped_labels': 0,
    'remaining_unmapped_records': 0,
    'record_aware_labels': [],
    'dialogue_records_modified': False,
    'source_variant_labels_preserved': ['காளிங்','காளிங்க','சொக்','சொக்க','ஜமீன்','ஜமீன்தார்','கண்ணாயிரத்தின் குரல்','சடையன் குரல்','விங்கன் குரல்'],
    'next_activity': NEXT,
}

qa = {
    'work_id': 'vandikkaran-magan',
    'phase': 'character-entity-index',
    'status': 'PASS',
    'dialogue_records_expected': 773,
    'dialogue_records_mapped': 773,
    'distinct_exact_source_labels_expected': 38,
    'distinct_exact_source_labels_mapped': 38,
    'entities': 32,
    'entity_type_counts': entity_type_counts,
    'verified_entities': 32,
    'review_entities': 0,
    'unresolved_entities': 0,
    'unmapped_labels': [],
    'unmapped_dialogue_records': [],
    'duplicate_dialogue_record_dispositions': 0,
    'dialogue_records_modified': False,
    'named_variant_merges': {
        'காளிங்கராயன்': ['காளிங்','காளிங்க'],
        'சொக்கலிங்கம்': ['சொக்','சொக்க'],
        'ஜம்புலிங்க பூபதி': ['ஜமீன்','ஜமீன்தார்'],
    },
    'source_explicit_voice_aliases': {
        'கண்ணாயிரம்': ['கண்ணாயிரத்தின் குரல்'],
        'சடையன்': ['சடையன் குரல்'],
        'விங்கன்': ['விங்கன் குரல்'],
    },
    'generic_labels_kept_categorical': sorted([x for x in labels if M[x][2] in {'role','collective'}]),
    'distinct_named_characters_kept_separate': ['ஜம்பு / ஜம்புலிங்க பூபதி', 'லிங்கன் / விங்கன்'],
    'checks': {
        'dialogue_gate_complete_verified': True,
        'all_38_exact_labels_inventoried': True,
        'all_38_exact_labels_mapped_once': True,
        'all_773_dialogue_records_mapped_once': True,
        'entity_counts_sum_to_773': True,
        'generic_roles_collectives_not_promoted_to_named_people': True,
        'named_voice_labels_linked_only_by_source_explicit_possessive_identity': True,
        'upstream_dialogue_mutation_required': False,
    },
    'next_activity': NEXT,
}

preflight_md = '''# வண்டிக்காரன் மகன் — character/entity label preflight\n\nStatus: **REVIEWED / CHARACTER GATE CLOSED**\n\nThe immutable dialogue layer supplied **773 records / 38 exact source speaker labels**. Every exact label was inventoried before interpretation. Dialogue labels were not normalized or rewritten.\n\n## Disposition\n\n- exact labels inventoried: **38/38**;\n- dialogue records covered: **773/773**;\n- character/entity records: **32** — **15 characters / 14 roles / 3 collectives**;\n- verified / review / unresolved labels: **38 / 0 / 0**;\n- verified / review / unresolved entities: **32 / 0 / 0**;\n- unmapped labels / records: **0 / 0**.\n\nSource-supported variant merges are confined to this interpretive layer: `காளிங்` + `காளிங்க` → காளிங்கராயன்; `சொக்` + `சொக்க` → சொக்கலிங்கம்; `ஜமீன்` + `ஜமீன்தார்` → ஜம்புலிங்க பூபதி. Source-explicit possessive voice labels `கண்ணாயிரத்தின் குரல்`, `சடையன் குரல்`, and `விங்கன் குரல்` link to their named characters without changing the source label. Generic roles and collectives remain categorical; `லிங்கன்` remains distinct from `விங்கன்`, and `ஜம்பு` remains distinct from `ஜம்புலிங்க பூபதி`.\n\n**PASS — character/entity index is COMPLETE-VERIFIED. Song/performance authorship is READY-NEXT.**\n'''

readme = f'''# வண்டிக்காரன் மகன் — character/entity index\n\n**Status:** **COMPLETE-VERIFIED / QA PASS**\n\nThis interpretive layer maps the closed immutable dialogue layer without rewriting any source speaker label or dialogue text.\n\n## Coverage\n\n- immutable dialogue records: **773/773 mapped exactly once**;\n- exact source speaker labels: **38/38 mapped**;\n- entities: **32** — **15 named characters / 14 generic roles / 3 collectives**;\n- verified / review / unresolved entities: **32 / 0 / 0**;\n- unmapped labels / records: **0 / 0**;\n- upstream dialogue records modified: **0**.\n\nVariant and voice mappings exist only here as interpretive metadata. `லிங்கன்` is not collapsed into `விங்கன்`; `ஜம்பு` is not collapsed into `ஜம்புலிங்க பூபதி`; generic labels remain categorical rather than being treated as one continuing person.\n\nSee `labels-preflight.json`, `labels-inventory.json`, `entities.json`, `record-dispositions.json`, and `../notes/character-index-qa.json`.\n\n## Next\n\n{NEXT}\n'''

for path, obj in [
    (C/'schema.json', schema),
    (C/'labels-inventory.json', label_inventory),
    (C/'record-dispositions.json', record_dispositions),
    (C/'entities.json', entities),
    (C/'index.json', index),
    (N/'character-index-qa.json', qa),
]:
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
(C/'labels-preflight.md').write_text(preflight_md, encoding='utf-8')
(C/'README.md').write_text(readme, encoding='utf-8')

# Re-load generated outputs and perform deterministic coverage checks.
ri = json.loads((C/'index.json').read_text(encoding='utf-8'))
rq = json.loads((N/'character-index-qa.json').read_text(encoding='utf-8'))
re = json.loads((C/'entities.json').read_text(encoding='utf-8'))
rl = json.loads((C/'labels-inventory.json').read_text(encoding='utf-8'))
rr = json.loads((C/'record-dispositions.json').read_text(encoding='utf-8'))
assert ri['status'] == 'complete-verified' and rq['status'] == 'PASS'
assert len(re) == 32 and len(rl) == 38 and len(rr) == 773
assert {x['speaker_label'] for x in rl} == set(labels)
assert {x['record_id'] for x in rr} == {r['id'] for r in records}
assert sum(x['dialogue_record_count'] for x in re) == 773
print('PASS: character/entity index 38/38 labels, 773/773 records, 32 entities (15 character / 14 role / 3 collective)')
