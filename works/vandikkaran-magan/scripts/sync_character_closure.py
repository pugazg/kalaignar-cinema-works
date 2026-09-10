#!/usr/bin/env python3
from pathlib import Path
import json, re

R = Path(__file__).resolve().parents[3]
W = R / 'works' / 'vandikkaran-magan'
C = json.loads((W/'characters/index.json').read_text(encoding='utf-8'))
Q = json.loads((W/'notes/character-index-qa.json').read_text(encoding='utf-8'))
assert C['status'] == 'complete-verified' and Q['status'] == 'PASS'
assert C['dialogue_records_source'] == 744 and C['distinct_source_labels'] == 38
assert C['entity_count'] == 32 and C['entity_type_counts'] == {'collective': 3, 'character': 15, 'role': 14}
assert C['label_coverage'] == '38/38' and C['dialogue_record_coverage'] == '744/744'
assert C['remaining_unmapped_labels'] == 0 and C['remaining_unmapped_records'] == 0

NEXT = C['next_activity']

# metadata.yaml
p = W/'metadata.yaml'; t = p.read_text(encoding='utf-8')
t = t.replace('  character_entity_index: ready-next\n  song_performance_authorship_gate: blocked', '''  character_entity_index: complete-verified
  character_entity_index_path: works/vandikkaran-magan/characters/index.json
  character_entity_count: 32
  character_entity_type_counts: character=15,role=14,collective=3
  character_exact_source_labels: 38
  character_label_coverage: 38/38
  character_dialogue_record_coverage: 744/744
  character_unmapped_labels: 0
  character_unmapped_records: 0
  character_qa: PASS
  character_qa_path: works/vandikkaran-magan/notes/character-index-qa.json
  song_performance_authorship_gate: ready-next''')
t, n = re.subn(r'^next_action: .*$', 'next_action: '+json.dumps(NEXT, ensure_ascii=False), t, flags=re.M); assert n == 1
p.write_text(t, encoding='utf-8')

# Work README
p = W/'README.md'; t = p.read_text(encoding='utf-8')
t = t.replace('- character/entity index: **READY-NEXT**;\n- song/performance authorship: **BLOCKED pending character/entity closure**;', '''- character/entity index: **COMPLETE-VERIFIED — 32 entities / 38/38 exact labels / 744/744 dialogue records / QA PASS**;
- entity types: **15 named characters / 14 roles / 3 collectives**;
- character mapping review / unresolved: **0 / 0**;
- song/performance authorship: **READY-NEXT**;''')
t = t.replace('See `dialogues/index.json`, `dialogues/README.md`, `notes/unlabelled-block-audit.json`, and `notes/dialogue-index-qa.json`.', 'See `dialogues/index.json`, `characters/index.json`, `characters/README.md`, `notes/dialogue-index-qa.json`, and `notes/character-index-qa.json`.')
t, n = re.subn(r'## Exact next activity\n\n> \*\*.*?\*\*\n?$', '## Exact next activity\n\n> **'+NEXT+'**\n', t, flags=re.S); assert n == 1
p.write_text(t, encoding='utf-8')

# Project handover
p = W/'PROJECT_HANDOVER.md'; t = p.read_text(encoding='utf-8')
t = t.replace('- character/entity index: **READY-NEXT**;\n- song/performance authorship gate: **BLOCKED pending character/entity closure**;', '''- character/entity index: **COMPLETE-VERIFIED — 32 entities / 38/38 labels / 744/744 dialogue records / QA PASS**;
- character/entity types: **15 named characters / 14 roles / 3 collectives**;
- character/entity review / unresolved: **0 / 0**;
- source label variants remain immutable upstream; interpretive merges exist only in `characters/`;
- song/performance authorship gate: **READY-NEXT**;''')
insert = '''\nCharacter/entity mapping closed with **0** unmapped labels and **0** unmapped dialogue records. Source-supported mappings include `காளிங்` + `காளிங்க` → காளிங்கராயன், `சொக்` + `சொக்க` → சொக்கலிங்கம், and `ஜமீன்` + `ஜமீன்தார்` → ஜம்புலிங்க பூபதி. Possessive voice labels `கண்ணாயிரத்தின் குரல்`, `சடையன் குரல்`, and `விங்கன் குரல்` link to their named characters only in the interpretive layer. Generic roles/collectives remain categorical; `லிங்கன்` remains distinct from `விங்கன்`, and `ஜம்பு` remains distinct from `ஜம்புலிங்க பூபதி`.\n'''
anchor = 'No canonical Tamil or scene file was changed by dialogue construction.\n'
assert anchor in t; t = t.replace(anchor, anchor+insert)
t, n = re.subn(r'## Exact next activity\n\n> \*\*.*?\*\*\n?$', '## Exact next activity\n\n> **'+NEXT+'**\n', t, flags=re.S); assert n == 1
p.write_text(t, encoding='utf-8')

