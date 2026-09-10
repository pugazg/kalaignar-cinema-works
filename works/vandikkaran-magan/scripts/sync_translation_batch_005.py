#!/usr/bin/env python3
from pathlib import Path
import json, re

ROOT = Path(__file__).resolve().parents[3]
W = ROOT / 'works' / 'vandikkaran-magan'
NEXT = ('Translate and verify archive scene ordinals 6–10 as the next bounded English batch. '
        'Preserve source order and exact Tamil label/provenance metadata; link reconciled immutable dialogue IDs exactly once; '
        'keep source-unlabelled speech unassigned; link only verified song/performance occurrences; '
        'do not modify closed Tamil, scene, dialogue, character or song records.')

# Authoritative current English checkpoint.
tidx = json.loads((W/'translations'/'index.json').read_text(encoding='utf-8'))
assert tidx['verified_scenes'] == 5 and tidx['translation_units'] == 88
assert tidx['immutable_dialogue_records_linked'] == 65
assert tidx['source_unlabelled_spoken_units'] == 2
bqa = json.loads((W/'translations'/'batch-002-005-qa.json').read_text(encoding='utf-8'))
assert bqa['status'] == 'PASS' and bqa['immutable_dialogue_records_linked'] == 34

# Dialogue active index: correct current distribution and downstream next action; preserve legacy-history fields.
p = W/'dialogues'/'index.json'; x = json.loads(p.read_text(encoding='utf-8'))
assert x['status'] == 'complete-verified-reconciled' and x['dialogue_record_count'] == 773
assert x['structural_collision_reconciliation']['existing_ids_preserved'] == 744
x['policy']['source_delimiter'] = 'preserved exactly; :— for 765 records and : for 8 records'
x['next_action'] = NEXT
p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# Character active index/QA: reconciled record authority is 773, not the historical 744 pre-reconciliation count.
p = W/'characters'/'index.json'; x = json.loads(p.read_text(encoding='utf-8'))
x['dialogue_records_source'] = 773; x['dialogue_record_coverage'] = '773/773'; x['next_activity'] = NEXT
p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
p = W/'notes'/'character-index-qa.json'; x = json.loads(p.read_text(encoding='utf-8'))
x['dialogue_records_expected'] = 773; x['dialogue_records_mapped'] = 773; x['next_activity'] = NEXT
p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# Song active index/QA stays source-only closed; only downstream next pointer changes.
for rel in ['songs/index.json','notes/song-performance-qa.json']:
    p=W/rel; x=json.loads(p.read_text(encoding='utf-8')); x['next_activity']=NEXT
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# Canonical transcription index is closed; reflect reconciled downstream state rather than a stale dialogue-ready pointer.
p=W/'transcription'/'index.json'; x=json.loads(p.read_text(encoding='utf-8'))
x['dialogue_index']='complete-verified-reconciled'; x['next_action']=NEXT
p.write_text(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')

# Patch current reusable character/song builders so reruns do not regenerate stale active counts/pointers.
p=W/'scripts'/'build_characters.py'; s=p.read_text(encoding='utf-8')
s=s.replace("'dialogue_records_source': 744", "'dialogue_records_source': 773")
s=s.replace("'dialogue_records_expected': 744", "'dialogue_records_expected': 773")
s=s.replace("'dialogue_records_mapped': 744", "'dialogue_records_mapped': 773")
p.write_text(s,encoding='utf-8')
p=W/'scripts'/'build_song_performance_index.py'; s=p.read_text(encoding='utf-8')
old='Begin a bounded English-translation pilot from source scene 1 using only closed canonical Tamil plus verified scene/dialogue/character/song-performance derivatives. Preserve exact Tamil source labels and provenance, link immutable dialogue IDs without rewriting them, and keep song/performance authorship unresolved wherever the source gate is unresolved. Run pilot QA before scaling to later scenes.'
s=s.replace(old,NEXT)
p.write_text(s,encoding='utf-8')

# Active layer READMEs.
(W/'dialogues'/'README.md').write_text(f'''# வண்டிக்காரன் மகன் — immutable dialogue layer\n\n**Status:** **COMPLETE-VERIFIED / RECONCILED / QA PASS**\n\nBuilt from the closed 72/72 source-led scene derivatives without rewriting canonical Tamil or scene files. A late structural-collision audit corrected a parser defect that had treated some explicit speaker-labelled lines ending in parenthetical action as stage directions.\n\n## Coverage\n\n- immutable dialogue records: **773**;\n- legacy IDs preserved: **744/744**; append-only repair records: **29**;\n- exact source speaker labels: **38**;\n- zero-dialogue scenes: **15**; cross-page records: **3**;\n- delimiters: **`:—` 765 / `:` 8**;\n- 31 structural collisions reviewed: **29 spoken records restored / 2 action-only labels excluded**;\n- unlabelled text assigned to speakers: **0**; label normalizations: **0**.\n\nSee `../notes/dialogue-structural-collision-audit.json` and `../notes/dialogue-index-qa.json`.\n\n## Downstream\n\nCharacter/entity and song/performance layers are reconciled and closed against this 773-record authority. English translation is verified through archive scene 5.\n\n**Next:** {NEXT}\n''',encoding='utf-8')

(W/'characters'/'README.md').write_text(f'''# வண்டிக்காரன் மகன் — character/entity index\n\n**Status:** **COMPLETE-VERIFIED / RECONCILED / QA PASS**\n\nThis interpretive layer maps the reconciled immutable dialogue authority without rewriting source speaker labels or dialogue text.\n\n## Coverage\n\n- immutable dialogue records: **773/773 mapped exactly once**;\n- exact source speaker labels: **38/38 mapped**;\n- entities: **32** — **15 named characters / 14 generic roles / 3 collectives**;\n- verified / review / unresolved entities: **32 / 0 / 0**;\n- unmapped labels / records: **0 / 0**;\n- upstream dialogue records modified: **0**.\n\nVariant and voice mappings exist only here as interpretive metadata. `லிங்கன்` is not collapsed into `விங்கன்`; `ஜம்பு` is not collapsed into `ஜம்புலிங்க பூபதி`; generic labels remain categorical.\n\n## Downstream\n\nSong/performance is closed at 9/9 source-visible occurrences; English translation is verified through archive scene 5.\n\n**Next:** {NEXT}\n''',encoding='utf-8')

(W/'songs'/'README.md').write_text(f'''# வண்டிக்காரன் மகன் — song / performance layer\n\n**Status:** **COMPLETE-VERIFIED-SOURCE-ONLY / AUTHORSHIP GATE CLOSED / QA PASS**\n\n- source-visible performance occurrences: **9/9**;\n- full or clearly bounded Tamil song/lyric bodies: **6**;\n- cue-only / non-lyric performance occurrences: **3**;\n- item-level source-attributed lyric authorship: **0**;\n- unresolved item-level lyric authorship: **6**;\n- non-lyric records where lyric authorship is not applicable: **3**.\n\nPDF 88 prints `பாடல்கள்: கவிஞர் வாலி`; it remains film-level metadata and is not promoted item-by-item. No missing lyric or chant text is reconstructed. The layer remains immutable while translation proceeds.\n\n**Next:** {NEXT}\n''',encoding='utf-8')

(W/'transcription'/'README.md').write_text(f'''# வண்டிக்காரன் மகன் — canonical Tamil transcription\n\nThe rendered scan is the controlling source. The canonical source layer is closed.\n\n## Closed checkpoint\n\n- transcription scope: **PDF 4–90 / 87 pages**;\n- first pass / visual / historical-glyph / final visual: **87/87 / 87/87 / 87/87 / 87/87 COMPLETE-PASS**;\n- final-pass corrections: **0**;\n- unresolved glyph holds / open uncertainty markers: **0 / 0**;\n- scene derivatives: **72/72 COMPLETE-VERIFIED / boundary QA PASS**.\n\n## Downstream state\n\nThe reconciled immutable dialogue authority is **773 records / 38 exact source labels / QA PASS**, preserving all **744/744** legacy IDs and adding **29** append-only repaired IDs. Character/entity coverage is **773/773**; song/performance is **9/9** source-only QA PASS; English translation is verified through archive scene 5. Canonical Tamil remains unchanged.\n\n**Next:** {NEXT}\n''',encoding='utf-8')

p=W/'scenes'/'README.md'; s=p.read_text(encoding='utf-8')
s=re.sub(r'## Downstream gate\n\n.*\Z',f'''## Downstream gate\n\nScene-text derivatives remain **COMPLETE-VERIFIED**. The reconciled dialogue authority is **773 records / 38 labels / QA PASS**; character/entity coverage is **32 entities / 38/38 labels / 773/773 records / QA PASS**; song/performance is **9/9 source-visible occurrences / QA PASS**; English translation is verified through archive scene 5.\n\n**Next:** {NEXT}\n''',s,flags=re.S)
p.write_text(s,encoding='utf-8')

# Work mapping: update only current gate summaries; historical 744 legacy statements elsewhere remain intact.
p=W/'mapping.md'; s=p.read_text(encoding='utf-8')
s=s.replace('- immutable dialogue records: **744 / COMPLETE-VERIFIED / QA PASS**;', '- immutable dialogue records: **773 / COMPLETE-VERIFIED-RECONCILED / QA PASS**;')
s=s.replace('- immutable dialogue records mapped: **744/744**;', '- immutable dialogue records mapped: **773/773**;')
s=re.sub(r'## Exact next activity\n\n\*\*.*?\*\*\s*\Z',f'## Exact next activity\n\n**{NEXT}**\n',s,flags=re.S)
p.write_text(s,encoding='utf-8')

# Work metadata: keep source identity and mature gate fields, update current status and translation checkpoint.
p=W/'metadata.yaml'; s=p.read_text(encoding='utf-8')
s=s.replace('  dialogue_index: complete-verified\n','  dialogue_index: complete-verified-reconciled\n')
s=s.replace('  dialogue_records: 744\n','  dialogue_records: 773\n')
s=s.replace('  character_dialogue_record_coverage: 744/744\n','  character_dialogue_record_coverage: 773/773\n')
s=s.replace('  english_translation: ready-next\n','''  english_translation: verified-through-scene-005\n  english_translation_index_path: works/vandikkaran-magan/translations/index.json\n  english_translation_verified_scenes: 5\n  english_translation_units: 88\n  english_translation_dialogue_units: 67\n  english_translation_stage_direction_units: 21\n  english_translation_immutable_dialogue_links: 65\n  english_translation_source_unlabelled_spoken_units: 2\n  english_translation_latest_batch_qa_path: works/vandikkaran-magan/translations/batch-002-005-qa.json\n''')
s=re.sub(r'^next_action: .*$', 'next_action: '+json.dumps(NEXT,ensure_ascii=False), s, flags=re.M)
p.write_text(s,encoding='utf-8')

# Work-local durable summaries.
(W/'README.md').write_text(f'''# வண்டிக்காரன் மகன்\n\nSource-led archival workspace for the 1978 first-edition dialogue/screenplay booklet **`வண்டிக்காரன் மகன்`**.\n\n## Source authority\n\nControlling source: `TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` — **90 PDF pages / 26,391,039 bytes / SHA-256 `03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253`**. The image-only scan is canonical authority.\n\n## Current verified state\n\n- canonical Tamil: **87/87 COMPLETE-VERIFIED / 0 unresolved**;\n- scene derivatives: **72/72 COMPLETE-VERIFIED / boundary QA PASS**;\n- reconciled immutable dialogue authority: **773 records / 38 exact labels / QA PASS** — **744/744 legacy IDs preserved + 29 append-only repairs**;\n- character/entity index: **32 entities — 15 characters / 14 roles / 3 collectives / 38/38 labels / 773/773 records / QA PASS**;\n- song/performance layer: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS** — 6 bounded Tamil bodies + 3 cue-only;\n- item-level lyric authorship: **0 source-attributed / 6 unresolved**; PDF 88 `பாடல்கள்: கவிஞர் வாலி` remains film-level metadata only;\n- English translation: **5/72 scenes VERIFIED / QA PASS — 88 units / 65 immutable dialogue links / 2 source-unlabelled spoken units / 0 inferred speakers**;\n- reader/export / Reading Room: **BLOCKED pending English closure**.\n\n## Exact next activity\n\n> **{NEXT}**\n''',encoding='utf-8')

(W/'PROJECT_HANDOVER.md').write_text(f'''# வண்டிக்காரன் மகன் — Project Handover\n\nRepository: `pugazg/kalaignar-cinema-works`  \nBranch: `main`  \nWork: `works/vandikkaran-magan/`\n\n**LIVE MAIN IS AUTHORITATIVE.**\n\n## Controlling source\n\n`TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` — **90 PDF pages / 26,391,039 bytes / SHA-256 `03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253` / first edition 1978 / image-only**.\n\n## Durable closed state\n\n- canonical source: **87/87 COMPLETE-VERIFIED / 0 uncertainties**;\n- scenes: **72/72 COMPLETE-VERIFIED / boundary QA PASS — 82/82 screenplay pages / 0 gaps / 0 overlaps**;\n- dialogue authority: **773 / 38 exact labels / COMPLETE-VERIFIED-RECONCILED / QA PASS**; legacy IDs **744/744 preserved**, append-only repairs **29**, action-only exclusions **2**;\n- character/entity: **32 entities / 38/38 labels / 773/773 dialogue records / QA PASS**;\n- song/performance: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS**; 6 bounded bodies / 3 cue-only / 0 source-attributed + 6 unresolved item-level lyric authorships;\n- English scene 1 pilot: **PASS — 40 units / 31 immutable links / 1 source-unlabelled speech**;\n- English post-pilot batch scenes 2–5: **PASS — 48 units / 34 immutable links / 1 source-unlabelled speech**;\n- cumulative English: **5/72 scenes / 88 units / 65 immutable links / 2 source-unlabelled spoken units / 0 inferred speakers**;\n- reader/export and Reading Room: **BLOCKED pending English closure**.\n\nKey durable commits: dialogue reconciliation `e228798a72c6f9ee90f45b36eec5171e6ab549c0`; scene-1 English pilot `1c2c4087ca5ee93572c0b19206e747d7caecb178`; scenes 2–5 English batch `6391e9fa125b5f6aacb031a0a4b18ae28a13e2a3`.\n\nDo not reopen or rewrite closed Tamil, scene, dialogue, character or song layers without new direct contradictory source evidence. Historical 744 counts refer only to the preserved pre-reconciliation ID set.\n\n## Exact next activity\n\n> **{NEXT}**\n''',encoding='utf-8')

(W/'NEXT_CHAT_PROMPT.md').write_text(f'''# Next Chat Prompt — வண்டிக்காரன் மகன் / English scenes 6–10\n\nContinue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/vandikkaran-magan/`. **LIVE MAIN IS AUTHORITATIVE.**\n\n## Controlling source\n\n`TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` — 90 pages, 26,391,039 bytes, SHA-256 `03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253`, first edition 1978, image-only.\n\n## Durable state\n\n- canonical Tamil: **87/87 COMPLETE-VERIFIED / 0 uncertainties**;\n- scenes: **72/72 COMPLETE-VERIFIED / boundary QA PASS**;\n- reconciled immutable dialogues: **773 / 38 exact labels / QA PASS** — 744 legacy IDs preserved + 29 append-only repairs;\n- characters/entities: **32 / 38/38 labels / 773/773 records / QA PASS**;\n- song/performance: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS**;\n- English translation: **5/72 scenes VERIFIED / QA PASS — 88 units / 65 immutable dialogue links / 2 source-unlabelled spoken units**;\n- verified archive scene ordinals: **1–5**; source scene IDs: `1`, `2`, `3`, `4`, `4-எ`;\n- latest English batch QA: `translations/batch-002-005-qa.json` — **PASS**.\n\nDo not reopen or rewrite closed canonical Tamil, scenes, reconciled immutable dialogue records, character/entity mappings, or song/performance records without new direct contradictory source evidence.\n\n## Translation rules\n\nFollow `docs/CINEMA_WORKS_PROCESSING_GUIDE.md` Phase 13. Translate only verified source units. Preserve source order, PDF/printed provenance, exact Tamil speaker labels as metadata and immutable dialogue-ID linkage. Source-unlabelled speech remains unassigned. Keep stage directions, written text, songs/performance cues and source-unlabelled speech structurally distinct. Do not invent speakers, missing lyrics, authorship, or synthetic scene-end prose.\n\n## Exact next activity\n\n> **{NEXT}**\n''',encoding='utf-8')

# Registry entry.
p=ROOT/'data'/'works.json'; arr=json.loads(p.read_text(encoding='utf-8'))
e=next(v for v in arr if v.get('id')=='vandikkaran-magan'); d=e['structured_derivatives']
d['dialogue_index']='complete-verified-reconciled'; d['dialogue_records']=773; d['character_dialogue_record_coverage']='773/773'
d['english_translation']='verified'; d['translation_index_path']='works/vandikkaran-magan/translations/index.json'; d['translation_scenes_verified']=5
d['translation_units']=88; d['translation_verified_units']=88; d['translation_review_units']=0; d['translation_draft_units']=0
d['translation_unit_kind_counts']={'dialogue':67,'stage_direction':21}; d['translation_dialogue_source_records_linked']=65
d['translation_source_unlabelled_spoken_units']=2; d['translation_cross_page_units']=0; d['translation_song_occurrence_links']=0
d['next_structured_derivative']='english-translation-continue'; e['next_action']=NEXT
p.write_text(json.dumps(arr,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# Root README current work block.
p=ROOT/'README.md'; s=p.read_text(encoding='utf-8')
block=f'''## வண்டிக்காரன் மகன் status\n\n`TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` is the current active cinema-work source.\n\n- canonical Tamil: **87/87 COMPLETE-VERIFIED / 0 open uncertainties**;\n- scenes: **72/72 COMPLETE-VERIFIED / boundary QA PASS**;\n- reconciled immutable dialogues: **773 / 38 exact labels / QA PASS** — **744/744 legacy IDs preserved + 29 append-only repairs**;\n- character/entity index: **32 entities / 38/38 labels / 773/773 records / QA PASS**;\n- song/performance gate: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS**;\n- English translation: **5/72 scenes VERIFIED / QA PASS — 88 units / 65 immutable dialogue links / 2 source-unlabelled spoken units**;\n- reader/export and Reading Room: **gated pending English closure**.\n\n**Next:** {NEXT}\n\n'''
s,n=re.subn(r'## வண்டிக்காரன் மகன் status\n.*?(?=## நாம் status)',block,s,flags=re.S); assert n==1,n
p.write_text(s,encoding='utf-8')

# Master handover: update only Vandikkaran current line and current-active sentence.
p=ROOT/'docs'/'HANDOVER_KALAIGNAR_CINEMA_WORKS.md'; s=p.read_text(encoding='utf-8')
s,n=re.subn(r'^- \*\*Vandikkaran Magan / வண்டிக்காரன் மகன்\*\* — .*$', '- **Vandikkaran Magan / வண்டிக்காரன் மகன்** — canonical Tamil **87/87 COMPLETE-VERIFIED**; scenes **72/72 / boundary QA PASS**; reconciled dialogues **773 / 38 labels / QA PASS**; characters **32 / 38/38 / 773/773 / QA PASS**; song/performance **9/9 source-only QA PASS**; English **5/72 verified / 88 units / 65 immutable dialogue links / 2 source-unlabelled spoken units**.', s, count=1, flags=re.M); assert n==1,n
s,n=re.subn(r'Ammayappan and Naam remain closed at their recorded checkpoints\. \*\*The current active production work is வண்டிக்காரன் மகன்:.*?\*\*', 'Ammayappan and Naam remain closed at their recorded checkpoints. **The current active production work is வண்டிக்காரன் மகன்: source/Tamil, scenes, reconciled 773-dialogue authority, character/entity and 9-record song/performance layers are closed; English translation is verified through archive scene 5 and continues with scenes 6–10.**', s, count=1); assert n==1,n
p.write_text(s,encoding='utf-8')

# Status consistency audit: current result, matrix row, Vandikkaran block and conclusion.
p=ROOT/'docs'/'STATUS_CONSISTENCY_AUDIT.md'; s=p.read_text(encoding='utf-8')
s,n=re.subn(r'\*\*PASS for the current repository-wide checkpoint\.\*\* Vandikkaran Magan.*?English translation is READY-NEXT\.', '**PASS for the current repository-wide checkpoint.** Vandikkaran Magan is closed through reconciled dialogue/character/song layers and English translation is now **verified through archive scene 5**: **5/72 scenes / 88 units / 65 immutable dialogue links / 2 source-unlabelled spoken units**. The dialogue authority is **773 records / 38 labels**, preserving 744 legacy IDs and adding 29 append-only repairs.', s, count=1, flags=re.S); assert n==1,n
s,n=re.subn(r'^\| Vandikkaran Magan / வண்டிக்காரன் மகன் \|.*$', '| Vandikkaran Magan / வண்டிக்காரன் மகன் | **87/87 canonical source pages complete-verified; 0 unresolved** | **72/72 scenes; 773 reconciled dialogues / 38 labels; 32 entities; song/performance 9/9 QA PASS** | **5/72 verified / 88 units / 65 immutable links / 2 source-unlabelled** | not-started |', s, count=1, flags=re.M); assert n==1,n
cp=f'''## Vandikkaran Magan current checkpoint\n\n- canonical Tamil / visual / historical-glyph / final visual: **87/87 / 87/87 / 87/87 / 87/87 COMPLETE-PASS**;\n- scene derivatives: **72/72 COMPLETE-VERIFIED / boundary QA PASS**;\n- immutable dialogue authority: **773 / 38 exact labels / COMPLETE-VERIFIED-RECONCILED / QA PASS** — 744 legacy IDs preserved + 29 append-only repairs;\n- character/entity index: **32 entities / 38/38 labels / 773/773 records / QA PASS**;\n- song/performance layer: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS**;\n- English translation: **5/72 scenes VERIFIED / QA PASS — 88 units / 65 immutable dialogue links / 2 source-unlabelled spoken units / 0 inferred speakers**;\n- latest batch: archive scene ordinals **2–5** / source IDs `2`, `3`, `4`, `4-எ` — **48 units / 34 immutable links / QA PASS**.\n\n**Next production phase:** {NEXT}\n\n'''
s,n=re.subn(r'## Vandikkaran Magan current checkpoint\n.*?(?=## Naam current checkpoint)',cp,s,flags=re.S); assert n==1,n
s,n=re.subn(r'Vandikkaran Magan is the active production work\. Its canonical Tamil/source gates and \*\*72/72 scene derivatives remain COMPLETE-VERIFIED\*\*; the immutable dialogue index is now \*\*COMPLETE-VERIFIED — 744 records / 38 exact labels / QA PASS\*\*\. \*\*Next: bounded English-translation pilot from source scene 1\.\*\*', 'Vandikkaran Magan is the active production work. Canonical Tamil and all 72 scene derivatives remain closed; the reconciled dialogue authority is **773 records / 38 exact labels / QA PASS**, character and song/performance layers are closed, and English translation is **5/72 scenes / 88 units / QA PASS**. **Next: archive scene ordinals 6–10.**', s, count=1); assert n==1,n
p.write_text(s,encoding='utf-8')

# Assertions for active state; historical pre-reconciliation files/scripts may legitimately retain 744.
assert json.loads((W/'characters'/'index.json').read_text(encoding='utf-8'))['dialogue_records_source']==773
assert json.loads((W/'notes'/'character-index-qa.json').read_text(encoding='utf-8'))['dialogue_records_expected']==773
assert json.loads((W/'translations'/'index.json').read_text(encoding='utf-8'))['verified_scenes']==5
assert 'English translation: **5/72 scenes VERIFIED' in (W/'README.md').read_text(encoding='utf-8')
assert 'archive scene ordinals 6–10' in (W/'NEXT_CHAT_PROMPT.md').read_text(encoding='utf-8')
print(json.dumps({'status':'PASS','dialogues':773,'legacy_ids':744,'append_only':29,'characters':'773/773','english_scenes':'5/72','translation_units':88,'immutable_links':65,'next':'scenes 6-10'},ensure_ascii=False))
