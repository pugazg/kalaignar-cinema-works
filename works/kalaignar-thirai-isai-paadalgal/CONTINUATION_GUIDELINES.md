# Continuation guidelines — கலைஞர் திரை இசைப் பாடல்கள்

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Work path: `works/kalaignar-thirai-isai-paadalgal/`

## Startup rule

Treat current GitHub `main` as authoritative over historical SHAs and older status prose. Before changing this work, read `PROJECT_HANDOVER.md`, this file, `NEXT_CHAT_PROMPT.md`, the work `README.md`/`metadata.yaml`/`PROGRESS.md`/`AUDIT.md`, `integrations/reading-room/README.md`, the English reader QA/manifest, and the current workflow.

## Immutable completed layers

Do not restart or rewrite the completed source-linked corpus for convenience:

- Tamil songs: 54/54 verified; fidelity complete; no unresolved readings.
- English: 54/54 complete-verified; 3 pilot-verified + 51 verified.
- Translation mode: `semantic-poetic-source-faithful`.
- Attribution: 54/54 `anthology-attributed`.
- Reader/export: deterministic complete-verified package, 1,105 paired line cues, 0 warnings/errors at the completed checkpoint.

Retain Kalaignar's repetition, rhetoric, political/social force, concrete imagery, colloquial energy, culture-bearing vocabulary and performance terms. Never smooth the verified English into generic lyric English.

## Reading Room integration rules

The public Reading Room is downstream and never becomes textual authority. Consume structured verified data; do not scrape generated HTML when JSON/source-linked records are available.

Natural navigation for this anthology is **film → song**, preserving first film appearance and anthology song order `001–054`. Tamil, English and parallel display are presentation choices only.

Preserve exact archival IDs, page provenance and all eight cross-page page arrays. Search normalization belongs in a separate index and must never overwrite stored Tamil/English strings.

Do not promote `anthology-attributed` to primary-source-verified original-film authorship without separate item-level upstream evidence.

## Integration payload checkpoint

A dedicated boundary now exists at `integrations/reading-room/` with:

- `README.md` — integration contract;
- `build.py` — deterministic payload builder/QA;
- `sync_status.py` — status synchronizer;
- expected generated outputs: `reading-room.json`, `QA_REPORT.md`, `manifest.json`.

The workflow `.github/workflows/kalaignar-song-anthology-english-preflight.yml` has been extended to run reader QA/build, then Reading Room payload build and status synchronization.

Do not claim the public site has been updated merely because the integration payload exists. Site application is a separate-repository activity.

## Exact continuation logic

1. Inspect current `main` and latest workflow run first.
2. If the workflow has generated and committed `reading-room.json`, `QA_REPORT.md` and `manifest.json`, verify QA is PASS and status synchronization is consistent.
3. If generated outputs are absent or the workflow failed, diagnose/fix the payload build without altering verified Tamil/English content unless source evidence independently requires it.
4. Once payload QA is PASS, the repository-internal integration-preparation gate is complete.
5. The next cross-repository activity is applying the verified payload to the Kalaignar Digital Library / Reading Room implementation repository. Do not cross that repository boundary unless it is explicitly in scope in the new chat.

## Commit discipline

Use meaningful phase-specific commits. Fetch current blob SHA before replacing existing files. Synchronize handover/status files after a gate is completed. Never manually edit generated payload/reader files; regenerate them through their builders.
