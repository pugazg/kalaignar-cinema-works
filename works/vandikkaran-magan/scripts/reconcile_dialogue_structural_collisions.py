#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter, defaultdict, deque
from copy import deepcopy
from pathlib import Path
import json, re

ROOT = Path(__file__).resolve().parents[3]
W = ROOT / 'works' / 'vandikkaran-magan'
PAGES = W / 'transcription' / 'pages'
SCENES = W / 'scenes'
D = W / 'dialogues'
R = D / 'records'
N = W / 'notes'

SOURCE_META_RE = re.compile(r'\A<!-- source: pdf=(\d+).*?status=visual-verified -->\n?')
SCENE_HEADING_RE = re.compile(r'^##\s+(காட்சி.*)$', re.M)
DIALOGUE_RE = re.compile(r'^(?P<label>[^:#\[\]{}<>\n]{1,60}?)(?P<delimiter>:\s*(?:—|–|-)?)\s*(?P<text>\S.*)$')
ALT_RE = re.compile(r'^(?P<label>[\u0B80-\u0BFF A-Za-z.]{1,28}?)\s*(?P<delimiter>[;—–-])\s*(?P<text>\S.*)$')
PURE_ACTION_RE = re.compile(r'^(?:\([^()\n]*\)|\[[^\[\]\n]*\]|\{[^{}\n]*\})$')
NON_SPEAKER_LABELS = {'இடம்','நேரம்','காலம்','பாட்டு','வசனம்','டைரக்ஷன்','கடிதத்தில்'}
SEPARATORS = {'★','★★★','* * *','---','***','___'}
EXPECTED_ANOMALOUS = {
    'உருட்டல்; மிரட்டல்;', 'பழுக்கப் பழுக்க-ரசம்', 'பிழியப் பிழியப்-பழம்',
    'கங்குலில் எங்கும் பனிமூட்டம் — உடல்', 'படுத்தாள்; புரண்டாள்;', 'வந்தான்; சேர்ந்தேன்',
    'மின்னும் — பொன்', 'மெத்தை — தத்தும்', 'தத்தை; தன்', 'சந்தம் — தன்', 'என்று—தன்',
    'காட்டுவேன்; பாருங்களே!', 'மேய்ப்பவன் என்று — எண்ணியிருக்கும்', 'ஊரைத் திருத்த - ஒரு',
    'பேரை நிறுத்த - இரு', 'கிளிப்புள்ளே; கிரிப்புள்ளே;'
}


def load_page(pdf:int)->str:
    raw=(PAGES/f'{pdf:03d}.md').read_text(encoding='utf-8')
    m=SOURCE_META_RE.match(raw)
    assert m and int(m.group(1))==pdf
    body=raw[m.end():]
    if body.startswith('\n'): body=body[1:]
    return body.rstrip('\n')


def structural_kind(s:str):
    if not s: return 'blank'
    if s.startswith('<!--') and s.endswith('-->'): return 'comment'
    if s.startswith('#'): return 'heading'
    if s in SEPARATORS: return 'separator'
    if s.startswith('**') and s.endswith('**'): return 'caption'
    if s.startswith('(') or s.startswith('[') or s.startswith('{'): return 'stage'
    if s.endswith(')') or s.endswith(']') or s.endswith('}'): return 'stage-continuation'
    return None


def append_piece(obj,pdf,text):
    segs=obj.setdefault('_segments',[])
    if not segs or segs[-1]['pdf_page']!=pdf:
        segs.append({'pdf_page':pdf,'printed_page':pdf-1,'lines':[text]})
    else:
        segs[-1]['lines'].append(text)


def finalize(obj):
    segs=obj.pop('_segments')
    pseg=[]
    for seg in segs:
        text='\n'.join(seg['lines']).strip('\n')
        assert text
        pseg.append({'pdf_page':seg['pdf_page'],'printed_page':seg['printed_page'],'text':text})
    obj['page_provenance']=[{'pdf_page':x['pdf_page'],'printed_page':x['printed_page']} for x in pseg]
    obj['text']='\n'.join(x['text'] for x in pseg)
    if len(pseg)>1: obj['page_segments']=pseg


