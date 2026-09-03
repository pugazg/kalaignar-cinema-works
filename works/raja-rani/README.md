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

The title/publication page visibly gives `மலர் மன்றம்`, `விருதுநகர்,` and `விலை அணா 0-8-0`. No explicit edition statement or publication year has been identified in the scan. The final screenplay page has the printer line `அன்பு அச்சகம், மதுரை:-- 56`; the terminal `56` is preserved as printed and is **not** promoted to a publication year without a source label.

## Printed Kalaignar / song credits

The cover directly prints `மு. கருணாநிதி`.

PDF 9 contains a film-wide `பாடல்கள்:` credit roster:

- `மு. கருணாநிதி`
- `ஏ. மருதகாசி`
- `கே. பி. காமாக்ஷி`
- `எம். கே. ஆத்மநாதன்`
- `வில்லிபுத்தன்`
- `விவேகன்`

This establishes film-wide participation only. It does **not** map any one of the 11 numbered song blocks to an individual lyricist.

## Verified source structure

- PDF 1: front cover
- PDF 2: book/title/publication details
- PDF 3: `கதைச் சுருக்கம்`
- PDF 4–first part of PDF 9: **11** numbered `பாட்டு` blocks
- second part of PDF 9: cast / performers / song-credit roster
- PDF 10–79: canonical screenplay/dialogue range, printed pp.9–78
- PDF 80: unnumbered back cover

Printed-page mapping for the screenplay is `printed page = PDF page - 1`.

Embedded dramatic sections:

- `சேரன் செங்குட்டுவன்`: PDF **13–19** / printed pp.12–18
- `அகல்யா நாடக ஒத்திகை`: PDF **40–first part of 41** / printed pp.39–40
- `சாக்ரடீஸ் (நாடகம்)`: PDF **66–first part of 73** / printed pp.65–72 (first part)

The booklet does **not** print numbered screenplay scenes. Archive IDs `raja-rani-s001`–`raja-rani-s058` are navigation derivatives only.

## Canonical Tamil / fidelity gate

Canonical source-order page layer: `pages/001.md`–`079.md`.

Rendered-scan audit:

- audited source pages: **79/79**
- verified source pages: **76**
- review source pages: **3 — PDF 27, 57, 74**
- audited screenplay pages: **70/70**
- verified screenplay pages: **67/70**
- review screenplay pages: **3/70**
- Tamil fidelity gate: **closed-with-source-limitations**

Bounded source limitations now remain only:

- PDF 27 / printed p.26: faint/washed internal-monologue word remains `⟦நீ?⟧`.
- PDF 57 / printed p.56: one compact colloquial group after `என்னடா இது, முன்னுக்கு பின்...` remains unresolved.
- PDF 74 / printed p.73: later `K. N. சங்கரன்` ownership/address overprint physically obscures original source text; hidden text is not reconstructed.

PDF 48 / printed p.47 is no longer a review page. User direct-scan review resolved the two previously insecure spans immediately before `சமரசம் வீடு` as **`வந்தனா`** and **`திடீர்னு`**.

Detailed fidelity history is retained in the visual-audit notes, `notes/tamil-fidelity-gate-disposition.md`, and `notes/post-fidelity-corrections.md`.

## Correction 005 — reconciled

The user-led old-glyph comparison campaign corrected surviving first-pass normalization/spelling errors from direct scan review. The dedicated downstream reconciliation is recorded in `notes/correction-005-reconciliation.md`.

Content reconciliation and count QA are **PASS**. Do not reopen the campaign merely because older notes or copied checkpoints describe it as pending.

Permanent examples include PDF 72 **`சாக்ரடீசின்`**, scene 17 exact source label **`தர்யம்`**, scene 34's corrected `ராணி` ownership occurrence, and the final manually adjudicated PDF 76–79 forms.

## Scene / dialogue / character layers

Source-supported segmentation and verified derivatives are complete with review-source exclusions:

- archival scene segments: **58**
- eligible verified scene-text segments: **51**
- blocked source-review segments: **7**
- completed verified scene-text files: **51/51 eligible**
- immutable dialogue records: **949** across all 51 eligible scenes
- zero-dialogue scenes: **15**
- genuine cross-page dialogue records: **12**
- tracked source-label/delimiter anomalies: **3**
- exact source speaker labels: **75/75 dispositioned**
- entities / roles / collectives: **42**, all verified