# Mapping
p = W/'mapping.md'; t = p.read_text(encoding='utf-8')
marker = '''## Exact next activity\n\n**Begin character/entity indexing from the complete-verified immutable dialogue layer. Preserve all exact source speaker labels as immutable provenance; map label variants to character/entity IDs only in a separate interpretive alias layer; keep generic roles, voices, collectives and source abbreviations explicit; and run whole-work label/entity coverage QA before opening the song/performance authorship gate. Do not rewrite canonical Tamil, scenes, or dialogue records.**\n'''
assert marker in t
t = t.replace(marker, f'''## Character/entity derivative gate\n\n- exact source labels mapped: **38/38**;\n- immutable dialogue records mapped: **744/744**;\n- entities: **32 — 15 characters / 14 roles / 3 collectives**;\n- verified / review / unresolved entities: **32 / 0 / 0**;\n- unmapped labels / dialogue records: **0 / 0**;\n- dialogue/source labels rewritten: **0**.\n\n## Exact next activity\n\n**{NEXT}**\n''')
p.write_text(t, encoding='utf-8')

# Dialogue and scene readmes downstream mirrors
p = W/'dialogues/README.md'; t = p.read_text(encoding='utf-8')
t = t.replace('Speaker labels and dialogue text are source-preserving; alias resolution belongs only to the next character/entity layer.', 'Speaker labels and dialogue text remain source-preserving. The downstream character/entity layer is now complete-verified and keeps alias resolution separate from these immutable records.')
t, n = re.subn(r'## Next\n\n.*?\n?$', '## Downstream\n\nCharacter/entity indexing is **COMPLETE-VERIFIED — 32 entities / 38/38 labels / 744/744 dialogue records / QA PASS**. Song/performance authorship is **READY-NEXT**.\n\n'+NEXT+'\n', t, flags=re.S); assert n == 1
p.write_text(t, encoding='utf-8')

p = W/'scenes/README.md'; t = p.read_text(encoding='utf-8')
t = t.replace('Scene-text derivatives remain **COMPLETE-VERIFIED**. The downstream immutable dialogue index is now **COMPLETE-VERIFIED — 744 records / QA PASS**. Character/entity indexing is **READY-NEXT**.', 'Scene-text derivatives remain **COMPLETE-VERIFIED**. Downstream dialogue indexing is **744 records / COMPLETE-VERIFIED / QA PASS** and character/entity indexing is **32 entities / 38/38 labels / 744/744 dialogue records / COMPLETE-VERIFIED / QA PASS**. Song/performance authorship is **READY-NEXT**.')
p.write_text(t, encoding='utf-8')

