# Manthiri Kumari — Reading Room integration QA

Status: **PASS**

This QA covers the **source-linked composition payload** prepared for the Kalaignar Digital Library / Reading Room. The payload references verified repository records instead of duplicating canonical/translated text; the site ingest step must resolve those paths without rewriting them.

## Structure

- navigation model: **story summary + performances**;
- story-summary record: **1/1**;
- story-summary logical units: **13**;
- story-summary cross-page units: **1**;
- performance records: **15/15**;
- performance sections: **52**;
- Tamil/English performance line-cues represented by linked records: **234/234**;
- mapping mismatches in authoritative translation layer: **0**;
- performance source order: **1–15 archival navigation only, not printed numbering**;
- synthetic screenplay scene IDs: **0**.

## Provenance / evidence

- source scan SHA-256: `a64ac0b5ff4adca75d0860d9d52c5324f93f55da3b060cecb43743d0bbc696ee`;
- expected source-link targets: **32** — 16 Tamil/source records + 16 English translation records;
- confirmed current-anthology witness: **1/15** — block 11 ↔ `kalaignar-song-001`;
- source-only in current anthology: **14/15**;
- booklet item-level lyricists: **0 verified / 15 unresolved**;
- authorship upgrades introduced by payload: **0**;
- performance 13 heading/turn-label mismatch remains explicitly protected.

## Integrity

- payload mode: `source-linked-composition`;
- `reading-room.json` bytes: **15,704**;
- SHA-256: `20a0db293b936757e7d01def336252f28543337f319dfae6ad7bf5ae886bab43`;
- canonical Tamil changed: **no**;
- site application status: **not-applied**.

**Result: PASS.**
