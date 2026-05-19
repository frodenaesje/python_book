---
title: "Kapittel 11 — Filbehandling og exceptions"
id: "tb_sc_ch_11_files_and_exceptions_README"
tags: ["fil", "exceptions", "try-except", "with", "pickle"]
difficulty: "medium"
prerequisites: ["funksjoner", "klasser"]
learning_outcomes:
  - "Åpne og lese filer med ulike metoder"
  - "Skrive og append data til filer"
  - "Håndtere exceptions med try/except/finally"
  - "Lage egne exceptions"
  - "Bruke context managers med with"
  - "Serialisere objekter med pickle"
author: "Frode Næsje & Copilot"
visibility: "student"
has_solution: true
---

## Kapittel 11 — Filbehandling og exceptions

Dette kapittelet viser grunnleggende filbehandling og unntakshåndtering i Python. Eksemplene er skrevet slik at du kan kjøre dem direkte og studere resultatene. Vi unngår bruk av `dict` og `set` per restriksjon.

Innhold (filer):

- `sc_11_01_open_write.py` — åpne filer, skrive med `write()` og `writelines()`
- `sc_11_02_read_methods.py` — forskjell mellom `read()`, `readline()` og `readlines()`
- `sc_11_03_append_numeric.py` — append, lese/skriv numeriske data (tekstformat og enkle parsing)
- `sc_11_04_file_dialog.py` — enkle fildialogbokser med `tkinter.filedialog` (GUI‑fri fallback)
- `sc_11_05_read_web.py` — lese tekst fra web (requests eller urllib)
- `sc_11_06_exceptions.py` — try/except/finally, grov og finmasket fangst, innebygde exception-klasser
- `sc_11_07_custom_exception.py` — lage egne exceptions og bruke dem
- `sc_11_08_context_manager.py` — `with open(...)` og skrive egen context manager
- `sc_11_09_pickle_example.py` — bruke `pickle` for å serialisere en Account‑klasse (leder på tidligere kapitler)


Kapitteltekst — teori og oversikt

Dette kapitlet introduserer praktisk filbehandling i Python og grunnleggende unntakshåndtering. Målet er at du etter å ha lest materialet skal forstå:

- Hvordan åpne, lese, skrive og legge til data i filer på en trygg og lesbar måte.
- Forskjellen mellom de vanlige lese‑metodene og når hver er hensiktsmessig.
- Hvordan representere enkle numeriske data i tekstfiler for senere lesing.
- Hvordan bruke enkle GUI‑dialoger for å velge filer, og en CLI‑fallback når GUI ikke er tilgjengelig.
- Hvordan hente tekst fra nettet med standardbiblioteket.
- Hvordan skrive robust kode ved å fange og håndtere exceptions korrekt — både grov og finmasket.
- Hvordan lage og bruke egne exceptions for tydelig feilhåndtering.
- Hvordan bruke `with` og lage egne context managers for trygt oppsett/rydding.
- Hvordan serialisere objekter med `pickle` for enkel vedvarende lagring (med advarsler om sikkerhet).

Under følger en grovmasket beskrivelse av hvert eksempelprogram i denne mappen. Hver beskrivelse peker på de viktigste funksjonene og hvilke linjer i kildefilen som implementerer dem — bruk dette som guide når du studerer koden.

1) `sc_11_01_open_write.py` — skrive filer
	 - Hensikt: vise hvordan man åpner en fil for skriving (`w`) og for append (`a`) og forskjellen mellom `write()` og `writelines()`.
	 - Viktige deler:
		 - `write_example()` implementeres linje 9–19: åpner fil med `with p.open('w', ...)` og skriver to linjer (linje 12–14), deretter demonstreres `writelines` i append‑modus (linje 16–19).
		 - `__main__`‑demoen som kjører eksemplet er linje 22–25.

2) `sc_11_02_read_methods.py` — lese metoder (read/readline/readlines)
	 - Hensikt: vise forskjellen på `read()` (hele filen som streng), `readline()` (én linje om gangen) og `readlines()` (liste av linjer), og når du bør bruke hver metode.
	 - Viktige deler:
		 - Oppretting av en demo‑fil: `prepare_demo()` linje 9–11.
		 - `demo_read()` bruker `read()` (linje 14–19).
		 - `demo_readline()` viser hvordan lese linje for linje i en løkke (linje 22–30).
		 - `demo_readlines()` leser hele filen som liste (linje 33–39).
		 - `__main__`‑kallet som viser alle tre er linje 42–47.

	 - Råd (kort): bruk `read()` for små filer eller når du trenger hele innholdet; `readline()` når du vil prosessere én linje om gangen og unngå å laste hele filen; `readlines()` når du ønsker en liste og filen er moderat liten.

