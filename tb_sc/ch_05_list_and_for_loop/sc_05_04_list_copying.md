---
title: "Listekopiering – Møte, Shallow og Deep"
id: "ch_05_list_and_for_loop_sc_05_04_list_copying"
tags: ["list", "copy", "reference", "shallow-copy", "deep-copy"]
difficulty: "medium"
prerequisites: ["lister"]
learning_outcomes:
  - "Forstå referansekopiering mot ekte kopiering"
  - "Bruke shallow copy med slicing, list(), copy()"
  - "Bruke deep copy for komplekse strukturer"
author: "Frode Næsje & Copilot"
visibility: "student"
---

# Listekopiering – Referanse, Shallow og Deep

Demonstrasjon av ulike kopierings-metoder:

## Referansekopiering (ingen kopi)
```python
list2 = list1  # Begge peker til samme objekt
```

## Shallow Copy (flere metoder)
- `list1[:]` – slicing
- `[x for x in list1]` – list comprehension
- `[] + list1` – konkatening
- `list1.copy()` – list-metode
- `copy.copy(list1)` – copy-modul

## Deep Copy
```python
import copy
copy.deepcopy(list1)  # Kopierer rekursivt
```

Se `sc_05_04_list_copying.py` for detaljerte eksempler.

## Viktig

For enkle lister av enkle typer (int, str) holder shallow copy.
For lister av lister/objekter bør du bruke deep copy.

