"""Genera data/feedback.json dal dump della collection lead_status della dashboard.
Uso: python tools/sync_feedback.py <cartella_dump_lead_status>
I motivi noti (non scritti dall'utente in dashboard) stanno in data/feedback_notes.json (id -> motivo)."""
import json, sys, os, glob
dump = sys.argv[1]
leads = {l['id']: l for l in json.load(open('data/leads.json', encoding='utf-8'))}
notes_p = 'data/feedback_notes.json'
notes = json.load(open(notes_p, encoding='utf-8')) if os.path.exists(notes_p) else {}
out = []
for f in sorted(glob.glob(os.path.join(dump, '*.json'))):
    doc = json.load(open(f, encoding='utf-8'))
    d = doc.get('data', doc); id_ = doc.get('id') or os.path.basename(f)[:-5]
    l = leads.get(id_, {})
    status = d.get('status')
    if status in (None, 'bozza'):
        continue
    reason = d.get('discardReason') or notes.get(id_) or d.get('responseNote') or ''
    out.append({'id': id_, 'name': l.get('name', id_), 'sector': l.get('sector', ''), 'comune': l.get('comune', ''),
                'channel': l.get('channel', ''), 'confidence': l.get('confidence', ''), 'status': status,
                'reason': reason, 'when': d.get('updatedAt', '')})
json.dump(out, open('data/feedback.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
from collections import Counter
print(Counter(o['status'] for o in out))
