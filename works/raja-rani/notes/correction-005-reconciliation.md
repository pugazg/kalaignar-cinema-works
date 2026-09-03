# Raja Rani — Correction 005 downstream reconciliation

Status: **content reconciliation and QA passed; shared repository mirror sync pending**

This note tracks downstream reconciliation after the late manual source-correction campaign recorded as Correction 005. Canonical Tamil page files remain authoritative.

## Invariants

- Controlling screenplay span: PDF 10–79; PDF 80 is the blank back cover.
- Review/source-limited pages remain PDF 27, 48, 57 and 74.
- Blocked scenes are not reconstructed from review-limited pages.
- Existing dialogue IDs, scene IDs, translation unit IDs and page provenance remain stable unless the source unit itself changes structurally.
- Corrected exact speaker labels propagate without normalization.
- Existing English records were reconciled only where their Tamil source changed; no new translation scenes were added during this correction gate.

## Canonical-to-scene / dialogue propagation — complete

The source-order Correction 005 propagation pass is complete for every eligible scene through the end of the screenplay. Existing scene and dialogue IDs/provenance were retained.

- scenes 001–007 / dialogue shards 001–007 — reconciled through PDF 21;
- scene 009 / dialogue shard 009 — reconciled across PDFs 21–25;
- scene 015 / dialogue shard 015 — reconciled across PDFs 28–30;
- scene 016 / dialogue shard 016;
- scene 017 / dialogue shard 017 — reconciled across PDFs 31–33, including exact source speaker-label occurrence `தர்யம்` without normalization;
- scene 018 / dialogue shard 018 — reconciled across PDFs 33–35;
- scene 021 / dialogue shard 021 — reconciled across PDFs 35–38, including its PDF 37→38 cross-page record/page segments;
- scene 023 / dialogue shard 023 — reconciled across PDFs 38–40;
- scene 024 / dialogue shard 024 — corrected `அகல்யா நாடக ஒத்திகை` material across PDFs 40–42;
- scene 025 / dialogue shard 025 — PDFs 42–43;
- scene 026 / dialogue shard 026 — PDF 43 `முத்திப்போச்சா`;
- scene 028 / dialogue shard 028 — PDFs 44–46;
- scene 034 / dialogue shard 034 — PDF 52 speaker-label correction; stable `raja-rani-s034-d060` retained;
- scene 040 / dialogue shard 040 — PDFs 58–59, including the cross-page record and page-segment correction;
- scene 041 / dialogue shard 041 — PDFs 59–61;
- scene 044 / dialogue shard 044 — PDFs 61–63, including the cross-page final record and page segments;
- scene 045 / dialogue shard 045 — PDFs 63–64;
- scene 046 / dialogue shard 046 — PDFs 64–65, including its cross-page record and page segments;
- scenes 048–050 / dialogue shards 048–050 — reconciled across the PDF 65–67 frontier;
- scene 051 / dialogue shard 051 — reconciled across PDFs 67–70, including its PDF 69→70 cross-page record/page segments;
- scene 052 / dialogue shard 052 — corrected Socrates material across PDFs 70–73;
- scene 056 — checked against corrected PDF 77 and requires no derivative text change;
- scenes 057–058 / dialogue shards 057–058 — final manual corrections across PDFs 77–79.

## Checked / no derivative text change required

- scenes 008, 010, 014, 027, 029–031, 035–038, 043, 047 and 056;
- scene 032 had the stage-only PDF 46 correction `கலகம் ஏற்பட`; it has no dialogue record to reconcile;
- scene 042 had the stage-only PDF 61 correction `சிபார்சு`; it has no dialogue record to reconcile.

## Intentionally blocked scenes

The following remain blocked because they intersect the bounded review/source-limited pages PDF 27, 48, 57 or 74:

- scenes 011–013 — PDF 27;
- scene 033 — PDF 48;
- scene 039 — PDF 57;
- scenes 053–055 — PDF 74.

## Existing English records — reconciled / audited

All English records that existed at the time of Correction 005 have now been checked against the corrected source.

- English scene 001: verified wording remains valid; source-fidelity note synchronized to corrected Tamil.
- English scenes 002–005: reconciliation completed without changing scene IDs, unit IDs, dialogue links or counts. Historical batch remains **98 units / 93 immutable dialogue links**.
- English scene 006: affected PDF-19 source correction reconciled without adding new translation work.
- English scenes 007–010: source changes audited; existing English remains semantically valid. Scene 009 retains the contextual English stage reading for source-exact `போர்வையை விளக்க` without changing canonical Tamil.
- English scene 014: no Correction 005 translation change required.
- English scene 015: `raja-rani-en-s015-u020` now preserves source `கிரஷ்` as `Crush` instead of stale `refreshment`; ID/link/provenance unchanged.
- English scene 016: corrected Tamil variants are semantic-neutral in English; no record rewrite required.
- English scene 017: `raja-rani-en-s017-u017.source.speaker_label` now preserves exact source `தர்யம்`; separate genuine `தாயம்` occurrences remain unchanged.
- English scene 018: corrected Tamil variants were audited and existing English sense remains valid.

