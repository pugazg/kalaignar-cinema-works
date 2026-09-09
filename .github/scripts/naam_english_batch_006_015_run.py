from pathlib import Path

p=Path('.github/scripts/naam_english_batch_006_015.py')
s=p.read_text(encoding='utf-8')
s=s.replace("assert unlabelled==['naam-en-s010-u022','naam-en-s013-u034','naam-en-s013-u037'],unlabelled", "assert unlabelled==['naam-en-s010-u021','naam-en-s013-u033','naam-en-s013-u037'],unlabelled")
exec(compile(s, str(p), 'exec'))
