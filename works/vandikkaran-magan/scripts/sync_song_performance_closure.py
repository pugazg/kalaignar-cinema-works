#!/usr/bin/env python3
from pathlib import Path
import json, re

ROOT = Path(__file__).resolve().parents[3]
W = ROOT / 'works' / 'vandikkaran-magan'
BUILD_SHA = 'b1d197fdb2e850efbb4dff30801c2236e77924c1'
NEXT = ('Begin a bounded English-translation pilot from source scene 1 using only closed canonical Tamil plus verified '
        'scene/dialogue/character/song-performance derivatives. Preserve exact Tamil source labels and provenance, link immutable '
        'dialogue IDs without rewriting them, and keep song/performance authorship unresolved wherever the source gate is unresolved. '
        'Run pilot QA before scaling to later scenes.')

idx = json.loads((W/'songs'/'index.json').read_text(encoding='utf-8'))
qa = json.loads((W/'notes'/'song-performance-qa.json').read_text(encoding='utf-8'))
assert idx['status'] == 'complete-verified-source-only'
assert idx['mapped_source_visible_occurrences'] == 9
assert idx['full_or_clearly_bounded_tamil_derivatives'] == 6
assert idx['cue_only_non_lyric_records'] == 3
assert idx['source_attributed_authorship_records'] == 0
assert idx['unresolved_item_level_authorship_records'] == 6
assert idx['english_translation_gate'] == 'ready-next'
assert qa['status'] == 'PASS'

# metadata.yaml — current work registry.
p = W/'metadata.yaml'; s=p.read_text(encoding='utf-8')
s=s.replace('  song_credit_disposition: film-level-source-credit-item-level-occurrence-mapping-deferred',
            '  song_credit_disposition: film-level-source-credit-preserved-six-item-level-authorships-unresolved-no-inference')
s=s.replace('  song_performance_authorship_gate: ready-next\n  english_translation: blocked',
'''  song_performance_authorship_gate: complete-verified-source-only
  song_performance_index_path: works/vandikkaran-magan/songs/index.json
  song_performance_occurrences: 9
  song_performance_bounded_tamil_bodies: 6
  song_performance_cue_only_records: 3
  song_performance_source_attributed_authorship: 0
  song_performance_unresolved_item_level_authorship: 6
  song_performance_qa: PASS
  song_performance_qa_path: works/vandikkaran-magan/notes/song-performance-qa.json
  english_translation: ready-next''')
s=re.sub(r'next_action: ".*"\s*$', 'next_action: "'+NEXT+'"\n', s, flags=re.S)
p.write_text(s,encoding='utf-8')

# Work README — rewrite the current-status mirror compactly.
(W/'README.md').write_text(f'''# வண்டிக்காரன் மகன்

Source-led archival workspace for the 1978 first-edition dialogue/screenplay booklet **`வண்டிக்காரன் மகன்`**.

## Source authority

Controlling source: `TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` — **90 PDF pages / 26,391,039 bytes / SHA-256 `03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253`**. The image-only scan is canonical authority. Preserve source spelling, punctuation, labels, scene numbering, performance structures and historical glyph identity without silent modernization.

## Current verified state

- canonical Tamil source records: **87/87 COMPLETE-VERIFIED / 0 unresolved**;
- visual / historical-glyph / final-visual gates: **87/87 / 87/87 / 87/87 PASS**;
- source-visible scene headings / scene derivatives: **72/72 / 72/72 COMPLETE-VERIFIED**;
- boundary ownership: **PASS — PDF 6–87 represented once, 0 gaps / 0 overlaps / 0 duplicate ownership**;
- immutable dialogue index: **744 records / 38 exact source labels / COMPLETE-VERIFIED / QA PASS**;
- character/entity index: **32 entities — 15 named characters / 14 roles / 3 collectives / 38/38 labels / 744/744 dialogue records / QA PASS**;
- song/performance layer: **9/9 source-visible occurrences / COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS**;
- bounded Tamil lyric/performance bodies: **6**; cue-only non-lyric occurrences: **3**;
- item-level lyric authorship: **0 source-attributed / 6 unresolved-item-level**;
- PDF 88 film-level `பாடல்கள்: கவிஞர் வாலி` credit: **preserved as metadata, not promoted item-by-item**;
- English translation: **READY-NEXT**;
- reader/export / Reading Room: **BLOCKED pending English closure**.

See `songs/index.json`, `songs/inventory.json`, `songs/credits.json`, `notes/song-performance-cue-preflight.json`, and `notes/song-performance-qa.json`.

## Exact next activity

> **{NEXT}**
''',encoding='utf-8')

