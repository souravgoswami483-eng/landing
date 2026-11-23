from pathlib import Path
p=Path('dist/index.html');s=p.read_text(encoding='utf-8-sig');s=s.replace('Tomorrow’s<br>Hospitality &<br>Healthcare','Tomorrow’s <br>Hospitality & <br>Healthcare');s=s.replace('[+0-9 ()\\-]{7,20}',r'[+0-9 \(\)\-]{7,20}');p.write_text(s,encoding='utf-8')