Scene 33 is now complete-verified and contains **57 immutable dialogue records**, including one genuine PDF 48→49 cross-page record. It introduces no new speaker-label string or character entity.

Blocked scenes now remain `s011`–`s013` (PDF 27), `s039` (PDF 57), and `s053`–`s055` (PDF 74).

## Song/performance inventory and authorship gate

The source-visible song layer under `songs/` remains complete with unresolved authorship where item-level evidence is absent:

- numbered source `பாட்டு` blocks: **11**
- standalone verified Tamil song derivatives: **11/11**
- screenplay singing references: **4** — scenes 4, 16, 40 and 58
- total inventoried song/singing occurrences: **15**
- later anthology-attributed Kalaignar songs: **5 — songs 3, 5, 6, 7, 8**
- unresolved lyricist: **6 — songs 1, 2, 4, 9, 10, 11**
- original-booklet item-level lyricist credits: **0**

Verified screenplay links remain scene 4→song 3, scene 16→song 5 and scene 40→song 8. Scene 58→song 11 remains review-level.

## English translation — in progress, verified

Source-linked English translation is under `translations/`.

Current checkpoint after `BATCH_024_034_REVIEW.md`:

- production policy: **10 eligible verified scenes per iteration**, skipping blocked scenes while continuing the eligible-scene count;
- eligible verified scenes translated: **30/51**;
- translated scenes: **1–10, 14–32, 34**;
- verified English units: **715**;
- immutable dialogue links: **622/622 expected in translated scenes**;
- unit mix: **633 dialogue / 78 stage direction / 2 performance cue / 2 written text**;
- source-unlabelled spoken units: **11**;
- genuine cross-page English units: **6**;
- translated screenplay song/performance occurrences: **2**;
- front-matter numbered song translations started: **0/11**.

The latest 10-scene iteration translated `s024`–`s032` plus `s034`; scene 33 was correctly skipped because PDF 48 was still unresolved at that time. It added **232 units / 198 immutable dialogue links / 3 source-unlabelled spoken units / 31 stage directions**. Scene 33 is now the first eligible scene in the next translation iteration.

Translation does not modify canonical Tamil, immutable dialogue IDs, character entities or song-authorship dispositions.

## Current gate

- source intake: **complete**
- structural mapping: **complete**
- canonical Tamil first pass: **complete**
- rendered-scan fidelity audit: **complete-with-source-limitations — 76 verified / 3 review**
- Correction 005 content reconciliation / QA: **PASS**
- scene segmentation/index: **complete — 58 segments**
- verified scene-text derivatives: **complete — 51 eligible / 7 blocked**
- dialogue index: **complete — 949 records**
- character/entity index: **complete-verified — 75 labels / 42 entities**
- song/performance authorship derivative: **complete-with-unresolved-authorship — 15 occurrences**
- English translation: **in-progress-verified — 30/51 scenes / 715 units**

`data/works.json` and the root README are shared repository mirrors and may lag this work-local checkpoint. The work-local indexes, metadata, reviews and Raja Rani handover are authoritative for current production until those shared mirrors can be safely synchronized.

## Source rules

- The rendered scan is the controlling source.
- OCR and parsed PDF text are navigation/comparison assistance only.
- Old Tamil glyphs must be read at sufficient enlargement; modern spelling expectations do not decide disputed forms.
- A user's explicit manual verdict from direct scan review controls that reviewed occurrence unless later direct scan evidence reopens it.
- Preserve occurrence-specific variants; no global normalization.
- No silent correction or modernization.
- No invented speakers.
- Song authorship requires item-level evidence.
- Later witnesses do not overwrite this edition's Tamil.
- Translation never repairs or upgrades source uncertainty/authorship.

## Next activity

Process the next **10 eligible verified scenes** for English translation:

`raja-rani-s033`, `s035`, `s036`, `s037`, `s038`, skip blocked `s039`, then `s040`, `s041`, `s042`, `s043`, `s044`.

Preserve exact immutable dialogue links and source labels, source-unlabelled speech, stage/performance structure and physical page crossings. Do not invent speakers, lyrics, scene endings or authorship.
