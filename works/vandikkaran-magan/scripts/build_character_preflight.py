#!/usr/bin/env python3
from pathlib import Path
from collections import Counter, defaultdict
import json

W = Path(__file__).resolve().parents[1]
D = W / 'dialogues'
C = W / 'characters'
C.mkdir(exist_ok=True)

idx = json.loads((D / 'index.json').read_text(encoding='utf-8'))
assert idx['status'] == 'complete-verified'
assert idx['dialogue_record_count'] == 744
assert idx['distinct_exact_speaker_labels'] == 38

all_records = []
scene_records = {}
for path in sorted((D / 'records').glob('scene-*.json')):
    rows = json.loads(path.read_text(encoding='utf-8'))
    scene_records[path.name] = rows
    all_records.extend(rows)

assert len(all_records) == 744
ids = [r['id'] for r in all_records]
assert len(ids) == len(set(ids))

by_label = defaultdict(list)
for r in all_records:
    by_label[r['speaker_label']].append(r)
assert len(by_label) == 38

out_labels = []
for label in sorted(by_label):
    rows = by_label[label]
    scene_ids = []
    source_scene_ids = []
    pdf_pages = []
    neighbor_labels = Counter()
    examples = []
    for r in rows:
        if r['scene_id'] not in scene_ids:
            scene_ids.append(r['scene_id'])
        if r['source_scene_id'] not in source_scene_ids:
            source_scene_ids.append(r['source_scene_id'])
        for p in r['page_provenance']:
            if p['pdf_page'] not in pdf_pages:
                pdf_pages.append(p['pdf_page'])
        scene_file = r['source_scene_file']
        srows = scene_records[scene_file]
        pos = next(i for i, x in enumerate(srows) if x['id'] == r['id'])
        prev_r = srows[pos-1] if pos > 0 else None
        next_r = srows[pos+1] if pos+1 < len(srows) else None
        if prev_r:
            neighbor_labels[prev_r['speaker_label']] += 1
        if next_r:
            neighbor_labels[next_r['speaker_label']] += 1
        if len(examples) < 6:
            examples.append({
                'dialogue_id': r['id'],
                'scene_id': r['scene_id'],
                'source_scene_id': r['source_scene_id'],
                'speaker_label': r['speaker_label'],
                'text': r['text'],
                'page_provenance': r['page_provenance'],
                'previous_dialogue': None if not prev_r else {
                    'id': prev_r['id'], 'speaker_label': prev_r['speaker_label'], 'text': prev_r['text']},
                'next_dialogue': None if not next_r else {
                    'id': next_r['id'], 'speaker_label': next_r['speaker_label'], 'text': next_r['text']},
            })
    out_labels.append({
        'speaker_label': label,
        'record_count': len(rows),
        'scene_ids': scene_ids,
        'source_scene_ids': source_scene_ids,
        'pdf_pages': sorted(pdf_pages),
        'neighbor_label_counts': dict(neighbor_labels.most_common()),
        'examples': examples,
        'mapping_status': 'unadjudicated'
    })

payload = {
    'work_id': 'vandikkaran-magan',
    'phase': 'character-entity-preflight',
    'status': 'review-ready',
    'dialogue_authority': '744 complete-verified immutable records',
    'dialogue_records_scanned': len(all_records),
    'distinct_exact_speaker_labels': len(out_labels),
    'labels': out_labels,
    'policy': {
        'dialogue_records_modified': False,
        'exact_source_labels_preserved': True,
        'alias_mapping_is_interpretive_metadata_only': True,
        'generic_roles_collectives_and_voices_not_auto_collapsed': True
    }
}
(C / 'labels-preflight.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('PASS: 744/744 dialogue records; 38/38 exact labels inventoried')
