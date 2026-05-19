---
title: "Slice Assignment – Erstatning og Innsetting"
id: "ch_05_list_and_for_loop_sc_05_08_slice_assignment"
tags: ["slicing", "list", "assignment", "modification"]
difficulty: "medium"
prerequisites: ["slicing", "lister"]
learning_outcomes:
  - "Bruke slice som venstre side av tilordning"
  - "Erstatte deler av liste"
  - "Fjerne elementer med slice assignment"
  - "Sette inn elementer på en bestemt plass"
author: "Frode Næsje & Copilot"
visibility: "student"
---

# Slice Assignment – Erstatning og Innsetting

Demonstrasjon av hvordan slice kan stå på venstre side av en tilordning.

## Eksempler

### Erstatning
```python
list1[1:4] = [10, 11, 12]  # Erstatter elementer på plass 1-3
```

### Sletting
```python
list1[2:4] = []  # Fjerner elementer på plass 2-3
```

### Innsetting
```python
list1[1:1] = [99, 100]  # Setter inn to elementer før indeks 1
```

## Viktig

- Høyre side kan være en liste med annen lengde enn slice
- Python tilpasser listens størrelse automatisk
- Enkelt verktøy for listemonalitering

Se `sc_05_08_slice_assignment.py` for detaljerte eksempler.

