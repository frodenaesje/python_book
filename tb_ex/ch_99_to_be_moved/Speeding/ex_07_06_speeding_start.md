---
title: "Fartsovertredelser – Detaljert Analyse"
id: "ch_07_tuple_set_dict_ex_07_06_speeding_start"
tags: ["dict", "datetime", "klasse", "fil"]
difficulty: "hard"
prerequisites: ["klasser", "dictionary", "datetime"]
learning_outcomes:
  - "Designe klasser for komplekse domener (kjøretøy, overtredelser)"
  - "Bruke dictionary for effektiv datalagringe"
  - "Håndtere tidsbasert matching av data fra flere kilder"
  - "Lese binære filer og strukturere data"
author: "Frode Næsje & Copilot"
visibility: "student"
has_solution: true
---

# Fartsovertredelser – Detaljert Analyse

En utvidet løsning for deteksjon av fartsovertredelser som inkluderer kjøretøyinformasjon og strukturert lagring av resultater.

## Oppgavebeskrivelse

Utvid systemet fra tidligere for å:

1. Lagre kjøretøyinformasjon (navn, eier, registreringsnummer)
2. Bygge en Vehicle-klasse som holder styr på alle overtredelser for hvert kjøretøy
3. Implementere persistens (lagre/hente fra fil)
4. Generere rapporter over fartsovertredelser

## Klasser

- **SpeedTicket**: Enkeltovotredelse (tid A, tid B, fart)
- **Vehicle**: Holder kjøretøydata og liste med SpeedTickets
- **SpeedingDatabase**: Administrerer all data, lesing/skriving

## Fil-format

`vehicles.dat` – Binær format eller strukturert tekstformat med kjøretøydata

Se [ex_07_06_speeding_start.py](ex_07_06_speeding_start.py) for startkode og [ex_07_06_speeding.py](ex_07_06_speeding.py) for løsning.

