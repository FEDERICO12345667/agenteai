#!/usr/bin/env python3
"""Controllo domini anti-falsi-positivi per lo Scout.

Uso:  python3 tools/dnsprobe.py "<nome attivita>[|<nome alternativo>|...]" "<comune>"

Prova centinaia di nomi di dominio plausibili (con e senza parole come "dal", "il", "di";
con e senza il comune; con parole tipo ristorante/pizzeria/bar...) su molte estensioni
(.it .com .eu .net .org .info .biz .shop ... e piattaforme gratuite) usando solo il DNS,
che funziona anche quando HTTP e bloccato.

Stampa i domini che RISOLVONO divisi per livello:
  A = nome completo dell'attivita (molto probabile sito suo)
  B = nome completo + comune
  C = parola tipo + nome distintivo
  D = solo nome distintivo (generico: spesso di altre attivita)
e segnala i domini che puntano agli stessi IP (PARCHEGGIO_PROBABILE).
Un dominio che risolve NON prova che il sito sia dell'attivita: va verificato con
WebSearch limitata a quei domini (parametro allowed_domains), vedi il prompt.
"""
import socket, sys, re, unicodedata, random, string
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

socket.setdefaulttimeout(4)


def norm(s):
    s = unicodedata.normalize('NFKD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.replace("'", '').replace('&', ' e ')
    return re.sub(r'[^a-z0-9 ]', ' ', s)


LEGAL = {'snc', 'srl', 'sas', 'sn', 'c', 'f', 'lli', 'fratelli', 'ditta', 'titolare', 'detto', 'anche', 'noto', 'societa', 'spa', 'di', 'e'}
ARTICLES = {'il', 'la', 'lo', 'le', 'i', 'gli', 'da', 'dal', 'dalla', 'del', 'della', 'dei', 'degli', 'al', 'alla', 'ai', 'delle', 'dello'}
TIPO = {'pizzeria', 'ristorante', 'trattoria', 'osteria', 'hosteria', 'bar', 'caffe', 'pasticceria', 'gelateria', 'parrucchieri', 'parrucchiere', 'parrucchiera', 'hair', 'estetica', 'centro', 'estetico', 'salone', 'panificio', 'macelleria', 'fioreria', 'boutique', 'toelettatura', 'agriturismo', 'bruschetteria', 'enoteca', 'pub', 'barberia', 'bottega', 'forno', 'pizza'}

nomi = [n for n in sys.argv[1].split('|') if n.strip()]
com = norm(sys.argv[2]) if len(sys.argv) > 2 else ''
com = ' '.join(t for t in com.split() if t not in ('vi', 'vicenza'))
comj = ''.join(com.split())
comh = '-'.join(com.split())

tiers = {}  # base -> livello (il migliore)


def add(base, tier):
    base = base.strip('-')
    if 4 <= len(base) <= 40:
        if base not in tiers or tiers[base] > tier:
            tiers[base] = tier


for nome in nomi:
    allt = [t for t in norm(nome).split() if t not in LEGAL]          # con articoli
    noart = [t for t in allt if t not in ARTICLES]                    # senza articoli
    core = [t for t in noart if t not in TIPO]                        # solo parte distintiva
    tipi = [t for t in noart if t in TIPO]
    for toks in (allt, noart):
        if not toks:
            continue
        j, h = ''.join(toks), '-'.join(toks)
        add(j, 1); add(h, 1)
        if comj:
            add(j + comj, 2); add(j + '-' + comj, 2); add(h + '-' + comh, 2); add(comj + j, 2)
    if len(toks := noart) >= 2:
        add(''.join(toks[:2]), 2)
    if core:
        cj, ch = ''.join(core), '-'.join(core)
        tlist = set(tipi) | {'ristorante', 'pizzeria', 'trattoria', 'osteria', 'bar'}
        for t in tlist:
            add(t + cj, 3); add(cj + t, 3); add(t + '-' + ch, 3)
            if comj:
                add(t + cj + comj, 3)
        if len(cj) >= 7 or len(core) >= 2:
            add(cj, 4); add(ch, 4)
            if comj:
                add(cj + comj, 3); add(cj + '-' + comj, 3)

bases = sorted(tiers)
TLD = ['it', 'com', 'eu', 'net', 'org', 'info', 'biz', 'shop', 'store', 'online', 'site', 'website', 'pizza', 'restaurant', 'cafe', 'bar', 'hair', 'beauty', 'srl', 'vi.it', 'veneto.it', 'ws', 'me', 'co', 'cc']
PLAT = ['altervista.org', 'jimdofree.com', 'jimdosite.com', 'webnode.it', 'webnode.page', 'weebly.com', 'godaddysites.com', 'carrd.co', 'site123.me', 'mystrikingly.com', 'wordpress.com', 'blogspot.com', 'netsons.org', 'webador.it', 'business.site']
suffixes = TLD + PLAT


def resolves(d):
    try:
        return socket.gethostbyname(d)
    except Exception:
        return None


def rnd():
    return 'zq' + ''.join(random.choice(string.ascii_lowercase) for _ in range(14))


wild = {s for s in suffixes if resolves(rnd() + '.' + s)}
cands = [(b + '.' + s, tiers[b]) for b in bases for s in suffixes if s not in wild]
with ThreadPoolExecutor(max_workers=60) as ex:
    res = list(ex.map(lambda x: (x[0], x[1], resolves(x[0])), cands))
found = [(d, t, ip) for d, t, ip in res if ip]
ipc = Counter(ip for _, _, ip in found)

print('CONTROLLO_DOMINI: nomi=%d basi=%d suffissi=%d testati=%d risolti=%d jolly_ignorati=%s' % (
    len(nomi), len(bases), len(suffixes) - len(wild), len(cands), len(found), ','.join(sorted(wild)) or 'nessuno'))
print('BASI_PROVATE:', ' '.join(bases))
for t, lab in ((1, 'A nome completo'), (2, 'B nome+comune'), (3, 'C tipo+nome'), (4, 'D solo nome distintivo')):
    rows = [(d, ip) for d, tt, ip in sorted(found) if tt == t]
    for d, ip in rows:
        flag = ' PARCHEGGIO_PROBABILE' if ipc[ip] >= 3 else ''
        print('RISOLVE [%s] %s %s%s' % (lab, d, ip, flag))
if not found:
    print('NESSUN_DOMINIO_RISOLVE')
else:
    print('DA_VERIFICARE_CON_WEBSEARCH: ' + ','.join(d for d, tt, ip in sorted(found) if tt <= 3)[:1500])
