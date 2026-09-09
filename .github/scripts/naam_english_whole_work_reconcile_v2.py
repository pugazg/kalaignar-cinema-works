from pathlib import Path
import collections, hashlib, json, re

W=Path('works/naam'); T=W/'translations'
NEXT=(
"Begin Phase 10 whole-work reader/export generation from the complete-verified Tamil and English structured layers. "
"Build deterministic Markdown, standalone HTML, machine-readable JSON, reader QA, and an integrity manifest; verify all 45 source scenes appear exactly once in canonical order and all 797 verified English units render exactly once; preserve all 590 immutable dialogue links, the seven retained performance records, the distinct scene-34 chant, written text, source-unlabelled speech, exact cross-page provenance, and source-page linkage; prohibit duplicate source-span ownership, synthetic scene-end prose, placeholder/editorial leakage, or upstream source-layer mutation. "
"After reader QA passes, prepare structured data for Kalaignar Digital Library / Reading Room integration. Do not create a PDF, EPUB, or other publication package unless separately requested."
)
UP=[W/'transcription',W/'scenes',W/'dialogues',W/'characters',W/'songs'/'records']
BATCH=['pilot-qa.json','batch-002-005-qa.json','batch-006-015-qa.json','batch-016-025-qa.json','batch-026-035-qa.json','batch-036-045-qa.json']
PH=re.compile(r'\b(?:TODO|TBD|PLACEHOLDER|FIXME|TRANSLATE(?:\s+ME)?)\b',re.I)
BID=re.compile(r'naam-s\d{3}-u\d{3}')
SYN={'scene ends','scene ends.','end of scene','end of scene.','the scene ends','the scene ends.','[scene ends]','[end of scene]'}

