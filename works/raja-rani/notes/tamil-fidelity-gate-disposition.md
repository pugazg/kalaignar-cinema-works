# ராஜா ராணி — Tamil Fidelity Gate Disposition

## Purpose

This note closes the **visual-fidelity audit phase** for the supplied `TVA_BOK_0017188_ராஜா_ராணி.pdf` scan without pretending that every source page is fully recoverable.

The rendered scan remains the controlling source. OCR, film audio, subtitles, web quotations, later editions, memory and semantic reconstruction are not canonical evidence.

## Audit coverage

The canonical source-order layer has been visually audited in full:

- source-order canonical range: **PDF 1–79 — 79/79 pages audited**;
- screenplay range: **PDF 10–79 / printed pp.9–78 — 70/70 pages audited**;
- verified source pages: **75/79**;
- review source pages: **4/79 — PDF 27, 48, 57 and 74**;
- verified screenplay pages: **66/70**;
- review screenplay pages: **4/70 — PDF 27, 48, 57 and 74**.

The earlier targeted high-resolution review is documented in `visual-fidelity-targeted-review-001.md`.

## Final disposition of the four remaining pages

### PDF 27 / printed p.26 — review retained

The washed/faint word in Rani's internal monologue cannot be made sufficiently secure from the supplied scan. The canonical layer therefore retains the explicit uncertainty `⟦நீ?⟧` rather than inferring the word from grammar, context or another edition.

Disposition: **unresolved glyph uncertainty in supplied scan**.

### PDF 48 / printed p.47 — review retained

High-resolution review has already restored source-visible `ராசா:` variants and `எடுத்துகிட்டு`. Two short spans in Raja's recollection immediately before `சமரசம் வீடு` remain visually insecure.

Disposition: **unresolved glyph uncertainty in supplied scan**.

### PDF 57 / printed p.56 — review retained

Repeated enlarged inspection confirms the line begins `என்னடா இது, முன்னுக்கு பின்...`, but the following compact colloquial word group is still not sufficiently unambiguous for verified promotion. A plausible linguistic reading is not substituted for visual evidence.

Disposition: **unresolved glyph uncertainty in supplied scan**.

### PDF 74 / printed p.73 — review retained

A later ownership/address overprint beginning `K. N. சங்கரன்` physically overlaps original source printing in the upper-right region. This is not merely a low-confidence glyph reading: part of the original printing is physically obstructed in the supplied scan.

The later overprint is non-canonical. Text hidden by it is not reconstructed from context, another edition, film audio, subtitles or OCR.

Disposition: **irreducible physical source obstruction in the supplied scan** unless a cleaner source image is later supplied.

## Gate decision

The **visual-fidelity audit phase is complete with documented source limitations**.

This does **not** promote PDF 27, 48, 57 or 74 to `verified`, and it does not change the verified-page counts. Those four page records remain `review`.

The Tamil fidelity gate is therefore closed only in the following archival sense:

> the supplied scan has been exhausted through full-range audit plus targeted high-resolution reinspection, and the remaining uncertainty is explicitly bounded rather than silently repaired.

## Downstream eligibility policy

Structured derivatives may now begin, but only from **verified Tamil source units**.

1. A scene index / segmentation map may represent the whole screenplay structurally, including blocked scenes, because it records source-supported boundaries rather than asserting textual verification.
2. A scene-text derivative may be marked verified/complete only when all Tamil source material included in that derivative is verified.
3. Any scene intersecting **PDF 27, 48, 57 or 74** is **blocked for verified scene-text derivation** until the affected source reading is resolved from a stronger source.
4. Dialogue records may be created only from explicitly speaker-labelled utterances whose source text is verified; no unresolved span is converted into an immutable verified dialogue record.
5. English translation begins only for corresponding verified Tamil source units. Review/obstructed Tamil must remain excluded or explicitly blocked; it must not be translated as if settled.
6. Character/entity and song/performance work may use verified source evidence but must not treat unresolved page text as verified evidence.
7. If a cleaner scan later resolves one of these pages, reopen that page, record the source-backed correction, then unblock only the affected downstream records.

## Phase status after this disposition

- source intake: **complete**;
- structural mapping: **complete**;
- canonical Tamil first pass: **complete as draft**;
- rendered-scan fidelity audit: **complete-with-source-limitations**;
- page verification: **75 verified / 4 review**;
- screenplay verification: **66 verified / 4 review**;
- Tamil fidelity gate: **closed-with-source-limitations**;
- scene segmentation/index: **eligible to begin**;
- verified scene-text derivatives: **eligible only for scenes not intersecting PDF 27, 48, 57 or 74**;
- dialogue / translation: **eligible only from verified Tamil units**.

## Next activity

Build the **source-supported scene segmentation and scene-text derivative eligibility map** for PDF 10–79. Derive boundaries only from verified source-visible separators/headings and clear dramatic transitions; do not use page breaks alone. Mark every scene intersecting PDF 27, 48, 57 or 74 as blocked for verified scene-text output, while allowing fully verified scenes to proceed.
