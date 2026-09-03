# ராஜா ராணி

## Source status

Source: `TVA_BOK_0017188_ராஜா_ராணி.pdf`

Source/archive identifier used by the archive: `TVA_BOK_0017188` (from the supplied/archive filename; not observed as a printed identifier in the scan).

Classification: full dialogue/screenplay publication with songs.

Physical scan:

- PDF pages: **80**
- byte size: **31,600,388**
- SHA-256: `26ecc026b89deafac94bb3b107ee7c5f361c68796c4a1cdf4d01ad7c1c0d31a4`
- embedded OCR text layer: **present**, navigation aid only; rendered scan remains canonical

The title leaf prints **`ராஜா ராணி`**. The cover presents **`ராஜாராணி`** without a clearly visible word gap and directly prints **`மு. கருணாநிதி`** beneath it. The cover does not print a role label next to that name.

The title/publication page visibly gives:

- `மலர் மன்றம்`
- `விருதுநகர்,`
- `விலை அணா 0-8-0`

No explicit edition statement or publication year has been identified in the scan. The final screenplay page has the printer line `அன்பு அச்சகம், மதுரை:-- 56`; the terminal `56` is preserved as printed and is **not** promoted to a publication year without a source label.

## Printed Kalaignar / song credits

The cover directly prints `மு. கருணாநிதி`.

PDF 9 contains a film-wide `பாடல்கள்:` credit roster:

- `மு. கருணாநிதி`
- `ஏ. மருதகாசி`
- `கே. பி. காமாக்ஷி`
- `எம். கே. ஆத்மநாதன்`
- `வில்லிபுத்தன்`
- `விவேகன்`

This roster establishes film-wide participation only. It does **not** map any one of the 11 numbered song blocks to an individual lyricist.

## Verified source structure

- PDF 1: front cover
- PDF 2: book/title/publication details
- PDF 3: `கதைச் சுருக்கம்`
- PDF 4–first part of PDF 9: songs/performance text — **11** numbered `பாட்டு` blocks
- second part of PDF 9: cast / performers / song-credit roster
- PDF 10–79: canonical screenplay/dialogue range (printed pp.9–78)
- PDF 80: unnumbered back cover

Printed-page mapping for the screenplay is `printed page = PDF page - 1`: PDF 10 → printed p.9 and PDF 79 → printed p.78.

Embedded dramatic sections:

- `சேரன் செங்குட்டுவன்`: PDF **13–19** / printed pp.12–18
- `அகல்யா நாடக ஒத்திகை`: PDF **40–first part of 41** / printed pp.39–40
- `சாக்ரடீஸ் (நாடகம்)`: PDF **66–first part of 73** / printed pp.65–72 (first part)

The Socrates boundary is source-verified: PDF 72 ends during Samarasam's staged-performance intervention; PDF 73 continues through the real-poison revelation, police arrival and Babu's arrest; only the following rule–star–rule ornament returns to parent-film `(மனப் போராட்டம்)`.

The booklet does **not** print numbered screenplay scenes.

## Canonical Tamil and fidelity gate

Canonical source-order page layer:

- `pages/001.md`–`079.md`
- screenplay PDF **10–79 / printed pp.9–78 — 70/70 pages**

Rendered-scan visual audit:

- audited source pages: **79/79**
- verified source pages: **75**
- review source pages: **4 — PDF 27, 48, 57, 74**
- audited screenplay pages: **70/70**
- verified screenplay pages: **66/70**
- review screenplay pages: **4/70**
- Tamil fidelity gate: **closed-with-source-limitations, with a late manual correction/reconciliation cycle now open**

Bounded source limitations:

- PDF 27 / printed p.26: faint/washed internal-monologue word remains `⟦நீ?⟧`.
- PDF 48 / printed p.47: two short spans before `சமரசம் வீடு` remain visually insecure.
- PDF 57 / printed p.56: one compact colloquial group remains unresolved after `என்னடா இது, முன்னுக்கு பின்...`.
- PDF 74 / printed p.73: later `K. N. சங்கரன்` ownership/address overprint physically obscures original source text; hidden text is not reconstructed.

The complete audit history is retained in `notes/visual-fidelity-audit-batch-001.md` through `notes/visual-fidelity-audit-batch-008.md`, `notes/visual-fidelity-targeted-review-001.md`, `notes/tamil-fidelity-gate-disposition.md` and `notes/post-fidelity-corrections.md`.

## Post-fidelity source corrections

Later source-backed reinspection restored surviving first-pass normalization errors without changing the review-page disposition:

- PDF 49–50: source-visible `ராசா:` dialogue labels restored while distinct printed `ராஜா` forms were retained.
- PDF 53: `ராசா:` labels and T036 `(ராசா, ராணியைக் கொண்டு வந்து விடுகிறான்...)` restored.
- PDF 58–59: exact source alternation of `ராஜா:` / `ராசா:` restored.
- PDF 66: opening Raja/Gnanakkan continuation restored to source-visible `ராசா:`.

