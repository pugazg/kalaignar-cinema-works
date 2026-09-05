# அம்மையப்பன் — Historical Tamil Glyph Audit

Controlling source: `TVA_BOK_0064230_அம்மையப்பன்.pdf`

Required guide: `docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`

## Purpose

`அம்மையப்பன்` is a 1954 printed screenplay/dialogue booklet with frequent historical Tamil typeforms. Ordinary visual source-fidelity review is not sufficient by itself because an older glyph can resemble a different modern Tamil character or sequence.

This work therefore has **two independent Tamil verification gates**:

1. **visual source-fidelity audit** — confirms that transcription matches all visible source text, structure, punctuation, labels, line content and page boundaries;
2. **historical-Tamil-glyph audit** — confirms that older Tamil glyph identities have been decoded correctly into modern Unicode without modernization or visual-lookalike substitution.

A canonical page is **final Tamil verified only when both gates pass**.

## Current checkpoint when this gate was introduced

- canonical screenplay pages: **105** — PDF **5–109** / logical printed pp. **3–107**;
- first-pass transcription: **105/105 draft-complete**;
- visual source-fidelity audit already completed: **PDF 5–74 / 70 pages**;
- historical-glyph pages formally cleared under this explicit guide: **0/105**;
- final dual-gate Tamil verified pages: **0/105** at gate introduction;
- PDF **5–74** therefore require a **retrospective historical-glyph pass**;
- PDF **75–109** must receive **visual fidelity + historical-glyph verification together** as source review continues.

The existing 70-page visual-fidelity evidence is preserved. It is not discarded. It simply does not, by itself, satisfy the newly explicit historical-glyph gate.

## Minimum historical families to inspect on every canonical page

Check the complete known set, even when the page appears straightforward:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

This is a minimum set, not an exhaustive list. Also inspect unusual ligatures, faint vowel marks, worn type, broken ink and edition-specific forms.

## Audit rules

For each page:

1. inspect the complete rendered page at enlarged/native resolution;
2. identify historical character identity before deciding Unicode transcription;
3. inspect all 13 known reform-sensitive families occurrence-by-occurrence;
4. compare uncertain forms with clearer same-edition/same-font occurrences;
5. do not use OCR, semantic expectation or modern spelling as proof;
6. do not global-replace any suspected historical form;
7. preserve source spelling, grammar, vocabulary, punctuation and spacing unless the pixels independently prove a transcription error;
8. record every historical-glyph correction separately from ordinary fidelity corrections;
9. if character identity remains uncertain, keep the page `needs-review`;
10. if a historical-glyph correction changes a page that previously passed visual fidelity, perform a local visual recheck of the corrected occurrence and record the post-fidelity correction.

## Dual-gate status model

| Status | Meaning |
|---|---|
| `visual-pass / glyph-pending` | visual fidelity passed earlier, but the explicit historical-glyph pass has not yet been completed |
| `visual-pending / glyph-pending` | neither gate has yet passed |
| `visual-pass / glyph-pass` | page is final Tamil verified |
| `needs-review` | either gate has unresolved source evidence |

## Coverage plan

### Forward combined audit

Continue from **PDF 75 / logical printed p.73**. Every new visual-fidelity page from PDF 75 onward must simultaneously receive the historical-glyph audit. A page may be promoted to final Tamil verified only after both checks pass.

### Retrospective backfill

Before the canonical Tamil layer is closed, perform a historical-glyph-only retrospective audit for **PDF 5–74**. Those pages retain their existing visual-fidelity pass unless a historical-glyph correction changes the canonical transcription; any changed occurrence must then receive a local visual recheck.

No structured derivatives, English translation or reader release may treat the whole Tamil layer as verified until this retrospective backfill and the forward combined audit both reach **105/105**.

## Per-page record template

```markdown
### PDF <n> / logical printed p.<n>

- visual fidelity: `pass | pending | needs-review`
- historical-glyph audit: `pass | pending | needs-review`
- full known family set checked: yes/no
- historical families observed: `<families or none>`
- corrections:
  - earlier/apparent reading: `...`
  - source-supported Unicode reading: `...`
  - historical family: `...`
  - evidence: enlarged source pixels / same-edition comparison
- unresolved clusters: `<none or details>`
- final Tamil status: `verified | needs-review | pending`
```

## Initial range status

| PDF range | Logical printed range | Visual fidelity | Historical glyph audit | Final Tamil |
|---|---|---|---|---|
| 5–74 | 3–72 | pass — 70 pages | retrospective pass required | not yet dual-gate verified |
| 75–109 | 73–107 | pending — 35 pages | pending — run together with visual audit | pending |

## Release gate

The Tamil source layer closes only when:

- visual source-fidelity audit = **105/105 pass**;
- historical-Tamil-glyph audit = **105/105 pass**;
- unresolved source/glyph review pages = **0**;
- all scan-supported corrections are synchronized into canonical full text and retained provenance;
- any correction to previously visually verified text has received local recheck and explicit audit notation.