def fp(r):
    return (
        r['scene_id'], r['speaker_label'], r['source_delimiter'], r['text'],
        tuple((x['pdf_page'],x['printed_page']) for x in r['page_provenance'])
    )

scene_idx=json.loads((SCENES/'index.json').read_text(encoding='utf-8'))
assert scene_idx['status']=='complete-verified' and scene_idx['total_scenes']==72
scenes=scene_idx['scenes']
collision=json.loads((N/'dialogue-structural-collision-audit.json').read_text(encoding='utf-8'))
assert collision['collision_count']==31
collision_raw={x['raw'] for x in collision['collisions']}
assert len(collision_raw)==31

old_by_scene={}
old_all=[]
for i in range(1,73):
    rows=json.loads((R/f'scene-{i:03d}.json').read_text(encoding='utf-8'))
    old_by_scene[i]=rows; old_all.extend(rows)
assert len(old_all) in {744,773}
old_pool=defaultdict(deque)
for r in old_all: old_pool[fp(r)].append(r)
old_ids={r['id'] for r in old_all}
assert len(old_ids)==len(old_all)

stream=''; page_ranges={}
for pdf in range(6,88):
    body=load_page(pdf)
    if stream: stream+='\n\n'
    st=len(stream); stream+=body; page_ranges[pdf]=(st,len(stream))
headings=list(SCENE_HEADING_RE.finditer(stream))
assert len(headings)==72

all_new=[]; per_scene={}; source_counts={}; action_only=[]; promoted=[]
label_counts=Counter(); delim_counts=Counter(); max_old={}
for i,rows in old_by_scene.items():
    nums=[int(x['id'].rsplit('d',1)[1]) for x in rows] or [0]
    max_old[i]=max(nums)