A later user-led word/glyph comparison campaign has superseded the earlier assumption that no further verified-span corrections were required. The user manually reviewed disputed old-Tamil glyphs because OCR, parsed PDF text and assistant visual readings repeatedly preferred incorrect modern/familiar forms.

Current late-correction checkpoint:

- pages **56–70**: user-approved manual corrections applied;
- pages **71–75**: user-approved manual corrections applied;
- PDF 72: later clarification applied as **`சாக்ரடீசின்`**;
- pages **51–55**: user manual verdicts exist but must still be checked against live canonical files during the final reconciliation;
- final user **075–080** comparison/correction batch: pending in the next chat;
- downstream reconciliation: intentionally blocked until that final batch is committed.

The detailed record is `notes/post-fidelity-corrections.md`; continuation instructions are in `../../docs/HANDOVER_RAJA_RANI.md` and `../../docs/NEXT_CHAT_PROMPT_RAJA_RANI.md`.

## Scene segmentation / index

Source-supported segmentation is **complete**.

- segmentation audit: `notes/scene-segmentation-audit.md`
- scene index: `scenes/index.json`
- archival scene segments: **58**
- source-numbered scenes: **none**
- eligible verified scene-text segments: **50**
- blocked source-review segments: **8**

Archive IDs `raja-rani-s001`–`raja-rani-s058` and their ordinals are navigation-only.

Blocked segments:

- `s011`, `s012`, `s013` — PDF 27
- `s033` — PDF 48
- `s039` — PDF 57
- `s053`, `s054`, `s055` — PDF 74

## Scene-text derivatives — pre-correction complete; reconciliation pending

The verified scene-text derivative phase was complete with review-source exclusions **before** the late manual glyph/spelling correction campaign.

Completed batch reports:

- `notes/scene-text-batch-001.md` through `notes/scene-text-batch-010.md`

Pre-correction totals:

- archival scene segments: **58**
- eligible scene-text segments: **50**
- completed verified scene-text files: **50/50**
- remaining eligible scene-text files: **0**
- blocked scene segments: **8**

The final Batch 010 resumed only after the blocked PDF-74 scene group at T056 on PDF 77 and completed:

- `scenes/scene-056.md` — `(முன்)` flashback, stopping before T057;
- `scenes/scene-057.md` — present-day return across PDF 77–79, stopping before T058;
- `scenes/scene-058.md` — `★ தோட்டம் ★` through the end of PDF 79, including the closing song cue, `நலம் வாழ்க!`, final ornament and printer line.

No wording from blocked `s053`–`s055` was imported into the final verified derivatives.

During the song gate, one earlier non-dialogue derivative omission was corrected from verified canonical PDF 30: `scenes/scene-016.md` now includes the source separator plus `[ராணி “வேலையில்லாத் தொல்லையில்லை” என்று பாடிக் கொண்டிருக்கிறாள்.]` before the first labelled dialogue.

Because canonical page wording has now changed after these derivatives were built, affected scene files are **reconciliation-pending** until the post-075–080 reconciliation explicitly compares them to the corrected page layer.

## Repository bookkeeping checkpoint

The repository-level Raja Rani work record and root README were maintained as mirrors of the earlier work-local phase state. They must be synchronized again when the late manual correction/reconciliation gate closes. Major earlier phase checkpoints are recorded in `notes/scene-layer-completion-dialogue-initialization.md`, `notes/character-label-inventory.md`, `notes/character-entity-mapping.md`, and `notes/song-performance-authorship-gate.md`.

## Dialogue index — pre-correction complete; reconciliation pending

The immutable dialogue layer is stored under `dialogues/`:

- `dialogues/README.md`
- `dialogues/schema.json`
- `dialogues/index.json`
- `dialogues/records/scene-###.json`

Completed dialogue production before the late correction campaign:

- Batch 001: verified `scene-001.md` through `scene-010.md` — **203 records**
- Batch 002: verified `scene-014.md` through `scene-023.md`, after blocked `s011`–`s013` — **221 records**
- Batch 003: verified `scene-024.md` through `scene-032.md`, stopping before blocked `s033` — **133 records**
- Batch 004: verified `scene-034.md` through `scene-038.md`, after blocked `s033` and stopping before blocked `s039` — **140 records**
- Batch 005: verified `scene-040.md` through `scene-052.md`, after blocked `s039` and stopping before blocked `s053`–`s055` — **165 records**
- Batch 006: verified `scene-056.md` through `scene-058.md`, after blocked `s053`–`s055` — **30 records**

Pre-correction dialogue state:

