# -*- coding: utf-8 -*-
"""facts.json + ko.KO + rich.RICH -> 단일 index.html 생성"""
import json
from ko import KO
from rich import RICH
try:
    from tips import TIPS
except ImportError:
    TIPS = {}

facts = json.load(open('facts.json', encoding='utf-8'))

order = {'N5': 0, 'N4': 1, 'N3': 2}
items, missing = [], []
for ch, f in facts.items():
    ko = KO.get(ch)
    if not ko:
        missing.append(ch)
    e = {'char': ch, 'level': f['level'], 'strokes': f['strokes'],
         'on': f['on'], 'kun': f['kun'], 'ko': ko or '', 'en': f['meanings'],
         'freq': f.get('freq'), 'grade': f.get('grade')}
    r = RICH.get(ch)
    if r:
        e['shape'] = r['shape']
        e['onNote'] = r.get('onNote', '')
        e['onWords'] = r['onWords']
        e['kunNote'] = r.get('kunNote', '')
        e['kunWords'] = r['kunWords']
    tip = TIPS.get(ch)
    if tip:
        e['tip'] = tip
    items.append(e)

# 기초 순서: JLPT 레벨 → 사용빈도(낮을수록 기초) → 획수 적은 순 → 글자
items.sort(key=lambda e: (order[e['level']], e['freq'] or 99999, e['strokes'] or 99, e['char']))

if missing:
    print("한국어 훈음 누락:", ''.join(missing))
print("총", len(items), "자 / 상세보유", len(RICH))

data_js = 'window.KANJI=' + json.dumps(items, ensure_ascii=False, separators=(',', ':')) + ';'
tpl = open('template.html', encoding='utf-8').read()
open('index.html', 'w', encoding='utf-8').write(tpl.replace('/*__DATA__*/', data_js))
print("wrote index.html")
