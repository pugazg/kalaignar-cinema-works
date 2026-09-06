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
- canonical Tamil: **partial first pass — PDF 5–19 / 15 of 67 pages**;
- canonical Tamil verified: **0/67**;
- visual fidelity audit: **not-started**;
- historical-glyph first-pass checked: **15/67**;
- historical-glyph final verified: **0/67**;
- open source uncertainty markers: **2**;
- downstream structured/English/reader layers: **blocked/not-started**.

Current canonical files:

- `transcription/index.json`;
- `transcription/README.md`;
- `transcription/parts/pdf-005-009.md`;
- `transcription/parts/pdf-010-014.md`;
- `transcription/parts/pdf-015-019.md`;
- `notes/textual-notes-pdf-005-009.md`;
- `notes/textual-notes-pdf-010-014.md`;
- `notes/textual-notes-pdf-015-019.md`;
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

- opening `காட்சி 1` through early `காட்சி 3`;
- PDF 6 `அவளை` is a historical-`ளை` decoding precedent;
- PDF 6 `சூரியனால்` was checked against `னா`;
- PDF 5 has no invented printed-page number;
- open source uncertainties: damaged PDF 5 introductory span + one unclear PDF 9 montage word.

### PDF 10–14

- continues through the opening of `காட்சி 6`;
- PDF 11 `கண்ணாடிச்` is a positive `ணா` first-pass case;
- PDF 12 `தளிர்ச்சிருக்கே`, PDF 13 `கீல்வலிக்கார தங்கையன்`, and PDF 14 `வாலாம்` remain source-visible forms;
- PDF 10–14 introduced **0** new explicit uncertainty markers.

### PDF 15–19

- continues through `காட்சி 7`, `காட்சி 8`, and the opening of `காட்சி 9`;
- this batch was rechecked against enlarged source pixels before synchronization;
- five local first-pass readings were corrected from the scan: PDF 15 `எல்லோருக்கும்`; PDF 15 `உருண்டோடிடுமே`; PDF 17 `அவன் கை வலி`; PDF 19 `என்னே`; PDF 19 `என் மருமகளும்`;
- PDF 15 `பிரேமா வாகவர்`, PDF 17's extended labour/tax rhetoric, and PDF 19 `சோபிதத்தை` / `காதியின்` remain unmodernized source readings;
- PDF 15–19 introduced **0** new explicit uncertainty markers;
- all 15 first-pass pages remain **draft / needs-review**, not verified.

## Historical Tamil glyph rule

Read `../../docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md` and `notes/historical-glyph-audit.md` before canonical work.

Every canonical page must be checked at enlarged/native resolution for at least:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

Decode historical character identity, then encode modern Unicode identity; do not modernize source wording. Never global-replace. Use same-edition evidence for doubtful glyphs and leave unresolved forms under review.

A page is not finally verified until both visual fidelity and historical-glyph gates pass.

## Performance / lyric evidence now source-confirmed

- PDF 16 / scene 7 — explicit `[பாட்டு]`, three numbered sections. PDF 4 identifies the item as **`ஆயிரம் தெய்வங்கள்` — பாரதியார்**. Only the booklet witness is transcribed; no outside lyric text is used.
- PDF 18 / scene 8 — source-visible lyrical duet beginning `பேசும் யாழே பெண் மானே`, lineated under `குமரன்`, `மீனு`, and `இருவர்`; authorship remains **not adjudicated**.
- PDF 15 `ஓரிடந்தனிலே...` remains a dialogue-owned quoted fragment, not a reconstructed standalone song.
- Later mapped structures remain PDF 35–36 / scene 21, PDF 49–50 / scene 31, PDF 59–60 between scenes 36–37, and PDF 64 / scene 39.

No unprinted title, missing lyric body or authorship may be reconstructed from outside sources.

## Exact next activity

> **Continue canonical Tamil first-pass transcription with PDF 20–24, preserving source order, stable page anchors and page-level historical-glyph checks. Keep all first-pass pages draft/needs-review until the later separate visual-fidelity and final historical-glyph gates pass.**

Do not reopen PDF 5–19 merely because a copied prompt is older unless new direct scan evidence resolves an existing uncertainty or demonstrates a concrete transcription error.
