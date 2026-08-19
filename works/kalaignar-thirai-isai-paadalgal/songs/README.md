# Song layer — கலைஞர் திரை இசைப் பாடல்கள்

This directory stores the anthology's **printed numbered lyric corpus `001–054`**.

## Authority

Each `song-NNN.md` is a transcription derivative of the corresponding numbered lyric page(s) in the supplied 2024 anthology.

The anthology controls this layer's:

- song number;
- film title as printed;
- lyric wording/lineation;
- composer/music line;
- voice/singer line when printed;
- singer/character turn labels;
- refrain/stanza labels;
- punctuation and source spellings.

It does not automatically function as an original film-era source for authorship history. Default authorship status is `anthology-attributed`.

## Inventory

`songs/index.json` contains all **54** numbered items.

The inventory separates:

- `contents_title` — wording read from PDF 21–23;
- `lyric_title` — wording established from the numbered lyric page when processed;
- `lyric_pdf_pages` — exact lyric page(s);
- `status` — `not-started`, `draft`, `review`, or `verified`;
- `attribution_status` — initially `anthology-attributed` unless stronger evidence is separately documented.

## Song-file format

Each song file contains:

1. provenance block;
2. source-visible metadata;
3. exact Tamil lyric body;
4. editorial/uncertainty notes separated from the lyric;
5. verification status.

Recommended anchor:

```md
<!-- source: pdf=29 printed=29 anthology_song=002 status=draft -->
```

## Transcription rules

- preserve source line order;
- preserve labels such as `(தொகையறா)`, `(பாட்டு)`, `பல்லவி`, singer initials, duet labels and character labels;
- preserve source punctuation and ellipses;
- preserve colloquial or unusual spellings unless the rendered source proves they were misread;
- do not import missing verses from recordings, websites or another book;
- do not change a lyric because a familiar soundtrack version differs;
- keep uncertain readings visible in an editorial note and re-open the scan.

## Verification

A draft is promoted to `verified` only after line-by-line comparison against the rendered source page(s).

The audit confirms song number, film, music/voice labels, every lyric line, refrains, lineation and page provenance. A source page that does not print a voice line must remain without an inferred singer.

## Special cases

The prose-mentioned censored/prohibited `மந்திரிகுமாரி` song `ஆளப்பிறந்தவன் தமிழன் அவன்தானே` is **not** a numbered lyric item here. See `../notes/anthology-notes.md`.

Song `009` is the first verified cross-page numbered lyric in this work: it spans PDF/printed **38–39** and remains one song file.

## Current state

- inventory: **54/54**;
- draft: **001–003** — 3 songs;
- verified: **004–011** — 8 songs;
- review: **0**;
- not started: **012–054** — 43 songs;
- latest batch audit: `../notes/BATCH_004_011_REVIEW.md`;
- next: **012–018** (`அம்மையப்பன்`, PDF **42–50**).

English translation remains blocked until the relevant Tamil lyric is verified.
