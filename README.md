# Kalaignar Cinema Works

A source-led archive of screenplay, dialogue, song, and related cinema writing credited to **Kalaignar M. Karunanidhi**.

The repository is organized by **work/film**, with each work preserving source provenance, page mapping, canonical transcription and derivative representations separately.

## Archival principles

1. **Primary source first.** The scanned publication controls the canonical transcription.
2. **No silent correction.** Apparent source errors are corrected only with the printed reading retained as provenance.
3. **Page provenance is mandatory.** Every transcribed or indexed unit remains traceable to its PDF/printed page.
4. **Uncertainty stays visible.** Doubtful source text is reviewed rather than guessed from outside copies or memory.
5. **Source text and derivatives are separate.** Scene files, indexes and translations never overwrite the canonical layer.
6. **Authorship is not inferred.** Mixed-credit material requires item-level attribution evidence.
7. **Rights are not assumed.** No repository-wide public-domain or open-license claim is made.

## Repository layout

```text
.
├── README.md
├── docs/
├── data/
│   └── works.json
└── works/
    └── parasakthi/
        ├── README.md
        ├── metadata.yaml
        ├── mapping.md
        ├── transcription/
        ├── scenes/
        │   ├── index.json
        │   └── scene-*.md
        ├── dialogues/
        │   ├── README.md
        │   ├── schema.json
        │   ├── index.json
        │   └── records/
        │       └── scene-*.json
        └── songs/
```

## First work: பராசக்தி

The first source is the scanned booklet **`பராசக்தி — முழு வசனம் + பாடல்கள்`**, whose title page credits `திரைக்கதை, வசனம் — கலைஞர் மு. கருணாநிதி`.

The canonical Tamil covers PDF **4–57 / printed pp.3–56** and is fully verified at **54/54 pages**, with no remaining uncertainty markers. PDF 58 is rear advertisement/back matter.

The source contains **46 observed scene headings**; scenes 23 and 34 are absent. The documented late transposition is preserved as source provenance while the canonical sequence uses scene 43 on PDF 49 and final scene 48 on PDF 57.

The scene derivative layer is **46/46 complete**.

The **dialogue index is now complete and verified for all 46 observed scenes**, totaling **642 speaker-labelled records** stored under `works/parasakthi/dialogues/records/`. The final scenes 41–48 batch adds 115 records. Scene 48 is a valid zero-record scene because its closing content is unlabelled song/back-of-work material.

The completed dialogue index contains **11 cross-page utterances**. Canonical scene 43 preserves `source_scene_heading: 48`, and canonical final scene 48 preserves `source_scene_heading: 43`.

The next structured derivative is the **character index**: map exact source speaker labels to stable character entities without rewriting the dialogue records. Ambiguous abbreviations and role labels must remain explicit and reviewable.

English translation may begin later as a separate derivative. Per-song authorship remains a separate gate because the booklet credits multiple lyric contributors.

## Status vocabulary

- `not-started`
- `draft`
- `draft-complete`
- `review`
- `verified`
- `complete-verified`

A derivative translation can begin only after the corresponding Tamil source text is verified.
