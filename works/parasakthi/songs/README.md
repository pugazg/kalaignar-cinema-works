# Parasakthi song / verse index

**Stage:** structured derivatives — authorship gate  
**Canonical authority:** verified Tamil transcription / scene derivatives  
**Status:** inventory complete; item-level authorship resolution in progress

This directory inventories song/verse material and records attribution evidence separately from the canonical Tamil. A lyric or verse appearing in this booklet is **not automatically a Kalaignar lyric**.

## Files

- `schema.json` — song/verse inventory record schema.
- `credits.json` — exact booklet-wide `பாடல்கள்` contributor list from PDF 3.
- `inventory.json` — canonical-order inventory of all candidate song/verse occurrences.
- `index.json` — current authorship-gate checkpoint.

No individual song-text derivative file is created until its authorship field has an explicit disposition.

## Booklet-wide song credits

The PDF 3 credits page prints the heading `பாடல்கள்` and lists:

- பாரதியார்
- பாரதிதாசன்
- உடுமலை நாராயணகவி
- மு. கருணாநிதி
- கே. பி. காமாட்சி சுந்தரம்
- கு. ம. அண்ணல்தங்கோ

These are **booklet-wide credits**. The credits page does not pair each contributor with a particular song. `credits.json` therefore records `item_level_assignment_present: false`.

## Candidate inventory

The first complete inventory contains **14 song/verse occurrences** in canonical order.

Classification is textual/source-led rather than based on later soundtrack knowledge:

- `unlabelled-song` — song/verse is set as verse without speaker labels, usually with scene context indicating singing;
- `speaker-labelled-verse` — individual sung/verse lines are explicitly attached to dialogue speaker labels;
- `quoted-verse` — verse is quoted/referred to in dialogue rather than staged as a song performance;
- `unlabelled-reprise` — a later partial recurrence of an earlier block.

The inventory improves on the earlier structural map's location aid. For example, scene 15 contains two structurally separable verse sections (`குதம்பாய்` and `தாண்டவக்கோனே`) and scene 28 contains a quoted Bharathidasan verse on PDF 33 even though the earlier map only flagged nearby lyric-formatted pages.

## Current authorship state

- Candidate blocks: **14**
- Authorship verified: **1**
- Authorship review: **0**
- Authorship unresolved: **13**

The only internally verified item at this checkpoint is `parasakthi-song-009`, beginning `கோரிக்கையற்று கிடக்குதண்ணே—இங்கு`. In scene 28, Narayana Pillai explicitly introduces the quotation by saying that **பாரதிதாசன்** wrote about widowhood immediately before the verse. Therefore its attribution is recorded as `verified` with `canonical-context-explicit` evidence.

All other items remain unresolved even when an attribution may be familiar from literary or film history. Familiarity is not archival evidence.

## Important structural cases

- Scene 4's `இவ்வாழ்வினிலே ஒளி ஏற்றும் தீபம்` is speaker-labelled verse and therefore already overlaps the dialogue index. Character performers do not imply lyric authorship.
- Scene 15's `தேசம், ஞானம்...` / `குதம்பாய்` section and `ஆரியக் கூத்தாடினாலும்...` / `தாண்டவக்கோனே` section are inventoried separately so later evidence can assign different authors if necessary.
- Scene 33's `புதுப்பெண்ணின் மனதைத் தொட்டுப் போறவரே` has a short reprise in scene 47; the reprise points back to the original inventory record.
- Scene 39 explicitly says the `நெஞ்சு பொறுக்குதில்லையே` song belongs to another person, but does not name the author in the scene text, so attribution remains unresolved pending documented evidence.
- Scene 48's closing `எல்லோரும் வாழ வேண்டும்` remains an unlabelled collective song; the preceding scene says `(பேதமின்றி பாடுகின்றனர்)`.

## Authorship rules

1. The canonical Tamil text must never be changed to fit an attribution source.
2. Booklet-wide credits are not item-level evidence.
3. A printed item-level attribution or explicit canonical-context attribution can establish `verified` authorship.
4. When the booklet does not disambiguate an item, reliable external evidence may be recorded as attribution metadata only.
5. If reliable evidence still does not resolve an item, keep `authorship.status: unresolved`.
6. Song-specific English translation remains blocked until the corresponding item's authorship disposition is recorded.

## Next activity

Resolve the **13 unresolved** items one by one. Prefer primary/official or other reliable attribution sources, record the source separately, and do not modify canonical Tamil, dialogue records, scene files, or character mappings.