def rt(p): return Path(p).read_text(encoding='utf-8')
def wt(p,s): Path(p).parent.mkdir(parents=True,exist_ok=True); Path(p).write_text(s,encoding='utf-8')
def rj(p): return json.loads(rt(p))
def wj(p,d): wt(p,json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def dg(root):
 h=hashlib.sha256()
 for p in sorted(Path(root).rglob('*')):
  if p.is_file(): h.update(str(p).encode());h.update(b'\0');h.update(p.read_bytes());h.update(b'\0')
 return h.hexdigest()
def pp(u): return [x['pdf_page'] for x in u['source']['page_provenance']]
def eng(u):
 t=u.get('translation',{})
 if isinstance(t.get('english_text'),str): yield t['english_text']
 for x in t.get('english_lines',[]) or []:
  if isinstance(x,str): yield x
 for x in t.get('line_map',[]) or []:
  if isinstance(x,dict) and isinstance(x.get('english'),str): yield x['english']

idx=rj(T/'index.json')
assert idx['status']=='scene-layer-complete-verified-45-of-45-whole-work-reconciliation-next'
assert (idx['verified_scenes'],idx['translation_units_verified'],idx['immutable_dialogue_links_verified'])==(45,797,590)
assert idx['source_unlabelled_speech_units_verified']==20 and idx['retained_performance_records_translated']==7
assert idx['song_line_cue_mappings_verified']==138 and idx['source_chant_line_cue_mappings_verified']==16
assert idx['whole_work_reconciliation_status']=='ready-next'

batch={}
for name in BATCH:
 q=rj(T/name); assert q['status']=='PASS'; batch[name]='PASS'
 if 'authorship_status_changed_by_translation' in q: assert q['authorship_status_changed_by_translation'] is False
 if 'external_or_unprinted_lyrics_imported' in q: assert q['external_or_unprinted_lyrics_imported'] is False

si=rj(W/'scenes'/'index.json'); sm={x['source_scene_number']:x for x in si['scene_records']}; assert set(sm)==set(range(1,46))
inv=rj(W/'songs'/'inventory.json'); prs=inv['records']; pids=[x['id'] for x in prs]
assert pids==['naam-perf-007','naam-perf-001','naam-perf-002','naam-perf-003','naam-perf-004','naam-perf-005','naam-perf-006']
assert inv['coverage']=='7/7' and inv['source_attributed_authorship_records']==1 and inv['unresolved_item_level_authorship_records']==6
pb={x['id']:x for x in prs}; assert pb['naam-perf-001']['author_as_printed']=='பாரதியார்' and pb['naam-perf-001']['authorship_status']=='source-attributed'
for x in prs:
 if x['id']!='naam-perf-001': assert x['authorship_status']=='unresolved-item-level' and x['author_as_printed'] is None
ua=rj(W/'notes'/'unlabelled-block-audit.json')['blocks']

ids=[]; links=[]; srcids=[]; kinds=collections.Counter(); unl=[]; unl_supported=[]; explicit_bids=[]
perforder=[]; perfunits=collections.defaultdict(list); perfmaps=collections.Counter(); cross=[]; written=[]
orderbad=[]; boundbad=[]; mapbad=[]; dup=[]; owners={}; placeholders=[]; synth=[]

for n in range(1,46):
 tr=rj(T/'records'/f'scene-{n:03d}.json'); src=rj(W/'dialogues'/'records'/f'scene-{n:03d}.json'); meta=sm[n]
 assert tr['scene_id']==f'naam-s{n:03d}' and tr['scene_ordinal']==n and tr['source_scene_number']==n and tr['scene_status']=='verified'
 assert tr['unit_count']==len(tr['units'])
 assert [u['id'] for u in tr['units']]==[f'naam-en-s{n:03d}-u{i:03d}' for i in range(1,len(tr['units'])+1)]
 lscene=[]; last=-1; scene_pages=set(meta['pdf_pages'])
 for u in tr['units']:
  ids.append(u['id']); kinds[u['kind']]+=1
  assert u['status']=='verified' and u['target_language']=='en' and u['scene_id']==tr['scene_id'] and u['scene_ordinal']==n and u['source_scene_number']==n
  pages=pp(u); assert pages and pages==sorted(dict.fromkeys(pages))
  if pages[0]<last: orderbad.append(u['id'])
  last=pages[0]
  if not set(pages).issubset(scene_pages): boundbad.append(u['id'])
  if len(pages)>1: cross.append(u['id'])
  rid=u['source'].get('source_record_id')
  if rid:
   lscene.append(rid);links.append(rid);r=next(x for x in src if x['id']==rid)
   assert u['kind']=='dialogue' and u['source']['speaker_label']==r['speaker_label'] and u['source']['source_delimiter']==r['source_delimiter'] and u['source']['page_provenance']==r['page_provenance'] and u['source']['speaker_label_origin']=='source-explicit'
  elif u['kind']=='dialogue':
   assert u['source'].get('speaker_label') is None and u['source'].get('source_delimiter') is None and u['source'].get('speaker_label_origin') is None
   loc=u['source'].get('source_locator') or {}; assert loc.get('kind')=='source-unlabelled-speech'
   unl.append(u['id'])
   candidates=[b for b in ua if b['scene_id']==u['scene_id'] and set(x['pdf_page'] for x in b['page_provenance']).intersection(pages)]
   assert candidates,u['id']; unl_supported.append(u['id'])
   m=BID.search(loc.get('description',''))
   if m:
    assert any(b['block_id']==m.group(0) for b in candidates); explicit_bids.append(m.group(0))
  occ=u['source'].get('source_occurrence_id')
  if occ:
   assert occ in pb
   if occ not in perforder: perforder.append(occ)
   perfunits[occ].append(u['id']); assert set(pages).issubset(set(pb[occ]['source_pdf_pages']))
   lm=u.get('translation',{}).get('line_map',[]) or []; perfmaps[occ]+=len(lm)
   if lm:
    if [x.get('ordinal') for x in lm]!=list(range(1,len(lm)+1)): mapbad.append(u['id'])
    for x in lm:
     if not str(x.get('tamil','')).strip() or not str(x.get('english','')).strip() or x.get('pdf_page') not in pages: mapbad.append(u['id'])
  if u['kind']=='written-text':
   written.append(u['id']); assert rid is None and u['source'].get('speaker_label') is None and u['source'].get('source_delimiter') is None
  if u['kind'] in {'stage-direction','narrative','performance-cue','chant','written-text'}:
   assert u['source'].get('speaker_label') is None and u['source'].get('source_delimiter') is None
  if rid is None and occ is None and u['kind']!='dialogue':
   loc=u['source'].get('source_locator') or {}; key=(u['scene_id'],u['kind'],u['source'].get('source_path'),tuple(pages),loc.get('kind'),loc.get('ordinal'),loc.get('description'))
   if key in owners: dup.append([owners[key],u['id']])
   else: owners[key]=u['id']
  payload=list(eng(u)); assert payload and any(x.strip() for x in payload)
  for x in payload:
   if PH.search(x): placeholders.append(u['id'])
   if x.strip().lower() in SYN: synth.append(u['id'])
 assert lscene==[x['id'] for x in src]
 srcids.extend(x['id'] for x in src)

assert len(ids)==len(set(ids))==797 and not orderbad and not boundbad and not mapbad
assert len(links)==len(set(links))==590 and links==srcids
assert len(unl)==len(unl_supported)==20
assert perforder==pids and set(perfunits)==set(pids) and sum(perfmaps.values())==138 and all(perfmaps[x]>0 for x in pids)
assert kinds['dialogue']==610 and kinds['song']==6 and kinds['chant']==1 and kinds['performance-cue']==6 and kinds['written-text']==2
assert kinds['stage-direction']+kinds['narrative']==172 and sum(kinds.values())==797
assert written==['naam-en-s041-u012','naam-en-s045-u025'] and not dup and not placeholders and not synth
assert cross==idx['cross_page_translation_units'] and len(cross)==12
chant=[];cm=0
for n in range(1,46):
 for u in rj(T/'records'/f'scene-{n:03d}.json')['units']:
  if u['kind']=='chant': chant.append(u['id']); assert u['scene_id']=='naam-s034' and u['source'].get('source_occurrence_id') is None; cm+=len(u['translation'].get('line_map',[]) or [])
assert chant==['naam-en-s034-u002'] and cm==16

before_path=Path('/tmp/naam-upstream-before.json'); before=json.loads(before_path.read_text()) if before_path.exists() else {str(p):dg(p) for p in UP}; after={str(p):dg(p) for p in UP}; assert before==after
qa={
'work_id':'naam','phase':'english-translation-whole-work-reconciliation','status':'PASS','source_scenes_expected':45,'source_scenes_verified':45,
'translation_units_expected':797,'translation_units_verified':797,'unit_ids_unique_and_sequential':True,'source_order_failures':orderbad,
'kind_counts':dict(sorted(kinds.items())),'stage_or_narrative_units':kinds['stage-direction']+kinds['narrative'],
'immutable_dialogue_records_expected':590,'immutable_dialogue_records_linked':590,'immutable_dialogue_ids_unique':True,'dialogue_source_order_exact':True,
'source_unlabelled_speech_units':20,'source_unlabelled_speaker_assignments':0,'source_unlabelled_units_supported_by_audit_scene_page':20,'source_unlabelled_units_with_explicit_audit_block_id':len(explicit_bids),
'retained_performance_records_expected':7,'retained_performance_records_translated':7,'performance_occurrence_order':perforder,'performance_line_cue_mappings':138,'performance_mapping_counts':dict(perfmaps),
'specific_source_authorship_preserved':{'naam-perf-001':'பாரதியார்'},'unsupported_authorship_upgrades':0,
'source_local_chant_units':chant,'source_local_chant_line_cue_mappings':16,'source_local_chant_promoted_to_performance_inventory':False,
'written_text_units':written,'cross_page_translation_units':cross,'cross_page_unit_count':12,'provenance_out_of_scene_bounds':boundbad,
'duplicate_non_dialogue_source_owners':dup,'placeholder_hits':placeholders,'synthetic_scene_end_hits':synth,'batch_qa_status':batch,
'upstream_integrity_before':before,'upstream_integrity_after':after,'upstream_source_layers_modified':False,'reader_export_gate':'READY-NEXT','next_activity':NEXT}
wj(T/'whole-work-reconciliation.json',qa)
wt(T/'WHOLE_WORK_RECONCILIATION.md',f'''# நாம் — Whole-work English translation reconciliation

**Status:** **PASS / COMPLETE-VERIFIED**  
**Scope:** source scenes **1–45**  
**Verified English units:** **797/797**  
**Immutable dialogue linkage:** **590/590 exactly once**

## Closure result

The complete 45-scene English layer was reconciled as one work-level gate. All **797** translation units have unique sequential scene-local IDs and remain in source-page order. All **590** immutable dialogue records are linked exactly once and in exact source dialogue order with Tamil labels, delimiters and page provenance preserved.

All **20** source-unlabelled speech units remain unassigned with **0** inferred speakers and have matching source-unlabelled audit support by scene/page. Written text remains non-dialogue. All **7/7** retained performances are represented in source order with **138** Tamil→English line/cue mappings. `naam-perf-001` retains **பாரதியார்**; the other six remain unresolved at item level. Scene 34's street-play remains a distinct **chant / 16 mappings** and is not promoted into the seven-record performance inventory.

## Whole-work QA

- scenes: **45/45**;
- units: **797/797 unique and sequential**;
- dialogue links: **590/590 exactly once**;
- dialogue units: **610** = 590 labelled + 20 source-unlabelled;
- stage/narrative units: **172**;
- performance-cue units: **6**;
- song units: **6**;
- chant: **1 / 16 mappings**;
- written text: **2 units**;
- performances: **7/7 / 138 mappings**;
- cross-page units: **12**;
- provenance outside scene bounds: **0**;
- duplicate non-dialogue source-span ownership: **0**;
- placeholder/editorial leakage: **0**;
- synthetic scene-end prose: **0**;
- upstream Tamil / scene / dialogue / character / Tamil performance mutations: **0**.

All six prior English QA checkpoints remain **PASS**. English translation is now **COMPLETE-VERIFIED**.

## Exact next activity

> **{NEXT}**
''')
idx.update({'status':'complete-verified','whole_work_reconciliation_status':'PASS','whole_work_reconciliation_qa':'whole-work-reconciliation.json','whole_work_reconciliation_report':'WHOLE_WORK_RECONCILIATION.md','reader_export_status':'ready-next','next_activity':NEXT,'whole_work_kind_counts':dict(sorted(kinds.items()))})
wj(T/'index.json',idx)

p=T/'README.md';s=rt(p);s=re.sub(r'\*\*Status:\*\* \*\*.*?\*\*','**Status:** **COMPLETE-VERIFIED / whole-work reconciliation PASS**',s,count=1);s=re.sub(r'## Next gate\n\n.*?(?=\n##|\Z)',f'## Next gate\n\n{NEXT}\n',s,flags=re.S)
if '## Whole-work English closure' not in s:s+=f'''\n## Whole-work English closure\n\n- **45/45 scenes / 797 units / 590/590 dialogue links / 20 source-unlabelled with 0 inferred speakers / 7/7 performances / 138 mappings / 1 chant (16 mappings) / 12 cross-page units**;\n- duplicate source ownership / placeholders / synthetic scene ends / upstream rewrites: **0 / 0 / 0 / 0**;\n- reconciliation: `whole-work-reconciliation.json` — **PASS**.\n\n**Next:** {NEXT}\n'''
wt(p,s)

p=W/'metadata.yaml';s=rt(p);s=re.sub(r'(?m)^  english_translation: scene-layer-complete-verified-45-of-45-whole-work-reconciliation-next$','  english_translation: complete-verified',s,count=1);s=re.sub(r'(?m)^  english_whole_work_reconciliation: ready-next$','  english_whole_work_reconciliation: PASS',s,count=1)
anchor='  english_whole_work_reconciliation: PASS'
if '  english_whole_work_reconciliation_qa_path:' not in s:s=s.replace(anchor,anchor+'\n  english_whole_work_reconciliation_qa_path: "translations/whole-work-reconciliation.json"\n  english_reader_export: ready-next',1)
s=re.sub(r'(?m)^  english_translation: in-progress-verified-25-of-45$','  english_translation: complete-verified-45-of-45',s,count=1);s=re.sub(r'(?m)^  reader_export: not-started$','  reader_export: ready-next',s,count=1);s=re.sub(r'(?m)^next_action:.*$','next_action: '+json.dumps(NEXT,ensure_ascii=False),s,count=1);wt(p,s)

p=W/'README.md';s=rt(p);s=re.sub(r'- English translation: \*\*45/45 SCENE LAYER VERIFIED.*?\*\*; reader / Reading Room: \*\*blocked until reconciliation PASS\*\*\.','- English translation: **45/45 COMPLETE-VERIFIED / 797 units / 590/590 dialogue links / 7/7 performance records / 138 performance mappings / 1 chant (16 mappings) / whole-work QA PASS**; reader/export: **READY-NEXT**.',s,count=1);s=re.sub(r'\*\*Next:\*\* Run whole-work English translation reconciliation.*?(?=\n|$)','**Next:** '+NEXT,s,count=1)
if '## English whole-work reconciliation closure' not in s:s+=f'''\n\n## English whole-work reconciliation closure\n\n- English **COMPLETE-VERIFIED**; whole-work QA **PASS**; **45/45 scenes / 797 units / 590/590 dialogue links / 20 unlabelled / 7/7 performances / 138 mappings / 1 chant (16 mappings) / 12 cross-page units**;\n- duplicate source owners / placeholders / synthetic scene ends / upstream changes: **0 / 0 / 0 / 0**;\n- reader/export: **READY-NEXT**.\n\n**Next:** {NEXT}\n''';wt(p,s)

p=W/'PROJECT_HANDOVER.md';s=rt(p);cur=f'''## Current checkpoint\n\n- source intake / scan / mapping: **complete / 72/72 / verified**;\n- canonical Tamil: **67/67 COMPLETE-VERIFIED**;\n- scene derivatives: **45/45 COMPLETE-VERIFIED / QA PASS**;\n- dialogue index: **590 records / COMPLETE-VERIFIED / QA PASS**;\n- character/entity: **28 entities / 45/45 labels / 590/590 records / COMPLETE-VERIFIED**;\n- song/performance: **7/7 COMPLETE-VERIFIED-SOURCE-ONLY / 1 source-attributed + 6 unresolved**;\n- English: **45/45 COMPLETE-VERIFIED / 797 units / 590/590 dialogue links / 20 unlabelled with 0 inferred speakers / 7/7 performances / 138 mappings / 1 chant (16 mappings) / whole-work QA PASS**;\n- reader/export: **READY-NEXT**; Reading Room integration: **not-started**.\n\nAuthoritative English closure: `translations/index.json`, `translations/whole-work-reconciliation.json`, `translations/WHOLE_WORK_RECONCILIATION.md`, and `translations/records/scene-001.json`–`scene-045.json`.\n\n## Current exact next activity\n\n> **{NEXT}**\n\n''';s=re.sub(r'## Current checkpoint\n.*?(?=## Source identity\n)',cur,s,count=1,flags=re.S);wt(p,s)
wt(W/'NEXT_CHAT_PROMPT.md',f'''# Next Chat Prompt — நாம்\n\nContinue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/naam/`. **Live `main` is authoritative.**\n\nCanonical Tamil **67/67 COMPLETE-VERIFIED**; scenes **45/45 COMPLETE-VERIFIED**; dialogue index **590 immutable records / QA PASS**; character/entity **28 entities / 45/45 labels / 590/590 records / QA PASS**; song/performance **7/7 COMPLETE-VERIFIED-SOURCE-ONLY**.\n\nEnglish translation is **COMPLETE-VERIFIED** after whole-work reconciliation: **45/45 scenes, 797 units, 590/590 immutable dialogue links, 20 source-unlabelled speech units with 0 inferred speakers, 7/7 retained performances, 138 performance mappings, 1 distinct scene-34 chant / 16 mappings, 2 written-text units, 12 cross-page units**. `translations/whole-work-reconciliation.json` is **PASS**.\n\nAuthorship remains source-honest: `naam-perf-001` → **பாரதியார்**; the other six remain unresolved item-level. Scene 34's chant is not a `naam-perf-*` record; scene 41 `கடிதத்தில் :-` remains written text, `ஜீவானந்தர் —` retains its source em dash, and `உன்மீனு` remains the exact source label; scene 45's closing rhetorical questions remain source-unlabelled.\n\nReader/export is **READY-NEXT**. Closed Tamil, scene, dialogue, character, song-source and English records are immutable downstream inputs.\n\n## Exact next activity\n\n> **{NEXT}**\n''')

p=Path('data/works.json');data=rj(p);work=next(x for x in data if x.get('id')=='naam');sd=work.setdefault('structured_derivatives',{});sd.update({'english_translation':'complete-verified','english_translation_verified_scenes':45,'english_translation_units':797,'english_dialogue_links_verified':590,'english_source_unlabelled_speech_units':20,'english_performance_records_translated':7,'english_song_line_cue_mappings_verified':138,'english_chant_units_verified':1,'english_chant_line_cue_mappings_verified':16,'english_whole_work_reconciliation':'PASS','english_whole_work_reconciliation_qa_path':'works/naam/translations/whole-work-reconciliation.json','reader_export':'ready-next'});work['next_action']=NEXT;wj(p,data)

p=Path('README.md');s=rt(p);s=re.sub(r'- English translation: \*\*45/45 scene layer VERIFIED.*?\*\*\.','- English translation: **45/45 COMPLETE-VERIFIED — 797 units / 590/590 dialogue links / 7/7 performance records / 138 mappings / 1 chant; whole-work reconciliation PASS; reader/export READY-NEXT**.',s,count=1);s=re.sub(r'\*\*Next:\*\* Run whole-work English translation reconciliation.*?(?=\n|$)','**Next:** '+NEXT,s,count=1);mark='<!-- Naam English whole-work closure current -->';
if mark not in s:s+=f'''\n\n{mark}\n**Naam current:** English **COMPLETE-VERIFIED**, reconciliation **PASS**, **45/45 / 797 / 590/590 / 7/7 / 138 / chant 1/16**, reader/export **READY-NEXT**, upstream rewrites **0**. **Next:** {NEXT}\n''';wt(p,s)
for p in [Path('docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md'),Path('docs/STATUS_CONSISTENCY_AUDIT.md')]:
 s=rt(p);mark='<!-- Naam English whole-work closure current -->'
 if mark not in s:s+=f'''\n\n{mark}\n**Naam English whole-work closure:** **PASS / COMPLETE-VERIFIED — 45/45 scenes / 797 units / 590/590 dialogue links / 20 unlabelled / 7/7 performances / 138 mappings / chant 1/16 / 12 cross-page units**; duplicate ownership, placeholders, synthetic scene ends, upstream rewrites **0**; reader/export **READY-NEXT**. **Next:** {NEXT}\n'''
 wt(p,s)
assert {str(p):dg(p) for p in UP}==before
print(json.dumps({'status':'PASS','english':'complete-verified','scenes':'45/45','units':797,'dialogue_links':'590/590','unlabelled':20,'performance_records':'7/7','performance_mappings':138,'chant':'1/16','written_text':2,'cross_page':12,'next':'Phase 10 reader/export'},ensure_ascii=False,indent=2))
