# Tamil transcription guide

This guide applies to canonical Tamil source transcription.

## Fidelity over modernization

Transcribe what the page shows. Do not modernize spelling, punctuation, dialogue style, character names, or scene numbering in the canonical layer.

## Page anchors

Each canonical page section should begin with a stable source anchor such as:

```md
<!-- source: pdf=4 printed=3 status=draft -->
```

Where the source has no printed page number, use only the PDF page.

## Headings

Scene headings must be reproduced exactly as printed. If the source jumps from one number to another or later returns to an earlier number, preserve that sequence and document it in `mapping.md`.

## Speakers and directions

Preserve speaker names, colons, brackets/parentheses, and stage directions as visible. Do not silently expand abbreviations or regularize names.

## Songs and verse

Preserve verse lineation as closely as the scan supports. A lyric block remains in `full-text.md` at its original source location even if a separate song-index file is later created.

Do not assign a lyricist unless the attribution is supported. Use `unresolved` in a derivative song record when necessary.

## Uncertainty notation

Use uncertainty sparingly and transparently:

- `⟦?⟧` — unreadable character/short span
- `⟦reading?⟧` — probable but unverified reading
- a note in `notes/textual-notes.md` — longer or consequential uncertainty

Never hide uncertainty by choosing a plausible word from memory, subtitles, or another edition.

## Review states

- `draft`: first transcription from the scan
- `review`: visually compared, but one or more uncertainties remain
- `verified`: visually compared and no unresolved reading remains for that page/unit

A later correction to a `verified` page must be documented in commit history and, when substantive, in textual notes.

## English translation

Translation is a separate derivative. It may start only after the corresponding Tamil source unit is `verified`, and it must retain a link/reference back to the canonical Tamil unit.
