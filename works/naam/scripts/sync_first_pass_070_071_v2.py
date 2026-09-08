#!/usr/bin/env python3
"""Compatibility wrapper for the final Naam first-pass synchronization.

The PDF 65–69 status synchronization advanced the live counters to PDF 69 but an
older metadata writer did not append `pdf-065-069.md` to `completed_batch_paths`.
Repair that durable-list omission first, then run the guarded final closure script.
"""
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[3]
metadata = ROOT / "works/naam/metadata.yaml"
text = metadata.read_text(encoding="utf-8")

p65 = '    - "transcription/parts/pdf-065-069.md"\n'
if p65 not in text:
    anchor = '    - "transcription/parts/pdf-060-064.md"\n'
    if anchor not in text:
        raise SystemExit("metadata compatibility repair: pdf-060-064 anchor missing")
    text = text.replace(anchor, anchor + p65, 1)
    metadata.write_text(text, encoding="utf-8")

runpy.run_path(
    str(ROOT / "works/naam/scripts/sync_first_pass_070_071.py"),
    run_name="__main__",
)
