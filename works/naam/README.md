# நாம்

Source-first archival workspace for the Kalaignar cinema work **நாம்**.

## Current checkpoint

- source intake: **complete**;
- structural mapping: **verified**;
- canonical Tamil transcription: **partial first pass — PDF 5–29 / 25 of 67 pages**;
- canonical Tamil verified pages: **0**;
- visual fidelity audit: **not-started**;
- historical-Tamil-glyph audit: **partial first pass — 25 pages checked / 0 final-verified**;
- open source uncertainty markers: **2**;
- scene/dialogue/character/song derivatives: **blocked until verified canonical Tamil**;
- English translation / reader / Reading Room: **not-started**.

Current transcription index: `transcription/index.json`  
Completed batches: `transcription/parts/pdf-005-009.md`, `transcription/parts/pdf-010-014.md`, `transcription/parts/pdf-015-019.md`, `transcription/parts/pdf-020-024.md`, `transcription/parts/pdf-025-029.md`  
Current textual notes: `notes/textual-notes-pdf-025-029.md`

## Controlling source

- file: `TVA_BOK_0064201_நாம்.pdf`;
- source identifier: `TVA_BOK_0064201`;
- PDF pages: **72**;
- byte size: **115,948,588**;
- SHA-256: `0f7a54882eb6a5a8f83b29060c771ef18dee2b9e108c8797184de2b97c30b7ad`;
- text layer: **image-only**;
- visible title: **நாம்**;
- visible author: **மு. கருணாநிதி**.

The rendered scan is the controlling textual authority. The source PDF itself is not stored in this repository.

## Source-visible publication / credit evidence

- PDF 1 prints the title, `மு. கருணாநிதி`, price `0-8-0`, and a physically damaged publication line;
- PDF 3 gives the fuller source-visible organization line **`ஆசீர்வாதபுரம் ஆதிதிராவிட நல உரிமைச் சங்கத்தார்`**;
- PDF 4 prints the broad credit **`கதை, வசனம், பாடல்... மு. கருணாநிதி`** and separately credits **`பாட்டு 'ஆயிரம் தெய்வங்கள்'—பாரதியார்.`**;
- PDF 4 also prints `தயாரிப்பாளர் ஜூபிடர் & மேகலா பிக்சர்ஸ்`;
- PDF 72 prints **`அச்சிட்டது ஆதி பிரஸ், சென்னை—12.`**;
- no explicit publication year or edition statement has been located in this scan, so none is inferred.

The Bharathiyar item-level credit is a source-specific exception and must survive the later song/authorship gate. The broad Kalaignar `பாடல்` credit must not be used to overwrite it.

## Source structure

- front matter: **PDF 1–4**;
- screenplay/dialogue text: **PDF 5–71** — **67 pages**;
- back matter / printer imprint: **PDF 72**;
- visible printed numerals: **6–71** on PDF 6–71;
- PDF 5 opens the screenplay but no printed page numeral is visibly established there; do not manufacture one in canonical anchors;
- source-numbered scene headings: **45**, sequential **காட்சி 1–45**;
- numbering gaps / repeats / out-of-order headings observed: **0 / 0 / 0**;
- full scene-start map: `mapping.md`.

Handwritten pencil numbers and marks near upper-right margins are later annotations and are not printed pagination or canonical text.

## Canonical Tamil first-pass checkpoint

PDF **5–29** has now been transcribed as source-order draft material in five five-page batches. The newest batch contains `காட்சி 12`, `காட்சி 13`, and opens `காட்சி 14`.

Safeguards:

