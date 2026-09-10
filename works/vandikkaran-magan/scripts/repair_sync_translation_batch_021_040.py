#!/usr/bin/env python3
from pathlib import Path
p = Path(__file__).with_name('sync_translation_batch_021_040.py')
s = p.read_text(encoding='utf-8')
old = """s, n3 = re.subn(r'Vandikkaran Magan is the active production work\\. Its canonical Tamil/source gates and \\*\\*72/72 scene derivatives remain COMPLETE-VERIFIED\\*\\*;.*?(?=\\n\\n<!-- Naam song gate)',
           f'Vandikkaran Magan is the active production work. Its source/Tamil, 72-scene, reconciled 773-dialogue, 32-entity and 9-occurrence song/performance authorities remain closed. English translation is **40/72 VERIFIED / QA PASS** at **{all_units} units / {all_links} immutable dialogue links**, using **20-scene iterations**. **Next: archive scene ordinals 41–60.**', s, count=1, flags=re.S)
assert n3 == 1
"""
new = """s, n3 = re.subn(r'Vandikkaran Magan is the active production work\\..*?(?=\\n\\n<!-- Naam song gate)',
           f'Vandikkaran Magan is the active production work. Its source/Tamil, 72-scene, reconciled 773-dialogue, 32-entity and 9-occurrence song/performance authorities remain closed. English translation is **40/72 VERIFIED / QA PASS** at **{all_units} units / {all_links} immutable dialogue links**, using **20-scene iterations**. **Next: archive scene ordinals 41–60.**', s, count=1, flags=re.S)
assert n3 == 1
"""
assert old in s, 'expected stale conclusion gate not found'
p.write_text(s.replace(old, new, 1), encoding='utf-8')
print('sync-script-repair-pass')
