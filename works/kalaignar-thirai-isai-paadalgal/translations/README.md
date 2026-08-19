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
- `PILOT_REVIEW.md` — approved pilot voice and structural decisions;
- `BATCH_004_011_REVIEW.md` — scaled review for the complete `நாம்` group;
- `BATCH_012_018_REVIEW.md` — scaled review for the complete `அம்மையப்பன்` group.

Each record preserves anthology song number, exact source-song path, source PDF page(s), film title, attribution status, exact Tamil section/turn labels, Tamil lines alongside English lines, and translator notes for source-specific wording.

## Current checkpoint

- source Tamil songs: **54/54 complete-verified**;
- English translated: **18/54**;
- pilot-verified: **3** (`001–003`);
- verified: **15** (`004–018`);
- draft: **0**;
- review: **0**;
- not started: **36** (`019–054`).

### Approved pilot — songs 001–003

The pilot established the voice baseline across rustic political/social satire, romantic image chains and maternal/class lament. Its approved decisions remain controlling for later work.

### First scaled batch — songs 004–011 (`நாம்`)

PASS — **8/8 verified**. It established that the Kalaignar-language rule survives folk devotion, social satire, romantic duet, lament, comic mythic performance, rationalist/agricultural politics, praise/reform rhetoric and political endurance.

See `BATCH_004_011_REVIEW.md`.

### Second scaled batch — songs 012–018 (`அம்மையப்பன்`)

PASS — **7/7 verified**.

Key retained source forces include:

- `012`: Ammaiyappa/Aiyan devotional address, paired opposites, honey/poison and fire/water paradoxes, king-to-`aandis` hierarchy, palanquin bearers/riders, toad-in-stone, sesame-oil and snake-fang venom;
- `013`: repeated **paappa**, blue sea, silver sand, sandalwood parrot, peacock, nectar-dove and repeated `sway`;
- `014`: realm of love, `come running`, cloud/grove-plumage, great gem, maiden dancing in the eyes, boundary of bliss, heart-veena and moon-of-love variation;
- `015`: deliberate sorrow-reprise of `014`, song drifting on the breeze, honey-rain and the source's unassigned `lap`;
- `016`: agal-lamp, sugarcane/rock-candy/fruit-nectar, red paddy, refined Tamil, Kaveri, casket of the learned, Dravida, and the difficult `நீ... இராவிடம் இருள் சூழும் / என்ற நிலை தந்த` wording preserved as an explicit source pressure point;
- `017`: living portrait, epic of flavour, flame, storm/flower-garden, fallen divine statue and empty temple;
- `018`: love-dove, tender-shoot body, repeated `come`, deer-skinned tiger, mango-cuckoo, sorrow-darkness, sleeping moon-maiden and love/deception reversal.

See `BATCH_012_018_REVIEW.md`.

No verified Tamil song file was changed by either scaled English batch.

## Next batch

Translate and verify songs **019–025** under the same source-faithful Kalaignar-language rules. Preserve multi-page provenance for `019`, `023` and `024`; the verified Tamil corpus remains immutable translation input.
