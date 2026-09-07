# நாம் — Canonical Tamil Transcription

Controlling source: `TVA_BOK_0064201_நாம்.pdf`

## Current checkpoint

- canonical range expected: **PDF 5–71 / 67 pages**;
- first-pass completed: **PDF 5–29 / 25 pages**;
- current first-pass status: **partial-first-pass**;
- verified pages: **0**;
- separate visual-fidelity audit: **not-started**;
- historical-glyph pages checked during first pass: **25/67**;
- historical-glyph final verified pages: **0/67**;
- open source uncertainty markers: **2**;
- completed batches: `parts/pdf-005-009.md`, `parts/pdf-010-014.md`, `parts/pdf-015-019.md`, `parts/pdf-020-024.md`, `parts/pdf-025-029.md`;
- current batch: `parts/pdf-025-029.md`;
- index: `index.json`.

The first pass is deliberately not the verification gate. A page remains draft/needs-review until direct source comparison and the historical-Tamil-glyph gate both close.

## Source anchors

- PDF 5: screenplay opening / `காட்சி 1`; printed numeral is not securely visible, so no printed-page value is manufactured;
- PDF 6–29: visible printed numerals 6–29, one-to-one with the PDF pages.

## Historical glyph handling

Binding guide: `../../../docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`.

Every page is inspected at enlarged/native resolution for at least:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

Examples established so far:

- PDF 6 `அவளை`: historical `ளை` identity was decoded rather than copying the apparent modern-lookalike shape;
- PDF 6 `சூரியனால்`: the `னா` family was explicitly checked before Unicode transcription;
- PDF 11 `கண்ணாடிச்`: positive `ணா`-family occurrence checked against the enlarged source;
- PDF 21 `நீதானா...?`: old `னா` can visually resemble modern `னு`; source-supported Unicode is `நீதானா...?`, not `நீதானு...?`;
- PDF 26 `அலைந்தான்`: source-backed historical `லை` decoding;
- PDF 27 `சாணைக்கல்லிலே` / `சாணைக்கல்லை`: checked historical `ணை` cases;
- PDF 28 `காதலை நான்`: checked against historical `லை` / `னா` forms;
- PDF 29 `அணா`: positive historical `ணா` case.

No global replacement is permitted. Source spelling, colloquial forms, punctuation, ellipses, labels and verse lineation remain source-controlled.

## PDF 15–19 source reconciliation

The third batch was rechecked against enlarged pixels before checkpoint synchronization. Five local first-pass readings were corrected without modernizing the source:

- PDF 15 `எல்லோருக்கும்`;
- PDF 15 `உருண்டோடிடுமே`;
- PDF 17 `அவன் கை வலி`;
- PDF 19 `என்னே`;
- PDF 19 `என் மருமகளும்`.

The source-irregular forms `பிரேமா வாகவர்`, PDF 17's extended labour/tax rhetoric, and PDF 19 `சோபிதத்தை` / `காதியின்` remain source-controlled.

See `../notes/textual-notes-pdf-015-019.md` for the full decision log.

## PDF 20–24 source decisions

The fourth batch continues `காட்சி 9`, contains source heading `காட்சி-10.`, and opens `காட்சி 11`.

Source-specific decisions include:

- PDF 20 retains `போறு ஞானம்!` and `பாய்சன்!` as printed;
- PDF 21 historical-`னா` decoding gives `நீதானா...?`, not the modern-lookalike `நீதானு...?`;
- PDF 21 retains colloquial `மாடெல்லே`, `முன்னாடியே`, `வர்றியே`, `ஓடணும்`, `ஒண்ணும்`;
- PDF 22 preserves standalone `எங்கம்மா?` without manufacturing a speaker label;
- PDF 23 retains source-visible `தூர பந்து`, `மட்டாக`, `காலராவா? ஜன்னியா?`;
- PDF 24 retains `கெளரவம்` in the source-visible spelling;
- PDF 20–24 introduced **0 new explicit uncertainty markers**.

See `../notes/textual-notes-pdf-020-024.md` for the batch decision log.

## PDF 25–29 source decisions

The fifth batch contains `காட்சி 12`, `காட்சி 13`, and opens `காட்சி 14`.

Source-specific decisions include:

- PDF 25 preserves the source speaker forms `சஞ்சீவி` / shortened `சஞ்` and introduces no new uncertainty;
- PDF 26 retains `தயாரப்பட்ட விஷம்`, `மதோன்மத்த வம்சத்தின்`, `மண்ணுங்கட்டியாவது`, and `சுத்தப் பைத்தியக்காரனு`; `அலைந்தான்` is a checked historical-`லை` case;
- PDF 27 preserves `உயில் ஒரு வாள்!`, `சாணைக்கல்லிலே`, `சாணைக்கல்லை`, `ஏராளமான சம்பத்துகள்`, and `ஏமாற்றத்தையும் ஏணிப்படியாக்கிக்`;
- PDF 28 preserves the unlabeled continuation `என் பிரேமா...இவ்வளவு நேரம்?`, source `லஷ்மி`, the unlabeled `வேண்டாம்! இங்கே கொண்டுவா.`, and `ஜமீன்தாரணி யாக்க`; `காதலை நான்` is checked against historical `லை` / `னா`;
- PDF 29 preserves `காண்டிராக்ட்காரன்` and the payment wording `ஒரு அணா!` / `ஒரு அணா.`; `அணா` is a positive historical-`ணா` case;
- PDF 25–29 introduced **0 new explicit uncertainty markers**.

See `../notes/textual-notes-pdf-025-029.md` for the batch decision log.

## Performance / lyric evidence encountered so far

- PDF 16 / `காட்சி 7` visibly prints `[பாட்டு]` followed by the three numbered booklet verses of **`ஆயிரம் தெய்வங்கள்`**. PDF 4 specifically credits this item to **பாரதியார்**; no outside lyric source was used.
- PDF 18 / `காட்சி 8` contains a source-confirmed lineated lyrical duet labelled `குமரன்`, `மீனு`, and `இருவர்`, beginning `பேசும் யாழே பெண் மானே`. It has no item-level author credit on that page and remains **authorship not adjudicated**.
- PDF 15's quoted `ஓரிடந்தனிலே...` fragment remains dialogue-owned and is not promoted into a reconstructed standalone song.
- PDF 20–29 introduces no newly distinct standalone song/lyric block.

## Open uncertainties

The cumulative explicit uncertainty count remains **2**:

1. PDF 5: part of the opening introductory prose line is physically damaged / too unclear for a responsible reading.
2. PDF 9: one word in the montage/action paragraph after `(நாட்கள் பல கடந்தன)` remains unclear; the draft records the visible approximate cluster rather than silently normalizing it.

PDF 10–29 introduced **0 new explicit uncertainty markers**.

## Next activity

**Continue the first-pass canonical Tamil transcription with PDF 30–34, preserving source order, stable page anchors and page-level historical-glyph checks.** Do not mark the completed first-pass pages verified yet.
