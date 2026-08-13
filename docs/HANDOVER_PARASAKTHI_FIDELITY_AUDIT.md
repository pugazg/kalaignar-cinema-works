# Parasakthi — controlling handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Handover refreshed: 2026-08-13

Current stage: **English translation in progress — canonical scenes 1–5 verified; scenes 6–10 in review**.

## Canonical/source state — immutable

- Source: `TVA_BOK_0062968_பராசக்தி.pdf`
- SHA-256: `b0024315ca2018a63807b8ff44eb02d132868a7250e6399a2144a10e47c4ad4c`
- 58 PDF pages; PDF 4–57 / printed pp.3–56 are canonical dialogue/song pages; PDF 58 is back matter.
- Canonical Tamil: **54 verified / 0 review / 0 unresolved markers**.
- Scene derivatives: **46/46 complete**; headings 23 and 34 are absent.
- Canonical scene 43 retains source heading 48; canonical final scene 48 retains source heading 43.
- Dialogue index: **642 complete-verified records**.
- Character index: **69/69 labels disposed across 48 entities**; `ராக` remains review and `நொண்டி` / `நொ` unresolved.
- Song authorship: **14/14 verified**.
- Tamil soundtrack derivatives: **11/11 complete-verified**, plus one separate Bharathidasan quoted-verse derivative.

Never use English translation, film audio, subtitles, web copies or later editions to repair the Tamil source.

## Translation files

- `works/parasakthi/translations/README.md`
- `works/parasakthi/translations/schema.json`
- `works/parasakthi/translations/index.json`
- `works/parasakthi/translations/records/scene-01.json` through `scene-10.json`

Translation rules:

- Tamil remains authoritative.
- Every English unit is source-linked.
- Exact Tamil `speaker_label` values remain immutable metadata.
- Stage directions may not gain invented action.
- Dialogue keeps rhetorical force, repetition, code-switching and social/political language where meaningful.
- Songs are semantic-poetic translations, never singable rewrites unless a separate future derivative explicitly says so.
- Cross-page source records remain one translation unit where the source record is one unit.
- English statuses (`draft`, `review`, `verified`) are independent from Tamil verification.

## Verified English coverage — scenes 1–5

The initial scene-1 pilot and the first full scenes-2–5 batch have passed deliberate second-pass review.

- scenes verified: **1, 2, 3, 4, 5**
- verified units: **70**

Review refinements applied before verification:

- scene 2 `அண்ணியிடம் போதல்`: English no longer adds an unsupported possessive;
- scene 2 `தங்கையின் வாழ்விலே பொன் விழா?`: question-shaped wording is preserved rather than normalized into a specific ceremony label;
- scene 4 `மாங்குயில்`: English uses natural `cuckoo`; the Tamil remains unchanged;
- scene 3's semantically unusual elder-brother sentence remains conservatively translated with an explicit note;
- scene 5's compressed wartime newspaper syntax remains unresolved at source level and is not silently repaired in English.

## Scenes 6–10 — second batch in review

New review units: **66**.

Per-scene counts:

- scene 6 — **22**: 19 dialogue + 3 stage directions;
- scene 7 — **24**: 22 dialogue + 2 stage directions;
- scene 8 — **10**: 5 dialogue + 4 stage directions + 1 song;
- scene 9 — **1**: one long cross-page dialogue;
- scene 10 — **9**: 7 dialogue + 2 stage directions.

Cumulative translation state:

- scenes started: **1–10**
- scenes verified: **1–5**
- scenes in review: **6–10**
- translation units: **136**
- verified: **70**
- review: **66**
- kinds: **109 dialogue / 24 stage direction / 3 song / 0 quoted verse**
- cross-page translation units: `parasakthi-en-s001-u004`, `parasakthi-en-s008-u002`, `parasakthi-en-s009-u001`

### Review-sensitive decisions in the new batch

- Scene 6: `முழுகாதிருக்கிற பெண்ணு` is rendered `a woman in her condition` as a contextual pregnancy euphemism; do not modernize the Tamil source.
- Scene 7: preserve the source's explicit references to begging/prostitution and Gunasekaran's irony about Tamil Nadu's `first voice`.
- Scene 8: `parasakthi-song-003` is one semantic-poetic unit across PDF 11→12. The compressed sequence around `பெண்களின் வாழ்க்கையை இழந்தவர்கள் கோடி` is deliberately flagged for review.
- Scene 9: `parasakthi-s009-d001` remains one English unit across PDF 12→13 with `english_page_segments`. The source `வங்கத்திலே` is semantically anomalous in context; current English uses context-neutral `in this land` and documents the choice. `தகுதி? போக்கியதை?` is also review-sensitive.
- Scene 10: source `பெட்டிலே` is rendered contextually as hospital `bed` only in English, with a note.

## Exact next work

Perform the second-pass fidelity/editorial review of all **66 units in scenes 6–10**:

1. verify ordering and source links against `scenes/scene-06.md` through `scene-10.md`;
2. verify all dialogue IDs, exact labels and page provenance against `dialogues/records/scene-06.json` through `scene-10.json`;
3. review scene 6's euphemistic/colloquial lines without flattening tone;
4. review scene 7's social vocabulary and Jolly dialogue without moral/editorial rewriting;
5. review scene 8's song carefully against `songs/tracks/06-o-rasikkum-seemane.md`, especially its compressed third stanza;
6. review scene 9's full rhetorical monologue, source anomalies and PDF 12→13 page split;
7. review scene 10's hospital vocabulary and grief dialogue;
8. alter English only when the review identifies a translation problem;
9. if accepted, mark scenes 6–10 and all 66 units `verified`;
10. then begin the next translation batch with canonical **scenes 11–15**.

## Overall status

- Structural mapping: verified
- Canonical Tamil: verified
- Tamil fidelity audit: complete
- Scene/dialogue/character/song Tamil derivatives: complete as documented above
- English translation: **in-progress-review — scenes 1–10 / 136 units / scenes 1–5 verified**