# Structural mapping — preserve closed mapping and replace only the downstream safeguard/next phase.
p=W/'mapping.md'; s=p.read_text(encoding='utf-8')
s=re.sub(r'## Song / performance safeguard\n.*?\n## Historical-glyph / source gates', '''## Song / performance derivative gate

- source-visible occurrences: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS**;
- full or clearly bounded Tamil bodies: **6** — source scenes `10`, `20`, `24-சி`, `36`, `48`, `53-சி`;
- cue-only / non-lyric performance records: **3** — source scenes `7`, `32`, `42-எ`;
- item-level source-attributed lyric authorship: **0**;
- unresolved item-level lyric authorship: **6**;
- PDF 88 `பாடல்கள்: கவிஞர் வாலி`: preserved as film-level metadata only, not promoted to item-level authorship;
- missing chant/lyric text reconstructed: **0**;
- canonical Tamil / scene / dialogue / character mappings changed by this layer: **0**.

## Historical-glyph / source gates''', s, flags=re.S)
s=re.sub(r'## Exact next activity\n\n\*\*.*?\*\*\s*$', '## Exact next activity\n\n**'+NEXT+'**\n', s, flags=re.S)
p.write_text(s,encoding='utf-8')

# Character README is a closed upstream mirror; only downstream state changes.
p=W/'characters'/'README.md'; s=p.read_text(encoding='utf-8')
s=re.sub(r'## Next\n\n.*?$', '''## Downstream state

Song/performance authorship is now **COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS — 9/9 occurrences, 6 bounded Tamil bodies, 3 cue-only records, 0 source-attributed and 6 unresolved item-level lyric authorships**. English translation is **READY-NEXT**. The character/entity mappings remain unchanged.
''', s, flags=re.S)
p.write_text(s,encoding='utf-8')

# Work handover — authoritative compact durable checkpoint.
(W/'PROJECT_HANDOVER.md').write_text(f'''# வண்டிக்காரன் மகன் — Project Handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Work: `works/vandikkaran-magan/`

**LIVE MAIN IS AUTHORITATIVE.**

## Controlling source

`TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` — **90 PDF pages / 26,391,039 bytes / SHA-256 `03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253` / first edition 1978 / image-only**.

## Durable closed state

- canonical source layer: **87/87 COMPLETE-VERIFIED — PDF 4–90 / 0 uncertainties**;
- scene headings / derivatives: **72/72 / 72/72 COMPLETE-VERIFIED**;
- scene boundary ownership: **PASS — 82/82 screenplay pages / 0 gaps / 0 overlaps / 0 duplicate ownership**;
- canonical/joined scene-body SHA-256: `84227c9855f3de942c8f1c240f9e6ddeee2d13f348fdda14b7712a81c4cfc19a`;
- immutable dialogue index: **744 records / 38 exact labels / COMPLETE-VERIFIED / QA PASS**;
- character/entity index: **32 entities / 15 characters / 14 roles / 3 collectives / 38/38 labels / 744/744 records / QA PASS**;
- song/performance inventory: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS**;
- bounded Tamil song/lyric bodies: **6** — scenes `10`, `20`, `24-சி`, `36`, `48`, `53-சி`;
- cue-only non-lyric performances: **3** — scenes `7`, `32`, `42-எ`;
- item-level source-attributed lyricists: **0**; unresolved item-level lyric authorships: **6**;
- broad PDF 88 lyricist credit: `பாடல்கள்: கவிஞர் வாலி` — **film-level metadata only; no item-level promotion**;
- missing lyrics/chant text reconstructed: **0**;
- song/performance build checkpoint: `{BUILD_SHA}`;
- English translation: **READY-NEXT**;
- reader/export / Reading Room: **BLOCKED**.

The three cue-only records preserve only what the source supplies: scene 7 mock-wedding music/mantra activity, scene 32 `கெட்டி மேளம்`, and scene `42-எ` `மந்திர ஒலி`. The six bounded bodies preserve exact source wording, lineation, cues and PDF/printed provenance. No canonical Tamil, scene text, immutable dialogue record or character/entity mapping was rewritten by song/performance construction.

## Exact next activity

> **{NEXT}**
''',encoding='utf-8')

