# அம்மையப்பன் — character/entity index

**Stage:** structured derivatives  
**Canonical authority:** 105/105 dual-gate verified Tamil, 63/63 verified scene derivatives, and the complete 1,024-unit dialogue layer  
**Character/entity status:** **COMPLETE VERIFIED RECONCILED — 62/62 exact labels, 1,024/1,024 dialogue units**

This directory maps the immutable dialogue evidence to stable characters, unnamed roles, or collective categories. It never rewrites, normalizes, or relabels dialogue records.

## Completion summary

- downstream dialogue units: **1,024**
- exact source speaker labels: **62**
- stable entities / role categories: **26**
- verified entities: **26**
- unresolved entities: **0**
- verified label coverage: **62/62**
- dialogue-unit coverage: **1,024/1,024**
- record-aware exact labels: **2** — `முத்`, `தன`
- record-aware units: **187**
- unresolved record dispositions: **0**
- dialogue records modified by this layer: **no**

## Record-aware cases

`முத்` cannot be globally normalized: the source uses it for both **முத்தன்** and **முத்தாயி**. The verified split is **80 → முத்தன் / 97 → முத்தாயி** and is preserved in `muth-record-dispositions.json` and the consolidated `record-aware-dispositions.json`.

`தன` also cannot be globally normalized. In scene 36 record `ammaiyappan-s036-d006` it is **தனபதி**; the remaining nine `தன` records belong to the recurring **தனவணிகர்**. This split is stored only in the derivative identity layer.

## Other important reconciliations

- `திரி / திரிசங்கு / திரு / திருசங்கு` → **திரிசங்கு**; the exceptional source semicolon form remains untouched in dialogue evidence.
- `வே / வேதா / வேதாளம்` → **வேதாளம்**.
- `தள / வேல / வேலழ / வேலழகன்` → **வேலழகன்**.
- `அர / அரச / சக்கரவர்த்தி` → the unnamed **வேங்கை நாட்டு மன்னன்**.
- `முத்தா` in scene 63 → **முத்தாயி**.
- `சாமி / சாமியார் / மாய் / மாய்கை* / மாப்பிள்ளை` → the same ascetic character, represented here as **மாய்கைநாதர் / மாப்பிள்ளைதாசு**.
- generic `ஆள்`, `நண்பன்`, and singular `வீரன்` variants are role categories; grouping them does **not** assert that every occurrence is one physical person.
- `வீரர்கள்` and `மக்கள்` remain collectives.

## Files

- `schema.json` — character/entity derivative schema.
- `labels-inventory.json` — all 62 exact labels with global vs record-aware disposition.
- `record-aware-dispositions.json` — all 187 record-level assignments for reused labels.
- `muth-record-dispositions.json` — detailed earlier `முத்` audit/disposition authority.
- `entities.json` — complete 26-entity mapping.
- `index.json` — compact completion checkpoint.

## Next activity

Synchronize the work-level handover/status to this closure, then open the English translation/reconciliation layer. Tamil dialogue evidence remains frozen unless a new source-backed correction is independently established.
