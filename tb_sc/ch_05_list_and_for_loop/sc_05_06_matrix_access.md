---
title: "2D Lister – Matrisetilgang og Modifikasjon"
id: "ch_05_list_and_for_loop_sc_05_06_matrix_access"
tags: ["2d-list", "matrix", "nested-list", "loop"]
difficulty: "medium"
prerequisites: ["lister", "for-loops"]
learning_outcomes:
  - "Få tilgang til elementer i 2D lister"
  - "Iterere over matriser med nestede løkker"
  - "Modifisere elementene i en matrise"
  - "Kopiere multidimensjonale lister riktig"
author: "Frode Næsje & Copilot"
visibility: "student"
---

# 2D Lister – Matrisetilgang og Modifikasjon

Demonstrasjon av:
- Tilgang til elementer: `matrix[rad][kolonne]`
- Iterasjon med nestede løkker
- Modifikasjon av elementer
- Kopiering av multidIM lister

## Tilgang

```python
matrix = [[1,2,3], [4,5,6], [7,8,9]]
value = matrix[1][2]  # 6
```

## Iterasjon

```python
for row in matrix:
    for value in row:
        print(value)
```

```python
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j])
```

## Kopiering

- Shallow: `matrix.copy()` – kopierer bare ytre liste
- Bedre: `[row.copy() for row in matrix]` – kopierer hver rad

Se `sc_05_06_matrix_access.py` for full eksempler.

