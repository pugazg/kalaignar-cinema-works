# Parasakthi — English Translation Handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Handover refreshed: 2026-08-14

This is the continuation entry point for any future **packaging/release** work. Translation and whole-work reader QA are complete.

## 1. Final English translation state

- status: **`complete-verified`**
- observed canonical scenes translated and second-pass verified: **1–22, 24–33, 35–48**
- observed scene records: **46/46 complete-verified**
- canonical scenes **23 and 34 are absent**
- translation units: **769**
- verified: **769**
- review/draft: **0**
- kinds: **641 dialogue / 114 stage-direction / 13 song / 1 quoted-verse**
- cross-page English units: **16**

There is no remaining translation batch.

## 2. Completed second-pass gates

- scenes 6–10: **66/66**;
- scenes 11–15: **88/88**;
- scenes 16–20: **87/87**;
- observed scenes 21, 22, 24 and 25: **96/96**; scene 23 absent;
- scenes 26–30: **93/93**;
- observed scenes 31, 32, 33 and 35: **95/95**; scene 34 absent;
- scenes 36–40: **43/43**;
- scenes 41–48: **131/131**.

Verified soundtrack occurrences through the ending include `parasakthi-song-012`, the four-line scene-47 reprise `parasakthi-song-013`, and closing `parasakthi-song-014`. The separate literary quotation remains `quoted-verse`.

## 3. Whole-work reader QA/export — complete

Publication-facing English derivatives now live under:

`works/parasakthi/editions/en/`

Automated whole-work QA status: **PASS**.

The successful QA validated:

- **769/769** unique, sequential, verified English units;
- **46/46** observed canonical scenes and the deliberate absence of scenes **23 and 34**;
- **641 dialogue / 114 stage direction / 13 song / 1 quoted verse**;
- all **16** cross-page English units exactly against `translations/index.json`;
- **634** immutable dialogue-record links, including scene, exact Tamil `speaker_label`, and page provenance;
- **14** verified song/verse occurrence links;
- **97** distinct source paths;
- PDF **4–57** / printed pp. **3–56** provenance and canonical source order;
- each verified unit exactly once in both Markdown and HTML reader output;
- no editorial placeholder tokens in reader text.

The QA explicitly preserves source material that does not fit a simple dialogue-record model:

- labelled direct source dialogue without invented dialogue IDs: `parasakthi-en-s032-u004`, `parasakthi-en-s033-u063`;
- source-unlabelled dialogue/performance without invented speaker labels: `parasakthi-en-s017-u004`, `parasakthi-en-s019-u003`, `parasakthi-en-s019-u004`, `parasakthi-en-s019-u006`, `parasakthi-en-s019-u007`;
- direct source-linked non-dialogue units: `parasakthi-en-s045-u003`, `parasakthi-en-s048-u003`.

The reader builder also preserves `english_lines` for semantic-poetic/performance units even where the archival unit kind is `dialogue`, rather than coercing every dialogue-kind unit into prose.

## 4. Generated reader derivatives

- `works/parasakthi/editions/en/reader-edition.md`
- `works/parasakthi/editions/en/reader-edition.html`
- `works/parasakthi/editions/en/reader-edition.json`
- `works/parasakthi/editions/en/QA_REPORT.md`
- `works/parasakthi/editions/en/manifest.json`

Build/QA source:

- `works/parasakthi/editions/en/build.py`
- `.github/workflows/parasakthi-english-edition.yml`

The successful workflow builds the derivatives and commits reproducible outputs. The manifest records build version, aggregate translation-input SHA-256, output SHA-256 values and byte sizes.

## 5. QA discoveries and corrections

The QA gate deliberately failed on real structural assumptions before passing; those failures were resolved without changing canonical Tamil.

1. **Legacy pilot metadata:** scene 1 used `pilot_status: verified` but lacked the later `scene_status` key. It now also carries `scene_status: verified`. Translation text, source links and provenance are unchanged.
2. **Source-unlabelled conscience/performance:** scene 17 u004 and four scene-19 performance units legitimately have no immutable dialogue record/speaker label. The builder was corrected to preserve them unlabelled rather than manufacturing speakers.
3. **Poetic dialogue payloads:** some scene-19 performance units are archival `dialogue` units with semantic-poetic `english_lines`. The builder was corrected to preserve the verified payload shape rather than demanding `english_text` based only on unit kind.

These are QA/export-layer corrections and one English-record status-metadata normalization only. They do not repair or reinterpret canonical Tamil.

## 6. Canonical/source state — immutable

- source: `TVA_BOK_0062968_பராசக்தி.pdf`
- SHA-256: `b0024315ca2018a63807b8ff44eb02d132868a7250e6399a2144a10e47c4ad4c`
- 58 PDF pages; canonical dialogue/song range PDF **4–57** / printed pp. **3–56**
- canonical Tamil: **54 verified / 0 review / 0 unresolved markers**
- observed scene headings: **46**; headings **23 and 34 absent**
- canonical scene 43 retains source-heading-48 provenance on PDF 49
- canonical final scene 48 retains source-heading-43 provenance on PDF 57
- dialogue index: **642 complete-verified records**
- song/verse inventory and authorship: **14/14 verified**
- Tamil soundtrack derivatives: **11/11 complete-verified**, plus one quoted-verse derivative

English translation/export must never be used to repair, normalize or overwrite the Tamil source. Film audio, subtitles, web copies, later editions and familiar quotations remain non-authoritative.

## 7. Repository discipline

Whole-work QA/export did not modify canonical Tamil, scene derivatives, immutable dialogue records, character mappings, song inventory, Tamil song derivatives or transcription files. Exact Tamil speaker labels and page provenance remain authoritative metadata where supplied; source-unlabelled material remains unlabelled.

## 8. Next activity

There is **no required Parasakthi English translation or whole-work QA/export activity remaining**.

If the project continues, treat the current reader derivatives and verified translation records as fixed authorities and perform **packaging/release only**—for example PDF/EPUB generation or a repository release—without altering canonical Tamil or silently rewriting verified English. Such packaging should be separately QA'd before release.

## 9. Continuation prompt

> Read `docs/HANDOVER_PARASAKTHI_ENGLISH_TRANSLATION.md`. Parasakthi English translation is complete-verified at 769/769 units and whole-work reader QA is PASS. No translation or reader-QA batch remains. If continuing, do packaging/release work only from the verified reader/translation authorities and preserve all canonical source layers.
