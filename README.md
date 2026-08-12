# Kalaignar Cinema Works

A source-led archive of screenplay, dialogue, song, and related cinema writing credited to **Kalaignar M. Karunanidhi**.

The repository is organized by **work/film**, with each work preserving its source provenance, page mapping, transcription status, and any derivative representations separately.

## Archival principles

1. **Primary source first.** The scanned publication controls the canonical transcription.
2. **No silent correction.** Spelling, punctuation, scene numbering, apparent printing errors, and unusual ordering are preserved unless a correction is explicitly documented.
3. **Page provenance is mandatory.** Every transcribed unit must remain traceable to the PDF page and, where present, the printed page number.
4. **Uncertainty stays visible.** Illegible or doubtful text is marked for review rather than guessed from film subtitles, later editions, web copies, or memory.
5. **Source text and derivatives are separate.** Scene files, indexes, translations, normalized text, and research notes must not overwrite the canonical source transcription.
6. **Authorship is not inferred.** A booklet may contain material by multiple writers or lyricists; per-item attribution must be supported by the source or by separately documented verification.
7. **Rights are not assumed.** No repository-wide public-domain or open-license claim is made unless established work by work.

## Repository layout

```text
.
├── README.md
├── docs/
│   ├── ARCHIVAL_WORKFLOW.md
│   ├── SOURCE_POLICY.md
│   └── TRANSCRIPTION_GUIDE.md
├── data/
│   └── works.json
└── works/
    └── parasakthi/
        ├── README.md
        ├── metadata.yaml
        ├── mapping.md
        ├── source/
        │   └── README.md
        ├── notes/
        │   └── textual-notes.md
        ├── transcription/
        │   ├── full-text.md
        │   └── scenes/
        │       └── README.md
        └── songs/
            └── README.md
```

## First work: பராசக்தி

The first source is the scanned booklet **`பராசக்தி — முழு வசனம் + பாடல்கள்`**. Its title page credits **`திரைக்கதை, வசனம் — கலைஞர் மு. கருணாநிதி`**. The scan contains 58 PDF pages and is image-only.

The structural map is complete in [`works/parasakthi/mapping.md`](works/parasakthi/mapping.md). It records all 58 PDF pages, the printed-page correspondence, all visible scene headings, source numbering anomalies, and first-pass verse/lyric-formatted locations.

Canonical Tamil transcription is in progress. The current draft covers **PDF pages 4–11 / printed pages 3–10**, with page anchors. The latest batch added **PDF 8–11 / printed pages 7–10**, carrying the text through the opening of `காட்சி—8`. The separate fidelity audit has not yet begun; the next transcription page is **PDF 12 / printed page 11**.

## Status vocabulary

- `not-started` — no transcription attempted
- `draft` — transcription exists but has not completed visual comparison
- `review` — compared to the scan but unresolved readings remain
- `verified` — visually checked against the source page and no unresolved reading remains

A derivative translation can begin only after the corresponding Tamil source text is `verified`.
