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

## Reusable onboarding for new cinema works

For every newly supplied Kalaignar cinema source, use these project-level documents before work begins:

- `docs/CINEMA_WORKS_PROCESSING_GUIDE.md` — the detailed mature workflow from source intake through Reading Room integration;
- `docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md` — project-level handover, reference implementations and lessons learned;
- `docs/START_NEW_CINEMA_WORK_PROMPT.md` — copy-paste prompt for starting a new work safely;
- `docs/ARCHIVAL_WORKFLOW.md`, `docs/SOURCE_POLICY.md`, and `docs/TRANSCRIPTION_GUIDE.md` — baseline source/transcription rules.

The preferred public reading destination for completed works is the **Kalaignar Digital Library / Reading Room at `https://nenjukkuneethi.org/read`**. Cinema works should normally be presented there by **scene**, using verified structured repository data. Standalone publication packages are secondary and should be created only when explicitly requested or independently useful.

## மனோகரா status

The source `TVA_BOK_0010102_மனோகரா.pdf` has completed the intake and structural-mapping gate, and canonical Tamil first-pass transcription is now in progress.

- source title: **`மனோகரா`**;
- printed credit: **`திரைக்கதை வசனம்` / `மு. கருணாநிதி`**;
- explicit edition statement: **`முதற்பதிப்பு : பிப்ரவரி 1954.`**;
- scan: **90 PDF pages**;
- source SHA-256: `87518fd8c290d7880aa2ddd9f2b5999c9d421d48fe1f02d61cf8e254393236a9`;
- `நாடகக் கதை`: PDF **4–5**;
- `முன்னுரை`: PDF **6**;
- main screenplay/dialogue: PDF **7–88 / logical printed pp.6–87** — **82 canonical pages**;
- back matter: PDF **89–90**;
- source-numbered scene headings: **none printed** — no scene count has been invented;
- structural mapping: **verified**;
- transition-heading audit: **complete for intake/mapping**;
- canonical Tamil first pass: **24/82 pages complete — PDF 7–30 / logical printed pp.6–29, status `draft`**;
- visual fidelity audit: **not-started**;
- later structured derivatives and translation: **blocked until Tamil verification**.

The first batch preserves the embedded play-within-the-play, source-visible song/performance references and the PDF-23 war proclamation in source order. Song authorship remains unresolved by design; the screenplay/dialogue credit is not treated as lyric credit.

**Next:** continue canonical Tamil first-pass transcription from **PDF 31 / logical printed p.30**, in source order, with stable page anchors. The separate visual fidelity audit remains a later gate before structured derivatives.

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

**Next:** no required Parasakthi English translation or QA/export activity remains. For public access, future downstream work should prioritize integration into `https://nenjukkuneethi.org/read`; standalone packaging should be done only when separately requested or useful.

## திரும்பிப்பார்! status

The second screenplay is archived from `TVA_BOK_0014652_திரும்பிப்பார்.pdf`.

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
- English translation: **complete-verified — scenes 1–93, 1,321 verified source-linked units**;
- English reader/export edition: **complete-verified — Markdown / HTML / JSON + QA report + integrity manifest**;
- English EPUB 3 package: **complete-verified — deterministic package QA PASS**.

Earlier audit work found and repaired a first-pass storage gap at PDF **61–63** and a missing explicit page anchor at PDF **80**; both are fidelity-verified. The final audit corrected the scene-72 structural label at PDF **87 / printed p.79** to the scan-visible `[தாசி வீடு`.

A later derivative-stage scan recheck also corrected scene 31 at PDF **38 / printed p.30** from the earlier transcription `பாண்டியன் என் செல்வம்` to the source-visible song title **`பாண்டியன் என் சொல்லை`**. The canonical Part 03 transcription and scene derivative were corrected from the scan, and the change is recorded in `works/tirumbippaar/notes/post-fidelity-corrections.md`.

The PDF-2 lower imprint remains a documented source crop. Reinspection supports only the visible partial `சிட்டி பிரஸ், மதுரை ரோ…`; the missing continuation is not reconstructed.

The song gate visually checked PDF **1–8** and found no lyricist/song-credit section. The cover `கதை - வசனம்` credit is not treated as song authorship. Item-level external music-catalog evidence is used only for the two exact source-named title matches; unnamed singing references and the scene-29 labour chant remain explicitly unresolved rather than being guessed onto other soundtrack rows.

The completed English derivative is stored under `works/tirumbippaar/translations/`. Final totals are **1,321/1,321 verified units: 1,047 dialogue / 254 stage direction / 7 song-reference / 2 chant / 11 written-text / 0 full-song units**. All **1,040 immutable labelled dialogue records** are linked exactly once; seven additional source-visible spoken units remain deliberately unlabelled in metadata.

The translation contains **12 genuine cross-page units** and preserves all six zero-dialogue source scenes (**10, 11, 25, 26, 43, 54**) through their source-visible narrative, performance or written material. Scene 31 links exactly to song occurrence `tirumbippaar-song-006`; scenes 42–43 preserve only source-visible `கலப்படம்` material, with absent lyrics remaining absent.

The publication-reader preflight performed a final derivative-only reconciliation. Residual synthetic `(Scene ends.)` units created solely from structural `★` separators were removed from scenes **21, 26, 27, 29, 30 and 34**; scene 29's `கோஷம்` heading and scene 30's location heading were restored to source order; and scene 47's three duplicated stage-action units were removed. Final diagnostics report **0 synthetic star-end units, 0 page-order regressions, 0 unit-ID errors, 0 missing dialogue links and 0 extra dialogue links**.

Scene 57 retains all **50** labelled dialogue records individually. Scene 90 retains the source direction `[மரணமூச்சுவிடும் பரந்தாமன்]`; scene 91 preserves `பத்திரிகை News` as written newspaper content; scene 93 preserves final `வணக்கம்.` and leaves the following `★` structural.

The provenance-safe reader/export layer under `works/tirumbippaar/editions/en/` passes whole-work QA across **93 scenes / 1,321 units / 1,040 immutable dialogue links / 12 cross-page units**. It generates `reader-edition.md`, standalone `reader-edition.html`, machine-readable `reader-edition.json`, `QA_REPORT.md` and `manifest.json`.

The same automated publication workflow now builds `tirumbippaar-en.epub` as a deterministic **EPUB 3** package. EPUB QA confirms **93 scene XHTML documents**, every one of the **1,321 verified unit IDs exactly once**, **99 ZIP members**, complete TOC/OPF/spine coverage, and first/uncompressed exact `mimetype`. The package is **370,615 bytes** with SHA-256 `17b9422cf2bf9cd30c90829a2dbd18115e20b8bd1cf7e5bb9da2cc0cdcc23c7f`; `EPUB_QA_REPORT.md` and `package-manifest.json` record the package checkpoint.

The active GitHub Actions workflow reruns reader preflight, whole-work reader QA, deterministic EPUB packaging and metadata synchronization when authoritative inputs change, and commits reproducible outputs only after all gates pass.

No canonical Tamil, scene, dialogue, character or song-inventory layer was changed by the English translation, final reader reconciliation, reader export or EPUB packaging.

**Next:** no required Tirumbippaar English translation, reader-export or EPUB-packaging activity remains. Its intended primary public destination is the scene-based Reading Room at `https://nenjukkuneethi.org/read`, using the verified Tamil/English structured data. Additional standalone packages are optional only when explicitly requested.

## Status vocabulary

`not-started` · `draft` · `draft-complete` · `review` · `verified` · `pilot-verified` · `complete-verified` · `unresolved`

Translation status is independent of source-transcription verification status.
