#!/usr/bin/env python3
from __future__ import annotations
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = ROOT/'dialogues'
C = ROOT/'characters'
S = ROOT/'scenes'

def load_records():
    explicit=[]
    for p in sorted((D/'records').glob('scene-*.json')):
        explicit.extend(json.loads(p.read_text(encoding='utf-8')))
    supplements=json.loads((D/'source-role-resolved-records.json').read_text(encoding='utf-8'))
    return explicit, supplements

def main():
    fi=json.loads((D/'final-index.json').read_text(encoding='utf-8'))
    scenes=json.loads((S/'index.json').read_text(encoding='utf-8'))['scene_records']
    explicit,supp=load_records()
    assert len(explicit)==1009
    assert len(supp)==fi['source_role_resolved_dialogue_records']
    assert len(explicit)+len(supp)==fi['total_dialogue_units_for_downstream_indexing']

    rows=[]
    for r in explicit:
        rows.append({
            'record_id':r['id'],
            'record_origin':'explicit-colon',
            'speaker_label':r['speaker_label'],
            'scene_id':r['archive_scene_id'],
            'scene_ordinal':r['archive_scene_ordinal'],
            'scene_heading':r['source_heading'],
            'source_scene_file':r['source_scene_file'],
            'page_provenance':r['page_provenance'],
            'text_preview':r['text'][:180],
        })
    for r in supp:
        rows.append({
            'record_id':r['id'],
            'record_origin':r['speaker_label_origin'],
            'speaker_label':r['speaker_label'],
            'scene_id':r['archive_scene_id'],
            'scene_ordinal':r['archive_scene_ordinal'],
            'scene_heading':next(x['heading'] for x in scenes if x['scene_id']==r['archive_scene_id']),
            'source_scene_file':r['source_scene_file'],
            'page_provenance':r['page_provenance'],
            'text_preview':r['text'][:180],
        })
    assert len(rows)==fi['total_dialogue_units_for_downstream_indexing']

    by_label=defaultdict(list)
    for r in rows: by_label[r['speaker_label']].append(r)
    inventory=[]
    for label in sorted(by_label):
        rs=by_label[label]
        inventory.append({
            'speaker_label':label,
            'record_count':len(rs),
            'scene_count':len({x['scene_ordinal'] for x in rs}),
            'scenes':sorted({x['scene_ordinal'] for x in rs}),
            'record_origins':dict(sorted(Counter(x['record_origin'] for x in rs).items())),
            'sample_records':[x['record_id'] for x in rs[:5]],
            'samples':[{
                'record_id':x['record_id'],
                'scene':x['scene_ordinal'],
                'heading':x['scene_heading'],
                'text_preview':x['text_preview']
            } for x in rs[:3]],
        })

    explicit_labels={x['speaker_label'] for x in explicit}
    supplement_labels={x['speaker_label'] for x in supp}
    doc={
        'work_id':'ammaiyappan',
        'phase':'character-entity-preflight',
        'status':'review-ready',
        'dialogue_authority':'../dialogues/final-index.json',
        'dialogue_units_scanned':len(rows),
        'explicit_dialogue_units':len(explicit),
        'source_role_supplement_units':len(supp),
        'distinct_labels_across_downstream_units':len(by_label),
        'distinct_explicit_colon_labels':len(explicit_labels),
        'supplement_labels':sorted(supplement_labels),
        'labels_new_only_in_supplement':sorted(supplement_labels-explicit_labels),
        'inventory':inventory,
        'policy':{
            'dialogue_records_modified':False,
            'global_label_merge_requires_identity_continuity':True,
            'record_aware_disposition_required_when_one_exact_label_is_reused_for_multiple_entities':True,
            'generic_roles_must_not_be_forced_into_named_characters':True,
            'source_punctuation_preserved':True,
        },
        'next_action':'Review every exact label and determine whether global label disposition is safe; for any context-reused label, create record-aware dispositions before entity assembly.'
    }
    C.mkdir(exist_ok=True)
    (C/'labels-preflight.json').write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

    md=['# அம்மையப்பன் — character/entity preflight','',
        'Status: **REVIEW READY**','',
        f'- dialogue units scanned: **{len(rows)}**',
        f'- explicit colon-labelled units: **{len(explicit)}**',
        f'- source-role-resolved supplements: **{len(supp)}**',
        f'- distinct labels across downstream units: **{len(by_label)}**','',
        '## Exact label inventory','']
    for x in inventory:
        md.append(f"- `{x['speaker_label']}` — {x['record_count']} records / {x['scene_count']} scenes — scenes {x['scenes']}")
    md += ['','## Mapping rule','',
           'A source label is globally mapped only when identity continuity is supported. If the same exact shorthand is reused for different people, dispositions must be record-aware; the dialogue layer remains unchanged.']
    (C/'labels-preflight.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
    print(json.dumps({
        'dialogue_units':len(rows),
        'distinct_labels':len(by_label),
        'labels':[{'label':x['speaker_label'],'count':x['record_count'],'scenes':x['scenes']} for x in inventory]
    },ensure_ascii=False))

if __name__=='__main__': main()
