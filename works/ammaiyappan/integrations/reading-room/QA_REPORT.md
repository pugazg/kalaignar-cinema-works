# Ammayappan — Reading Room integration payload QA

**Status:** PASS  
**Site application:** not-applied  
**Source scan SHA-256:** `eda6468a57022b418f44851a0013b090469bc6f4be44a682487800658771720d`  
**Reader authority:** `works/ammaiyappan/editions/en/reader-edition.json`

## Verified payload checks

- archival screenplay navigation: **63/63 scenes**, in source order; the booklet prints no scene numbers;
- Tamil scene texts: **63/63**, generated from the verified scene derivatives without provenance comments;
- verified English units: **1,210/1,210 exactly once**;
- dialogue/source-role links: **1,025/1,025 exactly once** = **1,009 explicit colon-labelled records + 16 closed supplements**;
- speaker-label provenance: **1,009 source-explicit-colon + 2 source-explicit-noncolon-delimiter + 14 source-context-attributed**;
- stage/action units: **181**;
- song-reference units: **3**; japa units: **1**;
- cross-page English units: **28/28**, with matching `english_page_segments` preserved;
- retained occurrence identities: **5/5**, represented through **7** intentional source-span links (`1,1,1,2,2`);
- source page provenance remains within PDF **5–109** / printed **3–107** with `printed = PDF - 2`;
- scene 3 `பூங் ; ...` and scene 5 `திரு; ...` retain non-colon source provenance;
- context-attributed supplements remain explicitly contextual and are not promoted into printed labels;
- absent song titles, lyric bodies and authorship are **not reconstructed**;
- payload editorial placeholder tokens: **0**;
- canonical Tamil/dialogue/character/song evidence modified by payload generation: **0**.

## Output

- `reading-room.json` — SHA-256 `f00efb816edf08b43702a3a1a9d71ed9cc54fd1a803b8881bc6e2c6466de1f8c` — **1,551,865 bytes**.

This payload is a deterministic data derivative for the separate Kalaignar Digital Library / Reading Room implementation. The public-site repository has **not** been modified or deployed by this step.
