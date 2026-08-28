# Tirumbippaar D1.2 — scan-fidelity reconciliation

## Authority and scope

Controlling source: `TVA_BOK_0014652_திரும்பிப்பார்.pdf`  
SHA-256: `973b9c3f7b84d6a1902a4a472af8799c783bf1ec2d6cd015796fc1df1ce59682`

D1.2 reopens punctuation, brackets, quote/dash glyphs, spacing and page attribution between the canonical transcription and the scene derivatives. The rendered scan decides every source-visible difference. Neither canonical nor scene text is presumed correct, and grammar/context is not used to repair the print.

The audit began from the post-PR-#2 main checkpoint `d4b394a7b4582935792df4cf2840fbd466dd41c5`.

## Why a scan adjudication was required

The first strict comparison proved that the mismatch direction was mixed. In directly checked cases canonical carried OCR-shaped defects such as `/` for `!`, `(` for `[`, mismatched `(…]`, and a wrong PDF-page anchor, while other cases showed the scene derivative missing a closing parenthesis or carrying a wrong opening bracket. Bulk propagation in either direction would therefore have corrupted source fidelity.

The page-aware probe covered the mismatch-bearing PDF pages 13, 16–19, 24–46, 65, 67 and 69. A later parser revision also exposed two bracketed source units that the earlier pairing had not classified separately; those were scan-adjudicated in the same pass.

Representative scan decisions include:

- printed p.5 / PDF 13: the opening publishing-house direction is square-bracketed, `புக்போஸ்டுகள்மீது` is closed up, `(ஆபீஸ் பையனிடம்)` is a complete parenthetical, and Pandiyan's `ஆசிரியர்......` ending retains the printed dots;
- printed p.8 / PDF 16: `பாமா! கண்ணே!` is printed with `!`, not the canonical OCR-like `/`;
- printed p.10 / PDF 18: scenes 9 and 10 use `[…]`, and the scene-8 separation marks are long dashes rather than canonical hyphens;
- printed p.11 / PDF 19: the source again supports the square-bracketed stage structure rather than canonical parenthesis drift;
- printed p.21 / PDF 29: `அம்மா !` confirms `!` rather than `/`;
- printed p.36 / PDF 44: `பூமாலை: அதைக் கேட்க நான் இருக்கிறேனே! அவனை எனக்கு நேராகவே` belongs to PDF 44; printed p.37 / PDF 45 begins with `குமுதா: உனக்கு உன் தம்பி பெரிசு!`.

## Applied repair rule

For each mismatch-bearing source unit:

1. inspect the rendered scan;
2. preserve the scan-visible word, punctuation, spacing and glyph form;
3. correct whichever textual layer disagrees with the scan;
4. preserve stable scene and dialogue IDs;
5. change page provenance only where the scan proves the existing attribution wrong;
6. do not use the user correction witness, OCR, grammar or an English translation to overrule the scan.

Scene-heading/location text that is stored as two physical source lines in canonical and as one Markdown scene heading in the scene derivative is treated as structural markup only when the complete source-visible text is still present. It is not counted as a body-text mismatch.

## Resulting source gate

After repair, the page-aware source-bearing comparison reports:

- aligned source-bearing scene pairs: **1,348**;
- exact text pairs: **1,348 / 1,348**;
- exact text + PDF attribution: **1,348 / 1,348**;
- unexplained source-visible mismatches: **0**;
- page-attribution mismatches: **0**.

The four remaining unaligned structures are scene-location continuations that canonical stores as a
separate physical line while the scene derivative folds them into one Markdown heading, so the text gate
cannot pair them. Two (`[பூமாலை வீடு- பகல்`, `[குமுதா மதறாஸ் வீடு : ஹால்`) are present verbatim inside the
combined heading. The other two were **not**: canonical read `(கருடன் பதிப்பகம்` and `(ஹோட்டல் அறை-பகல்`
where the scene derivative read `[`. Rendering printed pp. 30 and 98 at 600dpi shows the source prints `[`
in both, and `notes/scene-heading-audit.md` independently records `[` for scenes 32 and 89, so canonical was
repaired to `[` in each case.