# Next chat prompt rewritten for the next phase.
(W/'NEXT_CHAT_PROMPT.md').write_text(f'''# Next Chat Prompt — வண்டிக்காரன் மகன் / song-performance authorship\n\nContinue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/vandikkaran-magan/`. **LIVE MAIN IS AUTHORITATIVE.**\n\n## Controlling source\n\n`TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` — 90 pages, 26,391,039 bytes, SHA-256 `03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253`, first edition 1978, image-only. The attached/rendered scan remains canonical authority.\n\n## Durable closed state\n\n- canonical source layer: **87/87 COMPLETE-VERIFIED — PDF 4–90**;\n- open source/glyph uncertainty: **0**;\n- scene headings / derivatives: **72/72 / 72/72 COMPLETE-VERIFIED**;\n- scene boundary ownership: **PASS — 82/82 screenplay pages / 0 gaps / 0 overlaps / 0 duplicate ownership**;\n- immutable dialogue index: **744 records / 38 exact source labels / COMPLETE-VERIFIED / QA PASS**;\n- character/entity index: **32 entities / COMPLETE-VERIFIED / QA PASS**;\n- character/entity types: **15 named characters / 14 roles / 3 collectives**;\n- character label / dialogue coverage: **38/38 / 744/744**;\n- character review / unresolved entities: **0 / 0**;\n- unmapped character labels / dialogue records: **0 / 0**.\n\nDo not reopen or rewrite closed canonical Tamil, scenes, immutable dialogue records, or character/entity mappings without new direct contradictory source evidence.\n\n## Song/performance rules\n\nFollow `docs/CINEMA_WORKS_PROCESSING_GUIDE.md` song/performance authorship gate. Inventory every source-visible song, verse, chant or performance occurrence first. Preserve exact source wording, lineation, performance cues, scene/page provenance and whether a complete lyric body is actually printed. The film-level credit `பாடல்கள்: கவிஞர் வாலி` on PDF 88–89 is metadata but does **not** by itself authorize item-level authorship. Do not reconstruct missing lyrics or infer authorship from film memory, performer identity, proximity, or broad credits.\n\n## Exact next activity\n\n> **{NEXT}**\n''', encoding='utf-8')

