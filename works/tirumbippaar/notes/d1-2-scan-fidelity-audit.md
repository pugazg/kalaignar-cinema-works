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

**Scene-location bracket typography — ADJUDICATED (18 of 18).**
An earlier revision deferred these. They are now resolved, because D1.2 is the scan-fidelity phase and
the canonical↔scene gate cannot see them: canonical and scene agreed on `(`, so no mismatch was raised.
Each of the 18 was inspected individually on the controlling scan at 400dpi; no case was decided from
the pattern of earlier cases, from the heading audit alone, or from neighbouring scenes.

| scene | PDF | printed | scan | canonical before | scene before | after |
|---|---|---|---|---|---|---|
| 36 | 44 | 36 | `[` | `(` | `(` | `[` |
| 44 | 58 | 50 | `[` | `(` | `(` | `[` |
| 45 | 58 | 50 | `[` | `(` | `(` | `[` |
| 46 | 60 | 52 | `[` | `(` | `(` | `[` |
| 48 | 63 | 55 | `[` | `(` | `(` | `[` |
| 56 | 70 | 62 | `[` | `(` | `(` | `[` |
| 59 | 76 | 68 | `[` | `(` | `(` | `[` |
| 62 | 79 | 71 | `[` | `(` | `(` | `[` |
| 63 | 79 | 71 | `[` | `(` | `(` | `[` |
| 64 | 81 | 73 | `[` | `(` | `(` | `[` |
| 70 | 86 | 78 | `[` | `(` | `(` | `[` |
| 71 | 87 | 79 | `[` | `(` | `(` | `[` |
| 72 | 87 | 79 | `[` | `(` | `(` | `[` |
| 75 | 90 | 82 | `[` | `(` | `(` | `[` |
| 82 | 99 | 91 | `[` | `(` | `(` | `[` |
| 83 | 100 | 92 | `[` | `(` | `(` | `[` |
| 85 | 102 | 94 | `[` | `(` | `(` | `[` |
| 86 | 103 | 95 | `[` | `(` | `(` | `[` |

**18 checked · 18 corrected · 0 already correct · 0 unresolved.** Every scan reading was `[`; the
unanimity is a result, not a rule that was applied. Scene 56 stores its location inside the Markdown
heading rather than on its own line, and was corrected there.

**Scene-number closing marker — ADJUDICATED (22 of 22).**
A second surface, found while checking the location markers. An earlier revision corrected only the
three with scan evidence and left 19 open. All are now closed, each inspected individually on the
controlling scan at 400dpi.

| scene | PDF | printed | scan | before | after |
|---|---|---|---|---|---|
| 30 | 36 | 28 | `]` | `)` | `]` |
| 31 | 38 | 30 | `]` | `)` | `]` |
| 33 | 41 | 33 | `]` | `)` | `]` |
| 34 | 42 | 34 | `]` | `)` | `]` |
| 35 | 43 | 35 | `]` | `)` | `]` |
| 38 | 49 | 41 | `]` | `)` | `]` |
| 39 | 50 | 42 | `]` | `)` | `]` |
| 40 | 52 | 44 | `]` | `)` | `]` |
| 41 | 52 | 44 | `]` | `)` | `]` |
| 42 | 57 | 49 | `]` | `)` | `]` |
| 43 | 57 | 49 | `].` | `).` | `].` |
| 47 | 61 | 53 | `]` | `)` | `]` |
| 55 | 69 | 61 | `]` | `)` | `]` |
| 57 | 71 | 63 | `]` | `)` | `]` |
| 63 | 79 | 71 | `]` | `)` | `]` |
| 75 | 90 | 82 | `]` | `)` | `]` |
| 82 | 99 | 91 | `]` | `)` | `]` |
| 83 | 100 | 92 | `]` | `)` | `]` |
| 84 | 102 | 94 | `]` | `)` | `]` |
| 48 | 63 | 55 | `]` | *(none)* | `]` |
| 62 | 79 | 71 | `]` | *(none)* | `]` |
| 74 | 90 | 82 | `]` | *(none)* | `]` |

**22 checked · 22 corrected · 0 already correct · 0 unresolved.** Scenes 32, 44 and 56 were resolved in
the previous round and are not re-listed. Every reading was `]`; that is the result of twenty-two
separate inspections, not a rule extended from the first three.

Source anomalies are preserved rather than regularised: scene **5** prints `காட்சி 5[`, scene **36**
prints `காட்சி 36` with **no** closing glyph, and scene **43** prints `காட்சி 43].` — bracket followed
by a full stop.

