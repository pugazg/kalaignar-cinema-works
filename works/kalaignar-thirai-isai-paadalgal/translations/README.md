# English translations — கலைஞர் திரை இசைப் பாடல்கள்

This directory contains source-linked English translations of the **54/54 complete-verified Tamil song files** under `../songs/`.

## Translation authority

- verified Tamil song files are the controlling textual source;
- the anthology's page provenance remains attached to every translation record;
- English never overwrites or repairs Tamil;
- external recordings, subtitles, web lyrics and alternate editions are not translation authorities for this layer;
- authorship status remains independent: the default remains `anthology-attributed` unless stronger item-level evidence is separately established.

## Kalaignar-language rule

English must retain Kalaignar's language rather than flattening it into generic lyric prose.

Follow `docs/SONG_TRANSLATION_GUIDE.md`:

- preserve repetition and refrain architecture;
- preserve political/social satire without euphemism;
- preserve concrete images and rhetorical questions;
- preserve colloquial energy and culture-bearing vocabulary;
- do not invent rhyme or smooth away awkward/source-specific constructions merely to make the English prettier;
- when a verified Tamil form is unusual, translate conservatively and document the pressure point instead of silently correcting the Tamil.

The default translation mode is `semantic-poetic-source-faithful`. This is **not** a singable adaptation.

## Record layout

- `schema.json` — translation-record schema;
- `index.json` — whole-corpus English translation status;
- `records/song-001.json` etc. — source-linked English records;
- `PILOT_REVIEW.md` — approved pilot voice and structural decisions.

Each record preserves:

- anthology song number;
- exact source song-file path;
- source PDF page(s);
- film title and attribution status;
- exact Tamil section/turn labels;
- Tamil lines alongside their English lines for auditability;
- translator notes for source-specific wording.

## Current checkpoint

Pilot songs: **001–003**. They were selected because they exercise three different Kalaignar registers:

1. `001` — rustic political/social satire;
2. `002` — romantic metaphor and duet-turn language;
3. `003` — maternal lament and class contrast.

All three pilot translations are `pilot-verified` against the already verified Tamil files and rendered anthology pages.

Do not scale by rewriting these into smoother generic English. Their approved voice decisions are the baseline for later batches.
