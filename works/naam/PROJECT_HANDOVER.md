# நாம் — Project Handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Work: `works/naam/`

## Live-main rule

Fetch live `main` before every continuation. Preserve any newer durable work. The controlling source is the attached/resolved `TVA_BOK_0064201_நாம்.pdf`; do not substitute OCR, film audio, subtitles, web text, another edition or memory for its rendered pages.

## Current checkpoint

- source intake: **complete**;
- whole scan inspected: **72/72 PDF pages**;
- structural mapping: **verified**;
- source-numbered scenes: **45 / காட்சி 1–45**, sequential with no observed gaps/repeats/out-of-order numbers;
- canonical Tamil: **partial first pass — PDF 5–14 / 10 of 67 pages**;
- canonical Tamil verified: **0/67**;
- visual fidelity audit: **not-started**;
- historical-glyph first-pass checked: **10/67**;
- historical-glyph final verified: **0/67**;
- open source uncertainty markers: **2**;
- downstream structured/English/reader layers: **blocked/not-started**.

Current canonical files:

- `transcription/index.json`;
- `transcription/README.md`;
- `transcription/parts/pdf-005-009.md`;
- `transcription/parts/pdf-010-014.md`;
- `notes/textual-notes-pdf-005-009.md`;
- `notes/textual-notes-pdf-010-014.md`;
- `notes/historical-glyph-audit.md`.

## Source identity

- source: `TVA_BOK_0064201_நாம்.pdf`;
- source ID: `TVA_BOK_0064201`;
- pages: **72**;
- bytes: **115,948,588**;
- SHA-256: `0f7a54882eb6a5a8f83b29060c771ef18dee2b9e108c8797184de2b97c30b7ad`;
- image-only;
- visible title: `நாம்`;
- visible author: `மு. கருணாநிதி`;
- source-visible organization: `ஆசீர்வாதபுரம் ஆதிதிராவிட நல உரிமைச் சங்கத்தார்`;
- no printed publication year or edition statement located;
- printer on PDF 72: `அச்சிட்டது ஆதி பிரஸ், சென்னை—12.`.

## Credits safeguard

PDF 4 prints the broad credit `கதை, வசனம், பாடல்... மு. கருணாநிதி` but also separately prints `பாட்டு 'ஆயிரம் தெய்வங்கள்'—பாரதியார்.` The latter is item-level source evidence and must never be overwritten by the broad credit.

## Source ranges

- PDF 1–4: front matter;
- PDF 5–71: screenplay/dialogue, **67 pages**;
- PDF 6–71: visible printed numerals 6–71, one-to-one with PDF pages;
- PDF 5: screenplay opening / காட்சி 1, printed numeral not visibly established;
- PDF 72: back matter/printer imprint.

Handwritten pencil marks/numbers are later annotations, not canonical text.

## First-pass batches completed

### PDF 5–9

Coverage:

- PDF 5: opening `காட்சி 1`, introductory prose and opening village/Mari dialogue;
- PDF 6–7: Mari/rain discussion and performance; `காட்சி 2` begins on PDF 7;
- PDF 8: continuation of `காட்சி 2`, then `காட்சி 3` begins;
- PDF 9: continuation of `காட்சி 3` and montage/action paragraph.

Locked first-pass safeguards:

- PDF 5 has no invented printed-page number;
- exact source labels, parentheticals, stage directions, colloquial forms, punctuation, ellipses and verse lineation are preserved;
- PDF 6 `அவளை` is recorded as a historical-`ளை` glyph-decoding case;
- PDF 6 `சூரியனால்` was explicitly checked against the historical `னா` family;
- the rain/Mari song text remains canonical source text but receives **no item-level authorship adjudication at this phase**.

Open source uncertainties retained:

1. PDF 5 — one physically damaged introductory line below `காட்சி 1`;
2. PDF 9 — one unclear word in the montage/action paragraph after `(நாட்கள் பல கடந்தன)`.

### PDF 10–14

This second five-page batch continues through the opening of `காட்சி 6`.

Source decisions:

- PDF 10 lower action was resolved at enlarged pixels as `நாராயணி மறு வினாடி மாடியிலிருந்து கீழே உருட்டி விடப்படுகிறாள்.`;
- PDF 11 `கண்ணாடிச்` is logged as a positive `ணா`-family first-pass case;
- PDF 12's unusual `தளிர்ச்சிருக்கே` is retained as source-visible wording, not normalized;
- PDF 13 `கீல்வலிக்கார தங்கையன்` and `கொம்பேறி மூக்கன்` are retained without lexical modernization;
- PDF 14 visibly prints `வாலாம்` twice; the canonical draft does not silently change it to `வரலாம்`;
- PDF 10–14 introduced **0 new explicit uncertainty markers**;
- no page in either completed batch is marked verified.

## Historical Tamil glyph rule

Read `../../docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md` and `notes/historical-glyph-audit.md` before canonical work.

Every canonical page must be checked at enlarged/native resolution for at least:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

Decode historical character identity, then encode modern Unicode identity; do not modernize source wording. Never global-replace. Use same-edition evidence for doubtful glyphs and leave unresolved forms under review.

A page is not finally verified until both visual fidelity and historical-glyph gates pass.

## High-confidence performance structures already mapped

- PDF 16 / scene 7 — `[பாட்டு]`, `ஆயிரம் தெய்வங்கள்`, source-author `பாரதியார்`;
- PDF 35–36 / scene 21 — lyrical block beginning `மணமில்லா மலர் நானம்மா!`;
- PDF 49–50 / scene 31 — lyrical block with `(பேதம்)` cues;
- PDF 59–60 — poetic/song-like blocks between scenes 36 and 37;
- PDF 64 / scene 39 — `பின்னணிப் பாடல்`.

Only the first item currently has an item-specific author credit from the booklet. Other authorship/classification remains open until verified canonical text and the later song/performance gate.

## Exact next activity

> **Continue canonical Tamil first-pass transcription with PDF 15–19, preserving source order, stable page anchors and page-level historical-glyph checks. Keep all first-pass pages draft/needs-review until the later separate visual-fidelity and final historical-glyph gates pass.**

PDF 16 enters the already-mapped `காட்சி 7` explicit `[பாட்டு]` block whose item-level booklet credit is `ஆயிரம் தெய்வங்கள்` — `பாரதியார்`. Transcribe only what the scan prints; preserve the specific credit safeguard and do not use outside lyrics to fill or alter the booklet text.

Do not reopen PDF 5–14 merely because a copied prompt is older unless new source evidence resolves an existing uncertainty.