# Next-chat prompt.
(W/'NEXT_CHAT_PROMPT.md').write_text(f'''# Next Chat Prompt — வண்டிக்காரன் மகன் / English translation pilot

Continue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/vandikkaran-magan/`. **LIVE MAIN IS AUTHORITATIVE.**

## Controlling source

`TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` — 90 pages, 26,391,039 bytes, SHA-256 `03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253`, first edition 1978, image-only. The attached/rendered scan remains canonical authority.

## Durable closed state

- canonical source: **87/87 COMPLETE-VERIFIED / 0 uncertainties**;
- scenes: **72/72 COMPLETE-VERIFIED / boundary QA PASS**;
- immutable dialogues: **744 / 38 exact labels / COMPLETE-VERIFIED / QA PASS**;
- characters/entities: **32 / 38/38 labels / 744/744 records / COMPLETE-VERIFIED / QA PASS**;
- song/performance occurrences: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS**;
- bounded Tamil bodies / cue-only records: **6 / 3**;
- item-level lyric authorship: **0 source-attributed / 6 unresolved-item-level**;
- PDF 88 `பாடல்கள்: கவிஞர் வாலி`: **film-level metadata only; do not convert to item-level attribution without new item-specific evidence**;
- English translation: **READY-NEXT**.

Do not reopen or rewrite closed canonical Tamil, scenes, immutable dialogue records, character/entity mappings, or song/performance records without new direct contradictory source evidence.

## Translation rules

Follow `docs/CINEMA_WORKS_PROCESSING_GUIDE.md` Phase 13. Translate only verified source units. Preserve source order, PDF/printed provenance, exact Tamil speaker labels as metadata and immutable dialogue-ID linkage. Keep stage directions, written text, songs/performance cues and source-unlabelled speech structurally distinct. Do not invent speakers, absent lyrics, authorship, or synthetic scene-end prose. A source unit crossing pages remains one translation unit with multi-page provenance.

## Exact next activity

> **{NEXT}**
''',encoding='utf-8')

# data/works.json — structured project registry.
p=ROOT/'data'/'works.json'; data=json.loads(p.read_text(encoding='utf-8'))
work=next(x for x in data if x.get('id')=='vandikkaran-magan')
sd=work.setdefault('structured_derivatives',{})
sd.update({
    'song_performance_authorship_gate':'complete-verified-source-only',
    'song_performance_index_path':'works/vandikkaran-magan/songs/index.json',
    'song_performance_occurrences':9,
    'song_performance_bounded_tamil_bodies':6,
    'song_performance_cue_only_records':3,
    'song_performance_source_attributed_authorship':0,
    'song_performance_unresolved_item_level_authorship':6,
    'song_performance_qa':'PASS',
    'song_performance_qa_path':'works/vandikkaran-magan/notes/song-performance-qa.json',
    'english_translation':'ready-next',
    'next_structured_derivative':'english-translation-pilot'
})
work['next_action']=NEXT
p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# Root README — replace only active Vandikkaran status section.
p=ROOT/'README.md'; s=p.read_text(encoding='utf-8')
section=f'''## வண்டிக்காரன் மகன் status

`TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` is the current active cinema-work source.

- canonical Tamil: **87/87 COMPLETE-VERIFIED / 0 open uncertainties**;
- scenes: **72/72 COMPLETE-VERIFIED / boundary QA PASS**;
- immutable dialogues: **744 / 38 exact labels / COMPLETE-VERIFIED / QA PASS**;
- character/entity index: **32 entities / 38/38 labels / 744/744 records / COMPLETE-VERIFIED / QA PASS**;
- song/performance gate: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS**;
- bounded Tamil bodies / cue-only records: **6 / 3**;
- item-level lyric authorship: **0 source-attributed / 6 unresolved**; PDF 88 `பாடல்கள்: கவிஞர் வாலி` remains film-level metadata only;
- English translation: **READY-NEXT**;
- reader/export and Reading Room: **gated downstream**.

**Next:** {NEXT}


'''
s,n=re.subn(r'## வண்டிக்காரன் மகன் status\n.*?(?=## நாம் status)',section,s,flags=re.S)
assert n==1
p.write_text(s,encoding='utf-8')

