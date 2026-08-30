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
and the verified zero lyric-text drift. Read that note before any downstream
import or Reading Room application.

The Kalaignar-authorship inclusion boundary it left open has since been
adjudicated in its own activity, recorded in:

`notes/AUTHORSHIP_INCLUSION_EVIDENCE.md`

That note explains the complete 54-song evidence gate across **both** known
printed witnesses, the evidence levels and decision vocabulary, the withheld
group and why it is withheld, and the rule that `unresolved` and
`insufficient-evidence` are never read as findings that a song is not
Kalaignar's.

Witnesses adjudicated:

- controlling 2024 `TVA_BOK_0065867` — per-film song lists with a per-song
  lyricist column in 21 of 23 film sections;
- earlier 1989 `TVA_BOK_0065773` — 40 numbered sections, no lyricist credit
  anywhere, an explicit collection-scoped authorship claim in the compiler's
  preface and the independent foreword, and song-specific editorial notes naming
  கலைஞர் for 12 of those sections. Its 40 sections map to 39 current
  records; 15 current songs are absent from it, which is a source fact and never
  negative evidence.

Current authorship decisions: **48** `established-kalaignar`, **6** `unresolved`
(013–018, அம்மையப்பன்), **0** `insufficient-evidence`, **0**
`established-other`, **0** material conflicts.

**Authorship certainty and public display eligibility are separate fields.** The
owner's publication decision, recorded in section 8a of the authorship note, is:

| | |
| --- | ---: |
| Authorship established | **48 / 54** |
| Authorship unresolved | **6 / 54** (013–018) |
| Reading Room display set | **54 / 54** |
| May carry a positive Kalaignar-authorship claim | **48** |
| Authorship-uncertainty notice required | **6** (013–018) |

All 54 numbered lyrics are displayable because they are the controlling source's
numbered corpus and its front matter (PDF 12, PDF 16) presents that corpus as
Kalaignar's film songs. The அம்மையப்பன் section (PDF 43) is the explicit
source-internal exception, and it controls for songs 013–018.

> **PUBLIC DISPLAY DOES NOT RESOLVE AUTHORSHIP.** A displayable song is not
> thereby attributed to Kalaignar.

**E1 may consume all 54 lyric records for display, but MUST treat 013–018 as
unresolved-authorship records**: no Kalaignar-authorship claim for them, and the
Tamil/English notice from notice group `ammayappan-unresolved` shown with them.
Per-record fields carry this: `public_display`, `public_authorship_claim`,
`authorship_notice_required` and `public_authorship_notice_group`. The single
`public_inclusion` boolean has been retired because it conflated the two
questions; the validator fails if it reappears. **E1 is not started here.**

Machine-readable outputs: `authorship/inclusion-evidence.json` (54 records, 174
structured evidence items, the publication policy and the notice group),
`authorship/public-inclusion.json` (generated — do not hand-edit; it carries
`displayable_song_ids`, `established_kalaignar_song_ids`,
`unresolved_authorship_song_ids`, `authorship_notice_required_song_ids` and the
notice text) and the fail-closed `authorship/validate.py`, which recomputes
every authorship decision and every display/claim/notice flag from the evidence
items, re-parses the
committed cross-witness mapping in `songs/SOURCE_WITNESS_0065773_DEDUP.md`,
requires the manifest to pin the register's own SHA-256 and the source-main SHA
the gate was adjudicated against, and fails if the archival attribution layer
moves. Validator status: PASS.

All 54 records keep their `anthology-attributed` status — the register sits
alongside that field and does not promote, downgrade or replace it. Read that
note before any authorship-inclusion or public-selection work.

Both notes are hand-written and live under `notes/`, outside status-generator
control. `sync_status.py` owns only the regions delimited by its explicit
`BEGIN GENERATED: reading-room-status` / `END GENERATED: reading-room-status`
marker comments. Keep this pointer and all other human-authored prose outside
those generated blocks; do not duplicate, relocate or nest the markers, and do
not hand-edit generated content between them — change the generator and let it
regenerate.

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