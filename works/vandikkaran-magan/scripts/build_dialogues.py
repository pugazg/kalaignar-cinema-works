#!/usr/bin/env python3
# Stable-ID-aware dialogue builder/reconciler.
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).with_name('reconcile_dialogue_structural_collisions.py')), run_name='__main__')
