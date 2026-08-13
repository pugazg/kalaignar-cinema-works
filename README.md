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
        ├── dialogues/
        ├── characters/
        └── songs/
            ├── README.md
            ├── schema.json
            ├── credits.json
            ├── inventory.json
            └── index.json
```

## First work: பராசக்தி

The first source is the scanned booklet **`பராசக்தி — முழு வசனம் + பாடல்கள்`**, whose title page credits `திரைக்கதை, வசனம் — கலைஞர் மு. கருணாநிதி`.

The canonical Tamil covers PDF **4–57 / printed pp.3–56** and is fully verified at **54/54 pages**, with no remaining uncertainty markers. PDF 58 is rear advertisement/back matter.

The source contains **46 observed scene headings**; scenes 23 and 34 are absent. The documented late transposition is preserved as source provenance while the canonical sequence uses scene 43 on PDF 49 and final scene 48 on PDF 57.

The scene derivative layer is **46/46 complete**. The dialogue index is **complete-verified with 642 records**, and the character index is **complete-verified with explicit disposition for all 69 exact speaker labels**.

The **song/verse authorship gate is now active**. PDF 3 lists six booklet-wide song contributors—பாரதியார், பாரதிதாசன், உடுமலை நாராயணகவி, மு. கருணாநிதி, கே. பி. காமாட்சி சுந்தரம், and கு. ம. அண்ணல்தங்கோ—but does not pair them with individual songs.

A source-led inventory now contains **14 candidate song/verse occurrences**. **1 attribution is internally verified** (the scene-28 Bharathidasan quotation) and **13 remain unresolved** pending item-level evidence. Booklet-wide credit alone is never treated as an item-level assignment.

The next structured activity is to resolve those 13 remaining authorship records using primary/official or otherwise reliable attribution evidence. Outside sources may establish attribution metadata but must never be used to alter the canonical Tamil transcription.

English translation may begin later as a separate derivative, with song-specific translation remaining gated by item-level authorship disposition.

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
