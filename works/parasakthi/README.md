# பராசக்தி

Archival record for the scanned booklet **`பராசக்தி — முழு வசனம் + பாடல்கள்`**.

## Canonical source

- Source: `TVA_BOK_0062968_பராசக்தி.pdf`
- PDF pages: **58**
- SHA-256: `b0024315ca2018a63807b8ff44eb02d132868a7250e6399a2144a10e47c4ad4c`
- Canonical dialogue/song range: PDF **4–57** / printed pp. **3–56**
- PDF 58: rear advertisement / back matter
- Canonical Tamil: **54 verified / 0 review / 0 unresolved markers**

The source has **46 observed scene headings**; headings **23 and 34 are absent**. The documented late scene-number transposition remains source-provenanced while the canonical sequence uses scene 43 on PDF 49 and final scene 48 on PDF 57.

## Completed Tamil/source derivatives

- Scene index: **46/46 complete**
- Scene-text derivatives: **46/46 complete**
- Dialogue index: **complete-verified — 642 records**
- Character index: **complete-verified — 69/69 source labels disposed**
- Song/verse inventory: **14 occurrence records**
- Song authorship: **14/14 verified**
- Tamil soundtrack derivatives: **11/11 complete-verified**
- Separate quoted-verse derivative: **1**

None of these layers is rewritten by English translation or reader-export work.

## English translation layer

Source-linked English records live under [`translations/`](translations/).

Final checkpoint:

- status: **complete-verified**
- observed scenes translated/verified: **1–22, 24–33, 35–48 — 46/46 observed scenes**
- canonical scenes **23 and 34: absent**
- translation units: **769**
- verified: **769**
- review/draft: **0**
- kinds: **641 dialogue / 114 stage direction / 13 song / 1 quoted verse**

The translation preserves all verified cross-page units, the source-heading corrections for canonical scenes 43 and 48, soundtrack occurrence boundaries, source-visible material outside the dialogue derivative, and source-unlabelled dialogue/performance without invented speaker labels.

## English reader edition and whole-work QA

The publication-facing derivative is under [`editions/en/`](editions/en/). Its automated whole-work QA is **PASS**.

The QA validates:

- **769/769** unique sequential verified English units across **46/46** observed scenes;
- **634** links back to immutable dialogue records, including exact source speaker labels and page provenance;
- **14** verified song/verse occurrence links;
- all **16** cross-page English units;
- **97** distinct source paths;
- two direct source-linked labelled dialogue units without invented dialogue IDs;
- five direct source-linked unlabelled dialogue/performance units without invented speaker labels;
- two additional direct source-linked non-dialogue units;
- canonical PDF/printed-page range and scene/unit source order;
- every unit exactly once in the generated Markdown and HTML reader editions.

Generated reader derivatives:

- `editions/en/reader-edition.md`
- `editions/en/reader-edition.html`
- `editions/en/reader-edition.json`
- `editions/en/QA_REPORT.md`
- `editions/en/manifest.json`

The build is reproducible through `editions/en/build.py` and the active `.github/workflows/parasakthi-english-edition.yml` workflow.

During this QA activity, the legacy scene-1 pilot record was normalized by adding `scene_status: verified` alongside its existing `pilot_status: verified`; its verified translation text and source provenance were unchanged.

No canonical Tamil, scene derivative, dialogue record, character mapping, song inventory, Tamil song derivative or transcription file was modified.

## Next activity

There is **no required English translation or whole-work QA/export activity remaining**. Optional future work may package the verified reader edition into PDF/EPUB or a repository release without changing the verified source or translation authority.
