---
title: "Fartskontroll mellom Fotobokser"
id: "ch_07_tuple_set_dict_ex_07_04_speeding"
tags: ["dict", "klasse", "datetime", "fil"]
difficulty: "hard"
prerequisites: ["klasser", "dict", "datetime"]
learning_outcomes:
  - "Designe domeneklasser (SpeedTicket, Vehicle)"
  - "Håndtere kompleks data fra flere kilder"
  - "Implementere persistens med pickle"
  - "Lese og analysere loggdata"
author: "Frode Næsje & Copilot"
visibility: "student"
has_solution: true
---

# Fartskontroll mellom Fotobokser

I denne oppgaven skal du bygge en enkel terminalapp som registrerer kjøretøy og sjekker fartsoverskridelser basert på to fotobokser (A og B).

## Forutsetninger
- Bilene kjører kun fra A til B
- Avstand A→B = 5 km
- Fartsgrense = 60 km/t (minst lovlig kjøretid = 5 minutter)
- Loggformat (en per linje): `REGNR, YYYY-MM-DD HH:MM:SS`

## Del 1: Domeneobjekter
- `SpeedTicket`: lagrer tidspunkt i A og B samt beregnet fart. Implementer likhet slik at identiske passeringer ikke dupliseres.
- `Vehicle`: lagrer kjøretøydata og en liste av `SpeedTicket`.
	- Legg til nye tickets uten dubletter.
	- Skriv en rapport over alle overtredelser for kjøretøyet.
	- __str__ skal vise kjøretøyinfo og antall overtredelser (hvis noen).

## Del 2: Lagring
- Les/skriv alle kjøretøy til `vehicles.dat` med `pickle`.
- Hvis det ligger gamle objekter uten `_speed_tickets`, sørg for at feltet opprettes.

## Del 3: Fotoboksdata
- Funksjon for å lese en fotoboksfil til `{regnr: [datetime, ...]}` (filene `box_a.txt` og `box_b.txt`).
- Par A- og B-tider: for hver tid i A, finn første tid i B som er større eller lik.
- Beregn gjennomsnittsfart (km/t) gitt distanse og reisetid.

## Del 4: Fartssjekk
- `check_speeding_for_vehicle`: registrer overtredelser for ett kjøretøy når reisetid < `MIN_TID`.
- `check_all_vehicles`: kjør samme sjekk for alle kjøretøy og returner antall nye funn.

## Del 5: Meny
- List, legg til, søk/slett kjøretøy, vis tickets for ett kjøretøy, lagre og avslutt.
- Kjør fartssjekk én gang ved oppstart basert på loggene.

## Startkode
- Bruk filen `ex_07_06_speeding_start.py`.
- Linjene 1–95 og fra 210 og ned er ferdige og skal ikke røres.
- Se etter `TODO`-kommentarer for hva du skal implementere.

Lykke til!

