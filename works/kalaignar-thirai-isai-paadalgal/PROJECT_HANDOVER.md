# Project handover — கலைஞர் திரை இசைப் பாடல்கள்

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Work path: `works/kalaignar-thirai-isai-paadalgal/`

## Mandatory startup

Treat live GitHub `main` and current workflow state as authoritative over every SHA/status recorded below. Before changing anything, read completely:

- this `PROJECT_HANDOVER.md`;
- `CONTINUATION_GUIDELINES.md`;
- `NEXT_CHAT_PROMPT.md`;
- `README.md`, `metadata.yaml`, `PROGRESS.md`, `AUDIT.md`;
- `notes/FULL_PDF_SONG_PAGE_SCAN.md`;
- `songs/page-map.json`, `songs/index.json`;
- `translations/README.md`, `translations/index.json`, `translations/PILOT_REVIEW.md`, and batch reviews through `BATCH_047_054_REVIEW.md`;
- `editions/en/PREFLIGHT_QA_REPORT.md`, `editions/en/QA_REPORT.md`, `editions/en/manifest.json`, `editions/en/audit_probe.py`, `editions/en/build.py`;
- `integrations/reading-room/README.md`, `integrations/reading-room/build.py`, `integrations/reading-room/sync_status.py`;
- `docs/SONG_TRANSLATION_GUIDE.md`;
- `.github/workflows/kalaignar-song-anthology-english-preflight.yml`.

Then inspect live `main`, recent commits, and the latest workflow run before acting.

## Durable reconciliation record

The cross-layer title/film metadata reconciliation completed before any Reading
Room application is recorded in:

`notes/READING_ROOM_TITLE_RECONCILIATION.md`

It holds the five controlling-scan source adjudications, the three
project-created English-title repairs, the work-specific title-authority rule,
the verified zero lyric-text drift, and the still-unresolved Kalaignar-authorship
inclusion boundary. Read that note before any downstream import, Reading Room
application or authorship-inclusion work.

The note is hand-written and lives under `notes/`, which the status generator
never writes to. Do not move its contents into the audit, progress or work-readme
documents: the generator rewrites each of those from its next-activity heading to
end of file, and rewrites this file between its next-activity heading and its
repository-boundary heading. Prose placed inside those ranges is removed on the
next synchronization run.

## Controlling source

`TVA_BOK_0065867_கலைஞர்_திரை_இசைப்_பாடல்கள்.pdf`

- 194 physical PDF pages;
- SHA-256 `f0beac14c33ffc73c0231bd54ca57ec4093eef6e85072bd68ce48f7b5e258b05`;
- image-only source;
- rendered scan controls Tamil readings;
- classification: **62 song-bearing / 132 ignored pages / 54 numbered songs**.

Never import absent lyrics from elsewhere.

## Closed source-linked layers — do not restart

### Tamil

- `001–054`: **54/54 verified**;
- transcription: **complete-verified**;
- fidelity audit: **complete**;
- unresolved readings: **0**.

### English

- **54/54 complete-verified**;
- history: **3 pilot-verified + 51 verified**;
- mode: `semantic-poetic-source-faithful`;
- attribution: **54/54 `anthology-attributed`**;
- mapped Tamil/English line cues: **1,105 / 1,105**.

Do not smooth the verified English into generic lyric English. Retain Kalaignar's repetition, rhetoric, political/social force, concrete imagery, colloquial energy, culture-bearing vocabulary, performance terms and documented source pressure points.

Exactly eight songs are cross-page and must retain complete provenance: `009` 38–39, `019` 53–54, `023` 58–59, `024` 62–63, `036` 86–87, `037` 90–91, `051` 121–122, `052` 123–124.

## Reader/export checkpoint

English preflight and deterministic reader/export are **complete-verified / PASS**. The reader contains **54 songs / 1,105 paired line cues / 0 warnings / 0 errors** at the completed checkpoint. Generated reader files must not be hand-edited; rebuild them from authoritative structured inputs.

