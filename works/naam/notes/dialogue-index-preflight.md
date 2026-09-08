# நாம் — dialogue-index preflight

Status: **REVIEW COMPLETE — READY TO BUILD**

Authority: 45/45 complete-verified scene derivatives. No speaker-label normalization or source-unlabelled speaker inference is permitted.

## Coverage

- scene derivatives scanned: **45/45**
- explicit dialogue candidates: **590**
- distinct exact speaker labels: **45**
- delimiter distribution: **{':': 16, ':-': 573, '—': 1}**
- zero-explicit-dialogue scenes: **1**
- non-speaker colon/location/written-text cues rejected: **21**
- reviewed alternate-delimiter dialogue occurrences: **1**
- remaining dash candidates reviewed as non-speaker: **10**

## Exact speaker-label inventory

| Exact label | Turns |
|---|---:|
| `கும` | 102 |
| `குமரன்` | 62 |
| `சஞ்` | 49 |
| `மீனு` | 47 |
| `மல்` | 44 |
| `சஞ்சீவி` | 35 |
| `மலையப்பன்` | 24 |
| `நாரா` | 23 |
| `பிரே` | 22 |
| `பிரேமா` | 22 |
| `மாத்` | 14 |
| `மாத்திரை` | 14 |
| `பீமசேனன்` | 13 |
| `அண்ணுமலை` | 11 |
| `ஞா` | 11 |
| `கந்தசாமி` | 10 |
| `மல்லயப்ப` | 9 |
| `மல்லயப்பர்` | 7 |
| `ஜீவானந்தர்` | 6 |
| `ஞானம்` | 6 |
| `மல்ல` | 6 |
| `ஒருவன்` | 5 |
| `ஜீவா` | 5 |
| `ஜீவானந்த` | 5 |
| `பூசாரி` | 4 |
| `மல்லயப்பன்` | 4 |
| `ஒரு` | 3 |
| `திருடன்` | 3 |
| `பரமசிவம்` | 3 |
| `சப் இன்ஸ்.` | 2 |
| `தங்` | 2 |
| `நாராயணி` | 2 |
| `புரோகிதர்` | 2 |
| `மற்றொரு` | 2 |
| `உன்மீனு` | 1 |
| `தங்கையன்` | 1 |
| `நீதிபதி` | 1 |
| `பெண்` | 1 |
| `பெரியவர்` | 1 |
| `மக்கள்` | 1 |
| `மற்றொருவன்` | 1 |
| `மற்றொருவர்` | 1 |
| `மலைய` | 1 |
| `மலையப்பர்` | 1 |
| `வந்தவர்` | 1 |

## Occurrence-specific delimiter verdict

- `naam-s041`, PDF 66: `ஜீவானந்தர் — குமரன்! குமரன்!` is an explicit speaker-labelled utterance. The em dash is accepted **only for this reviewed occurrence**; no global dash-to-dialogue rule is introduced.

## Non-speaker safeguards

- `(இடம் ...` / `இடம் ...` location cues are structural, not speakers.
- `கடிதத்தில் :- ...` is written-text provenance, not a speaker label.
- `உன்மீனு :- ...` remains an exact source speaker label because it is explicitly printed/transcribed as such; no silent normalization is applied.

## Gate

Preflight review is closed. Immutable dialogue generation may proceed using these exact counts and occurrence-specific verdicts.
