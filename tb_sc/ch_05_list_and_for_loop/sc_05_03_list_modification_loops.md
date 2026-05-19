---
title: "Listemodifikasjon i Løkker"
id: "ch_05_list_and_for_loop_sc_05_03_list_modification_loops"
tags: ["list", "for-loop", "enumerate", "range", "index"]
difficulty: "easy"
prerequisites: ["for-loops", "lister"]
learning_outcomes:
  - "Forstå forskjellen mellom loop-variabel og indekstilgang"
  - "Modifisere liste-elementer direkte med index"
  - "Bruke enumerate() for å få både index og verdi"
author: "Frode Næsje & Copilot"
visibility: "student"
---

# Listemodifikasjon i Løkker

Demonstrasjon av tre metoder for å modifisere liste-elementer:

1. **Method 1**: For-variabel (ikke modifisert liste)
   - `for number in numbers:` – loop-variabelen er en kopi
   
2. **Method 2**: Indeks med range
   - `for index in range(len(numbers)):` – modifiserer direkte
   
3. **Method 3**: enumerate()
   - `for index, value in enumerate(numbers):` – både index og verdi

Se `sc_05_03_list_modification_loops.py` for kodeksampler.

## Viktig Innsikt

- Bare **Method 2** og **Method 3** modifiserer selve listen
- Method 1 fungerer bare for lesing