## Historical pre-payload integration-preparation checkpoint

**Historical — superseded by the generated Reading Room status block below.** This
section records an earlier checkpoint taken *before* the Reading Room payload was
built and committed. Read current payload status from the generated block below
and from live repository state, not from this section.

At that earlier point, repository-internal Reading Room integration preparation had been implemented but its generated-output gate was **not yet recorded complete**.

Implemented under `integrations/reading-room/`:

- `README.md` — downstream authority/navigation/language/search/attribution/provenance contract;
- `build.py` — deterministic Reading Room payload builder and QA;
- `sync_status.py` — repository status synchronizer.

The existing workflow `.github/workflows/kalaignar-song-anthology-english-preflight.yml` was extended to run the Reading Room payload build/QA after the verified English reader gate and then synchronize status.

Expected payload invariants:

- **23 film groups** in first-appearance order;
- **54 songs** in anthology order `001–054`;
- **1,105** paired Tamil/English line cues;
- Tamil/English titles and lyrics unchanged from verified layers;
- printed film year/music/voice metadata where available;
- exact source PDF page arrays;
- immutable source paths and archival IDs;
- **3 pilot-verified + 51 verified** history;
- **54/54 `anthology-attributed`**;
- all eight cross-page songs retaining complete provenance;
- film → song navigation and Tamil/English/parallel presentation guidance only at the downstream presentation layer.

`anthology-attributed` must not be promoted to primary-source-verified original-film authorship without separate upstream evidence.

## Historical live checkpoint from an earlier chat

**Historical — superseded by the generated Reading Room status block below.**

The workflow integration commit observed on `main` was `0b8d833bf4696b30e7a0d1a16679105aa0c4c026` (`Build Reading Room payload after reader QA`). A subsequent workflow-related commit `b8f8565647d612e0a6e2e3e34bbf9c8fe7507e22` was also made during this activity. These are historical pointers only; the next chat must verify current `main` rather than assuming either is still HEAD.

At the final explicit check in that earlier chat, `integrations/reading-room/reading-room.json` was **not found on `main`**. That observation is **historical only**: the payload has since been built, committed and verified, and the generated block below records the current complete-verified status. The underlying caution still holds in general — builder or workflow code existing is not by itself evidence that a gate has passed — but it no longer describes this work's state.

<!-- BEGIN GENERATED: reading-room-status -->

## Reading Room integration payload checkpoint

The downstream structured payload is **complete-verified** under `integrations/reading-room/`:

- `reading-room.json` — 23 film groups, 54 songs, 1,105 paired lines-cues;
- `QA_REPORT.md` — **PASS**;
- `manifest.json` — deterministic input/output hashes;
- `build.py` — deterministic payload builder;
- `README.md` — integration contract and authority rules.

Payload SHA-256: `8ec0e25f7fc1f1a9750d370ccbef5dd07caa66629a3dfacb8425bbeebd08fcce`.

QA confirms zero song/translation/line ID duplication, zero anthology-order or film-group coverage drift, zero source-page drift, zero Tamil or English text drift, zero status/attribution drift, and **0 warnings / 0 errors**.

The payload uses film-first navigation (23 anthology film sections) with anthology-song secondary navigation, preserves exact source IDs/page provenance, and keeps `anthology-attributed` distinct from original-film primary-source verification.

**Site application status remains `not-applied`.** No separate Reading Room implementation repository has been modified by this project checkpoint.

## Exact next activity

Apply the verified `integrations/reading-room/reading-room.json` payload in the separate Kalaignar Digital Library / Reading Room implementation repository only after that repository is explicitly authorized for modification. Preserve the source-faithful Tamil/English strings exactly; UI routing, cards, filters, search indexes and language switching remain presentation metadata.

<!-- END GENERATED: reading-room-status -->

## Repository boundary

This repository prepares a verified downstream payload; it does **not** by itself deploy or update `nenjukkuneethi.org/read`. Do not edit another repository without explicit user authorization.