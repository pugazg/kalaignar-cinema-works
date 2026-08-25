# Raja Rani — Next Phase Readiness Checkpoint

## Current phase

Source intake, structural mapping, canonical Tamil first pass, full rendered-scan fidelity audit, source-supported scene segmentation and the complete eligible verified scene-text derivative layer are complete for the supplied scan.

The Tamil fidelity gate remains **closed-with-source-limitations**. Four screenplay pages remain `review`: PDF **27, 48, 57 and 74**.

The repository-level Raja Rani bookkeeping gap is reconciled, and immutable dialogue indexing is **in progress from verified scene derivatives only**.

Controlling files:

- `notes/tamil-fidelity-gate-disposition.md`
- `notes/post-fidelity-corrections.md`
- `notes/scene-segmentation-audit.md`
- `notes/scene-text-batch-010.md`
- `notes/scene-layer-completion-dialogue-initialization.md`
- `notes/dialogue-batch-001.md`
- `notes/dialogue-batch-002.md`
- `notes/dialogue-batch-003.md`
- `notes/dialogue-batch-004.md`
- `scenes/index.json`
- `scenes/README.md`
- `dialogues/README.md`
- `dialogues/schema.json`
- `dialogues/index.json`

## Completed

- Source identity, checksum, pagination and content boundaries verified.
- Canonical source-order page layer complete: `pages/001.md`–`079.md`.
- Screenplay range complete: PDF **10–79 / printed pp.9–78 — 70/70 pages**.
- Full rendered-scan visual audit complete through PDF 79.
- Verified source pages: **75/79**.
- Review source pages: **4/79 — PDF 27, 48, 57, 74**.
- Verified screenplay pages: **66/70**.
- Review screenplay pages: **4/70**.
- Source-supported archival scene segmentation complete: **58 segments**.
- Verified scene-text eligibility: **50 segments**.
- Source-review-blocked scene segments: **8**.
- Scene-text Batch 001 through Batch 010 complete.
- Verified scene-text files completed: **50/50 eligible**.
- Remaining eligible scene-text files: **0**.
- `data/works.json` includes Raja Rani.
- Repository root README includes Raja Rani status.
- Dialogue layer initialized with schema, README and inventory index.
- Dialogue Batch 001 completed for verified `scene-001.md` through `scene-010.md`.
- Dialogue Batch 002 completed for verified `scene-014.md` through `scene-023.md`, after the blocked `s011`–`s013` group.
- Dialogue Batch 003 completed for verified `scene-024.md` through `scene-032.md`, stopping before blocked `s033`.
- Dialogue Batch 004 completed for verified `scene-034.md` through `scene-038.md`, after blocked `s033` and stopping before blocked `s039`.

## Scene-text completion position

The eight blocked archival segments remain intentionally without verified scene-text files:

`raja-rani-s011`, `raja-rani-s012`, `raja-rani-s013`, `raja-rani-s033`, `raja-rani-s039`, `raja-rani-s053`, `raja-rani-s054`, `raja-rani-s055`.

Their blocking pages are respectively PDF 27, PDF 48, PDF 57 and PDF 74. No uncertain or physically obscured wording has been reconstructed merely to create a complete 58/58 derivative set.

The eligible scene-text layer is therefore **complete-with-review-source-exclusions: 50/50 eligible complete**.

## Canonical-status / source recheck history

- Before Scene-Text Batches 002–004, stale local page-status bookkeeping was reconciled with already completed visual-audit findings.
- Scene-Text Batch 005 restored source-visible `ராசா:` labels on PDF 49–50.
- Scene-Text Batch 006 restored the corresponding PDF 53 labels and T036 stage-direction form.
- Scene-Text Batch 007 restored the exact PDF 58–59 `ராஜா:` / `ராசா:` alternation.
- Scene-Text Batch 008 restored PDF 66's opening continuation label to source-visible `ராசா:`.
- Scene-Text Batches 009–010 required no further correction in their verified spans.
- Dialogue Batches 001–004 required no new canonical Tamil correction.

No review page was promoted and the global fidelity totals remain unchanged.

## Bounded source limitations

- PDF 27: one faint/washed internal-monologue word remains unresolved.
- PDF 48: two short spans before `சமரசம் வீடு` remain unresolved.
- PDF 57: one compact colloquial phrase remains unresolved after repeated high-resolution review.
- PDF 74: later `K. N. சங்கரன்` ownership/address overprint physically obscures original printing; hidden text is not reconstructed.

These four pages remain `review` even though the audit phase itself is closed.

## Dialogue gate

Dialogue indexing is **in progress — verified-source-only**.

Current dialogue state:

- eligible verified scenes: **50**
- blocked scenes: **8**
- processed scenes: **34/50**
- immutable labelled-dialogue records: **697**
- zero-record scenes: **12 — `s008`, `s010`, `s014`, `s019`, `s020`, `s022`, `s027`, `s029`, `s030`, `s032`, `s037`, `s038`**
- cross-page dialogue records: **5**
- tracked non-colon source-label/delimiter anomalies: **3**

Batch 004 added **140 records** across `s034`–`s038`; `s037` and `s038` correctly yielded zero records. It added the cross-page record `raja-rani-s035-d012` across PDF 52→53 and introduced no new delimiter anomaly.

The verified `s034` unlabelled lines `மெள்ள, மெள்ள...` and `ஆ...பூச்சி, பூச்சி...` remain outside the immutable dialogue layer because they have no printed speaker label/delimiter. No speaker was inferred.

Rules:

- only explicitly speaker-labelled utterances from verified scene derivatives become records;
- source-unlabelled speech is not assigned an inferred speaker;
- exact source-visible speaker labels and delimiters are preserved;
- a labelled utterance crossing a page boundary remains one immutable record with multi-page provenance;
- blocked scenes remain outside dialogue production until their source span is fully verified.

## Readiness

- source intake: **COMPLETE**
- structural mapping: **COMPLETE**
- canonical Tamil first pass: **COMPLETE AS DRAFT**
- rendered-scan fidelity audit: **COMPLETE-WITH-SOURCE-LIMITATIONS**
- scene segmentation/index: **COMPLETE — 58 segments**
- verified scene-text derivatives: **COMPLETE — 50/50 eligible; 8 blocked**
- repository bookkeeping: **RECONCILED**
- dialogue extraction: **IN PROGRESS — 34/50 eligible scenes processed; 697 records**
- character/entity index: **not yet started**
- song/performance authorship gate: **not yet started**
- English translation: **not yet started; verified Tamil units only**

## Next activity

**Dialogue Batch 005:** skip blocked `s039`, process verified `scene-040.md` through `scene-052.md` in source order, then stop before blocked `s053`–`s055`.

Do not create shards for blocked `s039`, `s053`, `s054` or `s055`. Preserve exact source labels/delimiters and page provenance, keep cross-page utterances as single records, and continue to leave source-unlabelled material outside the immutable dialogue index.