- PDF 5 has no invented printed-page number;
- exact speaker labels, stage directions, source colloquial forms, punctuation and verse lineation are retained;
- PDF 6 `அவளை` is treated as a historical-`ளை` glyph-decoding case;
- PDF 6 `சூரியனால்` was checked against the historical `னா` family;
- PDF 11 `கண்ணாடிச்` is a positive `ணா`-family first-pass case;
- scan-backed reconciliation of PDF 15–19 corrected `எல்லோருக்கும்`, `உருண்டோடிடுமே`, `அவன் கை வலி`, `என்னே`, and `என் மருமகளும்`;
- PDF 21 `நீதானா...?` is a historical-`னா` decoding: the old glyph can resemble `நீதானு...?`, but the source-supported Unicode identity is `நீதானா...?`;
- PDF 26 `அலைந்தான்` is source-backed `லை`;
- PDF 27 `சாணைக்கல்லிலே` / `சாணைக்கல்லை` are checked historical-`ணை` cases;
- PDF 28 `காதலை நான்` is checked against historical `லை` / `னா` forms;
- PDF 29 `அணா` is a positive historical-`ணா` case;
- source-irregular forms such as PDF 20 `போறு ஞானம்!`, PDF 21 `மாடெல்லே`, PDF 22 `பாலிலா`, PDF 23 `தூர பந்து` / `மட்டாக`, PDF 24 `கெளரவம்`, and PDF 25–29 `மண்ணுங்கட்டியாவது`, `ஏணிப்படியாக்கிக்`, `லஷ்மி`, `ஜமீன்தாரணி யாக்க`, `காண்டிராக்ட்காரன்` remain unmodernized;
- two source uncertainties remain explicit rather than guessed: a damaged introductory line on PDF 5 and one unclear montage word on PDF 9;
- PDF 10–29 adds **0** new uncertainty markers;
- **0** of the twenty-five first-pass pages are called verified yet.

## Song / verse / performance structures mapped or confirmed so far

High-confidence source-visible structures now include:

1. PDF 16 / காட்சி 7 — explicit `[பாட்டு]`, the source-credited Bharathiyar item **ஆயிரம் தெய்வங்கள்**;
2. PDF 18 / காட்சி 8 — source-visible lyrical duet beginning **`பேசும் யாழே பெண் மானே`**, labelled `குமரன்`, `மீனு`, `இருவர்`; authorship **not adjudicated**;
3. PDF 35–36 / காட்சி 21 — multi-line lyrical block beginning `மணமில்லா மலர் நானம்மா!`;
4. PDF 49–50 / காட்சி 31 — multi-page lyrical block with repeated `(பேதம்)` cues;
5. PDF 59–60 — two poetic/song-like blocks between காட்சி 36 and காட்சி 37;
6. PDF 64 / காட்சி 39 — explicit **`பின்னணிப் பாடல்`** block.

PDF 15 also contains the quoted fragment `ஓரிடந்தனிலே...`; it remains dialogue-owned and is not promoted to a reconstructed standalone song. PDF 20–29 introduces no newly distinct standalone lyric/song block.

These structures remain source candidates until verified canonical transcription and the later song/performance gate. No missing lyrics or authorship will be reconstructed from outside sources.

## Historical Tamil glyph policy

This source uses older Tamil type and must follow `../../docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md` from the first canonical page onward.

Every canonical page must be inspected at enlarged/native resolution for at least the known families:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

Rules:

- identify historical character identity before encoding modern Unicode;
- preserve source spelling, grammar, vocabulary and punctuation;
- use same-edition glyph comparison when needed;
- OCR is navigation/discovery aid only;
- never global-replace a historical glyph family;
- unresolved clusters remain `needs-review`;
- a page will not be called verified until both ordinary visual fidelity and its historical-glyph check pass.

Work audit: `notes/historical-glyph-audit.md`.

## User-supplied contextual note

The user describes the film as making the rationalist movement its central protagonist, foregrounding the working-class voice, and introducing rationalist thought throughout. This is retained as **user-supplied context**, not silently promoted to source-visible bibliographic/textual evidence.

## Exact next activity

**Continue canonical Tamil first-pass transcription with PDF 30–34, preserving source order, stable page anchors and page-level historical-glyph checks. Keep all first-pass pages draft/needs-review until the later separate visual-fidelity and final historical-glyph gates pass.**