# Master handover — update high-level Vand bullet and active production sentence.
p=ROOT/'docs'/'HANDOVER_KALAIGNAR_CINEMA_WORKS.md'; s=p.read_text(encoding='utf-8')
s=re.sub(r'- \*\*Vandikkaran Magan / வண்டிக்காரன் மகன்\*\* — .*?\n',
'''- **Vandikkaran Magan / வண்டிக்காரன் மகன்** — canonical Tamil **87/87 COMPLETE-VERIFIED**; scenes **72/72 / boundary QA PASS**; dialogues **744 / 38 labels / QA PASS**; characters **32 / 38/38 / 744/744 / QA PASS**; song/performance gate **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / 6 bounded bodies / 3 cue-only / 0 source-attributed + 6 unresolved item-level authorships / QA PASS**; English translation **READY-NEXT**.\n''',s,count=1)
s=re.sub(r'Ammayappan and Naam remain closed at their recorded checkpoints\. \*\*The current active production work is வண்டிக்காரன் மகன்:.*?\*\*',
'''Ammayappan and Naam remain closed at their recorded checkpoints. **The current active production work is வண்டிக்காரன் மகன்: source/Tamil, scenes, dialogues, characters and the 9-record song/performance layer are closed with QA PASS; English translation is READY-NEXT.**''',s,count=1,flags=re.S)
# Repair any stale conclusion sentence for the active work.
s=s.replace('**Next: character/entity indexing from the immutable exact-label inventory.**', '**Next: bounded English-translation pilot from source scene 1.**')
p.write_text(s,encoding='utf-8')

# Status consistency audit — current summary, matrix row and active checkpoint.
p=ROOT/'docs'/'STATUS_CONSISTENCY_AUDIT.md'; s=p.read_text(encoding='utf-8')
s=re.sub(r'\*\*PASS for the current repository-wide checkpoint\.\*\*.*?\n\n',
'''**PASS for the current repository-wide checkpoint.** Vandikkaran Magan is now closed through the song/performance authorship gate: **9/9 source-visible occurrences / 6 bounded Tamil bodies / 3 cue-only records / QA PASS**, with **0 item-level source-attributed lyricists and 6 unresolved item-level lyric authorships**. The PDF 88 `பாடல்கள்: கவிஞர் வாலி` line remains film-level metadata and was not promoted item-by-item. English translation is READY-NEXT.\n\n''',s,count=1,flags=re.S)
s=re.sub(r'\| Vandikkaran Magan / வண்டிக்காரன் மகன் \|.*?\|\n',
'''| Vandikkaran Magan / வண்டிக்காரன் மகன் | **87/87 canonical source pages complete-verified; 0 unresolved** | **72/72 scenes; 744 dialogues / 38 labels; 32 entities; song/performance 9/9 QA PASS** | **READY-NEXT** | not-started |\n''',s,count=1)
checkpoint=f'''## Vandikkaran Magan current checkpoint

- canonical Tamil / visual / historical-glyph / final visual: **87/87 / 87/87 / 87/87 / 87/87 COMPLETE-PASS**;
- scene derivatives: **72/72 COMPLETE-VERIFIED / boundary QA PASS**;
- immutable dialogue index: **744 / 38 exact labels / COMPLETE-VERIFIED / QA PASS**;
- character/entity index: **32 entities / 38/38 labels / 744/744 records / COMPLETE-VERIFIED / QA PASS**;
- song/performance layer: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS**;
- bounded Tamil bodies: **6**; cue-only non-lyric occurrences: **3**;
- item-level source-attributed lyricists: **0**; unresolved item-level lyric authorships: **6**;
- film-level PDF 88 `பாடல்கள்: கவிஞர் வாலி`: **preserved, not promoted item-by-item**;
- upstream canonical Tamil / scene / dialogue / character mutation from song processing: **0**;
- English translation: **READY-NEXT**.

**Next production phase:** {NEXT}

'''
s,n=re.subn(r'## Vandikkaran Magan current checkpoint\n.*?(?=## Naam current checkpoint)',checkpoint,s,flags=re.S)
assert n==1
s=s.replace('**Next: character/entity indexing from the immutable exact-label inventory.**', '**Next: bounded English-translation pilot from source scene 1.**')
p.write_text(s,encoding='utf-8')

# Final consistency assertions.
assert 'song_performance_authorship_gate: complete-verified-source-only' in (W/'metadata.yaml').read_text(encoding='utf-8')
assert 'English translation: **READY-NEXT**' in (W/'README.md').read_text(encoding='utf-8')
assert 'song/performance gate: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS**' in (ROOT/'README.md').read_text(encoding='utf-8')
assert 'English translation **READY-NEXT**' in (ROOT/'docs'/'HANDOVER_KALAIGNAR_CINEMA_WORKS.md').read_text(encoding='utf-8')
assert 'song/performance 9/9 QA PASS' in (ROOT/'docs'/'STATUS_CONSISTENCY_AUDIT.md').read_text(encoding='utf-8')
print('PASS: Vandikkaran Magan song/performance closure synchronized to English READY-NEXT')