# data/works.json
p = R/'data/works.json'; works = json.loads(p.read_text(encoding='utf-8')); item = next(x for x in works if x.get('id') == 'vandikkaran-magan'); sd = item['structured_derivatives']
sd.update({
    'character_entity_index': 'complete-verified',
    'character_index': 'complete-verified',
    'character_entity_index_path': 'works/vandikkaran-magan/characters/index.json',
    'character_entity_count': 32,
    'character_entity_type_counts': {'character':15,'role':14,'collective':3},
    'character_distinct_source_labels': 38,
    'character_verified_labels': 38,
    'character_review_labels': 0,
    'character_unresolved_labels': 0,
    'character_verified_entities': 32,
    'character_review_entities': 0,
    'character_unresolved_entities': 0,
    'character_dialogue_record_coverage': '744/744',
    'character_qa': 'PASS',
    'character_qa_path': 'works/vandikkaran-magan/notes/character-index-qa.json',
    'song_performance_authorship_gate': 'ready-next',
    'next_structured_derivative': 'song-performance-authorship',
})
item['next_action'] = NEXT
p.write_text(json.dumps(works, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

# Root README: replace active section only.
p = R/'README.md'; t = p.read_text(encoding='utf-8')
section = f'''## வண்டிக்காரன் மகன் status\n\n`TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` is the current active cinema-work source.\n\n- source: **90 PDF pages / 26,391,039 bytes / SHA-256 `03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253` / first edition 1978**;\n- source credits: **`மூலக்கதை அண்ணா` / `திரைக்கதை-வசனம் கலைஞர்`**;\n- canonical Tamil: **87/87 COMPLETE-VERIFIED / 0 open uncertainties**;\n- scenes: **72/72 COMPLETE-VERIFIED / boundary QA PASS**;\n- immutable dialogues: **744 records / 38 exact labels / COMPLETE-VERIFIED / QA PASS**;\n- character/entity index: **32 entities / 15 characters / 14 roles / 3 collectives / COMPLETE-VERIFIED / QA PASS**;\n- character coverage: **38/38 labels / 744/744 dialogue records / 0 unmapped / 0 unresolved**;\n- song/performance authorship: **READY-NEXT**;\n- English and reader layers: **gated downstream**.\n\n**Next:** {NEXT}\n'''
t2, n = re.subn(r'## வண்டிக்காரன் மகன் status\n.*?(?=\n## நாம் status)', section+'\n', t, flags=re.S); assert n == 1
p.write_text(t2, encoding='utf-8')

# Master handover: high-level checkpoint and active statement.
p = R/'docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md'; t = p.read_text(encoding='utf-8')
t, n = re.subn(r'- \*\*Vandikkaran Magan / வண்டிக்காரன் மகன்\*\* — .*', '- **Vandikkaran Magan / வண்டிக்காரன் மகன்** — canonical Tamil **87/87 COMPLETE-VERIFIED**; scenes **72/72 COMPLETE-VERIFIED / boundary QA PASS**; dialogues **744 COMPLETE-VERIFIED / 38 exact labels / QA PASS**; characters/entities **32 COMPLETE-VERIFIED / 38/38 labels / 744/744 dialogue coverage / QA PASS**; song/performance authorship **READY-NEXT**.', t, count=1); assert n == 1
t, n = re.subn(r'Ammayappan and Naam remain closed at their recorded checkpoints\. \*\*The current active production work is வண்டிக்காரன் மகன்:.*?\*\*', 'Ammayappan and Naam remain closed at their recorded checkpoints. **The current active production work is வண்டிக்காரன் மகன்: canonical Tamil, 72 scenes, 744 immutable dialogues and the 32-entity character layer are COMPLETE-VERIFIED / QA PASS; song/performance authorship is READY-NEXT.**', t, count=1); assert n == 1
p.write_text(t, encoding='utf-8')

# Status consistency audit: result paragraph, matrix row and current checkpoint block.
p = R/'docs/STATUS_CONSISTENCY_AUDIT.md'; t = p.read_text(encoding='utf-8')
t, n = re.subn(r'\*\*PASS for the current repository-wide checkpoint\.\*\* Vandikkaran Magan .*?Ammayappan and the other recorded work checkpoints remain preserved\.', '**PASS for the current repository-wide checkpoint.** Vandikkaran Magan is now closed through character/entity indexing: **32 entities / 38/38 exact labels / 744/744 dialogue records / QA PASS**, with **0 unmapped labels, 0 unmapped records, 0 review entities and 0 unresolved entities**. Song/performance authorship is READY-NEXT. Ammayappan and the other recorded work checkpoints remain preserved.', t, count=1, flags=re.S); assert n == 1
t, n = re.subn(r'\| Vandikkaran Magan / வண்டிக்காரன் மகன் \|.*', '| Vandikkaran Magan / வண்டிக்காரன் மகன் | **87/87 canonical source pages complete-verified; 0 unresolved** | **72/72 scenes; 744 dialogues / 38 labels; 32 character/entities / character QA PASS** | not-started | not-started |', t, count=1); assert n == 1
block = f'''## Vandikkaran Magan current checkpoint\n\n- canonical Tamil / visual / historical-glyph / final visual: **87/87 / 87/87 / 87/87 / 87/87 COMPLETE-PASS**;\n- source-visible scene-heading inventory: **72/72**, including PDF 10 `காட்சி — 4 எ.` / source scene `4-எ`;\n- scene derivatives: **72/72 COMPLETE-VERIFIED / boundary ownership QA PASS**;\n- immutable dialogue index: **744 records / 38 exact labels / COMPLETE-VERIFIED / QA PASS**;\n- character/entity index: **32 entities / 15 characters / 14 roles / 3 collectives / COMPLETE-VERIFIED / QA PASS**;\n- character label / dialogue coverage: **38/38 / 744/744**;\n- character unmapped labels / records: **0 / 0**;\n- character review / unresolved entities: **0 / 0**;\n- upstream canonical Tamil / scene / dialogue mutation from character indexing: **0**;\n- song/performance authorship: **READY-NEXT**.\n\n**Next production phase:** {NEXT}\n\n'''
t2, n = re.subn(r'## Vandikkaran Magan current checkpoint\n.*?(?=## Naam current checkpoint)', block, t, flags=re.S); assert n == 1
p.write_text(t2, encoding='utf-8')

print('PASS: synchronized Vandikkaran Magan character closure and opened song/performance gate')
