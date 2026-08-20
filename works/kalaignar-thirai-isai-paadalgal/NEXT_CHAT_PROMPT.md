# Next-chat prompt — கலைஞர் திரை இசைப் பாடல்கள்

Continue the **கலைஞர் திரை இசைப் பாடல்கள்** archival/translation/Reading Room integration project directly in:

`pugazg/kalaignar-cinema-works`

Work on `main`.

Active work path:

`works/kalaignar-thirai-isai-paadalgal/`

## Mandatory startup

Treat current GitHub `main` and current workflow state as authoritative over stale SHAs or historical handover text.

Before making any repository change, read completely:

- `works/kalaignar-thirai-isai-paadalgal/PROJECT_HANDOVER.md`
- `works/kalaignar-thirai-isai-paadalgal/CONTINUATION_GUIDELINES.md`
- `works/kalaignar-thirai-isai-paadalgal/NEXT_CHAT_PROMPT.md`
- `works/kalaignar-thirai-isai-paadalgal/README.md`
- `works/kalaignar-thirai-isai-paadalgal/metadata.yaml`
- `works/kalaignar-thirai-isai-paadalgal/PROGRESS.md`
- `works/kalaignar-thirai-isai-paadalgal/AUDIT.md`
- `works/kalaignar-thirai-isai-paadalgal/integrations/reading-room/README.md`
- `works/kalaignar-thirai-isai-paadalgal/integrations/reading-room/build.py`
- `works/kalaignar-thirai-isai-paadalgal/integrations/reading-room/sync_status.py`
- `works/kalaignar-thirai-isai-paadalgal/editions/en/QA_REPORT.md`
- `works/kalaignar-thirai-isai-paadalgal/editions/en/manifest.json`
- `.github/workflows/kalaignar-song-anthology-english-preflight.yml`

Then inspect current `main`, recent commits and the latest workflow run. Check whether `integrations/reading-room/reading-room.json`, `QA_REPORT.md` and `manifest.json` have appeared since this handover.

## Completed work — do not restart

The source-linked corpus is closed:

- 54/54 Tamil songs verified;
- Tamil fidelity complete, unresolved readings 0;
- 54/54 English translations complete-verified;
- 3 pilot-verified + 51 verified;
- 54/54 `anthology-attributed`;
- 1,105 paired Tamil/English line cues;
- deterministic English reader/export complete-verified.

Do not smooth or genericize Kalaignar's English translation. Preserve repetition, rhetoric, political/social force, concrete imagery, colloquial energy, culture-bearing vocabulary and performance terms.

## Current activity

Reading Room integration preparation has started inside the cinema-works repository. The integration boundary contains an explicit contract plus deterministic `build.py` and `sync_status.py`, and the existing English-reader workflow has been extended to build/QA the Reading Room payload after reader QA.

## Exact next activity

First determine live state:

1. verify latest `main` and workflow result;
2. check whether generated Reading Room outputs now exist;
3. if they exist, inspect `QA_REPORT.md` and `manifest.json`, verify **PASS**, expected **23 film groups / 54 songs / 1,105 line cues**, preserved anthology order, attribution/status history, exact provenance including all eight cross-page songs, and synchronized repository status;
4. if they do not exist or the workflow failed, diagnose and fix the integration build/workflow, without reopening verified Tamil/English layers for UI convenience;
5. once payload QA is PASS, mark repository-internal Reading Room integration preparation complete and refresh handover/guidelines/prompt/status as needed.

Do **not** claim deployment to `nenjukkuneethi.org/read` from this repository. Applying the payload to the separate Reading Room implementation repository is the following activity and requires that repository to be explicitly brought into scope.
