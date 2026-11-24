#!/usr/bin/env python3
"""Junta i18n/*.json en i18n.js (window.L10N). Ejecutar tras tocar cualquier traducción."""
import json, os
D = os.path.dirname(os.path.abspath(__file__))
out = {}
for k in ['es', 'en', 'pt', 'fr', 'it']:
    out[k] = json.load(open(os.path.join(D, 'i18n', k + '.json'), encoding='utf-8'))
ref = out['es']
def keys(d, p=''):
    r = set()
    for k, v in d.items():
        r.add(p + k)
        if isinstance(v, dict): r |= keys(v, p + k + '.')
    return r
for k, v in out.items():
    a, b = keys(ref), keys(v)
    assert a == b, (k, sorted(a - b), sorted(b - a))
    for kind in ref['deck']:
        for lv in ref['deck'][kind]:
            assert len(v['deck'][kind][lv]) == len(ref['deck'][kind][lv]), (k, kind, lv)
    for lv in ref['duels']:
        assert len(v['duels'][lv]) == len(ref['duels'][lv]), (k, 'duels', lv)
open(os.path.join(D, 'i18n.js'), 'w', encoding='utf-8').write(
    '// Generado por build-i18n.py a partir de i18n/*.json\nwindow.L10N=' + json.dumps(out, ensure_ascii=False, separators=(',', ':')) + ';\n')
print('i18n.js', os.path.getsize(os.path.join(D, 'i18n.js')), 'bytes')