- eligible verified scenes: **50**
- blocked scenes: **8**
- completed dialogue scenes: **50/50 eligible**
- immutable labelled-dialogue records: **892**
- zero-record scenes: **15 — `s008`, `s010`, `s014`, `s019`, `s020`, `s022`, `s027`, `s029`, `s030`, `s032`, `s037`, `s038`, `s042`, `s043`, `s048`**
- cross-page records: **11**
- tracked non-colon source-label/delimiter anomalies: **3**

Batch 005 added six genuine cross-page records: `s040-d008`, `s044-d011`, `s046-d001`, `s050-d001`, `s051-d025`, and `s052-d011`. Batch 006 added no new cross-page record or delimiter anomaly.

The no-inference rule remains active through the ending. In `s057`, standalone material such as `(சத்தம் கேட்கவே) யாரது...என்னு?`, `சமரசம்...ஏய்...ஏய்...என்னப்பா என்ன தகராறு...?`, and the unlabelled `ஏய்! கொடு இப்படி. ஆளைப்பாரு...போடுங்க...` following a stage direction stays outside immutable dialogue records. In `s058`, `(இருவரும் பாடுகிறார்கள்)`, `நலம் வாழ்க!`, the closing ornament and printer line are not dialogue records.

The eight review-source-blocked archival scenes remain outside the dialogue layer. No unresolved or physically obscured source text was reconstructed simply to produce 58/58 dialogue shards.

Late source-backed corrections may change dialogue text and/or exact `speaker_label` forms. Stable dialogue IDs should be preserved where the source unit remains the same, but affected records must be reconciled against corrected canonical pages before the dialogue layer is again called synchronized.

Batch reports:

- `notes/dialogue-batch-001.md`
- `notes/dialogue-batch-002.md`
- `notes/dialogue-batch-003.md`
- `notes/dialogue-batch-004.md`
- `notes/dialogue-batch-005.md`
- `notes/dialogue-batch-006.md`

## Character/entity index — pre-correction complete; reconciliation conditional

The character/entity derivative was complete under `characters/` before the late correction campaign:

- immutable dialogue records considered: **892/892**;
- eligible verified dialogue scenes: **50/50**;
- distinct exact non-empty `speaker_label` strings: **74**;
- exact labels dispositioned: **74/74**;
- entities / role categories / collectives: **42**;
- verified entities: **42**;
- review entities: **0**;
- unresolved entities: **0**;
- verified labels: **74**;
- review labels: **0**;
- unresolved labels: **0**;
- dialogue records modified: **0**.

Character files:

- `characters/labels-inventory.json`
- `characters/entities.json`
- `characters/index.json`
- `characters/schema.json`
- `notes/character-label-inventory.md`
- `notes/character-entity-mapping.md`

Important context-sensitive mapping decisions are source-backed rather than spelling-driven. In particular, `ரா` in scene 45 maps to **Rani**, not Raja; the stage direction immediately before scene-52 `தாய்:` identifies her as **Geetha's mother / Thayammal**; and scene 57 explicitly introduces **Sangaran** before the `சங்:` label. The short `வேலை` label is represented as a context-sensitive worker/servant role category rather than one falsely continuous physical character.

Embedded dramatic identities in `சேரன் செங்குட்டுவன்`, the `அகல்யா` rehearsal and `சாக்ரடீஸ்` remain distinct from outer-film identities. Exact dialogue labels and delimiters remain immutable.

During reconciliation, re-run exact-label inventory only where corrected source speaker labels can affect it; do not rewrite unaffected entity mappings for style.

## Song/performance inventory and authorship gate — complete with unresolved authorship

The source-visible song layer is complete under `songs/`.

- numbered source `பாட்டு` blocks: **11**
- standalone verified Tamil song derivatives: **11/11** under `songs/tamil/`
- screenplay singing references: **4** — scenes 4, 16, 40 and 58
- total inventoried song/singing occurrences: **15**
- original-booklet item-level lyricist credits: **0**
- numbered songs with later verified Kalaignar-anthology item correspondence: **5**
- numbered songs with unresolved lyricist: **6**

The PDF-9 six-name `பாடல்கள்:` roster remains film-wide only and is not assigned to songs by order, singer or likelihood.

The later verified `works/kalaignar-thirai-isai-paadalgal/` archive provides exact Raja Rani item correspondence for numbered songs **3, 5, 6, 7 and 8**. Those five are recorded at **`anthology-attributed`** tier to `மு. கருணாநிதி`; this is not promoted to original-film primary-source item credit. Numbered songs **1, 2, 4, 9, 10 and 11** remain unresolved.

Cross-witness wording never replaces this booklet. Examples include song 6's source `கொடியவனே` versus the later anthology's `கொடியவளே`, and song 8's source opening `சீலா!...லாலீ!...அது போலீ!...` versus the later anthology's `வீணா!... வாலி!... அது போலி!...`.

