# Project handover — கலைஞர் திரை இசைப் பாடல்கள்

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Work path: `works/kalaignar-thirai-isai-paadalgal/`

## Mandatory startup in a new chat

Read completely before changing this work:

1. `docs/CINEMA_WORKS_PROCESSING_GUIDE.md`
2. `docs/SONG_ANTHOLOGY_PROCESSING_GUIDE.md`
3. `docs/ARCHIVAL_WORKFLOW.md`
4. `docs/SOURCE_POLICY.md`
5. `docs/TRANSCRIPTION_GUIDE.md`
6. `works/kalaignar-thirai-isai-paadalgal/README.md`
7. `works/kalaignar-thirai-isai-paadalgal/metadata.yaml`
8. `works/kalaignar-thirai-isai-paadalgal/mapping.md`
9. `works/kalaignar-thirai-isai-paadalgal/PROGRESS.md`
10. `works/kalaignar-thirai-isai-paadalgal/AUDIT.md`
11. `works/kalaignar-thirai-isai-paadalgal/notes/anthology-notes.md`
12. `works/kalaignar-thirai-isai-paadalgal/notes/BATCH_004_011_REVIEW.md`
13. `works/kalaignar-thirai-isai-paadalgal/songs/README.md`
14. `works/kalaignar-thirai-isai-paadalgal/songs/index.json`

Then inspect current GitHub `main`. Current repository state is authoritative over this handover if later work has advanced.

## Controlling source

Attached source filename:

`TVA_BOK_0065867_கலைஞர்_திரை_இசைப்_பாடல்கள்.pdf`

Binary checkpoint:

- size: `130427193` bytes;
- SHA-256: `f0beac14c33ffc73c0231bd54ca57ec4093eef6e85072bd68ce48f7b5e258b05`;
- physical PDF pages: **194**;
- image-only source;
- do not use OCR as authority.

Publication facts printed in the source:

- title: `கலைஞர் திரை இசைப் பாடல்கள்`;
- compiler: `நெல்லை ஜெயந்தா`;
- First Edition: June 2024;
- printed `No of pages`: 192;
- ISBN: `978-81-961205-2-8`;
- publisher: தமிழ்நாடு இயல் இசை நாடக மன்றம்.

Do not commit the source PDF unless explicitly requested.

## Source authority rule specific to this work

This is a **2024 anthology**, not an original film-era booklet for every represented song.

The anthology controls:

- its exact printed lyric text;
- its numbering `001–054`;
- its film grouping;
- its printed music/voice labels;
- its own authorship claims.

Default attribution state: **`anthology-attributed`**.

Do not silently upgrade to `primary-source-verified`. Do not overwrite source layers in `works/parasakthi/`, `works/manohara/`, `works/tirumbippaar/`, or any other film work with anthology text.

## Structural checkpoint

Full structural mapping is complete:

- front matter/context: PDF 1–20;
- contents: 21–23;
- numbered Tamil song corpus: **24–130**;
- 23 film sections;
- 54 numbered songs, `001–054`;
- other-language film detail: 131–139;
- film-world journey: 140–181;
- people/context: 182–188;
- bibliography: 189;
- notes/back matter: 190–194.

## Current song checkpoint

Inventory: **54/54 complete**.

Tamil lyric files:

- `songs/song-001.md` — draft — PDF 26;
- `songs/song-002.md` — draft — PDF 29;
- `songs/song-003.md` — draft — PDF 30;
- `songs/song-004.md` through `songs/song-011.md` — **verified** — PDF 33–41;
- songs 012–054 — not started.

Current totals:

- verified: **8** (`004–011`);
- draft: **3** (`001–003`);
- review: **0**;
- not started: **43** (`012–054`).

The latest verified batch is documented in `notes/BATCH_004_011_REVIEW.md`.

### `நாம்` batch safeguards

- PDF 32 places `கலைஞர்` beside the eight entries represented by songs 004–011. Keep them `anthology-attributed` unless stronger film-era evidence is separately established.
- The separate `ஆயிரம் தெய்வங்கள்` entry is printed with `பாரதியார்`; do not add it to the Kalaignar numbered batch.
- Song 004 source is `மாரி`, not `மாறி`.
- Song 006 has no printed `குரல்` line; do not infer a singer. Preserve `மீனா:` as the source role label.
- Song 009 is one lyric across PDF 38–39.
- Preserve unusual/colloquial source forms in all records; do not normalize from soundtrack familiarity.

## Special source case — மந்திரிகுமாரி

PDF 25 says Kalaignar wrote two songs, including `ஆளப்பிறந்தவன் தமிழன் அவன்தானே`, and states that this first song was censored/prohibited. Its lyric is not printed as a numbered item in the anthology.

Disposition:

- preserve the claim in notes;
- do **not** invent a song number;
- do **not** add absent lyrics from elsewhere;
- numbered song `001` remains `ஊருக்கு உழைப்பவண்டி`.

## Exact next activity

Process **songs 012–018**, film **`அம்மையப்பன்`**, PDF **42–50**.

For the batch:

1. inspect the film context/song-list page(s);
2. visually transcribe every numbered song in source order;
3. preserve exact composer/voice/character-turn labels;
4. preserve lineation, refrains, ellipses, colloquial/source spelling;
5. leave uncertain readings visible;
6. recheck the rendered scan before marking a record `verified`;
7. update `songs/index.json`, `PROGRESS.md`, `AUDIT.md`, `metadata.yaml` and work-level status documents;
8. do not begin English translation.

## Later gates

After song 054:

1. whole-corpus song-number/title/page reconciliation;
2. full visual fidelity reconciliation, including draft songs 001–003;
3. source-to-source cross-links to existing film works only where exact matches are confirmed;
4. English translation only for verified Tamil;
5. reader/export only after translation/QA if requested.

## Repository boundary

Work only inside `pugazg/kalaignar-cinema-works` unless the user explicitly requests another repository. Downstream Reading Room work is out of scope for this handover.
