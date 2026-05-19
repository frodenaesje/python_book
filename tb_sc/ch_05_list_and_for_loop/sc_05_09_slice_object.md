---
title: "Slice-Objekter og Standardverdier"
id: "ch_05_list_and_for_loop_sc_05_09_slice_object"
tags: ["slicing", "slice-object", "None", "step"]
difficulty: "medium"
prerequisites: ["slicing"]
learning_outcomes:
  - "Opprett slice-objekter med slice()-konstruktøren"
  - "Forstå hva None representerer i slice-objekter"
  - "Bruke slice-objekter eksplisitt"
author: "Frode Næsje & Copilot"
visibility: "student"
---

# Slice-Objekter og Standardverdier

En slice kan lages eksplisitt med `slice(start, stop, step)`.

## Slice-Konstruktøren

```python
s = "Hei på deg"
slice1 = slice(2, None)    # Fra indeks 2 til slutten
slice2 = slice(None, 5)    # Fra start til indeks 5
slice3 = slice(None, None) # Hele strengen
slice4 = slice(2, 8, 2)    # Fra 2 til 8, hopp 2
```

## Standardverdier

- `start=None` → fra start (indeks 0)
- `stop=None` → til slutten
- `step=None` → steg 1

## Attributter

```python
slice_obj.start
slice_obj.stop
slice_obj.step
```

Se `sc_05_09_slice_object.py` for praktiske eksempler.

