#!/usr/bin/env python3
from pathlib import Path
import json

p = Path(__file__).resolve().parents[3] / 'data' / 'works.json'
works = json.loads(p.read_text(encoding='utf-8'))
item = next(x for x in works if x.get('id') == 'vandikkaran-magan')
sd = item['structured_derivatives']
assert sd['dialogue_index'] == 'complete-verified'
assert sd['dialogue_records'] == 744
assert sd['dialogue_qa'] == 'PASS'
sd['character_entity_index'] = 'ready-next'
sd['character_index'] = 'ready-next'
sd['song_performance_authorship_gate'] = 'blocked'
sd['next_structured_derivative'] = 'character-index'
p.write_text(json.dumps(works, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('PASS: dialogue closed; character/entity ready-next; song gate blocked')