## Dialogue-layer synchronization

Because D1.2 changed source-visible punctuation/spacing and also exposed older corrected-reading drift that had never reached some immutable dialogue `text` fields, the dialogue layer was rechecked against the repaired scene source.

- dialogue records: **1,042**;
- stable dialogue IDs changed: **0**;
- records whose `text` field was synchronized: **51** across 18 scene files (recomputed on this branch; an
  earlier draft said 55/20);
- exact source-text mismatches after synchronization: **0**;
- known scene-63 `d020` + `d021` stable split retained unchanged; their concatenated text equals the single printed `கருடன்` utterance.

This synchronization includes earlier corrected readings such as `இது என்னா வேலை`, `அறிமுகமானான்`, `விளையாடுகிறான்`, `ஏம்மா`, `அதுக்குள்ளத்தான்`, `ஏன் மாமா`, and `சபாஸ்`, while preserving the already-settled user-confirmed `ஊஹும்` reading.

## English/source-link check

Of the 51 synchronized records, 11 changed at Tamil letter level and only **two** English units were
materially stale. Scene 5's `ஆசிரியர்......` unit already ended unfinished and needed no revision:

- scene 5 preserves the printed unfinished `ஆசிரியர்......` ending;
- scene 6 preserves the incomplete `சுருக்குப் போடப் .....` construction instead of expanding it;
- scene 6 preserves the as-printed third-person sequence `அறிமுகமானான் / விளையாடுகிறான் / ஓடிவிடுவானோ` rather than normalizing the speaker to first person.

No English unit IDs were renumbered.

Whole-work validation after these repairs:

- English units: **1,330**;
- dialogue links: **1,042 / 1,042**, unique and complete;
- missing links: **0**;
- extra links: **0**;
- translation/reader preflight (`editions/en/audit_probe.py`) on this branch: **PASS** — 0 synthetic
  scene-end units, 0 page regressions, 0 unit-ID errors, 0 duplicate IDs, 0 missing links, 0 extra links.

**No reader or EPUB artifacts are committed on this branch, and no EPUB QA is claimed for it.** The
`tirumbippaar-english-edition.yml` workflow triggers only on push to `main`, so the reader edition, manifest
and EPUB are regenerated by CI after merge. An EPUB byte size and hash quoted in an earlier draft came from a
local build of a different tree and is withdrawn.

## D1.2 disposition

**D1.2 repair set: PASS.** The scan-adjudicated canonical, scene, dialogue and materially affected English records are internally reconciled, with zero unexplained source-bearing text/page differences in the audited gate.

D2 remains blocked until this repair set is reviewed and merged to `main`, the normal Tirumbippaar English publication workflow completes on the merge, and the resulting `main` checkpoint is revalidated.

## Documented exceptions and out-of-gate findings

**Scene↔dialogue structural exceptions (2, pre-existing, not introduced by D1.2).**
`tirumbippaar-s072-d001` and `tirumbippaar-s072-d003` model a printed utterance together with the stage
direction that follows it, joining lines the scene derivative keeps separate. `scenes/scene-72.md` is
unchanged by this branch, so these are pre-existing modelling choices carried by `page_segments`, not drift.
They are reported rather than silently "fixed".

**Scene-location bracket typography, outside the canonical↔scene gate (18 cases).**
`notes/scene-heading-audit.md` records a square-bracket location marker for scenes 36, 44, 45, 46, 48, 56,
59, 62, 63, 64, 70, 71, 72, 75, 82, 83, 85 and 86, while *both* canonical and the scene derivative print `(`.
Because the two layers agree, the D1.2 canonical↔scene gate does not flag them, and they are **not** changed
here. The two scan checks performed for this branch (printed pp. 30 and 98) both showed `[`, and the same
OCR `(`-for-`[` substitution was proven repeatedly during this audit, so these 18 are likely wrong in both
layers. Resolving them requires a per-case scan adjudication of the scene-heading surface and belongs to a
separate audit, not to this reconciliation.