Current verified translation coverage after synchronizing the previously stale translation index:

- translated eligible scenes: **15 / 50** — scenes 1–10 and 14–18;
- translation units: **387 verified**;
- immutable dialogue links: **338 / 338 expected**;
- source-unlabelled spoken units: **8**;
- cross-page translation units: **4**;
- translated screenplay performance occurrences: **2**;
- unit mix: **346 dialogue / 37 stage direction / 2 performance cue / 2 written text**.

## Character/entity reconciliation — complete

The corrected source label `தர்யம்` is retained as a distinct exact source label and mapped to the existing Thayammal entity. The scene-034 `ராஜா`→`ராணி` ownership correction introduces no new label/entity.

Current character census:

- distinct exact source labels: **75**;
- labels dispositioned: **75/75**;
- entities / roles / collectives: **42**;
- verified entities: **42**;
- review/unresolved labels or entities: **0**.

## Song/performance reconciliation — complete

Correction 005 affected numbered-song source wording on songs **1, 3, 4, 7, 8 and 11**. Those Tamil derivatives were reconciled to the corrected canonical pages. Machine-readable source excerpts, derivative title lists, and the song-8 cross-witness source quotation were synchronized.

Authorship and occurrence-link dispositions were deliberately not promoted or otherwise changed.

Current song census:

- numbered song blocks / verified Tamil derivatives: **11/11**;
- screenplay singing references: **4**;
- total candidate occurrences: **15**;
- numbered songs anthology-attributed to Kalaignar: **5** — 3, 5, 6, 7, 8;
- numbered songs with unresolved lyricist: **6** — 1, 2, 4, 9, 10, 11;
- original-booklet item-level lyricist credits: **0**.

Performance links remain:

- scene 4 → song 3: verified;
- scene 16 → song 5: verified;
- scene 40 → song 8: verified;
- scene 58 → song 11: review.

## QA / count-consistency result — PASS

The live layer indexes now reconcile numerically:

- dialogue index: **892 records / 50 eligible scenes / 8 blocked scenes / 11 cross-page records / 3 source-label anomalies**;
- character index: **75/75 exact labels / 42 entities**;
- song index: **11 numbered + 4 screenplay references = 15 occurrences; 5 verified-attribution + 6 unresolved**;
- translation index: **15/50 scenes / 387 units / 338/338 immutable dialogue links**.

The dialogue count underlying the translated scenes also reconciles directly:

- translated scenes 1–10 contain **203** immutable dialogue records;
- translated scenes 14–18 contain **135**;
- cumulative expected = **338**, equal to the translation index's **338 linked** records.

The translation unit census also reconciles:

- prior 1–10 checkpoint: **234** units;
- scenes 14–18 batch: **153** units;
- cumulative: **387** units.

No content-layer inconsistency remains from Correction 005.

## Status synchronization

Raja Rani-local authoritative surfaces have been synchronized:

- `translations/index.json` and `translations/README.md` now report **15/50 scenes / 387 units**;
- `BATCH_014_018_REVIEW.md` records its post-Correction-005 audit;
- `characters/index.json` reports **75/75 / 42** with no character reconciliation pending;
- `songs/index.json`, inventory, affected song derivatives and song documentation are current;
- `docs/HANDOVER_RAJA_RANI.md` and `docs/NEXT_CHAT_PROMPT_RAJA_RANI.md` now point to English scenes **19–23**.

One shared repository mirror remains stale at this checkpoint:

- `data/works.json` still contains the older Raja Rani mirror values (**74 labels, pilot-only 1 translated scene / 11 units, next scenes 2–5**).

The connected GitHub action available in this session performs whole-file replacement only. `data/works.json` is a large one-line registry containing many unrelated works, so it has intentionally **not** been rewritten from a partial snippet merely to update Raja Rani. The root README should likewise not be declared synchronized until its Raja Rani mirror is safely checked/updated together with this registry.

Therefore the **content reconciliation and QA gate has passed**, but formal repository-wide mirror synchronization remains pending. Do not treat the stale shared mirror as authority over the Raja Rani-local indexes.

## Next production activity after shared-mirror synchronization

Resume source-linked English translation with verified scenes:

**`raja-rani-s019` through `raja-rani-s023`**.

The refreshed Raja Rani handover and next-chat prompt contain the exact production rules and current counts.

## Current checkpoint

Live `main` should be fetched again before any subsequent write. This note is a durable state description, not a substitute for the live branch.
