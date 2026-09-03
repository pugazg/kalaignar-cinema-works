# Raja Rani — Final Repository Handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Work: `works/raja-rani/` — **ராஜா ராணி**

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first. Do not reopen completed work because an older historical batch file contains an earlier count.

## Controlling source

- `TVA_BOK_0017188_ராஜா_ராணி.pdf`
- 80 PDF pages
- SHA-256: `26ecc026b89deafac94bb3b107ee7c5f361c68796c4a1cdf4d01ad7c1c0d31a4`
- numbered songs: PDF 4–9
- screenplay/dialogue: PDF 10–79 / printed pp.9–78

## Final archival state

- source pages: **79/79 verified**;
- screenplay pages: **70/70 verified**;
- archival scene derivatives: **58/58**, blocked 0;
- immutable dialogue records: **1,071**;
- exact source labels: **80/80**;
- verified entities/roles/collectives: **44**;
- numbered Tamil songs: **11/11**;
- song/performance occurrences: **15**;
- authorship: **5 later-anthology Kalaignar-attributed / 6 unresolved**.

Permanent direct-scan verdicts include PDF27 `இரவெல்லாம்`, PDF48 `வந்தனா` / `திடீர்னு`, PDF57 `முன்னுக்கு பின் முரணாயிகிட்டே போவது?`, and PDF74's `K. N. சங்கரன் ...` as a non-canonical ownership/library stamp.

The T055/T056 correction is permanent: scene 55 owns 25 immutable dialogue records, scene 56 owns 5, and deleted duplicate IDs `s055-d026`–`s055-d030` must never be restored.

## Final English state

Screenplay:

- **58/58 scenes**;
- **1,236 verified units**;
- **1,071/1,071 immutable dialogue links**;
- 19 source-unlabelled spoken units;
- 15 cross-page English units;
- 4/4 screenplay performance references.

Numbered songs:

- **11/11 verified English song records**;
- **67 sections**;
- **181/181 Tamil-English line/cue mappings**;
- 4 cross-page songs;
- authorship/performance tiers unchanged.

## Deterministic reader/export — COMPLETE

Directory: `works/raja-rani/editions/en/`

- preflight: **PASS** over 200 authoritative inputs;
- generated Markdown / HTML / JSON: **QA PASS**;
- Markdown SHA-256: `6437a0a39cebbaf17ab63f76f7aef6f9f62eb3c4abbd07864974d47be20902c8`;
- HTML SHA-256: `c24ea9ab0f1ee77b3bc795b3134e4ad8bed78f00d6a8f896f9749052ff074ec6`;
- JSON SHA-256: `76827d570f3079c04463e3142a9edf32f35c1497e2b820bfa467f8203d7441e2`.

The reader preserves 11 source-numbered songs separately from 58 archival-only screenplay navigation scenes.

## Reading Room payload — COMPLETE

Directory: `works/raja-rani/integrations/reading-room/`

- payload QA: **PASS**;
- payload bytes: **974,510**;
- payload SHA-256: `ab1058cb5a22ba78e68938f50efc586cc53eb07ef544bdf3919bb3c4b8c46c9b`;
- site application: **not-applied**.

The payload is ready for the separate Reading Room implementation repository but has not been applied there.

## Mandatory startup for any future Raja Rani work

Read:

1. `docs/CINEMA_WORKS_PROCESSING_GUIDE.md`
2. `docs/STATUS_CONSISTENCY_AUDIT.md`
3. this handover
4. `docs/NEXT_CHAT_PROMPT_RAJA_RANI.md`
5. `works/raja-rani/README.md`
6. `works/raja-rani/metadata.yaml`
7. `works/raja-rani/editions/en/QA_REPORT.md`
8. `works/raja-rani/editions/en/manifest.json`
9. `works/raja-rani/integrations/reading-room/QA_REPORT.md`
10. `works/raja-rani/integrations/reading-room/manifest.json`

## Exact next activity

There is **no required Raja Rani repository-internal activity** remaining.

If the user explicitly authorizes modification of the separate Kalaignar Digital Library / Reading Room implementation repository, apply `works/raja-rani/integrations/reading-room/reading-room.json` there while preserving its navigation, provenance, authorship and language-presentation rules. Otherwise make no further production changes merely to generate another standalone format.
