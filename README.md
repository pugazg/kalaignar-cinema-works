# Kalaignar Cinema Works

A source-led archive of screenplay, dialogue, song, and related cinema writing credited to **Kalaignar M. Karunanidhi**.

The repository preserves source provenance, canonical transcription and derivative representations separately.

## Archival principles

1. **Primary source first.** The scanned publication controls canonical transcription.
2. **No silent correction.** Source anomalies stay documented.
3. **Page provenance is mandatory.** Transcribed, indexed and translated units remain traceable to PDF/printed pages.
4. **Uncertainty stays visible.** Interpretive pressure points are reviewed rather than guessed away.
5. **Source and derivatives are separate.** English translation never overwrites Tamil.
6. **Authorship is not inferred.** Mixed-credit material requires item-level evidence.
7. **Rights are not assumed.** No repository-wide public-domain/open-license claim is made.

## Parasakthi status

The canonical Tamil covers PDF **4–57 / printed pp.3–56** and is fully verified at **54/54 pages**. PDF 58 is back matter.

Completed source/Tamil derivatives:

- scene layer: **46/46**;
- dialogue index: **642 records, complete-verified**;
- character index: **69/69 source labels disposed**;
- song/verse occurrences: **14**;
- song authorship: **14/14 verified**;
- Tamil soundtrack files: **11/11 complete-verified**;
- separate quoted verse: **1**.

The source-linked English translation is **complete-verified for all 46 observed canonical scenes**: scenes **1–22, 24–33 and 35–48**. Canonical scenes **23 and 34 are absent** and correctly have no translation records.

Final English totals are **769/769 verified units**: **641 dialogue / 114 stage direction / 13 song / 1 quoted verse**. A whole-work reader QA now also passes across all 769 units: **634 immutable dialogue-record links**, **14 song/verse occurrence links**, **16 cross-page units**, and **97 distinct source paths** were checked. Source-unlabelled dialogue/performance remains unlabelled rather than receiving invented speaker metadata.

Publication-facing, provenance-safe English derivatives are generated under `works/parasakthi/editions/en/` as Markdown, standalone HTML and machine-readable JSON, with a generated QA report and deterministic integrity manifest. The active GitHub Actions workflow reruns the QA/build when its authoritative inputs change.

No canonical Tamil, scene, dialogue, character, song or transcription derivative was modified by the English translation or reader-export work.

**Next:** no required Parasakthi English translation or QA/export activity remains. Optional future work may package the verified reader edition into formats such as PDF/EPUB or a release, without changing the verified source layers.

## திரும்பிப்பார்! status

The second screenplay is being archived from `TVA_BOK_0014652_திரும்பிப்பார்.pdf`.

- explicit source edition statement: **`முதல் பதிப்பு: 1953`**;
- scan: **112 PDF pages**;
- main screenplay: PDF **9–112 / printed pp.1–104**;
- scene-number pass: **93 scene starts, consecutively 1–93**;
- source intake: **complete**;
- structural mapping: **verified**;
- scene-heading / structural-label audit: **93/93 dispositioned**;
- canonical Tamil: **104 verified / 0 draft / 0 review**;
- fidelity audit: **complete**;
- scene index / scene-text derivatives: **93/93 complete**;
- dialogue index: **1,040 records across 93 scene shards, complete**;
- character index: **45/45 exact speaker labels dispositioned into 39 verified entities/role categories**;
- song/performance inventory: **8 source-visible occurrences dispositioned**;
- song authorship mapping: **3 verified occurrences / 5 unresolved occurrences**;
- source-named songs with verified item-level authorship: **`பாண்டியன் என் சொல்லை` — பாரதிதாசன்; `கலப்படம்` — கண்ணதாசன்**;
- Tamil song-lyric derivative files: **0**, because this booklet prints no complete lyric body for either source-named song;
- English translation: **in-progress — scenes 1–15 verified, 187 source-linked units**.

Earlier audit work found and repaired a first-pass storage gap at PDF **61–63** and a missing explicit page anchor at PDF **80**; both are fidelity-verified. The final audit corrected the scene-72 structural label at PDF **87 / printed p.79** to the scan-visible `[தாசி வீடு`.

A later derivative-stage scan recheck also corrected scene 31 at PDF **38 / printed p.30** from the earlier transcription `பாண்டியன் என் செல்வம்` to the source-visible song title **`பாண்டியன் என் சொல்லை`**. The canonical Part 03 transcription and scene derivative were corrected from the scan, and the change is recorded in `works/tirumbippaar/notes/post-fidelity-corrections.md`.

The PDF-2 lower imprint remains a documented source crop. Reinspection supports only the visible partial `சிட்டி பிரஸ், மதுரை ரோ…`; the missing continuation is not reconstructed.

The song gate visually checked PDF **1–8** and found no lyricist/song-credit section. The cover `கதை - வசனம்` credit is not treated as song authorship. Item-level external music-catalog evidence is used only for the two exact source-named title matches; unnamed singing references and the scene-29 labour chant remain explicitly unresolved rather than being guessed onto other soundtrack rows.

The English derivative is stored under `works/tirumbippaar/translations/`. Scenes 1–15 now contain **187 verified units: 147 dialogue / 36 stage direction / 4 song-reference**. Scene 11 is a zero-dialogue source scene whose boat movement and source-only singing reference remain separate unlabelled units. Scene 14 links only the printed stage-song reference; absent lyrics stay absent. Scene 15 preserves its source-unlabelled pocket/laundry line with a null speaker and no invented dialogue-record ID. The scene-1 Poomaal utterance across PDF 9→10 remains the only cross-page English translation unit so far.

**Next:** translate and verify **scenes 16–20**.

## Status vocabulary

`not-started` · `draft` · `draft-complete` · `review` · `verified` · `pilot-verified` · `complete-verified` · `unresolved`

Translation status is independent of source-transcription verification status.
