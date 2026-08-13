# பராசக்தி — dialogue index

**Stage:** structured derivatives  
**Canonical authority:** fully verified Tamil transcription  
**Dialogue index status:** in progress — verified for **38 observed scenes through the 31–40 range**

This directory is a machine-readable dialogue derivative built from the verified canonical Tamil / completed scene derivatives. It does **not** replace, normalize, or repair the canonical transcription.

## Files and storage

- `schema.json` — fixed deterministic dialogue-record schema.
- `index.json` — compact manifest and extraction checkpoint.
- `records/scene-XX.json` — all dialogue records belonging to one observed canonical scene.

The original scenes 1–2 pilot was migrated losslessly into scene-sharded files before bulk extraction. That was a storage-only change; the record schema remains fixed.

## Record rules

Each record represents exactly one explicitly speaker-labelled utterance and preserves the stable ID, canonical/source scene number, exact speaker label, exact Tamil text, PDF/printed-page provenance and source scene file. A `page_segments` array is added only when one utterance crosses a canonical page boundary.

Do **not** expand, merge or standardize labels. Character normalization belongs in the later character-index layer.

Included material must be explicitly marked by a speaker prefix. Standalone directions, narrative prose, unlabelled songs/verse, unlabelled monologue/prose, editorial comments, printer marks and back matter remain excluded. Parenthetical text inside a labelled utterance remains part of that record. Explicitly speaker-labelled sung/verse material remains eligible.

### Explicit-label punctuation anomalies

A speaker may still be explicit even when the booklet omits the usual colon. Do not alter the canonical Tamil to normalize punctuation.

Verified anomaly records remain:

- `parasakthi-s021-d040` — source form `கல் ! கிறுக்கண்ணு! கிறுக்கண்ணு!`.
- `parasakthi-s025-d011` — `சி. ஜி. டி.` line without colon.
- `parasakthi-s025-d017` — second `சி. ஜி. டி.` line without colon.

### Page boundaries

A single utterance crossing a page anchor remains one record with all pages in `page_provenance` and exact `page_segments`.

Verified cross-page records through this checkpoint:

- `parasakthi-s001-d001` — PDF 4→5.
- `parasakthi-s009-d001` — PDF 12→13.
- `parasakthi-s013-d023` — PDF 16→17.
- `parasakthi-s028-d023` — PDF 33→34.
- `parasakthi-s033-d053` — PDF 41→42.

### Scene-number provenance

Headings 23 and 34 are not observed and must not be invented. For the documented late booklet transposition:

- canonical scene 43 must retain `source_scene_heading: 48`;
- canonical scene 48 must retain `source_scene_heading: 43`.

## Verified extraction checkpoint

Dialogue indexing is now verified for **38 observed scenes**:

`1–22, 24–33, 35–40`

- Previous cumulative total through the 21–30 batch: **413**.
- Observed scenes 31–40 batch: **114**.
- Cumulative dialogue records: **527**.

This batch's per-scene counts:

- scene 31 — **13**
- scene 32 — **4**
- scene 33 — **56**
- scene 35 — **10**
- scene 36 — **4**
- scene 37 — **8**
- scene 38 — **8**
- scene 39 — **9**
- scene 40 — **2**

Scene 34 remains absent. Scene 33 is intentionally long: it continues across PDF 38–42 because no scene-34 heading occurs. Its record `parasakthi-s033-d053` crosses PDF 41→42. The unlabelled dream song inside scene 33 remains excluded. Scene 39's opening unlabelled song is also excluded; its explicitly labelled dialogue begins on PDF 45.

Scenes 26 and 29 continue to have valid zero-record dialogue files because they contain no explicitly speaker-labelled utterance.

## Next batch

Extract and verify the **final observed scenes 41–48**. Preserve the fixed schema and exact Tamil. The final batch must also preserve the source/canonical scene-heading distinction for canonical scenes **43 and 48**.
