---
title: "Konvertering – Streng til Liste"
id: "ch_05_list_and_for_loop_sc_05_10_string_to_list_input"
tags: ["string", "list", "input", "split", "conversion"]
difficulty: "easy"
prerequisites: ["for-loops", "lister", "string-methods"]
learning_outcomes:
  - "Bruke split() for å dele streng"
  - "Konvertere strenger til heltall i liste"
  - "Lese flere verdier fra en linje"
  - "Bruke list comprehension for konvertering"
author: "Frode Næsje & Copilot"
visibility: "student"
---

# Konvertering – Streng til Liste

Demonstrasjon av to måter å lese og konvertere tall fra brukerinput:

## Metode 1: En verdi per linje
```python
list1 = []
for i in range(3):
    tall = int(input(f"Tall {i+1}: "))
    list1.append(tall)
```

## Metode 2: Flere verdier på en linje
```python
s = input("Gi inn tall separert med mellomrom:")
list2 = [int(x) for x in s.split()]
```

## Nøkkelbegreper

- `split()` – deler streng på mellomrom (default)
- `int()` – konverterer streng til heltall
- List comprehension – elegant konvertering

Se `sc_05_10_string_to_list_input.py`.

