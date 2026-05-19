---
title: "Manuell Listekopiering med Løkke"
id: "ch_05_list_and_for_loop_sc_05_07_manual_list_copy"
tags: ["list", "copy", "for-loop", "append"]
difficulty: "easy"
prerequisites: ["for-loops", "lister"]
learning_outcomes:
  - "Kopiere liste elemento for element med løkke"
  - "Forstå append() i løkekontekst"
author: "Frode Næsje & Copilot"
visibility: "student"
---

# Manuell Listekopiering med Løkke

Demonstrasjon av den grunnleggende måten å kopiere en liste:

```python
original_list = [1, 2, 3, 4, 5]
copy_list = []
for element in original_list:
    copy_list.append(element)
```

## Nøkkelbegreper

- Starter med tom liste `[]`
- Løkke gjennom original
- Legger hver element til kopia

Dette er en grunnlegende pattern som tjener til utdanningsformål.
I praksis, bruk `list.copy()` eller slicing `list1[:]`.

Se `sc_05_07_manual_list_copy.py`.

