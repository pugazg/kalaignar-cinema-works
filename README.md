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
        ├── songs/
        │   ├── tracks/
        │   └── quoted-verses/
        └── translations/
            ├── README.md
            ├── schema.json
            ├── index.json
            └── records/
                └── scene-01.json
```

## First work: பராசக்தி

The canonical Tamil covers PDF **4–57 / printed pp.3–56** and is fully verified at **54/54 pages**, with no remaining uncertainty markers. PDF 58 is rear advertisement/back matter.

The source contains **46 observed scene headings**; scenes 23 and 34 are absent. The documented late transposition is preserved as source provenance while the canonical sequence uses scene 43 on PDF 49 and final scene 48 on PDF 57.

Structured derivatives now stand at:

- scene layer: **46/46 complete**;
- dialogue index: **complete-verified — 642 records**;
- character index: **complete-verified — 69/69 exact labels disposed across 48 entities**;
- song/verse inventory: **14 canonical occurrence records**;
- song authorship mapping: **complete-verified — 14/14 resolved**;
- Tamil soundtrack derivatives: **complete-verified — 11/11 composition files**;
- separate quoted-verse derivatives: **1**;
- English translation: **pilot-review — canonical scene 1 / 4 source-linked units**.

The translation layer is intentionally independent. The scene-1 pilot covers two stage directions, the verified `வாழ்க வாழ்கவே` song, and the cross-page Thangappan dialogue. Exact Tamil identifiers and PDF/printed-page provenance are retained as metadata; all four English units remain at `review` until the pilot is editorially accepted.

The next structured activity is to review that pilot. If accepted, it becomes `verified` and the first full English batch proceeds with canonical **scenes 2–5** using the same schema.

## Status vocabulary

- `not-started`
- `draft`
- `draft-complete`
- `review`
- `verified`
- `pilot-review`
- `pilot-verified`
- `complete-verified`
- `unresolved`

A derivative translation can begin only after the corresponding Tamil source text is verified.
