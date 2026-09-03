# Raja Rani — character exact-label inventory checkpoint

## Scope

This checkpoint began as the mandatory exact-speaker-label inventory before entity normalization. It has now been **synchronized to the fully unblocked final dialogue corpus**.

Controlling derivative source:

- `works/raja-rani/dialogues/index.json`
- `works/raja-rani/dialogues/records/scene-###.json`
- `works/raja-rani/characters/labels-inventory.json`

## Final coverage reconciliation

- verified scene shards examined: **58/58**
- blocked scene shards: **0**
- non-zero dialogue scene shards: **42**
- zero-record dialogue scene shards: **16**
- immutable dialogue records examined: **1,071/1,071**
- distinct exact non-empty `speaker_label` strings: **80**
- exact labels inventory status: **complete**
- dialogue records changed by label inventory: **none**

The 16 zero-record scenes are `s008`, `s010`, `s012`, `s014`, `s019`, `s020`, `s022`, `s027`, `s029`, `s030`, `s032`, `s037`, `s038`, `s042`, `s043`, `s048`.

The final source-unblocking work added exact labels from scenes that had been excluded in the original 50-scene checkpoint, including `மனம்`, `நிழல்`, `ஞானக்கண் குரல்`, `ராஜாவின் குரல்`, and `சமரசம் குரல்`. Source-exact `தர்யம்` was added during the preceding correction reconciliation. None is normalized in this inventory.

## Inventory policy

The inventory is intentionally exact and non-normalizing. It preserves source-visible variants as different labels even when downstream evidence maps them to one entity. Examples include:

- `ராஜா`, `ராசா`, `ராஜ`, `ராஜாவின் குரல்`, and distinct Rani label `ரா`;
- `சமரசம்`, `சம`, `சமரசம் குரல்`;
- `சாந்தம்`, `சாந்தம்மா`, `சாந்`;
- `ஞானக்கண்`, `ஞான`, `ஞா`, `ஞானக்கண் குரல்`;
- `கரண்ட்`, `கரண்டு`, `கர`;
- `தாயம்மாள்`, `தாயம்`, source-exact `தர்யம்`, `தா`, `தாய்`;
- `சாக்ரடீஸ்`, `சாக்`;
- `மெலிடஸ்`, `மெலி`.

No merge is asserted by listing variants together.

Generic/collective labels, role labels and embedded-performance identities remain exact source strings. The personified scene-13 `மனம்` and `நிழல்` labels are not rewritten as Rani.

## T055 / T056 boundary reconciliation

Final English QA discovered that the old scene-55 derivative had duplicated the complete scene-56 `(முன்)` flashback. The five duplicate `s055-d026`–`s055-d030` records were removed. Their exact labels already exist legitimately in scene 56, so the distinct-label inventory remains **80** while the corrected immutable dialogue census is **1,071**.

Canonical page transcription was unchanged.

## Integrity checks

1. Every exact label in `labels-inventory.json` occurs in at least one current dialogue shard.
2. Every listed scene ordinal contains that exact source label.
3. The inventory contains **80 unique labels**.
4. Dialogue shard counts reconcile to **1,071 unique immutable records**.
5. No blocked source scenes remain.
6. No dialogue `speaker_label`, delimiter, Tamil text or provenance was modified by this inventory.
7. Deleted duplicate T055 records are not counted as evidence.

## Disposition

**PASS — exact-label inventory complete at 80/80.**

Entity mapping is also complete at **44 verified entities / roles / collectives**. Preserve this layer while the separate numbered-song English translation phase proceeds.
