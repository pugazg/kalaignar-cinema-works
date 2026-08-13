# Kalaignar Cinema Works

A source-led archive of screenplay, dialogue, song, and related cinema writing credited to **Kalaignar M. Karunanidhi**.

The repository is organized by **work/film**, with each work preserving source provenance, page mapping, canonical transcription and derivative representations separately.

## Archival principles

1. **Primary source first.** The scanned publication controls the canonical transcription.
2. **No silent correction.** Apparent source errors are corrected only with the printed reading retained as provenance.
3. **Page provenance is mandatory.** Every transcribed, indexed or translated unit remains traceable to its PDF/printed page.
4. **Uncertainty stays visible.** Doubtful source text or interpretive translation is reviewed rather than guessed away.
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
        └── translations/
            ├── README.md
            ├── schema.json
            ├── index.json
            └── records/
                └── scene-XX.json
```

## First work: பராசக்தி

The canonical Tamil covers PDF **4–57 / printed pp.3–56** and is fully verified at **54/54 pages**, with no remaining uncertainty markers. PDF 58 is rear advertisement/back matter.

The source contains **46 observed scene headings**; scenes 23 and 34 are absent. The documented late transposition is preserved as source provenance while the canonical sequence uses scene 43 on PDF 49 and final scene 48 on PDF 57.

Completed Tamil/source derivatives:

- scene layer: **46/46 complete**;
- dialogue index: **complete-verified — 642 records**;
- character index: **complete-verified — 69/69 exact labels disposed across 48 entities**;
- song/verse inventory: **14 canonical occurrences**;
- song authorship mapping: **complete-verified — 14/14 resolved**;
- Tamil soundtrack derivatives: **complete-verified — 11/11 composition files**;
- separate quoted-verse derivative: **1**.

The English translation layer is now in progress as a strictly separate derivative. Canonical **scene 1 is verified** in English; canonical **scenes 2–5 are in review**. Current translation coverage is **70 source-linked units: 4 verified / 66 review**, comprising 55 dialogue, 13 stage-direction and 2 song units.

The next activity is a second-pass fidelity/editorial review of scenes 2–5. After acceptance, those units can be marked verified and the next translation batch can proceed with scenes 6–10.

Outside sources may establish attribution metadata, but no outside source is allowed to alter canonical Tamil wording. English fluency likewise never authorizes retroactive Tamil correction.

## Status vocabulary

- `not-started`
- `draft`
- `draft-complete`
- `review`
- `verified`
- `pilot-verified`
- `complete-verified`
- `unresolved`

Translation status is independent of source-transcription verification status.
