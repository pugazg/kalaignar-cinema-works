# Parasakthi song / verse index

**Stage:** structured derivatives — authorship gate  
**Canonical authority:** verified Tamil transcription / scene derivatives  
**Status:** complete-verified

This directory inventories song/verse material and records attribution evidence separately from the canonical Tamil. A lyric or verse appearing in this booklet is **not automatically a Kalaignar lyric**.

## Files

- `schema.json` — song/verse inventory record schema.
- `credits.json` — exact booklet-wide `பாடல்கள்` contributor list from PDF 3.
- `tracklist-evidence.json` — user-supplied soundtrack screenshot, matched to the public Tamil Wikipedia soundtrack table, with 11-track → inventory-occurrence reconciliation.
- `inventory.json` — canonical-order inventory of all 14 candidate song/verse occurrences with final authorship dispositions.
- `index.json` — completed authorship-gate checkpoint.

The canonical source-order text remains in `../transcription/`; these files are derivative metadata and must never become an alternative transcription authority.

## Booklet-wide song credits

PDF 3 prints `பாடல்கள்` and lists:

- பாரதியார்
- பாரதிதாசன்
- உடுமலை நாராயணகவி
- மு. கருணாநிதி
- கே. பி. காமாட்சி சுந்தரம்
- கு. ம. அண்ணல்தங்கோ

These are booklet-wide credits only. The page does not pair each contributor with a particular song.

## Item-level soundtrack evidence

A user-supplied screenshot was matched exactly to the Tamil Wikipedia `பராசக்தி (1952 திரைப்படம்)` soundtrack table: the same **11 rows**, row order, titles, singers, lyricists, durations and total length **35:46**.

The 11 soundtrack tracks are:

1. `தேசம் ஞானம் கல்வி` — **உடுமலை நாராயண கவி**
2. `கா கா கா` — **உடுமலை நாராயண கவி**
3. `நெஞ்சு பொறுக்கு தில்லையே` — **சுப்பிரமணிய பாரதி**
4. `இல் வாழ்வினிலே` — **பாரதிதாசன்**
5. `புது பெண்ணின் மனதை` — **கே. பி. காமாட்சிசுந்தரம்**
6. `ஓ ரசிக்கும் சீமானே` — **கே. பி. காமாட்சிசுந்தரம்**
7. `எல்லோரும் வாழ வேண்டும்` — **அண்ணல் தங்கோ**
8. `கொஞ்சு மொழி சொல்லும்` — **கே. பி. காமாட்சிசுந்தரம்**
9. `பூமாலை` — **மு. கருணாநிதி**
10. `பொருளே இல்லார்க்கு` — **கே. பி. காமாட்சிசுந்தரம்**
11. `வாழ்க வாழ்கவே` — **பாரதிதாசன்**

The public table is secondary evidence. Its article cites a 1952 National Pictures song booklet among the music references, but that archived PDF could not be directly retrieved in this session. This limitation is preserved in `tracklist-evidence.json` rather than being hidden.

## Inventory reconciliation

The source-led canonical inventory still contains **14 occurrence records**, not 11, because it records textual/source structure rather than only soundtrack-track identity:

- **13 occurrence records** correspond to the 11 soundtrack tracks.
- `parasakthi-song-005` (`குதம்பாய்` section) and `parasakthi-song-006` (`தாண்டவக்கோனே` section) are separate canonical text occurrences but both belong to soundtrack track `தேசம் ஞானம் கல்வி` and are authored by **உடுமலை நாராயண கவி**.
- `parasakthi-song-013` is a partial reprise of `parasakthi-song-011` (`புது பெண்ணின் மனதை`) and inherits **கே. பி. காமாட்சிசுந்தரம்**.
- `parasakthi-song-009`, beginning `கோரிக்கையற்று கிடக்குதண்ணே—இங்கு`, is a **literary quotation**, not one of the 11 soundtrack tracks. Scene 28 itself explicitly introduces it as Bharathidasan's verse.

This preserves both soundtrack identity and the booklet's canonical textual organization.

## Final authorship state

- Candidate occurrences: **14**
- Authorship verified: **14**
- Authorship review: **0**
- Authorship unresolved: **0**
- Soundtrack tracks represented: **11**
- Quoted literary-verse records: **1**

No canonical Tamil, scene file, dialogue record, or character mapping was changed during authorship resolution.

## Authorship rules retained

1. Canonical Tamil text is never changed to fit an attribution source.
2. Booklet-wide credits are not item-level evidence.
3. Item-level soundtrack evidence may resolve attribution metadata when the exact title/opening can be reconciled to canonical text.
4. A source occurrence and a soundtrack composition are not always one-to-one; reprises and multi-section tracks must remain explicitly linked.
5. Literary quotations remain distinct from soundtrack songs.
6. Future song-specific derivative files must copy Tamil only from the verified canonical transcription/scene derivative, never from web lyric pages or audio memory.

## Next activity

Create song-specific Tamil derivative files for the **11 soundtrack compositions**. Each file should include authorship evidence, source PDF/printed-page provenance, canonical scene occurrence(s), and exact canonical Tamil text. Keep the scene-28 Bharathidasan quotation as a separate quoted-verse derivative, and keep scene 47 as a reprise link to the scene-33 composition rather than treating it as a new song.
