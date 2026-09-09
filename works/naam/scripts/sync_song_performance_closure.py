#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, re
from pathlib import Path

R=Path(__file__).resolve().parents[3]
W=R/'works'/'naam'
NEXT=("Begin Phase 9 source-linked English translation from the complete-verified Tamil, scene, dialogue, character/entity and song/performance layers. Preserve source scene order and exact Tamil speaker labels as metadata; link labelled dialogue to immutable IDs; keep source-unlabelled speech unassigned; translate all six retained performance structures from their source-visible Tamil only, carrying `பாரதியார்` attribution only for `ஆயிரம் தெய்வங்கள்` and leaving the other five authorship states unresolved. Follow `docs/SONG_TRANSLATION_GUIDE.md` for performance units, run whole-work scene/unit/dialogue/performance coverage QA, and do not alter closed Tamil or structured source layers.")

def rd(p): return Path(p).read_text(encoding='utf-8')
def wr(p,s): Path(p).write_text(s,encoding='utf-8')
def upstream():
    fs=list((W/'transcription'/'parts').glob('pdf-*.md'))+list((W/'scenes').glob('scene-*.md'))+list((W/'dialogues'/'records').glob('scene-*.json'))+list((W/'characters').glob('*.json'))
    return {str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in fs}

before=upstream()
idx=json.loads(rd(W/'songs'/'index.json')); inv=json.loads(rd(W/'songs'/'inventory.json')); qa=json.loads(rd(W/'notes'/'song-performance-qa.json'))
assert idx['status']=='complete-verified-source-only' and idx['retained_performance_records']==6
assert inv['coverage']=='6/6' and len(inv['records'])==6
assert qa['status']=='PASS' and qa['source_attributed_authorship_records']==1 and qa['unresolved_item_level_authorship_records']==5
assert qa['specific_item_credit']['author_as_printed']=='பாரதியார்'
for i in range(1,7): assert (W/'songs'/'records'/f'naam-perf-{i:03d}.md').exists()

# metadata.yaml
p=W/'metadata.yaml'; s=rd(p)
old='mapped_source_visible_performance_structures:\n  status: verified-canonical-candidates-awaiting-song-gate\n  high_confidence_blocks: 6'
new='mapped_source_visible_performance_structures:\n  status: complete-verified-source-only\n  high_confidence_blocks: 6\n  retained_records: 6\n  source_attributed_authorship_records: 1\n  unresolved_item_level_authorship_records: 5\n  index_path: "songs/index.json"\n  qa_path: "notes/song-performance-qa.json"'
assert old in s; s=s.replace(old,new,1)
marker='  character_entity_qa_path: "notes/character-entity-qa.json"\n'; assert marker in s
if '  song_performance_index_path:' not in s:
    s=s.replace(marker,marker+'  song_performance_index: complete-verified-source-only\n  song_performance_index_path: "songs/index.json"\n  song_performance_record_count: 6\n  song_performance_authorship_resolved: 1\n  song_performance_authorship_unresolved: 5\n  song_performance_qa_path: "notes/song-performance-qa.json"\n',1)
s=s.replace('  song_authorship_gate: ready-next','  song_authorship_gate: complete-verified-source-only')
s=s.replace('  english_translation: blocked-pending-structured-derivatives-and-song-gate','  english_translation: ready-next')
s=re.sub(r'next_action:\s*".*"\s*$', 'next_action: '+json.dumps(NEXT,ensure_ascii=False), s, count=1, flags=re.M); wr(p,s)

# work README
p=W/'README.md'; s=rd(p)
s=s.replace('- song/performance/authorship gate: **ready-next**;','- song/performance/authorship gate: **6/6 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS; 1 source-attributed + 5 unresolved item-level authorships**;')
s=s.replace('- English translation / reader / Reading Room: **not-started**.','- English translation: **ready-next**; reader / Reading Room: **not-started**.')
if '## Song / performance / authorship closure checkpoint' not in s:
    mark='## Source-visible publication / credit evidence\n'; assert mark in s
    block='## Song / performance / authorship closure checkpoint\n\n- mapped source-visible performance structures: **6/6 retained**;\n- clearly bounded Tamil performance derivatives: **6**;\n- item-level authorship resolved from source: **1** — `ஆயிரம் தெய்வங்கள்` → `பாரதியார்` (PDF 4 credit; body PDF 16);\n- unresolved item-level authorship: **5**;\n- broad PDF 4 `கதை, வசனம், பாடல்... மு. கருணாநிதி` credit is preserved but not promoted to unsupported item-level attributions;\n- QA: `notes/song-performance-qa.json` — **PASS**;\n- upstream canonical / scene / dialogue / character modifications: **0 / 0 / 0 / 0**.\n\n**Next:** '+NEXT+'\n\n'
    s=s.replace(mark,block+mark,1)
s=re.sub(r'\*\*Next:\*\* Begin Phase 8 song/performance/authorship gating[^\n]*','**Next:** '+NEXT,s); wr(p,s)

