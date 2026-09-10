#!/usr/bin/env python3
from pathlib import Path
p=Path(__file__).with_name('translation_batch_041_060_data_c.py')
s=p.read_text(encoding='utf-8')
old="""54: [
{'text':'Entrance to the estate temple.','locator_kind':'location-caption'},
{'text':'(Vingan, Kannaayiram, the poet and elders of the town arrive at the temple entrance. A guard stands blocking them.)'},
{'text':'(Vingan pushes the guard.)'},
{'text':'(Vingan lifts and throws aside the guard who blocks him. Vingan, the others, Kannaayiram and the poet pound on the door and ram it hard. The door opens. Everyone enters.)'}
],"""
new="""54: [
{'text':'Entrance to the estate temple.','locator_kind':'location-caption'},
{'text':'(Vingan, Kannaayiram, the poet and elders of the town run up. Sadaiyan follows a little behind them. Vingan reaches the door.)'},
{'text':'(The guard holds a spear-like implement horizontally across his body.)'},
{'text':'(Vingan pushes the guard.)'},
{'text':'(Vingan lifts and throws aside the guard who blocks him. Vingan, the others, Kannaayiram and the poet pound on the door and ram it hard. The door opens. Everyone enters.)'}
],"""
assert old in s
p.write_text(s.replace(old,new,1),encoding='utf-8')
print('scene-54-nd-repair-pass')
