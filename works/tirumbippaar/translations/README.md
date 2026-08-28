# திரும்பிப்பார்! — English translation layer

**Canonical authority:** corrected/scan-closed Tamil transcription, reconciled 93-scene derivatives, immutable **1,042-record** dialogue corpus, and regenerated character/entity layer  
**Target language:** English (`en`)  
**Source reconciliation:** **complete — 93/93 scenes**  
**Publication status:** **complete-verified — reader and deterministic EPUB QA PASS**

This directory contains interpretive English derivatives. Nothing here repairs, normalizes or overwrites the authoritative Tamil source.

## Translation principles

1. Tamil remains authoritative; English fluency is never evidence for changing canonical Tamil.
2. Every source-labelled utterance is linked exactly once to the immutable dialogue corpus.
3. Exact Tamil speaker labels remain exact metadata, including printed spacing variants.
4. Stage directions do not gain actions absent from the source.
5. Repetition, questions, code-switching, imagery and rhetorical force are retained rather than silently flattened.
6. Genuine cross-page source units remain one English unit with full provenance.
7. Song/performance content is limited to what the booklet prints; absent lyrics are not reconstructed.
8. Source-unlabelled speech stays unlabelled.
9. Printed `★` separators are structural and are not translated into invented `(Scene ends.)` prose.
10. Historical surviving English unit IDs remain stable. Source-proven recovered units may therefore appear out of numeric-ID order after their correct source position is restored.

## Final corrected-source checkpoint

Scenes **1–93** are `corrected-source-reconciled` in `index.json`.

The English layer contains **1,330 verified units**:

- **1,049 dialogue-kind** = 1,042 labelled dialogue links + 7 deliberately unlabelled source-spoken units;
- **262 stage-direction**;
- **7 song-reference**;
- **2 chant**;
- **10 written-text**;
- **0 reconstructed full-song**.

All **1,042 / 1,042** immutable labelled-dialogue record IDs are linked exactly once. The seven source-visible unlabelled spoken units remain unlabelled. All 12 genuine cross-page English units remain intact.

## Closure repairs retained

The final source-reconciliation and publication QA passes preserved several nontrivial repairs:

- scene 41 links the two recovered labelled source utterances without renumbering earlier IDs;
- scene 63 preserves the stable d020/d021 split and its PDF 79→80 continuation;
- scenes 37 and 39 retain recovered carry-over stage directions at their true source positions even though their stable English IDs are numerically higher;
- exact speaker-label metadata is synchronized to the immutable dialogue records, including `சப்- இன்ஸ்பெக்டர்` / `சப் - இன்ஸ்பெக்டர்` spacing variants;
- stale English provenance was corrected where the reconciled scene source proves the page boundary, including scene 66, scene 77 and scene 82;
- scene 92 begins with the newspaper heading and source-visible Court setting;
- scene 93 begins with the source-visible Jail setting and retains the final children/warders departure, `வணக்கம்.`, and structural closing star without invented prose.

The canonical Part04 three-string synchronization is also closed, so the upstream Tamil part file and its scene/dialogue derivatives agree.

## Cross-page English units

The verified cross-page units are:

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

These seven source-visible passages remain dialogue-kind units without invented speaker metadata or dialogue-record IDs:

- `tirumbippaar-en-s005-u026`
- `tirumbippaar-en-s015-u018`
- `tirumbippaar-en-s034-u012`
- `tirumbippaar-en-s044-u004`
- `tirumbippaar-en-s084-u002`
- `tirumbippaar-en-s088-u004`
- `tirumbippaar-en-s091-u014`

The six source scenes with no labelled dialogue records — **10, 11, 25, 26, 43 and 54** — remain represented only by source-visible narrative, performance or written material.

## Publication verification

The deterministic publication workflow has now rebuilt and revalidated the Markdown, HTML and JSON reader derivatives plus the EPUB 3 package.

Reader release gate:

- scenes: **93/93**
- English units: **1,330/1,330**
- immutable dialogue links: **1,042/1,042**
- page regressions: **0**
- missing/extra dialogue links: **0 / 0**
- synthetic star-end units: **0**
- QA: **PASS**

EPUB release gate:

- scenes: **93/93**
- units packaged exactly once: **1,330/1,330**
- scene XHTML documents: **93**
- ZIP members: **99**
- bytes: **370,218**
- SHA-256: `88bf02ac345926d02a3b6e25ea262c3f6aafe59383a620b2bb160cdd3fabbb31`
- QA: **PASS**

Generated publication commit: **`55bb983eb2959190f025250099793ab5efce2b9f`**.

See `../editions/en/QA_REPORT.md`, `../editions/en/manifest.json`, `../editions/en/EPUB_QA_REPORT.md` and `../editions/en/package-manifest.json` for machine-checked release details.

## Downstream use

There is no remaining English source-reconciliation or publication rebuild batch. Downstream consumers should use these verified records or `../editions/en/reader-edition.json`; they must not derive replacement Tamil or speaker metadata from the English output.
