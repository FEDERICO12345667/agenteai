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

- [08/10, Scout, DECISIONE DELL'UTENTE] Settori target: SOLO attivita dove il cliente sceglie guardando online e un sito vetrina serve molto: parrucchieri/barbieri, centri estetici/nail, pizzerie, ristoranti/trattorie, bar/pasticcerie/gelaterie, botteghe di vicinato (alimentari, panetterie, fiorerie, boutique). NON vanno bene falegnamerie, idraulici, elettricisti, officine, carrozzerie, imprese edili, impianti e in generale ambienti tecnici/B2B, ne studi professionali o agenzie immobiliari: vengono scartati subito.

## Come usare i motivi di scarto dell'utente
Se in data/feedback.json compare un nuovo motivo di scarto, trasformalo in una regola qui sopra (una riga, con data e agente a cui si rivolge) e usalo da subito.

## Registro giornaliero (ogni agente aggiunge righe: "IMPARATO: ...")
<!-- il Direttore aggiunge qui sotto una sezione per giorno -->
