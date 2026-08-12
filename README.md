# Kalaignar Cinema Works

A source-led archive of screenplay, dialogue, song, and related cinema writing credited to **Kalaignar M. Karunanidhi**.

The repository is organized by **work/film**, with each work preserving its source provenance, page mapping, transcription status, and derivative representations separately.

## Archival principles

1. **Primary source first.** The scanned publication controls the canonical transcription.
2. **No silent correction.** Spelling, punctuation, scene numbering, apparent printing errors, and unusual ordering are preserved unless a correction is explicitly documented.
3. **Page provenance is mandatory.** Every transcribed unit remains traceable to the PDF page and, where present, the printed page number.
4. **Uncertainty stays visible.** Illegible or doubtful text is marked for review rather than guessed from film subtitles, later editions, web copies, or memory.
5. **Source text and derivatives are separate.** Scene files, indexes, translations, normalized text, and research notes do not overwrite the canonical source transcription.
6. **Authorship is not inferred.** A booklet may contain material by multiple writers or lyricists; per-item attribution must be supported by the source or separately documented verification.
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
        ├── notes/
        │   └── fidelity-audit.md
        ├── transcription/
        │   ├── full-text.md
        │   └── parts/
        │       ├── part-01-pdf-4-35.md
        │       └── part-02-pdf-36-57.md
        └── songs/
```

## First work: பராசக்தி

The first source is the scanned booklet **`பராசக்தி — முழு வசனம் + பாடல்கள்`**. Its title page credits **`திரைக்கதை, வசனம் — கலைஞர் மு. கருணாநிதி`**. The scan contains 58 PDF pages and is image-only.

The corrected structural map is complete in [`works/parasakthi/mapping.md`](works/parasakthi/mapping.md). The detailed transcription pass confirms **46 visible scene headings**: headings 23 and 34 were not observed, `காட்சி-48` appears on PDF 49 / printed p.48, and the source places `காட்சி-43` at the end on PDF 57 / printed p.56.

The **first-pass canonical Tamil transcription is complete** for all printed dialogue/song content: **PDF 4–57 / printed pp. 3–56**. PDF 58 is rear advertisement/back matter and is recorded as paratext rather than film dialogue.

The page-by-page **Tamil fidelity audit is now in progress through PDF 27 / printed p.26**; the next audit page is PDF **28 / printed p.27**. The audit ledger is [`works/parasakthi/notes/fidelity-audit.md`](works/parasakthi/notes/fidelity-audit.md). The audit has found two substantive first-pass omissions so far — the `காட்சி—3` opening block on PDF 7 and a lyric stanza on PDF 12 — and has visually resolved ten existing uncertainty markers pending the consolidated part-01 rewrite. English translation remains blocked until the corresponding Tamil is verified.

## Status vocabulary

- `not-started` — no transcription attempted
- `draft` — transcription exists but first-pass coverage is incomplete
- `draft-complete` — complete first-pass source coverage exists but has not completed visual fidelity review
- `review` — compared to the scan but unresolved readings remain
- `verified` — visually checked against the source page and no unresolved reading remains

A derivative translation can begin only after the corresponding Tamil source text is `verified`.
