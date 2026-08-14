# Parasakthi — English translation layer

**Canonical authority:** verified Tamil transcription and immutable structured derivatives  
**Target language:** English (`en`)  
**Status:** **complete-verified** — every observed canonical scene is translated and second-pass verified; canonical scenes **23 and 34 are absent**

This directory contains interpretive English derivatives. Nothing here may repair, normalize, or overwrite the verified Tamil source.

## Translation principles

1. **Tamil remains authoritative.** Smoother English is never evidence for changing Tamil.
2. **Every unit is source-linked.** Preserve canonical scene, source path, record/occurrence ID where available, and PDF/printed-page provenance.
3. **Exact identifiers stay exact.** Tamil `speaker_label` values remain immutable metadata.
4. **Stage directions do not gain action.** Translate only what the verified source supplies.
5. **Dialogue preserves rhetorical force.** Repetition, questions, code-switching, metaphors and political/social rhetoric are not flattened merely for fluency.
6. **Songs are semantic translations, not singable rewrites.** No rhyme, metre or imagery is invented.
7. **Quoted verse remains distinct from soundtrack song.**
8. **Cross-page source units remain one translation unit.**
9. **Source-visible material absent from a structured derivative may be source-located directly.** Do not manufacture dialogue IDs or speaker labels.
10. **No external text substitution.** Web translations, subtitles, film audio, familiar quotations and later English versions do not replace source-linked work.

## Final coverage

Verified English scene records exist for every observed canonical scene: **1–22, 24–33 and 35–48**. Canonical scenes **23 and 34 are absent** and correctly have no translation records.

Final totals:

- observed scene records translated/verified: **46/46**;
- translation units: **769**;
- verified: **769**;
- review/draft: **0**;
- kinds: **641 dialogue / 114 stage direction / 13 song / 1 quoted verse**;
- cross-page units: **16**.

All 13 verified soundtrack occurrence records are represented in English, including the scene-47 partial reprise `parasakthi-song-013`; the separate literary quotation remains `quoted-verse` rather than soundtrack song.

## Whole-work QA and reader edition

The downstream publication-facing edition lives at `../editions/en/`. Its automated whole-work QA is **PASS** and treats these verified records as the English authority rather than rewriting them.

The QA checked all **769/769** units and, among other invariants:

- cross-checked **634** immutable dialogue-record links for scene, exact Tamil `speaker_label`, and page provenance;
- cross-checked **14** verified song/verse occurrence links;
- verified **97** distinct source paths exist;
- verified the exact **16** cross-page unit list;
- retained the two indexed direct source-linked labelled dialogue units without invented record IDs;
- retained **five** source-unlabelled dialogue/performance units without inventing speaker labels;
- retained the two indexed direct source-linked non-dialogue units;
- verified canonical PDF **4–57** / printed **3–56** provenance and source order;
- verified every unit appears exactly once in both the Markdown and HTML reader editions;
- preserved both prose `english_text` and semantic-poetic/performance `english_lines` payloads according to each verified record.

Generated outputs:

- `../editions/en/reader-edition.md`
- `../editions/en/reader-edition.html`
- `../editions/en/reader-edition.json`
- `../editions/en/QA_REPORT.md`
- `../editions/en/manifest.json`

The reproducible builder is `../editions/en/build.py`; `.github/workflows/parasakthi-english-edition.yml` reruns the QA/build when authoritative inputs change.

During QA, the legacy scene-1 pilot record gained `scene_status: verified` alongside its existing `pilot_status: verified`; no verified English text or source provenance changed. The QA also explicitly preserves source-unlabelled material such as scene 17's conscience block and scene 19's performance blocks without manufactured speaker metadata.

No canonical Tamil, scene file, dialogue record, character record, song inventory, Tamil song derivative or transcription file was modified.

## Next activity

There is **no required English translation or reader-QA activity remaining**. Optional future work may package the verified reader edition as PDF/EPUB or a release while keeping these records and all canonical source layers immutable.
