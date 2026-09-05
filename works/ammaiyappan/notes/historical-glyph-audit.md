# அம்மையப்பன் — Historical Tamil Glyph Audit

## Forward combined-gate checkpoint through PDF 84 — 2026-09-05

- visual fidelity passed: **80/105 — PDF 5–84 / logical pp.3–82**;
- historical-glyph passed: **80/105 — PDF 5–84 / logical pp.3–82**;
- final dual-gate verified: **80/105**;
- PDF 75–84 combined audit: **10/10 PASS**, commit `0da97f94e829bef9b387bf59be580933b97ed122`;
- markers **88–97 resolved**; open markers now **98–116 (19)**;
- next page: **PDF 85 / logical printed p.83**;
- retrospective glyph-backfill range remains **PDF 5–74** and is not redefined by this forward checkpoint.

Controlling source: `TVA_BOK_0064230_அம்மையப்பன்.pdf`

Required guide: `docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`

## Purpose

`அம்மையப்பன்` is a 1954 printed screenplay/dialogue booklet with frequent historical Tamil typeforms. Ordinary visual source-fidelity review is not sufficient by itself because an older glyph can resemble a different modern Tamil character or sequence.

This work therefore has **two independent Tamil verification gates**:

1. **visual source-fidelity audit** — confirms that transcription matches all visible source text, structure, punctuation, labels, line content and page boundaries;
2. **historical-Tamil-glyph audit** — confirms that older Tamil glyph identities have been decoded correctly into modern Unicode without modernization or visual-lookalike substitution.

A canonical page is **final Tamil verified only when both gates pass**.

## Current authoritative closure — 2026-09-05

The retrospective historical-glyph pass for **PDF 5–74 / 70 canonical pages is CLOSED**.

- visual fidelity: **70/105 — PDF 5–74 passed**;
- historical glyph audit: **70/105 — PDF 5–74 passed**;
- final dual-gate verified: **70/105**;
- correction-bearing retrospective pages: **38**;
- correction synchronization: **complete** — `880978627191a122f55b50522d112d163faa7e10`;
- sync manifest/report: `historical-glyph-sync-manifest.json` / `historical-glyph-sync-report.json`;
- global replacement used: **no**;
- genuine controls on PDF 48, 62, 64 and 69: **preserved / PASS**;
- next page: **PDF 75 / logical printed p.73**, with visual fidelity + historical glyph audit together.

The older checkpoint sections below are retained as historical audit evidence. Their `sync-pending` language describes the state *before* commit `880978627191a122f55b50522d112d163faa7e10` and must not be used as the current work status.

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
| `glyph-reviewed / sync-pending` | source pixels have established one or more historical-glyph corrections, but the corrections have not yet been synchronized into every canonical/provenance surface |
| `needs-review` | either gate has unresolved source evidence |

## Coverage plan

### Forward combined audit

Continue from **PDF 75 / logical printed p.73** only after the retrospective backfill through PDF 74 is complete and all backfill corrections are synchronized. Every new visual-fidelity page from PDF 75 onward must simultaneously receive the historical-glyph audit. A page may be promoted to final Tamil verified only after both checks pass.

### Retrospective backfill

Before the canonical Tamil layer is closed, perform a historical-glyph-only retrospective audit for **PDF 5–74**. Those pages retain their existing visual-fidelity pass unless a historical-glyph correction changes the canonical transcription; any changed occurrence must then receive a local visual recheck.

No structured derivatives, English translation or reader release may treat the whole Tamil layer as verified until this retrospective backfill and the forward combined audit both reach **105/105**.

## Per-page record template

