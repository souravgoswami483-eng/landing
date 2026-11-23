from html.parser import HTMLParser
from pathlib import Path
class Check(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.links=[];self.assets=[]
 def handle_starttag(self,t,a):
  d=dict(a)
  if 'id' in d:self.ids.append(d['id'])
  if t=='a':self.links.append(d.get('href',''))
  if t=='img':self.assets.append(d['src']);assert 'alt' in d
p=Check();p.feed(Path('dist/index.html').read_text(encoding='utf-8-sig'))
assert len(p.ids)==len(set(p.ids))
for a in p.assets:assert (Path('dist')/a).is_file(),a
for h in p.links:
 if h.startswith('#') and len(h)>1:assert h[1:] in p.ids,h
print('PASS: all image files, unique IDs, and internal anchor targets')
