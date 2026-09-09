from pathlib import Path

p = Path('.github/scripts/naam_english_batch_036_045.py')
s = p.read_text(encoding='utf-8')

# The retained `naam-perf-005` body has 39 mappings (2 role cues + 37 lyric lines),
# not 38. Together with `naam-perf-006`'s 15 lyric mappings, the final batch adds 54.
assert 'assert maps==53' in s
s = s.replace('assert maps==53', 'assert maps==54')
s = s.replace("'performance_line_cue_mappings':53", "'performance_line_cue_mappings':54")
s = s.replace('**53**', '**54**')
s = s.replace('137', '138')

exec(compile(s, str(p), 'exec'))
