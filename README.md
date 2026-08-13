# Kalaignar Cinema Works

A source-led archive of screenplay, dialogue, song, and related cinema writing credited to **Kalaignar M. Karunanidhi**.

The repository is organized by **work/film**, with each work preserving its source provenance, page mapping, transcription status, and derivative representations separately.

## Archival principles

1. **Primary source first.** The scanned publication controls the canonical transcription.
2. **No silent correction.** Spelling, punctuation, scene numbering, apparent printing errors, and unusual ordering are preserved unless a correction is explicitly documented with the printed source reading retained as provenance.
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

The corrected structural map is complete in [`works/parasakthi/mapping.md`](works/parasakthi/mapping.md). The detailed transcription and fidelity audit confirm **46 visible scene headings**; headings 23 and 34 were not observed.

The booklet misnumbers/transposes two late scene headings: PDF 49 / printed p.48 prints `காட்சி-48` where the canonical sequence is **`காட்சி-43`**, while the final scene on PDF 57 / printed p.56 prints `காட்சி-43` where the canonical sequence is **`காட்சி-48`**. The canonical transcription corrects the visible headings while retaining both printed readings as documented provenance.

The canonical Tamil dialogue/song transcription covers **PDF 4–57 / printed pp. 3–56**, with PDF 58 recorded as rear advertisement/back matter. The complete canonical range has passed page-by-page visual fidelity audit, consolidated correction, and the Part 02 post-rewrite verification pass.

Current page status is **54 verified / 0 review**. The final two Part 01 readings were resolved directly from the scan with reviewer assistance: PDF 5 reads `கல்யாணிக்குக் கல்யாணம் உங்களுக்குத் தெரியுமா?`, and PDF 16 reads `குதிரைக்கு பதிலாக நரம்பு தெறிக்கத்தெறிக்க ரிக்ஷா இழுத்துக்...`. No canonical uncertainty marker remains.

The Tamil source is now fully verified. English translation may begin as a separate derivative activity; per-song authorship mapping remains a separate prerequisite for song-specific attribution work.

## Status vocabulary

- `not-started` — no transcription attempted
- `draft` — transcription exists but has not passed visual fidelity review
- `draft-complete` — complete first-pass source coverage exists but the work as a whole has not completed visual fidelity review
- `review` — compared to the scan but unresolved readings remain
- `verified` — visually checked against the source page and no unresolved reading remains

A derivative translation can begin only after the corresponding Tamil source text is `verified`.