```markdown
### PDF <n> / logical printed p.<n>

- visual fidelity: `pass | pending | needs-review`
- historical-glyph audit: `pass | pending | needs-review | reviewed-sync-pending`
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
| 5–74 | 3–72 | pass — 70 pages | retrospective pass required | not yet fully dual-gate verified |
| 75–109 | 73–107 | pending — 35 pages | pending — run together with visual audit | pending |

## Retrospective checkpoint 1 — PDF 1–24

The audit was deliberately restarted from **PDF 1**, per source-review instruction.

- PDF **1–4**: front matter inspected for typeface/reference evidence; these pages are outside the 105-page canonical screenplay count.
- PDF **4** supplies especially clear same-edition reference forms in `விலை எட்டணா` for historical `லை` and `ணா`.
- canonical pages source-reviewed for the historical-glyph gate: **PDF 5–24 = 20/105 pages**.
- pages with no glyph correction required after complete family check: **PDF 7, 11, 12, 18, 21 = 5 pages**.
- those five pages already hold the independent visual-fidelity pass and therefore qualify as `visual-pass / glyph-pass`.
- pages with one or more positively established glyph corrections awaiting canonical/provenance synchronization: **PDF 5, 6, 8, 9, 10, 13, 14, 15, 16, 17, 19, 20, 22, 23, 24 = 15 pages**.
- no global replacement was used. Every reading below was adjudicated occurrence-by-occurrence from the rendered scan, with same-edition comparison where needed.
- next retrospective source page: **PDF 25 / printed p.23**.
- PDF 75 forward visual-fidelity work remains blocked until the retrospective pass reaches PDF 74 and the resulting corrections are synchronized.

### Same-edition reference findings

- PDF 4 `விலை எட்டணா` gives clear historical `லை` / `ணா` shapes.
- PDF 8 `சொன்னாரா?` supplies a clear historical `னா` comparison form.
- PDF 11 `நன்று சொன்னீர்` supplies a true `று` comparison against the historical `றா` form encountered on PDF 13.
- the source also contains genuine colloquial modern-looking `ணு`/`னு` sequences; therefore apparent `ணு` or `னு` was never converted merely from linguistic expectation.

### PDF 5 / logical p.3

- visual fidelity: `pass`
- historical-glyph audit: `reviewed-sync-pending`
- full known family set checked: yes
- corrections:
  - `ஒன்றுமில்ல...` → `ஒன்றுமில்லை...` — historical `லை`
  - `உன்னுடையதுதானு?` → `உன்னுடையதுதானா?` — historical `னா`
- unresolved glyph clusters: none

### PDF 6 / printed p.4

- visual fidelity: `pass`
- historical-glyph audit: `reviewed-sync-pending`
- full known family set checked: yes
- corrections:
  - `முத்தண்ணு` → `முத்தண்ணா` — historical `ணா`
  - `சுகந்தானு?` → `சுகந்தானா?` — historical `னா`
  - `அப்பாவையும் தானு!` → `அப்பாவையும் தானா!` — historical `னா`
- unresolved glyph clusters: none

### PDF 7 / printed p.5

- visual fidelity: `pass`
- historical-glyph audit: `pass`
- full known family set checked: yes
- corrections: none
- unresolved glyph clusters: none
- final Tamil status: `verified`

### PDF 8 / printed p.6

- visual fidelity: `pass`
- historical-glyph audit: `reviewed-sync-pending`
- full known family set checked: yes
- corrections:
  - `இல்ல ஊதியம்...` → `இல்லை ஊதியம்...` — historical `லை`
- note: source-visible `சொன்னாரா?` occurrences are already correctly decoded and serve as same-edition `னா` witnesses.
- unresolved glyph clusters: none

### PDF 9 / printed p.7

- visual fidelity: `pass`
- historical-glyph audit: `reviewed-sync-pending`
- full known family set checked: yes
- corrections:
  - `வழக்கம் தானே அண்ணு இது!...` → `வழக்கம் தானே அண்ணா இது!...` — historical `ணா`
- unresolved glyph clusters: none

### PDF 10 / printed p.8

- visual fidelity: `pass`
- historical-glyph audit: `reviewed-sync-pending`
- full known family set checked: yes
- corrections:
  - `பருவமோ இல்ல எனக்கு` → `பருவமோ இல்லை எனக்கு` — historical `லை`
- unresolved glyph clusters: none

### PDF 11 / printed p.9

- visual fidelity: `pass`
- historical-glyph audit: `pass`
- full known family set checked: yes
- corrections: none
- same-edition witness: `நன்று சொன்னீர்` is a true `று` occurrence used to distinguish PDF 13 historical `றா`.
- final Tamil status: `verified`

### PDF 12 / printed p.10

- visual fidelity: `pass`
- historical-glyph audit: `pass`
- full known family set checked: yes
- corrections: none
- final Tamil status: `verified`

### PDF 13 / printed p.11

- visual fidelity: `pass`
- historical-glyph audit: `reviewed-sync-pending`
- full known family set checked: yes
- corrections:
  - `லட்சணம் நன்றுயிருக்கிறது` → `லட்சணம் நன்றாயிருக்கிறது` — historical `றா`
- evidence: enlarged source pixels plus direct same-edition comparison with PDF 11 `நன்று`; only character identity changes, preserving the source's joined wording/sandhi.
- unresolved glyph clusters: none

### PDF 14 / printed p.12

- visual fidelity: `pass`
- historical-glyph audit: `reviewed-sync-pending`
- full known family set checked: yes
- corrections:
  - `இப்ப என்னு வாள் பயிற்சி` → `இப்ப என்னா வாள் பயிற்சி` — historical `னா`
  - `வாள் வீரனு விடலாம்.` → `வாள் வீரனா விடலாம்.` — historical `னா`
  - `என்ன! வாள் வீரனு?...` → `என்ன! வாள் வீரனா?...` — historical `னா`
  - `பரவா இல்ல...` → `பரவா இல்லை...` — historical `லை`
- evidence: the apparent `னு` form was compared directly with same-edition PDF 8 `சொன்னாரா?` and supports historical `னா` identity.
- unresolved glyph clusters: none

### PDF 15 / printed p.13

- visual fidelity: `pass`
- historical-glyph audit: `reviewed-sync-pending`
- full known family set checked: yes
- corrections:
  - `இலக்கணமே எனக்குத் தேவை இல்ல.` → `இலக்கணமே எனக்குத் தேவை இல்லை.` — historical `லை`
- unresolved glyph clusters: none

### PDF 16 / printed p.14

- visual fidelity: `pass`
- historical-glyph audit: `reviewed-sync-pending`
- full known family set checked: yes
- corrections:
  - `பரவா இல்ல முத்தா` → `பரவா இல்லை முத்தா` — historical `லை`
  - `ஒன்றுமில்ல முத்தா` → `ஒன்றுமில்லை முத்தா` — historical `லை`
  - `இல்ல தம்பி.` → `இல்லை தம்பி.` — historical `லை`
  - `உயிரை வாங்குறானு?` → `உயிரை வாங்குறானா?` — historical `னா`
  - `ஆணுகப் பிறக்கிறதோ?` → `ஆணாகப் பிறக்கிறதோ?` — historical `ணா`
  - `இல்ல தம்பி இல்ல.` → `இல்லை தம்பி இல்லை.` — historical `லை` at both occurrences
- unresolved glyph clusters: none

### PDF 17 / printed p.15

- visual fidelity: `pass`
- historical-glyph audit: `reviewed-sync-pending`
- full known family set checked: yes
- corrections:
  - `அழைப்பதில்ல.` → `அழைப்பதில்லை.` — historical `லை`
  - `இல்ல தம்பி.` → `இல்லை தம்பி.` — historical `லை`
  - `சரிதானு?` → `சரிதானா?` — historical `னா`
- unresolved glyph clusters: none

### PDF 18 / printed p.16

- visual fidelity: `pass`
- historical-glyph audit: `pass`
- full known family set checked: yes
- corrections: none
- unresolved glyph clusters: none
- final Tamil status: `verified`

### PDF 19 / printed p.17

- visual fidelity: `pass`
- historical-glyph audit: `reviewed-sync-pending`
- full known family set checked: yes
- corrections:
  - `யாருமில்ல...` → `யாருமில்லை...` — historical `லை`
  - `சொல்லிவிட்டேனு என்ன?` → `சொல்லிவிட்டேனா என்ன?` — historical `னா`
- unresolved glyph clusters: none

### PDF 20 / printed p.18

- visual fidelity: `pass`
- historical-glyph audit: `reviewed-sync-pending`
- full known family set checked: yes
- corrections:
  - `இல்ல...இல்ல...மன்னிக்கவும்` → `இல்லை...இல்லை...மன்னிக்கவும்` — historical `லை` at both occurrences
- unresolved glyph clusters: none

### PDF 21 / printed p.19

- visual fidelity: `pass`
- historical-glyph audit: `pass`
- full known family set checked: yes
- corrections: none
- source-visible forms such as `இல்லையா`, `இல்லையே`, `கண்ணப்ப`, and `நாயனாரோ` are already correctly decoded.
- final Tamil status: `verified`

### PDF 22 / printed p.20

- visual fidelity: `pass`
- historical-glyph audit: `reviewed-sync-pending`
- full known family set checked: yes
- corrections:
  - `அதெல்லாம் ஒன்றுமில்ல.` → `அதெல்லாம் ஒன்றுமில்லை.` — historical `லை`
  - `இல்ல தம்பி...` → `இல்லை தம்பி...` — historical `லை`
- unresolved glyph clusters: none

### PDF 23 / printed p.21

- visual fidelity: `pass`
- historical-glyph audit: `reviewed-sync-pending`
- full known family set checked: yes
- corrections:
  - `அது இல்ல தம்பி-` → `அது இல்லை தம்பி-` — historical `லை`
- unresolved glyph clusters: none

### PDF 24 / printed p.22

- visual fidelity: `pass`
- historical-glyph audit: `reviewed-sync-pending`
- full known family set checked: yes
- corrections:
  - `கண்ணுளா...` → `கண்ணா...` — historical `ணா`; the word crosses the source line boundary, with `கண்` at the line end and the historical `ணா` form at the next line start.
- unresolved glyph clusters: none

## Synchronization rule for checkpoint 1

The fifteen correction-bearing pages above **must not** be counted as glyph-pass merely because the source reading has been established. Their canonical `full-text.md` occurrences and any retained provenance copy must first be corrected occurrence-by-occurrence, followed by a local visual recheck of every changed occurrence. Until then their status is `glyph-reviewed / sync-pending`.

The five clean pages **7, 11, 12, 18, 21** require no canonical text change and can immediately retain the existing visual pass plus the new glyph pass.

## Release gate

The Tamil source layer closes only when:

- visual source-fidelity audit = **105/105 pass**;
- historical-Tamil-glyph audit = **105/105 pass**;
- unresolved source/glyph review pages = **0**;
- all scan-supported corrections are synchronized into canonical full text and retained provenance;
- any correction to previously visually verified text has received local recheck and explicit audit notation.