# handover and next prompt
p=W/'PROJECT_HANDOVER.md'; s=rd(p)
if '## Song/performance/authorship closure checkpoint' not in s:
    s+='\n\n## Song/performance/authorship closure checkpoint\n\n- status: **COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS**;\n- mapped structures / retained records: **6 / 6**;\n- item-level source attribution: **1 resolved / 5 unresolved**;\n- `ஆயிரம் தெய்வங்கள்` remains specifically credited to **பாரதியார்** from PDF 4;\n- broad Kalaignar story/dialogue/song credit is not used to overwrite that specific credit or infer the other five items;\n- upstream source/derivative rewrites: **0**.\n\n## Exact next activity\n\n> **'+NEXT+'**\n'
s=re.sub(r'> \*\*Begin Phase 8 song/performance/authorship gating[^\n]*','> **'+NEXT+'**',s); wr(p,s)
wr(W/'NEXT_CHAT_PROMPT.md','# Next Chat Prompt — நாம்\n\nContinue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/naam/`. Live `main` is authoritative.\n\nCanonical Tamil is **67/67 COMPLETE-VERIFIED**. Scene-text derivatives are **45/45 COMPLETE-VERIFIED**. Immutable dialogue indexing is **590 records / COMPLETE-VERIFIED / QA PASS**. Character/entity indexing is **28 entities / 45/45 labels / 590/590 records / COMPLETE-VERIFIED / QA PASS**. Song/performance/authorship gating is **COMPLETE-VERIFIED-SOURCE-ONLY: 6/6 retained source-visible structures, 1 item-level source attribution (`ஆயிரம் தெய்வங்கள்` → `பாரதியார்`) and 5 unresolved item-level authorships, QA PASS**.\n\nSong/performance index: `works/naam/songs/index.json`. QA: `works/naam/notes/song-performance-qa.json`. Do not alter closed Tamil or structured layers except for later source-supported corrections.\n\n## Exact next activity\n\n> **'+NEXT+'**\n')

# data/works.json
p=R/'data'/'works.json'; data=json.loads(rd(p)); n=next(x for x in data if x.get('id')=='naam'); sd=n.setdefault('structured_derivatives',{})
sd.update({'song_performance_index':'complete-verified-source-only','song_performance_index_path':'works/naam/songs/index.json','song_performance_records':6,'song_performance_authorship_resolved':1,'song_performance_authorship_unresolved':5,'song_performance_qa':'PASS','song_performance_qa_path':'works/naam/notes/song-performance-qa.json','english_translation':'ready-next','next_structured_derivative':'english-translation'}); n['next_action']=NEXT; wr(p,json.dumps(data,ensure_ascii=False,separators=(',',':'))+'\n')

# root README
p=R/'README.md'; s=rd(p)
s=s.replace('- English remains downstream of scene/dialogue/character/song gates.','- song/performance/authorship gate: **6/6 retained source-visible structures / QA PASS / 1 source-attributed + 5 unresolved item-level authorships**;\n- English translation: **ready-next**.',1)
s=re.sub(r'\*\*Next:\*\* Begin Phase 8 song/performance/authorship gating[^\n]*','**Next:** '+NEXT,s); wr(p,s)

# repo handover
p=R/'docs'/'HANDOVER_KALAIGNAR_CINEMA_WORKS.md'; o=rd(p); lines=o.splitlines()
for i,line in enumerate(lines):
    if line.startswith('- **Naam / நாம்**'):
        lines[i]='- **Naam / நாம்** — canonical Tamil **67/67 COMPLETE-VERIFIED**; scenes **45/45 COMPLETE-VERIFIED**; dialogue index **590 records COMPLETE-VERIFIED / QA PASS**; character/entity index **28 entities / 45/45 labels / 590/590 records COMPLETE-VERIFIED / QA PASS**; song/performance gate **6/6 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS (1 source-attributed, 5 unresolved item-level)**; English translation next.'
s='\n'.join(lines)+('\n' if o.endswith('\n') else ''); s=re.sub(r'\*\*Exact next activity:\*\* Begin Phase 8 song/performance/authorship gating[^\n]*','**Exact next activity:** '+NEXT,s); wr(p,s)

# status audit
p=R/'docs'/'STATUS_CONSISTENCY_AUDIT.md'; o=rd(p); lines=o.splitlines()
for i,line in enumerate(lines):
    if line.startswith('| Naam / நாம் |'):
        lines[i]='| Naam / நாம் | canonical Tamil 67/67 complete-verified; 0 unresolved | **45/45 scenes; 590 dialogue records; 28 character/entities; song/performance 6/6 QA PASS** | English translation next | not-started |'
s='\n'.join(lines)+('\n' if o.endswith('\n') else ''); s=re.sub(r'\*\*Next production phase:\*\* Begin Phase 8 song/performance/authorship gating[^\n]*','**Next production phase:** '+NEXT,s); wr(p,s)

assert before==upstream()
print(json.dumps({'status':'PASS','song_records':6,'coverage':'6/6','source_attributed':1,'unresolved':5,'upstream_modified':0,'next_action':NEXT},ensure_ascii=False,indent=2))
