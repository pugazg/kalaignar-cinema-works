#!/usr/bin/env python3
"""Regression test: Reading Room status synchronization must be idempotent.

`sync_status.py` writes into documents that also hold hand-written prose. It has
to satisfy ``F(F(x)) == F(x)``: the first run may bring stale status text up to
date, and every run after that must produce no further change.

Two defects previously broke that.

1. ``replace_section`` anchored on a heading that the generated block itself
   re-emits at its end, so each run found the copy inside the previous block and
   inserted the block again ahead of it.
2. ``replace_idempotent`` tested ``old`` before ``new``. Several updates are
   append-style, where ``new`` starts with the whole of ``old``, so ``old`` still
   matched after the update and the addition was appended again on every run.

The test runs synchronization twice against a disposable copy of the repository
and asserts the second run is a no-op, that the generated sections are not
duplicated, and that the hand-written reconciliation note and its handover
pointer are untouched.

Run:  python3 works/kalaignar-thirai-isai-paadalgal/integrations/reading-room/test_sync_idempotency.py
"""

from __future__ import annotations

import hashlib
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
WORK_REL = "works/kalaignar-thirai-isai-paadalgal"
SYNC_REL = f"{WORK_REL}/integrations/reading-room/sync_status.py"
NOTE_REL = f"{WORK_REL}/notes/READING_ROOM_TITLE_RECONCILIATION.md"
HANDOVER_REL = f"{WORK_REL}/PROJECT_HANDOVER.md"

# Every document sync_status.py may write.
CONTROLLED = [
    "README.md",
    "docs/STATUS_CONSISTENCY_AUDIT.md",
    "data/works.json",
    f"{WORK_REL}/metadata.yaml",
    f"{WORK_REL}/README.md",
    f"{WORK_REL}/PROJECT_HANDOVER.md",
    f"{WORK_REL}/AUDIT.md",
    f"{WORK_REL}/PROGRESS.md",
]

# Generated headings that must never appear more than once.
SINGLE_OCCURRENCE = [
    (f"{WORK_REL}/AUDIT.md", "## Reading Room integration payload gate"),
    (f"{WORK_REL}/AUDIT.md", "## Next activity"),
    (f"{WORK_REL}/PROGRESS.md", "## Reading Room integration payload"),
    (f"{WORK_REL}/README.md", "## Reading Room integration payload"),
    (f"{WORK_REL}/PROJECT_HANDOVER.md", "## Reading Room integration payload checkpoint"),
    ("README.md", "- Reading Room integration payload: **complete-verified"),
    ("docs/STATUS_CONSISTENCY_AUDIT.md", "| Reading Room payload |"),
]

failures: list[str] = []


def check(condition: bool, message: str) -> None:
    if condition:
        print(f"  ok   {message}")
    else:
        failures.append(message)
        print(f"  FAIL {message}")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def snapshot(base: Path) -> dict[str, str]:
    return {rel: digest(base / rel) for rel in CONTROLLED}


def sync(base: Path) -> None:
    result = subprocess.run(
        [sys.executable, str(base / SYNC_REL)], capture_output=True, text=True
    )
    if result.returncode != 0:
        raise SystemExit(f"sync_status.py failed: {result.stdout}{result.stderr}")


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp) / "repo"
        shutil.copytree(ROOT, base, ignore=shutil.ignore_patterns(".git"))

        note_before = digest(base / NOTE_REL)
        pointer_before = (base / HANDOVER_REL).read_text(encoding="utf-8").count(
            "READING_ROOM_TITLE_RECONCILIATION.md"
        )

        sync(base)
        first = snapshot(base)

        sync(base)
        second = snapshot(base)

        print("idempotency")
        drifted = [rel for rel in CONTROLLED if first[rel] != second[rel]]
        check(not drifted, f"second run produces no change (drifted: {drifted or 'none'})")

        sync(base)
        third = snapshot(base)
        drifted3 = [rel for rel in CONTROLLED if second[rel] != third[rel]]
        check(not drifted3, f"third run produces no change (drifted: {drifted3 or 'none'})")

        print("no duplicated generated content")
        for rel, marker in SINGLE_OCCURRENCE:
            count = (base / rel).read_text(encoding="utf-8").count(marker)
            check(count == 1, f"{rel}: {marker!r} appears once (found {count})")

        print("hand-written record is untouched")
        check(
            digest(base / NOTE_REL) == note_before,
            "reconciliation note is byte-identical after synchronization",
        )
        handover = (base / HANDOVER_REL).read_text(encoding="utf-8")
        check(
            handover.count("READING_ROOM_TITLE_RECONCILIATION.md") == pointer_before == 1,
            "handover pointer to the note survives exactly once",
        )
        check(
            handover.find("## Durable reconciliation record")
            < handover.find("<!-- BEGIN GENERATED: reading-room-status -->"),
            "handover pointer sits outside the generated block",
        )

    print()
    if failures:
        print(f"FAIL — {len(failures)} check(s) failed")
        return 1
    print("PASS — status synchronization is idempotent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