**Scene 45 speaker form — corrected on the user's direct PDF verification.**
The user checked the controlling PDF: the source prints `பாண்டியன் : தொழிலாளர்கள்`, with **no** full
stop after the speaker name. Canonical and the scene derivative both carried `பாண்டியன். :`; the stray
stop is removed from both. The dialogue record `tirumbippaar-s045-d013` already held
`speaker_label: "பாண்டியன்"` and is unchanged — it was correct all along, and the defect was in the
layers above it. **No `பாண்டியன்.` label variant was created and the character inventory stays at 45
exact source labels.** An earlier revision of this note flagged the record as the possible outlier;
that reading is withdrawn.

## Scene-5 provenance chain

The restored line `கருடன் : இல்லை பரந்தாமன்.` sits under `pdf=14 printed=6` in the scene, but its
dependent records still pointed at PDF 13 / printed 5:

- `tirumbippaar-s005-d007` — corrected to `pdf_page: 14, printed_page: 6`;
- `tirumbippaar-en-s005-u010` — corrected to `pdf_page: 14, printed_page: 6`.

No unrelated PDF-13 record was moved.

`tirumbippaar-s005-d004` also dropped the printed ellipsis: the scan at 600dpi shows
`உண்மையான ஆசிரியர்......`, which canonical and the scene both carry, so the dialogue record was
restoring-corrected to match. The note on `tirumbippaar-en-s005-u007` claimed the source "ends without
added ellipsis after `ஆசிரியர்`", which is false; it now records what the page prints. The English text
gains the visible unfinished cue, consistent with the 229 other units in this edition that end in an
explicit ellipsis.

## Provenance gates

Text alone was not sufficient, so provenance is now gated separately.

- **dialogue provenance** — 1,042 records paired with their scene utterances in source order:
  943 label/page pairs verified directly, **0 page-provenance mismatches**.
  Four records have no separately labelled scene line under a strict `label:` parser and were checked
  individually: `s063-d021` (the documented split), `s081-d002` (`Echo`, a Latin label),
  `s057-d036` (source prints the label with no colon) and `s086-d021` (source prints a semicolon after
  the label). All four are present with their labels and their page provenance agrees.
- **dialogue↔translation provenance** — every linked English unit checked against its dialogue record
  for scene, page provenance and speaker label: **0 mismatches**. This gate is what catches the
  scene-5 `d007`/`u010` class of bug.
- **scene↔dialogue text** — 1,042 checked, 2 flagged, both the documented pre-existing scene-72
  structural records; **0 unexplained**.

Recorded, not changed: `tirumbippaar-s045-d013` carries the speaker label `பாண்டியன்` while the scene
line prints `பாண்டியன்.` with a full stop before the colon. This predates D1.2 — it is the same on the
post-D1.1 baseline `d4b394a7` — and the archive's label model has evidently treated the printed stop as
punctuation rather than part of the label. Changing it would add a 46th entry to the 45-label character
inventory, which is outside this reconciliation. Flagged for a separate decision.

## Method statement

No reading in this phase was decided by grammar, gender agreement, expected syntax, contextual
plausibility, character identity or modern spelling. The controlling scan decided every case, and where
the scan was the only authority the layer that disagreed with it was the one corrected. The
user-confirmed reading `ஊஹும்` was not reopened: it stands at five occurrences each in the
transcription, scene and dialogue layers, with `ஊஹூம்` absent from the work.

Reader and EPUB artifacts remain **post-merge CI only** — `tirumbippaar-english-edition.yml` runs on
push to `main`. No EPUB byte size or hash is asserted for this branch.

## Final gate results (D1.2 closure)

| gate | result |
|---|---|
| canonical↔scene | **1348/1348 exact text; 1348/1348 exact text + page; 0 mismatches** |
| page attribution | **0** |
| scene↔dialogue text | 1042 checked · 2 flagged · **0 unexplained** (both documented scene-72 structural records) |
| scene↔dialogue provenance | **0 mismatches** |
| dialogue↔translation provenance | **0 mismatches** (scene, page, speaker label) |
| dialogue links | **1042 exactly once**, 0 duplicate, 0 orphan, 0 unlinked |
| character source labels | **45** — no `பாண்டியன்.` variant exists |
| translation/reader preflight | PASS |
| heading markers | 18 location-opening + 22 scene-number closing · **0 unresolved** |

Census: 104 canonical pages (83 `verified` + 21 `verified-reconciled`, 0 draft, 0 review,
`printed = pdf − 8` with 0 violations) · 93 scenes · 1042 dialogue records · 1330 translation units.
`ஊஹும்` stands at 5/5/5 across transcription, scenes and dialogues with **0 `ஊஹூம்` in live reading
layers**; the only remaining occurrences of the superseded form are documentary, inside this note.

Four scenes (57, 63, 81, 86) have one more dialogue record than a strict `label:` parser finds, because
the source prints those labels without a colon, with a semicolon, or in Latin (`Echo`), and because
scene 63 carries the deliberate `d020`/`d021` split. Each was checked individually; all are present with
their labels and correct provenance.

Reader and EPUB artifacts remain **post-merge CI only**; no EPUB hash is asserted for this branch.

