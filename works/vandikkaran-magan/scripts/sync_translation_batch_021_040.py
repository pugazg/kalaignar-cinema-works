#!/usr/bin/env python3
from pathlib import Path
import json, re

W = Path(__file__).resolve().parents[1]
ROOT = W.parents[1]
T = W / 'translations'
N = W / 'notes'
NEXT = (
    'Translate and verify archive scene ordinals 41–60 as the next 20-scene English batch. '
    'Preserve source order and exact Tamil label/provenance metadata; link reconciled immutable dialogue IDs exactly once; '
    'keep source-unlabelled speech unassigned; link only verified song/performance occurrences; preserve unresolved item-level '
    'authorship as unresolved; and do not modify closed Tamil, scene, dialogue-record, character-mapping or song-record authorities.'
)

idx = json.loads((T/'index.json').read_text(encoding='utf-8'))
qa = json.loads((T/'batch-021-040-qa.json').read_text(encoding='utf-8'))
assert idx['status'] == 'verified-through-scene-040'
assert idx['verified_scenes'] == 40 and idx['verified_scene_ordinals'] == list(range(1,41))
assert idx['translation_units'] == 740
assert idx['immutable_dialogue_records_linked'] == 512
assert idx['source_unlabelled_spoken_units'] == 13
assert idx['performance_occurrence_links'] == 4
assert idx['batch_size_scenes'] == 20
assert qa['status'] == 'PASS' and qa['verified_scenes'] == 20
assert qa['immutable_dialogue_records_linked'] == 261
assert qa['source_unlabelled_spoken_units'] == 9
assert qa['unique_performance_occurrence_links'] == 2

all_units = idx['translation_units']
all_counts = idx['unit_kind_counts']
all_links = idx['immutable_dialogue_records_linked']
all_unlabelled = idx['source_unlabelled_spoken_units']
all_perf_ids = idx['performance_occurrence_ids_linked']
new_units = qa['verified_units']

# Active control pointers only; immutable record files are never touched.
def update_json_pointer(rel, key, value, extra=None):
    p = W / rel
    obj = json.loads(p.read_text(encoding='utf-8'))
    obj[key] = value
    if extra:
        obj.update(extra)
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

