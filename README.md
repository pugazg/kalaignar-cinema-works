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
        ├── characters/
        │   ├── README.md
        │   ├── schema.json
        │   ├── labels-inventory.json
        │   ├── entities-pilot.json
        │   ├── entities.json
        │   └── index.json
        └── songs/
```

## First work: பராசக்தி

The first source is the scanned booklet **`பராசக்தி — முழு வசனம் + பாடல்கள்`**, whose title page credits `திரைக்கதை, வசனம் — கலைஞர் மு. கருணாநிதி`.

The canonical Tamil covers PDF **4–57 / printed pp.3–56** and is fully verified at **54/54 pages**, with no remaining uncertainty markers. PDF 58 is rear advertisement/back matter.

The source contains **46 observed scene headings**; scenes 23 and 34 are absent. The documented late transposition is preserved as source provenance while the canonical sequence uses scene 43 on PDF 49 and final scene 48 on PDF 57.

The scene derivative layer is **46/46 complete**.

The **dialogue index is complete-verified for all 46 observed scenes**, totaling **642 speaker-labelled records**. It contains 11 verified cross-page utterances and preserves exact source labels/punctuation without normalization.

The **character index is also complete-verified**. All **69 distinct exact speaker labels** have an explicit disposition across **48 character/role/collective entities**: 66 labels are verified, `ராக` remains at review, and `நொண்டி` / `நொ` remain explicitly unresolved. No dialogue record was rewritten to achieve this mapping.

The next structured derivative is the **per-song authorship gate**. Because the booklet credits multiple lyric contributors, each song or verse block must be identified and its authorship resolved from the printed credits or separately documented reliable evidence before song-specific extraction or translation.

English translation may begin later as a separate derivative. Outside sources must never be used to alter the canonical Tamil transcription.

## Status vocabulary

- `not-started`
- `draft`
- `draft-complete`
- `review`
- `verified`
- `pilot-verified`
- `complete-verified`
- `unresolved`

A derivative translation can begin only after the corresponding Tamil source text is verified.
