# Parasakthi song / verse derivatives

**Stage:** structured derivatives  
**Canonical authority:** verified Tamil transcription / scene derivatives  
**Authorship status:** complete-verified  
**Tamil soundtrack derivatives:** complete-verified — **11/11 compositions**

This directory preserves song/verse attribution metadata and source-faithful Tamil derivatives separately from the canonical transcription. A derivative file never replaces or repairs the canonical Tamil.

## Files

- `schema.json` — song/verse inventory record schema.
- `credits.json` — exact booklet-wide `பாடல்கள்` contributor list from PDF 3.
- `tracklist-evidence.json` — item-level soundtrack evidence and mapping to canonical occurrence IDs.
- `inventory.json` — 14 canonical song/verse occurrence records.
- `index.json` — final song-layer checkpoint.
- `tracks/` — **11 source-faithful Tamil soundtrack-composition derivatives**.
- `quoted-verses/` — source-faithful literary quotation derivatives kept outside the soundtrack set.

## Authorship evidence

PDF 3 lists six booklet-wide contributors:

- பாரதியார்
- பாரதிதாசன்
- உடுமலை நாராயணகவி
- மு. கருணாநிதி
- கே. பி. காமாட்சி சுந்தரம்
- கு. ம. அண்ணல்தங்கோ

That page does not assign contributors item by item. Item-level soundtrack attribution was later reconciled from the user-supplied soundtrack screenshot, independently matched to the Tamil Wikipedia `பராசக்தி (1952 திரைப்படம்)` soundtrack table. `tracklist-evidence.json` records the source, limitation and mapping.

Final authorship state: **14/14 canonical occurrence records verified**, including the separate scene-28 Bharathidasan quotation.

## Source-faithful soundtrack files

1. [`tracks/01-desam-gnanam-kalvi.md`](tracks/01-desam-gnanam-kalvi.md) — `தேசம் ஞானம் கல்வி` — உடுமலை நாராயண கவி — occurrences `005` + `006`.
2. [`tracks/02-kaa-kaa-kaa.md`](tracks/02-kaa-kaa-kaa.md) — `கா கா கா` — உடுமலை நாராயண கவி.
3. [`tracks/03-nenju-porukkuthillaiye.md`](tracks/03-nenju-porukkuthillaiye.md) — `நெஞ்சு பொறுக்கு தில்லையே` — சுப்பிரமணிய பாரதி.
4. [`tracks/04-il-vaazhvinile.md`](tracks/04-il-vaazhvinile.md) — `இல் வாழ்வினிலே` — பாரதிதாசன்.
5. [`tracks/05-pudhu-pennin-manathai.md`](tracks/05-pudhu-pennin-manathai.md) — `புது பெண்ணின் மனதை` — கே. பி. காமாட்சிசுந்தரம் — primary scene 33 plus scene-47 reprise.
6. [`tracks/06-o-rasikkum-seemane.md`](tracks/06-o-rasikkum-seemane.md) — `ஓ ரசிக்கும் சீமானே` — கே. பி. காமாட்சிசுந்தரம்.
7. [`tracks/07-ellorum-vaazha-vendum.md`](tracks/07-ellorum-vaazha-vendum.md) — `எல்லோரும் வாழ வேண்டும்` — அண்ணல் தங்கோ.
8. [`tracks/08-konju-mozhi-sollum.md`](tracks/08-konju-mozhi-sollum.md) — `கொஞ்சு மொழி சொல்லும்` — கே. பி. காமாட்சிசுந்தரம்.
9. [`tracks/09-poomalai.md`](tracks/09-poomalai.md) — `பூமாலை` — மு. கருணாநிதி.
10. [`tracks/10-porule-illaarkku.md`](tracks/10-porule-illaarkku.md) — `பொருளே இல்லார்க்கு` — கே. பி. காமாட்சிசுந்தரம்.
11. [`tracks/11-vaazhga-vaazhgave.md`](tracks/11-vaazhga-vaazhgave.md) — `வாழ்க வாழ்கவே` — பாரதிதாசன்.

The soundtrack title in file metadata follows `tracklist-evidence.json`; the Tamil body follows the verified canonical scene text exactly. Track metadata must never be used to normalize the source wording.

## Separate quoted verse

[`quoted-verses/001-vidhavayin-kaadhal.md`](quoted-verses/001-vidhavayin-kaadhal.md) preserves the scene-28 quotation beginning `கோரிக்கையற்று கிடக்குதண்ணே—இங்கு`. It is explicitly attributed to **பாரதிதாசன்** by the canonical dialogue and is **not** one of the 11 soundtrack compositions.

## Structural rules preserved

- `தேசம் ஞானம் கல்வி` is one soundtrack composition but two canonical occurrence records: `parasakthi-song-005` (`குதம்பாய்`) and `parasakthi-song-006` (`தாண்டவக்கோனே`). Both source sections remain separately marked inside one track file.
- `புது பெண்ணின் மனதை` uses scene 33 as the primary composition text. Scene 47 is preserved as a reprise section in the same track file, not as a twelfth soundtrack composition.
- Scene 4's speaker labels remain in the Tamil derivative because they are part of the verified canonical representation.
- Cross-page source anchors are retained where they occur inside song text.
- Scene 48's song derivative contains only the closing song text; `—சுபம்—` and the printer line are not folded into the song.

## Immutability rule

No song derivative may modify:

- the canonical transcription;
- scene derivatives;
- dialogue records;
- character mappings;
- song occurrence inventory wording.

Web lyrics, audio, later editions and familiar versions are never used to repair the Tamil body.

## Next activity

Begin **English translation as a separate derivative layer**. First define a source-linked translation schema and create a small verified pilot. Translation must reference immutable Tamil source units and must never overwrite the Tamil canonical or derivative layers.
