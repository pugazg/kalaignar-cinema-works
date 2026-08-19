# Anthology source notes

## 1. Edition authority

`கலைஞர் திரை இசைப் பாடல்கள்` is a compiled publication, First Edition June 2024. It is treated as the controlling witness for **this anthology edition**.

The anthology's lyric text must not be silently replaced by film audio, online lyric sites, subtitles, memory, or another edition.

Attribution terminology:

- `anthology-attributed`: this anthology attributes the numbered song to Kalaignar;
- `primary-source-verified`: a separate original/near-contemporary item-level source has been checked and supports the attribution;
- `review`: evidence conflicts or needs further examination;
- `unresolved`: evidence is insufficient.

The initial corpus is `anthology-attributed` unless a separate verification record says otherwise.

## 2. Physical page-count discrepancy

The mounted source binary contains **194 PDF pages**. The printed colophon says **`No of pages : 192`**. These are distinct source facts.

A conversation-file preview layer exposed only 150 pages during intake. That preview limitation is not used as the archival physical-page count; direct binary inspection controls the technical PDF count.

## 3. மந்திரிகுமாரி — censored/prohibited song mentioned but not printed as numbered lyric

PDF 25, beneath `இப்படத்தில் இடம் பெற்ற பாடல்கள்`, contains an editorial note saying that **15 songs** were prepared for the film and that Kalaignar wrote two songs:

1. `ஆளப்பிறந்தவன் தமிழன் அவன்தானே`
2. `ஊருக்கு உழைப்பவண்டி (எரும கன்னுக்குட்டி)`

The note states that the first song was prohibited/censored (`சென்சாரால் தடைசெய்யப்பட்டுவிட்டது`). It also discusses uncertainty about its disc/record availability.

The anthology's numbered lyric corpus prints only `ஊருக்கு உழைப்பவண்டி` as song **001** on PDF 26.

Archival disposition:

- do not create a synthetic numbered record for `ஆளப்பிறந்தவன் தமிழன் அவன்தானே`;
- do not reconstruct its lyric from outside sources;
- preserve the prose claim as an editorial note;
- if a future independent source supplies the song, archive that source separately and cross-reference it.

## 4. பராசக்தி — anthology item-level attribution

PDF 28 lists songs from the film and explicitly aligns `கலைஞர்` with:

- `இல் வாழ்வினிலே ஒளி ஏற்றும் தீபம்`;
- `பூமாலை நீயே`.

These correspond to numbered anthology songs **002** and **003**.

This is useful **item-level anthology evidence**, but it does not overwrite the existing `works/parasakthi/` source layers. Any textual variation between the 2024 anthology and the archived Parasakthi booklet should be documented as source variation, not normalized away.

## 5. Initial difficult readings requiring recheck

The initial direct read of song 001 on PDF 26 preserves several source-looking colloquial/typographical forms in the final stanza rather than correcting them from familiarity. Recheck these forms before verification.

Song 003 on PDF 30 likewise contains a small number of visually difficult forms; the draft file marks them for reinspection instead of guessing.

## 6. Contents titles are provisional incipits

The `பொருளடக்கம்` on PDF 21–23 establishes the 54-song inventory. Its wording is stored as `contents_title` in `songs/index.json`.

When a numbered lyric page is processed, the lyric page becomes the controlling source for:

- displayed lyric incipit/title;
- music/voice labels;
- stanza/turn labels;
- exact lyric text.

A contents/lyric-page difference must be preserved as a variant, not silently reconciled.