Three screenplay links are source-secure: scene 4 → song 3; scene 16 → song 5; scene 40 → song 8. Scene 58's `(இருவரும் பாடுகிறார்கள்)` strongly echoes song 11 but remains a review-level link because the source prints neither the song number nor lyric there. No absent closing lyrics are supplied.

Song files:

- `songs/schema.json`
- `songs/credits.json`
- `songs/cross-witness-evidence.json`
- `songs/inventory.json`
- `songs/index.json`
- `songs/tamil/README.md`
- `songs/tamil/song-001.md` through `songs/tamil/song-011.md`
- `notes/song-performance-authorship-gate.md`

Only re-open song/performance links during reconciliation if a corrected canonical span actually touches one of those cues. Unrelated authorship decisions stay unchanged.

## English translation — pilot verified, expansion paused

The source-linked English layer is initialized under `translations/`.

Pilot: `raja-rani-s001` / PDF 10 / printed p.9.

- translation status: **pilot-verified at the pre-correction checkpoint**
- eligible verified scenes: **50**
- blocked review-source scenes: **8**
- scenes translated and verified: **1/50 eligible**
- verified English units: **11**
- unit mix: **9 dialogue / 2 stage direction**
- immutable dialogue links: **9/9 scene-1 records linked exactly once**
- source-unlabelled spoken units in pilot: **0**
- cross-page English units in pilot: **0**
- song/performance units in pilot: **0**

Files:

- `translations/schema.json`
- `translations/index.json`
- `translations/README.md`
- `translations/PILOT_REVIEW.md`
- `translations/records/scene-001.json`

The pilot establishes source-faithful handling of the colloquial hospital exchange. Exact `டாக்டர்` / `டாக்` speaker labels remain immutable metadata. `Amma` / `amma` and `Appa` are retained where translating them literally would over-specify or flatten the source relationship/register; the broken `அப்படின்னு... அவங்கண்...?` remains a broken `Then... his eyes...?` rather than being repaired into smoother prose.

The 11 numbered front-matter song bodies are not forced into archive scene IDs. They will use a parallel song-linked English record set. Screenplay singing references remain scene units and may link `songs/index.json` only where the source-supported relation is secure.

**Do not expand translation** until the final 075–080 correction batch and the downstream reconciliation are complete. The prior next action `raja-rani-s002`–`s005` is paused.

## Current gate

- source intake: **complete**
- structural mapping: **complete**
- canonical Tamil first pass: **complete as draft**
- rendered-scan fidelity audit: **complete-with-source-limitations**
- late manual glyph/spelling correction campaign: **in progress — 56–75 applied; 51–55 must be checked in reconciliation; final 075–080 pending**
- post-correction downstream reconciliation: **not-started — mandatory immediately after final 075–080 update**
- scene segmentation/index: **pre-correction complete — 58 segments**
- verified scene-text derivatives: **pre-correction complete — reconciliation pending where affected**
- dialogue index: **pre-correction complete — 892 records; reconciliation pending where affected**
- character/entity index: **pre-correction complete-verified — recheck only if corrected labels affect inventory/mapping**
- song/performance authorship derivative: **complete-with-unresolved-authorship — recheck only affected cues**
- English translation: **pilot-verified, expansion paused until reconciliation closes**

## Source rules

- The scan is the controlling source.
- OCR and parsed PDF text are navigation/comparison assistance only.
- Old Tamil glyphs must be read at sufficient enlargement, glyph by glyph; do not let modern spelling expectations decide disputed forms.
- A user's explicit manual verdict from direct scan review controls that reviewed occurrence unless later direct scan evidence reopens it.
- Preserve occurrence-specific variants; no global normalization.
- No silent correction or modernization.
- No invented speakers.
- Song authorship requires item-level evidence.
- Later witnesses do not overwrite this edition's Tamil.
- Translation never repairs or upgrades source uncertainty/authorship.
- Uncertainty remains explicit instead of being repaired from memory or external sources.

## Next activity

Continue in a fresh chat using `../../docs/NEXT_CHAT_PROMPT_RAJA_RANI.md`.

1. Apply the user's final **075–080** comparison/manual corrections first. Page 75 is an intentional overlap and must be rechecked if the new batch includes it.
2. Then perform the mandatory end-to-end reconciliation described in `../../docs/HANDOVER_RAJA_RANI.md` and `notes/post-fidelity-corrections.md`.
3. Reconcile pages **51–55** against the user's earlier manual verdicts during that gate; do not assume they are already synchronized.
4. Propagate corrected canonical text only into affected scene/dialogue/character/song/translation derivatives, preserve stable IDs/provenance, revalidate counts, and synchronize repository metadata.
5. Resume English translation only after the reconciliation is documented and passes.
