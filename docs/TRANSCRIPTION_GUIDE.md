# Tamil transcription guide

This guide applies to canonical Tamil source transcription.

## Fidelity over modernization

Transcribe what the page shows. Do not modernize spelling, punctuation, dialogue style, character names, or scene numbering in the canonical layer.

## Old Tamil typefaces and glyph-sensitive review

Older Tamil metal/type and low-resolution scans can make distinct glyphs look deceptively similar. This is a **visual-fidelity problem**, not a spelling-normalization problem.

When a page uses an older typeface or a disputed word has multiple candidate readings:

1. inspect the rendered scan at sufficient enlargement;
2. read the disputed token **glyph by glyph**, in its printed context;
3. treat OCR, PDF parsed text, prior transcription and comparison files only as candidate readings, never as authority;
4. do not prefer a modern, familiar or linguistically expected spelling merely because it looks more plausible;
5. compare easily confused consonants, vowel signs, pulli marks and ligatures explicitly rather than reading the word by semantic expectation;
6. if two different forms occur on the same or adjacent pages, preserve them occurrence by occurrence; never global-normalize them;
7. if enlargement still does not support a secure reading, mark the token `review`/uncertain instead of guessing;
8. when the user has manually inspected the controlling scan and explicitly supplies the source-visible form for a disputed token, record and apply that verdict exactly for that reviewed occurrence rather than allowing OCR or a previous assistant reading to override it.

A page should not be called visually verified merely because OCR and a plausible modern reading agree.

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

If a source-backed correction is made after scene/dialogue/translation or other derivatives already exist, those affected derivatives become **reconciliation-pending** until they have been compared against the corrected canonical text. Do not continue downstream production as though the previous derivative state were still verified.

## English translation

Translation is a separate derivative. It may start only after the corresponding Tamil source unit is `verified`, and it must retain a link/reference back to the canonical Tamil unit.
