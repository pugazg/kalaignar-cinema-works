# Next-chat prompt — கலைஞர் திரை இசைப் பாடல்கள்

Continue the **கலைஞர் திரை இசைப் பாடல்கள்** archival/translation/Reading Room integration-preparation project directly in:

`pugazg/kalaignar-cinema-works`

Work on `main`.

Active path:

`works/kalaignar-thirai-isai-paadalgal/`

## Mandatory startup

Treat current GitHub `main` and current workflow state as authoritative over stale SHAs and historical status text.

Before making any repository change, read completely:

1. `works/kalaignar-thirai-isai-paadalgal/PROJECT_HANDOVER.md`
2. `works/kalaignar-thirai-isai-paadalgal/CONTINUATION_GUIDELINES.md`
3. `works/kalaignar-thirai-isai-paadalgal/NEXT_CHAT_PROMPT.md`
4. `works/kalaignar-thirai-isai-paadalgal/README.md`
5. `works/kalaignar-thirai-isai-paadalgal/metadata.yaml`
6. `works/kalaignar-thirai-isai-paadalgal/PROGRESS.md`
7. `works/kalaignar-thirai-isai-paadalgal/AUDIT.md`
8. `works/kalaignar-thirai-isai-paadalgal/integrations/reading-room/README.md`
9. `works/kalaignar-thirai-isai-paadalgal/integrations/reading-room/build.py`
10. `works/kalaignar-thirai-isai-paadalgal/integrations/reading-room/sync_status.py`
11. `works/kalaignar-thirai-isai-paadalgal/editions/en/PREFLIGHT_QA_REPORT.md`
12. `works/kalaignar-thirai-isai-paadalgal/editions/en/QA_REPORT.md`
13. `works/kalaignar-thirai-isai-paadalgal/editions/en/manifest.json`
14. `.github/workflows/kalaignar-song-anthology-english-preflight.yml`

Then inspect live `main`, recent commits, and the latest workflow run before acting.

## Completed work — immutable unless source evidence requires reopening

The source-linked corpus is closed:

- **54/54** Tamil songs verified;
- Tamil fidelity complete; unresolved readings **0**;
- **54/54** English translations complete-verified;
- status history **3 pilot-verified + 51 verified**;
- **54/54 `anthology-attributed`**;
- **1,105** paired Tamil/English line cues;
- deterministic English reader/export **complete-verified / PASS**.

Do not smooth or genericize Kalaignar's English translation. Preserve repetition, rhetoric, political/social force, concrete imagery, colloquial energy, culture-bearing vocabulary and performance terms.

Eight cross-page songs must retain exact provenance: `009` 38–39, `019` 53–54, `023` 58–59, `024` 62–63, `036` 86–87, `037` 90–91, `051` 121–122, `052` 123–124.

## Current activity

Repository-internal Reading Room integration preparation is implemented but **not yet proven complete by generated outputs**.

The integration layer contains an explicit contract, deterministic `build.py`, and `sync_status.py`. The existing English-reader workflow has been extended to run payload build/QA and status synchronization after reader QA.

Last known implementation checkpoints from the preceding chat include `0b8d833bf4696b30e7a0d1a16679105aa0c4c026` and later `b8f8565647d612e0a6e2e3e34bbf9c8fe7507e22`; these are historical pointers only. Verify live HEAD.

At the final explicit check before this handover was refreshed, `integrations/reading-room/reading-room.json` was **not found on `main`**. Do not infer PASS from the presence of builder/workflow code.

## Exact next activity

Proceed without asking for a redundant clarification:

1. inspect live `main`, recent commits, and the latest run of `.github/workflows/kalaignar-song-anthology-english-preflight.yml`;
2. check whether all three outputs exist:
   - `integrations/reading-room/reading-room.json`
   - `integrations/reading-room/QA_REPORT.md`
   - `integrations/reading-room/manifest.json`;
3. if absent, inspect workflow jobs/steps/logs, identify the first failure, and fix the integration builder/workflow/status plumbing without reopening verified Tamil/English content for UI convenience;
4. if present, verify **QA PASS**, exactly **23 film groups / 54 songs / 1,105 line cues**, anthology order `001–054`, **3 pilot-verified + 51 verified**, **54/54 anthology-attributed**, all eight cross-page provenance arrays, source paths/IDs and manifest integrity;
5. verify `sync_status.py` has synchronized repository status and no file falsely claims website deployment;
6. once PASS is established, mark the **repository-internal Reading Room integration-preparation gate complete** and refresh handover/guidelines/prompt/status documents;
7. stop at this repository boundary.

## Important boundary

Do **not** claim or perform deployment to `nenjukkuneethi.org/read` from this repository. Applying the verified payload to the separate Kalaignar Digital Library / Reading Room implementation repository is a subsequent activity and requires explicit user authorization to bring that repository into scope.