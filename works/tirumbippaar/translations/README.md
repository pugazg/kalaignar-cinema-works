# திரும்பிப்பார்! — English translation layer

**Canonical authority:** verified Tamil transcription, completed scene derivatives and immutable dialogue records  
**Target language:** English (`en`)  
**Status:** **complete-verified — scenes 1–93, 1,321/1,321 units verified**

This directory contains interpretive English derivatives. Nothing here repairs, normalizes, expands or overwrites the verified Tamil source.

## Files

- `schema.json` — schema for the 93 scene-sharded source-linked translation records; it supports both the richer early units and the later compact units.
- `index.json` — completed translation / integrity checkpoint.
- `records/scene-XX.json` — 93 scene-sharded English translation records.
- `../editions/en/` — publication-facing reader/export layer generated from these verified records.

## Translation principles

1. **Tamil remains authoritative.** English fluency is never evidence for changing the canonical Tamil.
2. **Every source-labelled utterance is linked.** All **1,040** immutable dialogue records are represented exactly once.
3. **Exact Tamil speaker labels stay exact metadata.** Character normalization does not rewrite them.
4. **Stage directions do not gain action.** Translate only what the verified scene supplies.
5. **Dialogue preserves rhetorical force.** Repetition, questions, code-switching, imagery and political/social rhetoric are not silently flattened.
6. **Cross-page source units remain one English unit.** Genuine source-spanning units retain all page provenance.
7. **Song/performance material is limited to what this booklet prints.** Do not import absent lyrics from audio, web pages, streaming metadata or another booklet.
8. **Unlabelled source material stays unlabelled.** Direct speech, letters, newspaper blocks, advertisements, chants and other source-visible material do not receive invented speakers or dialogue-record IDs.
9. **External authorship metadata is not translation text.** It may identify a song occurrence, but it cannot supply missing Tamil or English lyrics.
10. **The printed `★` is structural.** It is not translated into an invented `(Scene ends.)` unit.

## Final verified coverage

All canonical scenes **1–93** are translated and verified.

- scenes 1–5 — **81 units**
- scenes 6–10 — **43 units**
- scenes 11–15 — **63 units**
- scenes 16–20 — **66 units**
- scenes 21–25 — **27 units**
- scenes 26–30 — **96 units**
- scenes 31–35 — **84 units**
- scenes 36–40 — **122 units**
- scenes 41–45 — **92 units**
- scenes 46–50 — **81 units**
- scenes 51–55 — **46 units**
- scenes 56–60 — **111 units**
- scenes 61–65 — **50 units**
- scenes 66–70 — **67 units**
- scenes 71–75 — **44 units**
- scenes 76–80 — **81 units**
- scenes 81–85 — **49 units**
- scenes 86–90 — **82 units**
- scenes 91–93 — **36 units**
- **total — 1,321 verified / 0 review / 0 draft**

Final kinds: **1,047 dialogue / 254 stage-direction / 7 song-reference / 2 chant / 11 written-text / 0 full-song units**.

The 1,047 dialogue-kind units consist of the **1,040 immutable source dialogue records plus 7 source-visible unlabelled spoken units**. Those seven intentionally retain null speaker/dialogue-record metadata.

## Cross-page English units

Twelve source units genuinely span canonical page boundaries and remain single English units:

- `tirumbippaar-en-s001-u008` — PDF 9→10
- `tirumbippaar-en-s026-u002` — PDF 31→32
- `tirumbippaar-en-s041-u001` — PDF 52→53
- `tirumbippaar-en-s041-u046` — PDF 56→57
- `tirumbippaar-en-s045-u018` — PDF 59→60
- `tirumbippaar-en-s061-u001` — PDF 78→79
- `tirumbippaar-en-s063-u004` — PDF 79→80
- `tirumbippaar-en-s072-u002` — PDF 87→88
- `tirumbippaar-en-s076-u014` — PDF 91→92
- `tirumbippaar-en-s080-u024` — PDF 96→97
- `tirumbippaar-en-s080-u032` — PDF 97→98
- `tirumbippaar-en-s083-u002` — PDF 100→101

## Source-unlabelled spoken units

These seven source-visible spoken passages remain `dialogue` units without invented speaker metadata or dialogue-record IDs:

- `tirumbippaar-en-s005-u026`
- `tirumbippaar-en-s015-u018`
- `tirumbippaar-en-s044-u004`
- `tirumbippaar-en-s051-u003`
- `tirumbippaar-en-s084-u002`
- `tirumbippaar-en-s088-u004`
- `tirumbippaar-en-s091-u014`

The six source scenes with no labelled dialogue records — **10, 11, 25, 26, 43 and 54** — are nevertheless represented from their source-visible narrative/performance/written material.

## Song/performance constraint

Seven translated song references are linked to verified source occurrences `tirumbippaar-song-001`, `002`, `003`, `004`, `006`, `007` and `008`. Scene 31 is linked to `tirumbippaar-song-006`, whose scan-visible title is **`பாண்டியன் என் சொல்லை`**. Scenes 42–43 link the source-visible `கலப்படம்` material to occurrences `007` and `008`.

The booklet prints no complete lyric body for either source-named soundtrack song, so this layer contains **zero reconstructed full-song translations**. The scene-29 labour slogan and scene-86 begging chant remain chants, not fabricated soundtrack lyrics.

## Final reader-export reconciliation

The publication-facing reader preflight exposed and repaired derivative-only structural residue without changing canonical Tamil, scenes, dialogue records, character mappings or song inventory.

- **93/93** translation scene files remain verified.
- **1,040/1,040** labelled source dialogue records are linked exactly once.
- Scene 31 uses exact song occurrence `tirumbippaar-song-006`.
- Scene 57 retains all **50** labelled dialogue records individually.
- Residual synthetic `(Scene ends.)` units derived only from structural `★` markers were removed from scenes **21, 26, 27, 29, 30 and 34**.
- Scene 29's `கோஷம்` structural heading was restored to its source position before the chant body.
- Scene 30's source-visible location heading was restored to source order.
- Scene 47's three duplicated stage-action units were removed because those actions were already represented in their source-order units.
- Final preflight reports **0 synthetic star-end units, 0 page-order regressions, 0 unit-ID errors, 0 missing dialogue links and 0 extra dialogue links**.
- Scene 90 retains `[மரணமூச்சுவிடும் பரந்தாமன்]`; scene 91 retains `பத்திரிகை News` as written text; scene 93 retains final `வணக்கம்.` while its following `★` remains structural.

## Reader/export status

`../editions/en/` now contains generated Markdown, standalone HTML and machine-readable JSON reader editions together with a whole-work `QA_REPORT.md` and deterministic `manifest.json`. The GitHub Actions reader QA/build is active and passes against this final checkpoint.

No required English translation activity remains.
