# Manthiri Kumari — Reading Room integration payload

This directory contains the deterministic **source-linked Reading Room composition payload** for `மந்திரி குமாரி`.

It does **not** modify or deploy the separate public Reading Room implementation repository.

## Payload model

`reading-room.json` is intentionally source-linked rather than a second duplicated text corpus. It points to the complete-verified Tamil and English records that the Reading Room ingest step must resolve.

Authoritative linked inputs:

- bilingual reader composition: `works/manthiri-kumari/editions/bilingual/reader-edition.json`;
- Tamil story summary: `works/manthiri-kumari/story-summary/index.json`;
- English story summary: `works/manthiri-kumari/translations/story-summary.json`;
- Tamil performance records: `works/manthiri-kumari/songs/records/001.json`–`015.json`;
- English performance records: `works/manthiri-kumari/translations/performances/001.json`–`015.json`.

## Navigation

The booklet is not a screenplay. The Reading Room must present:

1. `கதைச்சுருக்கம் / Story Summary`;
2. 15 performance blocks in source occurrence order.

The performance ordinals are archival navigation only, not printed numbering. No screenplay scenes may be invented.

## Evidence boundaries

- printed credit: `கதை, வசனம் : மு. கருணாநிதி`;
- item-level lyric authorship: **0 verified / 15 unresolved**;
- one confirmed current-anthology witness: block 11 ↔ `kalaignar-song-001`;
- 14 blocks remain source-only against the current anthology;
- performance 13 keeps heading `பார்த்திபன்—மந்திரிகுமாரி` while internal source labels remain `பார்த்திபன்` / `அமுதவல்லி`.

## Completion checkpoint

Status: **payload-complete-verified — QA PASS**.

- payload mode: `source-linked-composition`;
- payload bytes: **16,061**;
- payload SHA-256: `2d4f0071b0faf463699255c29d10ae0c734a2d367c581ad469987a6a2f2bbb3d`;
- site application: **not-applied**.

The separate Reading Room implementation repository must be explicitly authorized before this payload is applied there.
