# Lavagna degli agenti (Scout, Analista, Copywriter, Direttore)

Questo file e la memoria condivisa della squadra. Si legge SEMPRE prima di iniziare e si aggiorna a fine esecuzione.
Il file data/feedback.json contiene i giudizi REALI dell'utente (lead scartati con motivo, inviati, risposte, "nessuna risposta"): sono piu affidabili di qualsiasi ipotesi degli agenti.

## Regole apprese (verificate, valgono per tutti)
- [08/10, Scout] Un'attivita "senza sito" secondo la sola ricerca puo averlo: Record Bike (Malo) aveva recordbike.com. Segnali di rischio: fonti solo aggregatori (PromoQui, Matrimonio.com) o store-locator di marchi (Hamilton, Longines), confidenza non "alto". Fare SEMPRE il controllo DNS dei domini plausibili e disambiguare con "site:dominio".
- [08/10, Scout] Attenzione agli omonimi: gioielleriastefani.it e di una gioielleria di Massarosa (LU), non di quella di Marano Vicentino. Un dominio che risolve va attribuito all'attivita giusta (citta/indirizzo/telefono).
- [08/10, Scout] Le attivita che vendono marchi noti (gioiellerie/orologerie, bici di marca, ottiche, concessionari) e i professionisti con profilo su portali (fotografi su Matrimonio.com) hanno quasi sempre un sito proprio: non sono buoni lead.
- [01/10, Scout] Attivita chiuse definitivamente (es. ambulatorio veterinario di Malo) vanno scartate.
- [01/10, Copywriter] Il canale e l'incontro di persona: mai proporre chiamate/videochiamate, mai link alla demo, firma "Sono Federico", mai segnaposto [Nome]. La PEC si riporta ma non si usa per il messaggio informale.
- [08/10, Direttore] Dato reale al 08/10 (19 lead valutati dall'utente): 9 scartati, 7 inviati, 3 "risposto no", 0 interessati. Priorita: qualita e correttezza dei lead, non quantita. Pochi lead giusti battono tre sbagliati.
- [09/10, Scout] Un dominio al DNS con nome molto specifico e coincidente con il nome dell'attivita (es. agriturismocabrele.it, pasticceriagambarato.it, osteriacortesconta.it) e quasi certamente il sito proprio anche senza poterne leggere il contenuto (HTTP bloccato in sandbox): scartare subito. Domini generici/ambigui (es. "atavola.it") vanno invece scartati per dubbio, non accettati alla cieca come prova di assenza di sito.
- [09/10, Scout] Nei piccoli comuni (es. Carre) le directory (Cylex/Virgilio) spesso riportano solo indirizzo e telefono senza il nome commerciale: la verifica e impossibile con il solo WebSearch in questi casi, serve un accesso a Google Maps non disponibile in questo sandbox.

- [08/10, Scout, DECISIONE DELL'UTENTE] Settori target: SOLO attivita dove il cliente sceglie guardando online e un sito vetrina serve molto: parrucchieri/barbieri, centri estetici/nail, pizzerie, ristoranti/trattorie, bar/pasticcerie/gelaterie, botteghe di vicinato (alimentari, panetterie, fiorerie, boutique). NON vanno bene falegnamerie, idraulici, elettricisti, officine, carrozzerie, imprese edili, impianti e in generale ambienti tecnici/B2B, ne studi professionali o agenzie immobiliari: vengono scartati subito.

## Come usare i motivi di scarto dell'utente
Se in data/feedback.json compare un nuovo motivo di scarto, trasformalo in una regola qui sopra (una riga, con data e agente a cui si rivolge) e usalo da subito.

## Registro giornaliero (ogni agente aggiunge righe: "IMPARATO: ...")
<!-- il Direttore aggiunge qui sotto una sezione per giorno -->

### 2026-10-09
- Scout: dominio con nome molto specifico e coincidente con il nome dell'attività che risolve al DNS (es. agriturismocabrele.it, pasticceriagambarato.it, osteriacortesconta.it, algallo.it) è quasi certamente il sito proprio anche senza poter leggere il contenuto (HTTP bloccato in sandbox): euristica utile per scartare velocemente. Domini generici/ambigui (es. "atavola.it") vanno invece scartati per dubbio, non accettati alla cieca. Nei piccoli comuni come Carrè, Cylex/Virgilio spesso riportano solo indirizzo e telefono senza il nome commerciale dell'attività: verifica impossibile con il solo WebSearch, servirebbe Google Maps (non disponibile in questo sandbox).
- Analista/Copywriter: non coinvolti oggi (Scout ha restituito 0 candidati validi).
- Direttore: giornata a zero lead. Scartati oggi: Osteria Corte Sconta (Santorso) — ha sito proprio (osteriacortesconta.it/.com); Agriturismo Cabrele (Santorso) — ha sito proprio (agriturismocabrele.it); Agriturismo "Da Mea" (Santorso) — ha sito proprio (agriturismodamea.it); Bar Pasticceria Al Gallo (Vicenza) — ha sito proprio (algallo.it/.com/.net); Pasticceria Gambarato (Vicenza) — ha sito proprio (pasticceriagambarato.it); Gastronomia "A tavola con... Alessandro" (Vicenza) — dominio trovato troppo generico per attribuzione certa, scartato per dubbio; Trattoria Alla Baracca (Vicenza) — email su dominio proprio (info@allabaracca.it); Ponte delle Bele (Vicenza) — scheda ufficiale cita esplicitamente un sito; ChezMoi atelier vintage (Vicenza) — presenza online troppo debole/non verificabile; Giuli Pet Toelettatura (Vicenza) — un risultato cita esplicitamente "sito ufficiale"; Creative Nails (Vicenza) — nessuna recensione reale verificabile, solo scheda booking; parrucchieri/estetiste di Carrè (4 indirizzi via Cylex) — impossibile verificare, nome commerciale mai trovato; Trattoria De Gobbi — in realtà a Creazzo, comune fuori zona.
