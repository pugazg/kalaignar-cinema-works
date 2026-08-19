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
- `records/song-001.json` through `records/song-054.json` — source-linked English records;
- `PILOT_REVIEW.md` — approved pilot voice and structural decisions;
- `BATCH_004_011_REVIEW.md`;
- `BATCH_012_018_REVIEW.md`;
- `BATCH_019_025_REVIEW.md`;
- `BATCH_026_032_REVIEW.md`;
- `BATCH_033_039_REVIEW.md`;
- `BATCH_040_046_REVIEW.md`;
- `BATCH_047_054_REVIEW.md` — final translation gate.

Each record preserves anthology song number, exact source-song path, source PDF page(s), film title, attribution status, exact Tamil section/turn labels, Tamil lines alongside English lines, and translator notes for source-specific wording.

## Final checkpoint

- source Tamil songs: **54/54 complete-verified**;
- English translated: **54/54 complete-verified**;
- pilot-verified: **3** (`001–003`);
- verified: **51** (`004–054`);
- draft: **0**;
- review: **0**;
- not started: **0**.

All scaled translation gates pass. No verified Tamil song file was changed by the English layer.

### Final scaled batch — songs 047–054

PASS — **8/8 verified**.

Key retained source forces include:

- `047`: **sons of the soil**, literal eye/eyelid civic-duty imagery, repeated sky/sea courage-wisdom lines, **hand for kinship / voice for rights**, and `naam / naan` lip-position wordplay; verified `பிரிவாது` remains a documented semantic pressure point;
- `048`: `kalaignan`, `udanpirappe`, direct caste/religion division and **sledgehammer** imagery, **Valluvar, the primordial son**, and source-pressure `inba-pagai`;
- `049`: mother-warrior pride and grief, **casket of sculpted beauty**, **maiden young-deer**, **played ball with the tuskers**, source-shaped **turned the steeds to cotton**, battlefield fame and womb-bearing motherhood;
- `050`: `mullai`, Tamil `mandram`, `bhava`, `jathi`, `veena`, printed jathi vocables, source-pressure `nyaayirene`, `Nasika Poosani`, and the deliberately abrupt `உலகிலே யார் காட்டு` ending;
- `051`: full PDF **121–122** provenance, `machaan / aandi / thaali / saivam / asaivam / mama / saami-kutham`, fried-fish/mat sexual-comic language, **raw-rice smile**, the explicit demand that men reform and slavery end, and source-pressure phrases retained without soundtrack repair;
- `052`: full PDF **123–124** provenance, **affection-parrot**, `kurinji`, repeated chorus `ஆட`, conservative **land-peacock**, child-fruit, Kannagi, Classical Tamil, red jasmine, eyelid imagery, younger-sister/mother repetition and eyes becoming ponds;
- `053`: the printed clipped short-line architecture, deer-kind, `bhava`, forest peacock, bird-kind, silk flag, victory parasol, **Pearl-Tamil** and Chola-land praise remain segmented rather than recomposed into polished prose;
- `054`: `venu`, Todi, Thiruvathirai, Thiruvenkadu, `magudi`, repeated love-disease lines, `Kodumudi kokilam`, honey/milk imagery, `aanpaal`, `paayiram`, and the classical **water upon red earth** image.

Detailed review: `BATCH_047_054_REVIEW.md`.

## Next activity

Run a **whole-corpus English reader/export preflight** over all 54 source-linked translation records. Preserve anthology order, Tamil/source provenance, `anthology-attributed` status, and the distinction between the 3 `pilot-verified` records and 51 `verified` records. Do not alter the complete-verified Tamil or English source-linked layers merely for publication smoothness.
