# Archival workflow

This repository treats a scanned primary source as the controlling object. The workflow is designed so that a later researcher can reconstruct exactly how a transcription or derivative file relates to the scan.

## 1. Source intake

For every source:

1. Preserve the original filename.
2. Record the source identifier, if present.
3. Record byte size, PDF page count, and SHA-256.
4. Determine whether the PDF is image-only or has reliable embedded text.
5. Inspect front matter, pagination, content boundaries, and back matter visually.
6. Do not treat scan-creation metadata as publication metadata.

## 2. Structural mapping gate

No canonical transcription begins until a `mapping.md` exists for the work.

The map should record:

- PDF-page ↔ printed-page correspondence;
- title/credit pages;
- scene/chapter/section headings exactly as printed;
- visible numbering gaps, repeats, and out-of-order headings;
- song/verse blocks or other distinct textual structures;
- advertisements or unrelated back matter;
- any missing, duplicated, cropped, or unreadable scan pages.

A numbering anomaly in the source is **not** repaired during mapping.

## 3. Canonical transcription

The canonical transcription is source-order text, not an edited screenplay.

For each page:

1. Read from the rendered page image.
2. Transcribe only what is visible.
3. Preserve scene headings and source order.
4. Preserve material such as stage directions, speaker labels, songs, parentheticals, and printer marks when they are part of the textual work.
5. Add page anchors so the text remains traceable to PDF and printed pagination.
6. Mark doubtful readings explicitly; do not guess.

## 4. Fidelity audit

A page may move to `verified` only after a separate visual comparison against the scan.

Audit checks include:

- omitted or duplicated lines;
- speaker-name errors;
- punctuation and numeral fidelity;
- Tamil character confusions;
- scene-heading fidelity;
- song/verse line breaks where meaningful;
- page-boundary continuity.

## 5. Structured derivatives

Only after the underlying Tamil is verified may it be reorganized into:

- individual scene files;
- dialogue indexes;
- character indexes;
- song indexes;
- normalized/search text;
- English translation.

Derivatives must point back to canonical source pages and must never silently replace source wording.

## 6. Authorship gate for songs and mixed-credit material

Cinema booklets may credit multiple lyricists or writers. A song appearing inside a Kalaignar-credited dialogue booklet is **not automatically a Kalaignar lyric**.

Song-specific files require an explicit authorship field with a source. If the booklet does not disambiguate a particular song, set authorship to `unresolved` until a separately documented source establishes it.

## 7. Translation gate

English translation is blocked until the corresponding Tamil transcription is `verified`.

Translations are interpretive derivatives and must never be used to repair or retroactively normalize the Tamil source layer.

## 8. Publication and Reading Room integration

The preferred public reading surface for completed Kalaignar archive works is the **Kalaignar Digital Library / Reading Room at `https://nenjukkuneethi.org/read`**.

Once a work has verified archival and reader-ready derivatives, downstream work should normally prepare those structured records for Reading Room integration rather than creating additional standalone publication formats by default.

Guidelines:

1. Treat the repository's verified structured data as the content authority for the Reading Room. The website is a presentation layer, not a new source layer.
2. Do not create a print-ready PDF, another EPUB, or a separate publication package merely because the reader layer is complete. Do so only when explicitly requested for a separate purpose.
3. Preserve each work's natural navigation model in the site. Chapter-based works should remain chapter-based; scene-based cinema works should remain scene-based.
4. Prefer structured JSON/source-linked records for web integration rather than scraping generated HTML or using OCR text as the source.
5. Search, filtering, Tamil/English switching, collection cards, summaries, counts, labels and other UI metadata are presentation features. They must not alter canonical Tamil, source provenance, dialogue IDs, speaker labels, scene order, or translation records.
6. Public-facing counts should be derived from the verified repository checkpoint and updated when the underlying verified data changes.
7. Existing standalone derivatives may remain in the repository as reproducible archival artifacts, but they are not automatically the primary public destination.

For **`திரும்பிப்பார்!`**, the intended Reading Room presentation is a scene-based collection using the verified **93 scenes / 104 printed pages**, with Tamil and English available where supported, and search over scene/dialogue/full-text content. Its primary public destination should be `https://nenjukkuneethi.org/read`, not a newly created print-ready PDF.

## 9. Status model

- `not-started`
- `draft`
- `review`
- `verified`

A work may have separate statuses for mapping, transcription, fidelity review, song attribution, translation, reader integration, and publication derivatives.