for ordinal,(scene,heading) in enumerate(zip(scenes,headings),1):
    assert scene['ordinal']==ordinal and scene['source_heading']==heading.group(1).strip()
    archive_sid=f'vandikkaran-magan-s{ordinal:03d}'
    source_sid=scene['scene_id']; scene_file=f'scene-{ordinal:03d}.md'
    scene_start=heading.start(); scene_end=headings[ordinal].start() if ordinal<len(headings) else len(stream)
    generated=[]; active=None

    def flush():
        global active
        if active is not None:
            finalize(active); generated.append(active); active=None

    for pdf in scene['pdf_pages']:
        p0,p1=page_ranges[pdf]; a,b=max(scene_start,p0),min(scene_end,p1)
        if a>=b: continue
        for raw in stream[a:b].splitlines():
            s=raw.strip()
            if not s:
                flush(); continue
            m=DIALOGUE_RE.match(s)
            if m:
                label=m.group('label').strip(); text=m.group('text'); delim=m.group('delimiter')
                if label in NON_SPEAKER_LABELS:
                    flush(); continue
                if PURE_ACTION_RE.fullmatch(text.strip()):
                    flush()
                    if s in collision_raw:
                        action_only.append({'scene_ordinal':ordinal,'source_scene_id':source_sid,'pdf_page':pdf,'raw':s})
                    continue
                flush()
                active={
                    'scene_id':archive_sid,'scene_ordinal':ordinal,'source_scene_id':source_sid,
                    'source_heading':scene['source_heading'],'speaker_label':label,'source_delimiter':delim,
                    'source_scene_file':scene_file,'_segments':[],'_raw_start':s
                }
                append_piece(active,pdf,text)
                continue
            kind=structural_kind(s)
            if kind is not None:
                flush(); continue
            am=ALT_RE.match(s)
            if am and s in EXPECTED_ANOMALOUS:
                flush(); continue
            if active is not None:
                append_piece(active,pdf,s)
        # page boundary deliberately does not flush an active utterance
    flush()

    assigned=[]; next_id=max_old[ordinal]
    for g in generated:
        raw_start=g.pop('_raw_start')
        key=fp(g)
        if old_pool[key]:
            old=old_pool[key].popleft()
            chk=deepcopy(g); chk['id']=old['id']
            assert chk==old, (ordinal,old['id'])
            rec=old
        else:
            next_id+=1
            rec=deepcopy(g); rec['id']=f'{archive_sid}-d{next_id:03d}'
            assert raw_start in collision_raw, (ordinal,raw_start)
            promoted.append({'record_id':rec['id'],'scene_ordinal':ordinal,'source_scene_id':source_sid,
                             'pdf_page':rec['page_provenance'][0]['pdf_page'],'speaker_label':rec['speaker_label'],
                             'source_delimiter':rec['source_delimiter'],'raw':raw_start})
        assigned.append(rec)
    (R/f'scene-{ordinal:03d}.json').write_text(json.dumps(assigned,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    per_scene[archive_sid]=len(assigned); source_counts[source_sid]=len(assigned)
    all_new.extend(assigned); label_counts.update(x['speaker_label'] for x in assigned); delim_counts.update(x['source_delimiter'] for x in assigned)

assert not any(old_pool.values()), 'an old immutable record failed to match corrected source parsing'
assert len(all_new)==773, len(all_new)
assert len({x['id'] for x in all_new})==773
assert len(label_counts)==38
assert dict(sorted(delim_counts.items()))=={':':8,':—':765}, dict(delim_counts)
if len(old_all)==744:
    assert len(promoted)==29
else:
    assert len(promoted)==0
assert len(action_only)==2
assert {x['pdf_page'] for x in action_only}=={62,72}

multi=[x for x in all_new if len(x['page_provenance'])>1]
assert len(multi)==3
zero_archive=[k for k,v in per_scene.items() if v==0]
zero_source=[s['scene_id'] for s in scenes if source_counts[s['scene_id']]==0]
assert len(zero_archive)==15

# Reconcile the collision audit and preserve the first repair's append-only ID evidence.
if promoted:
    collision['promoted_dialogue_records']=promoted
else:
    collision.setdefault('promoted_dialogue_records',[])
collision.update({
    'status':'PASS-CLOSED','reconciled_dialogue_records':773,'omitted_dialogue_lines_repaired':29,
    'source_labelled_action_only_excluded':2,'action_only_exclusions':action_only,
    'stable_existing_dialogue_ids_preserved':744,'new_append_only_dialogue_ids':29,
    'remaining_structural_collision_omissions':0
})
(N/'dialogue-structural-collision-audit.json').write_text(json.dumps(collision,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

idx=json.loads((D/'index.json').read_text(encoding='utf-8'))
idx.update({
    'status':'complete-verified-reconciled','dialogue_record_count':773,
    'distinct_exact_speaker_labels':38,'delimiter_distribution':{':':8,':—':765},
    'multi_page_dialogue_records':3,'scene_record_counts':per_scene,'source_scene_record_counts':source_counts,
    'zero_dialogue_scenes':zero_archive,'zero_dialogue_source_scene_ids':zero_source,
    'structural_collision_reconciliation':{
        'status':'PASS','audit':'../notes/dialogue-structural-collision-audit.json','collisions_reviewed':31,
        'omitted_explicit_utterances_restored':29,'source_labelled_action_only_excluded':2,
        'existing_ids_preserved':744,'append_only_ids_added':29
    },
    'next_action':'Reconcile the closed character/entity and song/performance layers against the corrected 773-record immutable dialogue authority, then begin the bounded English-translation pilot from source scene 1.'
})
(D/'index.json').write_text(json.dumps(idx,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

qa={
 'work_id':'vandikkaran-magan','phase':'immutable-dialogue-index','status':'PASS-RECONCILED',
 'scene_derivatives':'72/72 complete-verified','dialogue_records':773,'distinct_exact_speaker_labels':38,
 'delimiter_distribution':{':':8,':—':765},'zero_dialogue_scenes':zero_archive,'zero_dialogue_source_scene_ids':zero_source,
 'multi_page_dialogue_records':3,'multi_page_record_ids':[x['id'] for x in multi],
 'reviewed_anomalous_non_colon_candidates':16,'anomalous_candidates_promoted_to_dialogue':0,
 'unlabelled_source_blocks_assigned_a_speaker':0,'duplicate_dialogue_ids':0,'speaker_label_normalizations':0,
 'canonical_or_scene_files_modified_by_reconciliation':0,
 'late_structural_collision_reconciliation':{
   'collisions_reviewed':31,'omitted_explicit_utterances_restored':29,'source_labelled_action_only_excluded':2,
   'legacy_record_count':744,'reconciled_record_count':773,'existing_ids_preserved':744,'append_only_ids_added':29
 },
 'assertions':{
   'all_corrected_source_explicit_utterances_indexed':True,'all_legacy_ids_preserved':True,
   'action_only_source_labels_not_promoted_to_spoken_dialogue':True,'three_cross_page_utterances_remain_single_records':True,
   'eight_colon_only_records_preserved':True,'zero_dialogue_scenes_preserved':True
 }
}
(N/'dialogue-index-qa.json').write_text(json.dumps(qa,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(N/'dialogue-index-qa.md').write_text('''# வண்டிக்காரன் மகன் — immutable dialogue index QA\n\nStatus: **PASS / RECONCILED**\n\nA late source-structure audit found **31** explicit-label lines that the legacy parser could misclassify solely because the complete line ended in a bracket. Direct canonical text review established **29 spoken utterances + 2 source-labelled action-only lines**.\n\n- immutable dialogue records: **773**;\n- existing immutable IDs preserved: **744/744**;\n- append-only repaired IDs: **29**;\n- exact source labels: **38**;\n- delimiters: **`:—` 765 / `:` 8**;\n- action-only source labels promoted to speech: **0/2**;\n- zero-dialogue scenes: **15**;\n- cross-page dialogue records: **3**;\n- duplicate IDs / label normalizations / inferred unlabelled speakers: **0 / 0 / 0**.\n\n**PASS — the corrected immutable dialogue layer is the downstream authority.**\n''',encoding='utf-8')
(D/'README.md').write_text('''# வண்டிக்காரன் மகன் — immutable dialogue layer\n\n**Status:** **COMPLETE-VERIFIED / RECONCILED / QA PASS**\n\nBuilt from the closed 72/72 source-led scene derivatives without rewriting canonical Tamil or scene files. A late structural-collision audit corrected a parser defect that had treated some explicit speaker-labelled lines ending in parenthetical action as stage directions.\n\n## Coverage\n\n- immutable dialogue records: **773**;\n- legacy IDs preserved: **744/744**; append-only repair records: **29**;\n- exact source speaker labels: **38**;\n- zero-dialogue scenes: **15**; cross-page records: **3**;\n- delimiters: **`:—` 765 / `:` 8**;\n- 31 structural collisions reviewed: **29 spoken records restored / 2 action-only labels excluded**;\n- unlabelled text assigned to speakers: **0**; label normalizations: **0**.\n\nSee `../notes/dialogue-structural-collision-audit.json` and `../notes/dialogue-index-qa.json`.\n\n## Next\n\nReconcile character/entity and song/performance downstream controls to the corrected 773-record dialogue authority, then begin the bounded English scene-1 pilot.\n''',encoding='utf-8')

# Preserve the historical preflight while making its supersession explicit.
pf=json.loads((N/'dialogue-index-preflight.json').read_text(encoding='utf-8'))
pf['status']='superseded-by-structural-collision-reconciliation'
pf['historical_preflight_explicit_dialogue_candidates']=pf.get('explicit_dialogue_candidates',744)
pf['current_reconciled_dialogue_records']=773
pf['structural_collision_reconciliation']='dialogue-structural-collision-audit.json'
pf['note']='Historical navigation preflight retained for audit history. It undercounted 29 spoken source-labelled lines because its legacy structural classifier ran before speaker parsing. Current authority is dialogues/index.json plus dialogue-structural-collision-audit.json.'
(N/'dialogue-index-preflight.json').write_text(json.dumps(pf,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(N/'dialogue-index-preflight.md').write_text('''# வண்டிக்காரன் மகன் — dialogue-index preflight\n\nStatus: **SUPERSEDED / HISTORICAL**\n\nThe original preflight counted **744** explicit dialogue candidates. A later structural-collision audit established that the parser had skipped **29** genuine source-labelled spoken utterances whose lines ended with parenthetical action, while correctly excluding **2** source-labelled action-only lines.\n\nCurrent immutable dialogue authority: **773 records / 38 exact labels / QA PASS-RECONCILED**. Existing 744 IDs were preserved and 29 repair IDs were added append-only.\n\nSee `dialogue-structural-collision-audit.json`, `dialogue-index-qa.json`, and `../dialogues/index.json`.\n''',encoding='utf-8')

src=(N/'dialogue-source-review.md').read_text(encoding='utf-8')
src=src.replace('Status: **PASS / CLOSED**','Status: **PASS / CLOSED / LATE RECONCILIATION APPLIED**')
src=src.replace('The final immutable dialogue layer contains **744 records / 38 exact labels**, with **15** legitimate zero-dialogue scenes, **3** multi-page records, **0** duplicate dialogue IDs and **0** speaker-label normalizations.', 'A later structural-collision audit reopened this gate on direct canonical evidence: 31 explicit-label lines had been hidden from the legacy parser by line-ending parenthetical syntax. **29** are spoken utterances and were restored with append-only IDs; **2** are source-labelled action-only lines and remain outside dialogue. The reconciled immutable dialogue layer therefore contains **773 records / 38 exact labels**, with **15** legitimate zero-dialogue scenes, **3** multi-page records, **0** duplicate dialogue IDs and **0** speaker-label normalizations. All original **744/744 IDs** remain unchanged.')
(N/'dialogue-source-review.md').write_text(src,encoding='utf-8')

# Retire the destructive legacy builder: the reconciliation script is idempotent and stable-ID-aware.
(D.parent/'scripts'/'build_dialogues.py').write_text("#!/usr/bin/env python3\n# Stable-ID-aware dialogue builder/reconciler.\nfrom pathlib import Path\nimport runpy\nrunpy.run_path(str(Path(__file__).with_name('reconcile_dialogue_structural_collisions.py')), run_name='__main__')\n",encoding='utf-8')

# Patch the navigation preflight parser so source-labelled lines are tested before line-ending bracket structure.
pp=W/'scripts'/'build_dialogue_preflight.py'
s=pp.read_text(encoding='utf-8')
if 'if DIALOGUE_RE.match(s):\n        return None' not in s:
    s=s.replace('    if s.startswith("#"):\n        return "heading"\n', '    if s.startswith("#"):\n        return "heading"\n    # Speaker syntax takes precedence over a line-ending parenthetical action.\n    if DIALOGUE_RE.match(s):\n        return None\n')
    s=s.replace('                    text = m.group("text")\n', '                    text = m.group("text")\n                    if PURE_ACTION_RE.fullmatch(text.strip()):\n                        flush_active(); flush_unlabelled()\n                        classification_counts["source_labelled_action_only"] += 1\n                        continue\n')
    s=s.replace('SEPARATORS = {"★", "★★★", "* * *", "---", "***", "___"}\n', 'SEPARATORS = {"★", "★★★", "* * *", "---", "***", "___"}\nPURE_ACTION_RE = re.compile(r"^(?:\\([^\\n]*\\)|\\[[^\\n]*\\]|\\{[^\\n]*\\})$")\n')
pp.write_text(s,encoding='utf-8')

print(json.dumps({'status':'PASS','dialogue_records':773,'legacy_ids_preserved':744,'new_append_only_ids':29,'action_only_excluded':2,'labels':38,'delimiter_distribution':dict(sorted(delim_counts.items()))},ensure_ascii=False))
