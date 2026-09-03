# Source policy

## Primary-source rule

The scanned publication is the controlling source for canonical text. External sources may be used only for clearly labelled research, bibliographic verification, or authorship verification; they must not silently overwrite the scan.

## What must be preserved

Preserve, where visible and relevant:

- exact title and credits;
- printed pagination;
- scene/section numbering, including gaps or out-of-order numbering;
- speaker labels;
- stage directions and parentheticals;
- songs/verse blocks in their source position;
- apparent typographical or printing irregularities unless separately annotated.

## What must not be inferred

Do not infer:

- publication year from PDF creation metadata;
- edition from an undated scan;
- missing scene numbers;
- song authorship from proximity alone;
- film dialogue from subtitles, audio, web quotations, or later editions;
- public-domain status or an open license.

## Unclear text

When a character or word cannot be read with confidence, keep the uncertainty visible in the transcription/review apparatus. Do not replace the reading with what 'must have been said' in the film.

For older Tamil typefaces, a visually unfamiliar spelling is not evidence of an error. OCR, embedded PDF text and modern spelling expectations must not be allowed to resolve a disputed glyph. Enlarge the rendered scan and compare the printed characters themselves. Preserve occurrence-specific variation when the source genuinely prints different forms.

If the user performs a direct manual review of the controlling scan and explicitly supplies the printed form for a disputed word, that reviewed source reading is authoritative for the workflow unless later direct scan evidence reopens it. Record consequential overrides rather than silently reverting to an OCR or assistant-generated reading.

## External verification

When outside research is eventually used, record:

- the question being verified;
- the external source;
- access date where appropriate;
- whether it confirms, conflicts with, or supplements the scanned source.

Conflicting evidence must remain documented rather than harmonized without explanation.

## Source binaries

The repository may track source PDFs separately from text files. A textual source manifest must always record the original filename and cryptographic checksum even when the binary itself is stored elsewhere or managed through Git LFS.
