# Kalaignar Cinema Works — Song Anthology Processing Guide

This guide applies when `pugazg/kalaignar-cinema-works` receives a **song anthology / collected film-lyrics source** rather than a screenplay or dialogue booklet.

It supplements:

- `docs/CINEMA_WORKS_PROCESSING_GUIDE.md`
- `docs/ARCHIVAL_WORKFLOW.md`
- `docs/SOURCE_POLICY.md`
- `docs/TRANSCRIPTION_GUIDE.md`
- `docs/SONG_TRANSLATION_GUIDE.md` for English derivative work

The supplied scan remains the controlling source for the **text and claims of that scanned edition**.

## 1. Distinguish anthology authority from original-film authority

A later anthology can be authoritative for:

- what that anthology prints;
- the anthology's song numbering;
- the anthology's film grouping;
- its lyric text, headings, singer/music labels and editorial notes;
- its own attribution claims.

It does **not automatically replace** an original film booklet, screenplay, gramophone label or other primary source for historical questions.

Use these attribution states where useful:

- `anthology-attributed` — the song is presented by the anthology as a Kalaignar song;
- `primary-source-verified` — an original/near-contemporary item-level source independently supports the attribution;
- `review` — evidence conflicts or needs examination;
- `unresolved` — evidence is insufficient.

Do not silently upgrade `anthology-attributed` to `primary-source-verified`.

## 2. Repository layout

Use a work directory for the anthology and a dedicated `songs/` layer:

```text
works/<anthology-id>/
├── README.md
├── metadata.yaml
├── mapping.md
├── PROGRESS.md
├── AUDIT.md
├── PROJECT_HANDOVER.md
├── notes/
└── songs/
    ├── README.md
    ├── index.json
    ├── schema.json
    └── song-001.md
```

When English translation begins, add a separate `translations/` layer rather than modifying the verified Tamil files.

If the anthology prints stable song numbers, preserve them. Do not renumber them to match a different soundtrack catalogue.

## 3. Intake and mapping

Before lyric transcription:

1. inspect the actual scan;
2. record file name, byte size, PDF pages and SHA-256;
3. record printed title, compiler/editor, publisher, edition/year and ISBN exactly as visible;
4. distinguish PDF page count from any printed `No of pages` statement;
5. map front matter, contents, filmography tables, numbered lyric corpus and back matter;
6. map every film/section and its printed page range;
7. count the printed numbered songs independently from prose references to songs.

A prose mention of a deleted, censored, lost or otherwise unprinted song is **not** a numbered lyric record unless the anthology actually prints it as one.

## 4. Song inventory

Create the complete inventory before large-scale transcription.

Each inventory row should retain:

- stable archive ID;
- anthology song number;
- film title as printed;
- film year as printed in the anthology section/contents;
- contents title / incipit as printed;
- lyric source page(s) when confirmed;
- music credit as printed;
- voice/singer credit as printed;
- transcription status;
- attribution status;
- notes on variants, deletions or source anomalies.

The contents list is useful for the initial inventory but does not override the actual lyric page. If a title/incipit differs, retain both readings and let the lyric page control the lyric derivative.

## 5. Lyric transcription

For each numbered song:

- transcribe only visible text;
- preserve the anthology's spelling and punctuation;
- preserve stanza/line order;
- preserve labels such as `தொகையறா`, `பாட்டு`, `பல்லவி`, singer initials, character labels and duet-turn labels;
- preserve ellipses, hyphens and parenthetical repetitions;
- keep source-visible English/other-language text as printed;
- do not silently modernize colloquial forms;
- do not add missing verses from audio, web lyrics, subtitles or memory.

Recommended source anchor:

```md
<!-- source: pdf=29 printed=29 anthology_song=002 status=draft -->
```

## 6. Film-section context pages

Many anthologies place editorial film metadata before lyrics. Keep that context separate from the lyric text.

Record, where printed:

- release date;
- story/dialogue/song credit;
- composer;
- director;
- actors;
- production company;
- list of songs in the film and their lyricists;
- editorial notes about censored/deleted songs or unavailable recordings.

These pages can be valuable evidence but are not themselves lyric text.

## 7. Cross-linking existing cinema works

When the anthology contains a song connected to an already archived film such as `works/parasakthi/`:

- add a cross-reference only after confirming the exact song/fragment;
- do not overwrite the existing film booklet transcription;
- do not copy the anthology lyric into the screenplay source layer;
- document textual variants source-by-source;
- preserve each edition as an independent textual witness.

## 8. Verification gate

A song remains `draft` until the stored lyric is visually checked line-by-line against its rendered source page(s).

Verification checks:

- song number;
- film title;
- composer/voice labels;
- every lyric line;
- stanza/turn labels;
- punctuation and ellipses;
- page boundaries;
- repeated refrains;
- source spelling;
- no imported or inferred lines.

## 9. Translation and reader work

Do not translate or build a public reader until the corresponding Tamil song is verified.

For English translation, follow `docs/SONG_TRANSLATION_GUIDE.md` in addition to this guide.

The default English goal is **source-faithful literary translation that retains Kalaignar's language**, not a singable adaptation. In particular:

- retain the song number and film provenance;
- keep Tamil source text immutable;
- preserve repetition and refrain structure;
- preserve satire, political/class language and rhetorical force without euphemism;
- preserve concrete images and culturally specific wording before smoothing them into generic English;
- preserve colloquial energy where formal English would erase the source register;
- document difficult or anomalous verified Tamil forms rather than silently repairing them through English;
- do not invent rhyme/metre at the cost of meaning;
- keep source-attribution status visible;
- do not imply stronger authorship evidence than the repository actually holds.

For structured translation records, preserve explicit links back to the verified Tamil song file and source PDF page(s). Where practical, map every Tamil lyric line/cue to an English line/cue so that translation QA can detect omissions.

## 10. Major checkpoint synchronization

After each major song batch, update at least:

- `works/<anthology-id>/songs/index.json` when Tamil/song status changes;
- `works/<anthology-id>/translations/index.json` when English work exists;
- `works/<anthology-id>/PROGRESS.md`;
- `works/<anthology-id>/AUDIT.md`;
- `works/<anthology-id>/metadata.yaml`;
- `works/<anthology-id>/README.md`;
- `data/works.json` when the repository-level checkpoint changes.

At handover points, refresh `PROJECT_HANDOVER.md` with the exact next song number/page range or translation batch.