3) `sc_11_03_append_numeric.py` — skrive og lese tall
	 - Hensikt: demonstrere å lagre tall som tekstlinjer og lese dem tilbake med enkel parsing.
	 - Viktige deler:
		 - `write_numbers()` skriver en liste av tall til fil (linje 9–13).
		 - `append_number()` viser hvordan legge til én ny linje (linje 16–19).
		 - `read_numbers()` viser enkel robust parsing med `try/except` for `int()` (linje 22–34).
		 - Demo i `__main__` (linje 37–41) viser skriving, append og lesing.

4) `sc_11_04_file_dialog.py` — fildialoger med fallback
	 - Hensikt: vise hvordan man kan bruke `tkinter.filedialog` for å be brukeren velge filer, samtidig som vi har en CLI‑fallback for ikke‑GUI miljøer.
	 - Viktige deler:
		 - Import og sjekk for tkinter (linje 9–14) setter `TK_AVAILABLE`.
		 - `pick_file_dialog()` gir dialog‑ eller input‑fallback (linje 17–26).
		 - `pick_save_dialog()` for lagring (linje 29–36).
		 - Enkel CLI/demo i `__main__` (linje 39–46).

5) `sc_11_05_read_web.py` — lese fra web med urllib
	 - Hensikt: demonstrere enkel henting av tekst via HTTP uten eksterne biblioteker.
	 - Viktige deler:
		 - `fetch_text(url, max_bytes)` åpner en URL og leser opptil `max_bytes` (linje 9–13).
		 - `__main__` (linje 16–21) viser bruk og enkel feilbehandling.
	 - Merk: krever nettverkstilgang; for robuste programmer bør du håndtere statuskoder, timeouts og større responser.

6) `sc_11_06_exceptions.py` — try/except/finally og grov vs finmasket håndtering
	 - Hensikt: vise mønstre for feilbehandling og diskutere når du skal fange spesifikke exceptions vs bredt.
	 - Viktige deler:
		 - `divide(a, b)` demonstrerer spesifikke unntak (`ZeroDivisionError`, `TypeError`), `else` og `finally` (linje 7–21). Dette viser ren struktur for sikker beregning.
		 - `broad_handler_example(values)` viser grovfangst med `except Exception as exc` i en batch‑prosess (linje 24–32).
		 - Demo som kjører funksjonene er linje 35–41.

7) `sc_11_07_custom_exception.py` — egne exceptions
	 - Hensikt: vise hvordan lage en enkel `ValidationError` for klarere feilrapportering i funksjoner som validerer input.
	 - Viktige deler:
		 - `ValidationError` klassen (linje 7–9).
		 - `positive_int(value)` som bruker `ValidationError` for ikke‑heltall eller negative tall (linje 12–19).
		 - Demoen som viser eksempler på feil er linje 22–28.

8) `sc_11_08_context_manager.py` — `with` og egen context manager
	 - Hensikt: demonstrere standard `with` for filhåndtering og hvordan bygge en egen context manager‑klasse for å håndtere oppsett/rydding.
	 - Viktige deler:
		 - `SimpleLogger` med `__enter__`/`__exit__` (linje 9–22) viser mønsteret for logging og feiloppdagelse.
		 - `demo_with_file()` som bruker `with p.open(...)` (linje 25–28).
		 - `__main__`‑demoen (linje 31–34).

9) `sc_11_09_pickle_example.py` — serialisering med pickle
	 - Hensikt: illustrere enkel objektlagring og gjenlasting med `pickle`. Vi bruker en enkel `Account`‑klasse med ledende underscore for attributter som i tidligere kapitler.
	 - Viktige deler:
		 - `Account` klassen (linje 10–28) med `deposit`/`withdraw` og `__repr__`.
		 - `save_account()` (linje 31–34) og `load_account()` (linje 37–40) gjør dump/load via fil.
		 - Demo av lagring og lesing (linje 43–50).
	 - Advarsel: `pickle` skal kun brukes på data du stoler på — unpickle av ukjente filer kan kjøre ondsinnet kode.

Avsluttende kommentarer
 - Alle eksemplene er holdt enkle for undervisningsformål. De er ment å kjøres lokalt og modifiseres stegvis for å utforske effektene (prøv å skrive store filer, manglende rettigheter, feil input etc.).
 - Et passende øvingsløp: kjør filskriving, lesing med alle tre metodene, test append og numerisk parsing, så bygg små feilscenarier og fang dem med `try/except` for å se hvordan programmet oppfører seg.
 - Hvis du ønsker, kan jeg også legge til en tabell i README som sammenfatter for/ulemper ved `read()`/`readline()`/`readlines()`, eller lage øvingsoppgaver med løsningsforslag.

Hvis du vil at jeg skal endre formuleringer (mer lærebok‑formelt språk), legge til bilder/diagrammer eller generere oppgaver med løsninger, si fra — så gjør jeg det som neste steg.


