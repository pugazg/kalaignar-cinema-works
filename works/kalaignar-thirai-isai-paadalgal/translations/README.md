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
- `BATCH_004_011_REVIEW.md` — first scaled batch review for the complete `நாம்` group.

Each record preserves:

- anthology song number;
- exact source song-file path;
- source PDF page(s);
- film title and attribution status;
- exact Tamil section/turn labels;
- Tamil lines alongside their English lines for auditability;
- translator notes for source-specific wording.

## Current checkpoint

- source Tamil songs: **54/54 complete-verified**;
- English translated: **11/54**;
- pilot-verified: **3** (`001–003`);
- verified: **8** (`004–011`);
- draft: **0**;
- review: **0**;
- not started: **43** (`012–054`).

### Approved pilot

Songs `001–003` established the voice baseline across rustic political/social satire, romantic image chains, and maternal/class lament. Their approved decisions remain controlling for later work.

### First scaled batch — songs 004–011

The complete `நாம்` group is now verified in English. The batch demonstrates that the Kalaignar-language rule holds across devotional/social satire, romantic duet, female lament, comic mythic performance, rationalist/agricultural political song, praise/reform rhetoric, and political-philosophical exhortation.

Key retained source forces include:

- song `004`: Mari/Kali folk-devotional vocabulary, rain/science debate, Kodumpavi and the direct tax grievance;
- song `005`: yaazh, doe, Tamil epic, unpainted painting, repeated `பேசி பேசி / வீசி வீசி`, and women/warriors imagery;
- song `006`: the `மணம்` fragrance/marriage wordplay and the full veena/thunderbolt/vine/cyclone/pollen/dark-house image chain;
- song `007`: the yaazh that **plucks an unreturning sorrow**, singing ghost and inscribed-page imagery;
- song `008`: source-anomalous transliterations, `Dei`, kichili fruit, consumption, monkey/moustache/tail ridicule and Bhimasena;
- song `009`: ignorance-as-wasteland, knowledge-as-plough-point, science/ploughing, field labour, Nandanar versus hands-and-legs labour, golden queen/comrade and common granary;
- song `010`: fourfold `வாழ்க`, Arignar, buffalo/worm/eagle/mouse/tiger political images, rational thought and conservative handling of possible title/wordplay phrases;
- song `011`: snakes, prison, torture, Socrates, deathless Gandhi, honey-to-scorpion, battlefront death, army, fury and slander.

See `BATCH_004_011_REVIEW.md` for the detailed gate.

## Next batch

Translate and verify songs **012–018** (`அம்மையப்பன்`) under the same source-faithful Kalaignar-language rules. The verified Tamil files must remain immutable translation inputs.
