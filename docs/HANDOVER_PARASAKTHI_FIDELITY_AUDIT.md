# Parasakthi — controlling handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Handover refreshed: 2026-08-14

Current stage: **all source/Tamil archival derivatives, the complete English translation, and the whole-work English reader QA/export are complete**.

## Canonical/source state — immutable

- Source: `TVA_BOK_0062968_பராசக்தி.pdf`
- SHA-256: `b0024315ca2018a63807b8ff44eb02d132868a7250e6399a2144a10e47c4ad4c`
- 58 PDF pages; PDF **4–57** / printed pp. **3–56** are canonical dialogue/song pages.
- Canonical Tamil: **54 verified / 0 review / 0 unresolved markers**.
- Scene derivatives: **46/46 complete**; headings **23 and 34 are absent**.
- Canonical scene 43 retains source heading 48 provenance on PDF 49; final canonical scene 48 retains source heading 43 provenance on PDF 57.
- Dialogue index: **642 complete-verified records**.
- Character layer: **69/69 exact source labels disposed**; documented review/unresolved identities remain separate from English translation.
- Song/verse inventory and authorship: **14/14 verified**.
- Tamil soundtrack derivatives: **11/11 complete-verified**, plus one separate quoted-verse derivative.

Never use English translation, reader exports or external versions to repair the Tamil source.

## English translation final checkpoint

- status: **`complete-verified`**
- observed scenes translated/verified: **1–22, 24–33, 35–48 — 46/46 observed scenes**
- scenes in review: **none**
- translation units: **769**
- verified: **769**
- review/draft: **0**
- kinds: **641 dialogue / 114 stage direction / 13 song / 1 quoted verse**
- cross-page English units: **16**

All second-pass gates are complete through scene 48. Source occurrence boundaries, late cross-page dialogue records, source-heading corrections, and source-visible material outside the dialogue derivative remain preserved without invented IDs.

## Whole-work English reader QA/export

Status: **PASS / complete-verified**.

Publication-facing outputs live under `works/parasakthi/editions/en/` and are generated reproducibly by `build.py` plus the active `Parasakthi English reader QA` GitHub Actions workflow.

The successful QA validated:

- **769/769** unique sequential verified English units across **46/46** observed scenes;
- absent scenes **23 and 34** remain absent;
- **634** immutable dialogue-record links, including exact source speaker labels and page provenance;
- **14** verified song/verse occurrence links;
- all **16** indexed cross-page English units;
- **97** distinct source paths;
- canonical PDF/printed-page range and source order;
- all verified units exactly once in both Markdown and HTML reader editions;
- source-unlabelled dialogue/performance retained without invented speaker labels;
- semantic-poetic/performance `english_lines` retained even when the archival unit kind is dialogue.

Generated outputs:

- `works/parasakthi/editions/en/reader-edition.md`
- `works/parasakthi/editions/en/reader-edition.html`
- `works/parasakthi/editions/en/reader-edition.json`
- `works/parasakthi/editions/en/QA_REPORT.md`
- `works/parasakthi/editions/en/manifest.json`

The only verified-record normalization made during whole-work QA was the addition of `scene_status: verified` to the legacy scene-1 pilot record alongside its existing `pilot_status: verified`; no English translation text or provenance changed.

No canonical Tamil, scene derivative, immutable dialogue record, character mapping, song inventory, Tamil song derivative or transcription file was modified by the reader QA/export activity.

## Exact next work

There is **no required translation or reader-QA/export work remaining**. Any continuation should be downstream **packaging/release only**—for example PDF/EPUB generation or a repository release—from the verified reader/translation authorities. Packaging must not alter canonical Tamil or silently rewrite verified English and should receive its own release QA.

## Overall status

- Structural mapping: verified
- Canonical Tamil: verified
- Tamil fidelity audit: complete
- Scene derivatives: complete
- Dialogue index: complete-verified
- Character index: complete-verified
- Song authorship/Tamil derivatives: complete-verified
- English translation: **complete-verified — 769/769 units**
- English reader edition whole-work QA: **PASS / complete-verified**