update_json_pointer('dialogues/index.json','next_action',NEXT)
update_json_pointer('characters/index.json','next_activity',NEXT)
update_json_pointer('songs/index.json','next_activity',NEXT, {'english_translation_gate':'in-progress-verified-through-scene-040'})
update_json_pointer('notes/character-index-qa.json','next_activity',NEXT)
update_json_pointer('notes/song-performance-qa.json','next_activity',NEXT)
if (N/'dialogue-index-qa.json').exists():
    dq = json.loads((N/'dialogue-index-qa.json').read_text(encoding='utf-8'))
    if 'next_activity' in dq: dq['next_activity'] = NEXT
    if 'next_action' in dq: dq['next_action'] = NEXT
    (N/'dialogue-index-qa.json').write_text(json.dumps(dq,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# Work metadata: replace only the active English block.
mp = W / 'metadata.yaml'
m = mp.read_text(encoding='utf-8')
english_block = f'''  english_translation: verified-through-scene-040
  english_translation_index_path: works/vandikkaran-magan/translations/index.json
  english_translation_verified_scenes: 40
  english_translation_batch_size_scenes: 20
  english_translation_units: {all_units}
  english_translation_unit_kind_counts: {','.join(f'{k}={v}' for k,v in sorted(all_counts.items()))}
  english_translation_immutable_dialogue_links: {all_links}
  english_translation_source_unlabelled_spoken_units: {all_unlabelled}
  english_translation_performance_occurrence_links: {len(all_perf_ids)}
  english_translation_latest_batch_qa_path: works/vandikkaran-magan/translations/batch-021-040-qa.json
  english_translation_latest_batch_review_path: works/vandikkaran-magan/translations/BATCH_021_040_REVIEW.md
'''
m, nsub = re.subn(r'  english_translation:.*?\n  reader_export:', english_block + '  reader_export:', m, count=1, flags=re.S)
assert nsub == 1
m, nsub = re.subn(r'^next_action: .*$', 'next_action: ' + json.dumps(NEXT, ensure_ascii=False), m, count=1, flags=re.M)
assert nsub == 1
mp.write_text(m, encoding='utf-8')

# Work-local current-status mirrors.
(W/'README.md').write_text(f'''# வண்டிக்காரன் மகன்

Source-led archival workspace for the 1978 first-edition dialogue/screenplay booklet **`வண்டிக்காரன் மகன்`**.

## Source authority

Controlling source: `TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` — **90 PDF pages / 26,391,039 bytes / SHA-256 `03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253`**. The image-only scan is canonical authority.

## Current verified state

- canonical Tamil: **87/87 COMPLETE-VERIFIED / 0 unresolved**;
- scene derivatives: **72/72 COMPLETE-VERIFIED / boundary QA PASS**;
- reconciled immutable dialogue authority: **773 records / 38 exact labels / QA PASS** — **744/744 legacy IDs preserved + 29 append-only repairs**;
- character/entity index: **32 entities — 15 characters / 14 roles / 3 collectives / 38/38 labels / 773/773 records / QA PASS**;
- song/performance layer: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS** — 6 bounded Tamil bodies + 3 cue-only;
- item-level lyric authorship: **0 source-attributed / 6 unresolved**; PDF 88 `பாடல்கள்: கவிஞர் வாலி` remains film-level metadata only;
- English translation: **40/72 scenes VERIFIED / QA PASS — {all_units} units / {all_links} immutable dialogue links / {all_unlabelled} source-unlabelled spoken units / {len(all_perf_ids)} verified performance occurrences linked / 0 inferred speakers**;
- latest English batch: **scenes 21–40 / PASS — {new_units} units / 261 immutable dialogue links / 9 source-unlabelled spoken units / 2 verified performance occurrences linked**;
- English production cadence: **20 scenes per iteration**;
- reader/export / Reading Room: **BLOCKED pending English closure**.

## Exact next activity

> **{NEXT}**
''', encoding='utf-8')

(W/'PROJECT_HANDOVER.md').write_text(f'''# வண்டிக்காரன் மகன் — Project Handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Work: `works/vandikkaran-magan/`

**LIVE MAIN IS AUTHORITATIVE.**

## Controlling source

`TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` — **90 PDF pages / 26,391,039 bytes / SHA-256 `03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253` / first edition 1978 / image-only**.

## Durable closed state

- canonical source: **87/87 COMPLETE-VERIFIED / 0 uncertainties**;
- scenes: **72/72 COMPLETE-VERIFIED / boundary QA PASS — 82/82 screenplay pages / 0 gaps / 0 overlaps**;
- dialogue authority: **773 / 38 exact labels / COMPLETE-VERIFIED-RECONCILED / QA PASS**; legacy IDs **744/744 preserved**, append-only repairs **29**, action-only exclusions **2**;
- character/entity: **32 entities / 38/38 labels / 773/773 dialogue records / QA PASS**;
- song/performance: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS**; 6 bounded bodies / 3 cue-only / 0 source-attributed + 6 unresolved item-level lyric authorships;
- English scene 1 pilot: **PASS — 40 units / 31 immutable links / 1 source-unlabelled speech**;
- English scenes 2–5: **PASS — 48 units / 34 immutable links / 1 source-unlabelled speech**;
- English scenes 6–20: **PASS — 267 units / 186 immutable links / 2 source-unlabelled spoken units / 2 verified performance occurrences linked**;
- English scenes 21–40: **PASS — {new_units} units / 261 immutable links / 9 source-unlabelled spoken units / 2 verified performance occurrences linked**;
- cumulative English: **40/72 scenes / {all_units} units / {all_links} immutable links / {all_unlabelled} source-unlabelled spoken units / {len(all_perf_ids)} unique verified performance occurrence links / 0 inferred speakers**;
- English batch policy: **20 scenes per iteration**;
- reader/export and Reading Room: **BLOCKED pending English closure**.

Do not reopen or rewrite closed Tamil, scene, immutable dialogue-record, character-mapping or song-record authorities without new direct contradictory source evidence. Historical 744 counts refer only to the preserved pre-reconciliation ID set.

## Exact next activity

> **{NEXT}**
''', encoding='utf-8')

(W/'NEXT_CHAT_PROMPT.md').write_text(f'''# Next Chat Prompt — வண்டிக்காரன் மகன் / English scenes 41–60

Continue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/vandikkaran-magan/`. **LIVE MAIN IS AUTHORITATIVE.**

## Controlling source

`TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` — 90 pages, 26,391,039 bytes, SHA-256 `03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253`, first edition 1978, image-only.

## Durable state

- canonical Tamil: **87/87 COMPLETE-VERIFIED / 0 uncertainties**;
- scenes: **72/72 COMPLETE-VERIFIED / boundary QA PASS**;
- reconciled immutable dialogues: **773 / 38 exact labels / QA PASS** — 744 legacy IDs preserved + 29 append-only repairs;
- characters/entities: **32 / 38/38 labels / 773/773 records / QA PASS**;
- song/performance: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS**;
- English translation: **40/72 scenes VERIFIED / QA PASS — {all_units} units / {all_links} immutable dialogue links / {all_unlabelled} source-unlabelled spoken units / {len(all_perf_ids)} verified performance occurrences linked**;
- verified archive scene ordinals: **1–40**;
- latest English batch QA: `translations/batch-021-040-qa.json` — **PASS / 20 scenes / {new_units} units / 261 of 261 immutable dialogue links**;
- production batch size: **20 scenes per iteration**.

Do not reopen or rewrite closed canonical Tamil, scene derivatives, reconciled immutable dialogue records, character/entity mappings, or song/performance records without new direct contradictory source evidence.

## Translation rules

Follow `docs/CINEMA_WORKS_PROCESSING_GUIDE.md` Phase 13 and `docs/SONG_TRANSLATION_GUIDE.md` for verified performance material. Translate only verified source units. Preserve source order, PDF/printed provenance, exact Tamil speaker labels as metadata and immutable dialogue-ID linkage. Source-unlabelled speech remains unassigned. Keep stage directions, written text, songs/performance cues and source-unlabelled speech structurally distinct. Do not invent speakers, missing lyrics, item-level authorship, or synthetic scene-end prose. Preserve a cross-page source unit as one translation unit with all source pages in its provenance.

## Exact next activity

> **{NEXT}**
''', encoding='utf-8')

(W/'transcription'/'README.md').write_text(f'''# வண்டிக்காரன் மகன் — canonical Tamil transcription

The rendered scan is the controlling source. The canonical source layer is closed.

## Closed checkpoint

- transcription scope: **PDF 4–90 / 87 pages**;
- first pass / visual / historical-glyph / final visual: **87/87 / 87/87 / 87/87 / 87/87 COMPLETE-PASS**;
- final-pass corrections: **0**;
- unresolved glyph holds / open uncertainty markers: **0 / 0**;
- scene derivatives: **72/72 COMPLETE-VERIFIED / boundary QA PASS**.

## Downstream state

The reconciled immutable dialogue authority is **773 records / 38 exact source labels / QA PASS**, preserving all **744/744** legacy IDs and adding **29** append-only repaired IDs. Character/entity coverage is **773/773**; song/performance is **9/9** source-only QA PASS; English translation is verified through archive scene **40/72** at **{all_units} units / {all_links} immutable dialogue links**. Canonical Tamil remains unchanged.

**Production cadence:** English translation proceeds in **20-scene iterations**.

**Next:** {NEXT}
''', encoding='utf-8')

# Tail replacements in active layer READMEs/mapping.
def replace_tail(rel, heading, body):
    p = W / rel
    s = p.read_text(encoding='utf-8')
    pattern = re.escape(heading) + r'.*$'
    s, n = re.subn(pattern, heading + '\n\n' + body.strip() + '\n', s, count=1, flags=re.S)
    if n == 0:
        s = s.rstrip() + '\n\n' + heading + '\n\n' + body.strip() + '\n'
    p.write_text(s, encoding='utf-8')

replace_tail('dialogues/README.md','## Next',f'English translation is verified through archive scene **40/72**. {NEXT}')
replace_tail('characters/README.md','## Next',f'English translation is verified through archive scene **40/72**. {NEXT}')
replace_tail('songs/README.md','## Next',f'English translation is verified through archive scene **40/72**. Item-level authorship states remain unchanged. {NEXT}')
replace_tail('scenes/README.md','## Downstream gate',f'''Scene-text derivatives remain **COMPLETE-VERIFIED**. Downstream dialogue authority is **773 records / COMPLETE-VERIFIED-RECONCILED / QA PASS**; character/entity coverage is **773/773 / QA PASS**; song/performance is **9/9 source-only QA PASS**; English translation is **40/72 VERIFIED / QA PASS** at **{all_units} units / {all_links} immutable dialogue links**.

**Next:** {NEXT}''')
replace_tail('mapping.md','## Exact next activity',f'''English translation is now **40/72 VERIFIED / QA PASS** with a **20-scene iteration** cadence.

**{NEXT}**''')

# Source transcription index: control metadata only.
tip = W/'transcription'/'index.json'
ti = json.loads(tip.read_text(encoding='utf-8'))
ti['dialogue_index'] = 'complete-verified-reconciled'
ti['next_action'] = NEXT
tip.write_text(json.dumps(ti,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')

# data/works.json.
data_path = ROOT / 'data' / 'works.json'
data = json.loads(data_path.read_text(encoding='utf-8'))
entry = next(x for x in data if x['id'] == 'vandikkaran-magan')
sd = entry['structured_derivatives']
sd.update({
    'dialogue_index':'complete-verified-reconciled','dialogue_records':773,
    'character_dialogue_record_coverage':'773/773',
    'english_translation':'verified-through-scene-040','translation_index_path':'works/vandikkaran-magan/translations/index.json',
    'translation_scenes_verified':40,'translation_units':all_units,'translation_verified_units':all_units,
    'translation_unit_kind_counts':dict(sorted(all_counts.items())),
    'translation_dialogue_source_records_linked':all_links,
    'translation_source_unlabelled_spoken_units':all_unlabelled,
    'translation_performance_occurrence_links':len(all_perf_ids),
    'translation_batch_size_scenes':20,
    'translation_latest_batch_qa_path':'works/vandikkaran-magan/translations/batch-021-040-qa.json',
    'next_structured_derivative':'english-translation-scenes-041-060'
})
entry['next_action'] = NEXT
data_path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# Root README: replace only the active Vandikkaran Magan section.
root = ROOT / 'README.md'
s = root.read_text(encoding='utf-8')
section = f'''## வண்டிக்காரன் மகன் status

`TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` is the current active cinema-work source.

- canonical Tamil: **87/87 COMPLETE-VERIFIED / 0 open uncertainties**;
- scenes: **72/72 COMPLETE-VERIFIED / boundary QA PASS**;
- reconciled immutable dialogues: **773 / 38 exact labels / COMPLETE-VERIFIED-RECONCILED / QA PASS**;
- character/entity index: **32 entities / 38/38 labels / 773/773 records / COMPLETE-VERIFIED / QA PASS**;
- song/performance gate: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS**;
- item-level lyric authorship: **0 source-attributed / 6 unresolved**; PDF 88 `பாடல்கள்: கவிஞர் வாலி` remains film-level metadata only;
- English translation: **40/72 scenes VERIFIED / QA PASS — {all_units} units / {all_links} dialogue links / {all_unlabelled} source-unlabelled spoken units / {len(all_perf_ids)} unique performance occurrence links**;
- latest English batch: **21–40 / PASS — {new_units} units / 261 dialogue links**;
- English production cadence: **20 scenes per iteration**;
- reader/export and Reading Room: **gated downstream**.

**Next:** {NEXT}

'''
s, nsub = re.subn(r'## வண்டிக்காரன் மகன் status\n.*?(?=\n## நாம் status)', section.rstrip(), s, count=1, flags=re.S)
assert nsub == 1
root.write_text(s, encoding='utf-8')

# Master handover targeted current bullet/active-summary update.
hp = ROOT / 'docs' / 'HANDOVER_KALAIGNAR_CINEMA_WORKS.md'
h = hp.read_text(encoding='utf-8')
line = f'- **Vandikkaran Magan / வண்டிக்காரன் மகன்** — canonical Tamil **87/87 COMPLETE-VERIFIED**; scenes **72/72 / boundary QA PASS**; dialogues **773 / 38 labels / QA PASS-RECONCILED**; characters **32 / 38/38 / 773/773 / QA PASS**; song/performance **9/9 source-only QA PASS**; English **40/72 VERIFIED / {all_units} units / {all_links} dialogue links / {len(all_perf_ids)} performance occurrences**; production batches **20 scenes each**.'
h, nsub = re.subn(r'^- \*\*Vandikkaran Magan / வண்டிக்காரன் மகன்\*\* — .*$', line, h, count=1, flags=re.M)
assert nsub == 1
h, nsub2 = re.subn(
    r'Ammayappan and Naam remain closed at their recorded checkpoints\. \*\*The current active production work is வண்டிக்காரன் மகன்:.*?\*\*',
    f'Ammayappan and Naam remain closed at their recorded checkpoints. **The current active production work is வண்டிக்காரன் மகன்: English translation is verified through archive scene 40/72 at {all_units} units / {all_links} immutable dialogue links, with 20-scene production batches; source/Tamil, scene, reconciled dialogue, character and song/performance authorities remain closed.**', h, count=1)
assert nsub2 == 1
hp.write_text(h, encoding='utf-8')

# Repository status audit: result, row, dedicated checkpoint, conclusion.
sp = ROOT / 'docs' / 'STATUS_CONSISTENCY_AUDIT.md'
s = sp.read_text(encoding='utf-8')
s, n0 = re.subn(r'\*\*PASS for the current repository-wide checkpoint\.\*\* Vandikkaran Magan.*?\n\n',
           f'**PASS for the current repository-wide checkpoint.** Vandikkaran Magan English translation is now **40/72 scenes VERIFIED / QA PASS** at **{all_units} units / {all_links} immutable dialogue links / {all_unlabelled} source-unlabelled spoken units / {len(all_perf_ids)} unique verified performance occurrence links**. Translation production proceeds in **20-scene iterations**. All closed Tamil/scene/dialogue/character/song authorities remain unchanged.\n\n', s, count=1, flags=re.S)
assert n0 == 1
row = f'| Vandikkaran Magan / வண்டிக்காரன் மகன் | **87/87 canonical source pages complete-verified; 0 unresolved** | **72/72 scenes; 773 dialogues / 38 labels; 32 entities; song/performance 9/9 QA PASS** | **40/72 VERIFIED / {all_units} units / {all_links} dialogue links / {len(all_perf_ids)} performance occurrences** | not-started |'
s, nsub = re.subn(r'^\| Vandikkaran Magan / வண்டிக்காரன் மகன் \|.*$', row, s, count=1, flags=re.M)
assert nsub == 1
block = f'''## Vandikkaran Magan current checkpoint

- canonical Tamil / visual / historical-glyph / final visual: **87/87 / 87/87 / 87/87 / 87/87 COMPLETE-PASS**;
- scene derivatives: **72/72 COMPLETE-VERIFIED / boundary QA PASS**;
- reconciled immutable dialogue index: **773 / 38 exact labels / COMPLETE-VERIFIED-RECONCILED / QA PASS**;
- character/entity index: **32 entities / 38/38 labels / 773/773 records / COMPLETE-VERIFIED / QA PASS**;
- song/performance layer: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS**;
- item-level source-attributed lyricists: **0**; unresolved item-level lyric authorships: **6**;
- English translation: **40/72 VERIFIED / QA PASS — {all_units} units / {all_links} immutable dialogue links / {all_unlabelled} source-unlabelled spoken units / {len(all_perf_ids)} unique performance occurrence links**;
- latest English batch: **21–40 / PASS — {new_units} units / 261 immutable dialogue links / 9 source-unlabelled spoken units**;
- English batch size: **20 scenes per iteration**;
- upstream canonical Tamil / scene / dialogue-record / character-mapping / song-record mutation from this translation batch: **0**.

**Next production phase:** {NEXT}

'''
s, nsub = re.subn(r'## Vandikkaran Magan current checkpoint\n.*?(?=## Naam current checkpoint)', block, s, count=1, flags=re.S)
assert nsub == 1
s, n3 = re.subn(r'Vandikkaran Magan is the active production work\..*?(?=\n\n<!-- Naam song gate)',
           f'Vandikkaran Magan is the active production work. Its source/Tamil, 72-scene, reconciled 773-dialogue, 32-entity and 9-occurrence song/performance authorities remain closed. English translation is **40/72 VERIFIED / QA PASS** at **{all_units} units / {all_links} immutable dialogue links**, using **20-scene iterations**. **Next: archive scene ordinals 41–60.**', s, count=1, flags=re.S)
assert n3 == 1
sp.write_text(s, encoding='utf-8')

# Final consistency gates.
assert '40/72 scenes VERIFIED' in (W/'README.md').read_text(encoding='utf-8')
assert '41–60' in (W/'NEXT_CHAT_PROMPT.md').read_text(encoding='utf-8')
assert '20 scenes per iteration' in (W/'NEXT_CHAT_PROMPT.md').read_text(encoding='utf-8')
assert json.loads((W/'songs'/'index.json').read_text(encoding='utf-8'))['english_translation_gate'] == 'in-progress-verified-through-scene-040'
assert next(x for x in json.loads(data_path.read_text(encoding='utf-8')) if x['id']=='vandikkaran-magan')['structured_derivatives']['translation_scenes_verified'] == 40
print(json.dumps({
    'status':'PASS','batch_scenes':'21-40','batch_size':20,'batch_units':new_units,'batch_dialogue_links':261,
    'cumulative_scenes':40,'cumulative_units':all_units,'cumulative_dialogue_links':all_links,
    'source_unlabelled_spoken_units':all_unlabelled,'performance_occurrence_links':len(all_perf_ids),
    'next':'41-60'
}, ensure_ascii=False))
