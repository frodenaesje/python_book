---
title: "2D Liste-Initialisering – Løkker og Comprehension"
id: "ch_05_list_and_for_loop_sc_05_11_twodim_init"
tags: ["2d-list", "matrix", "nested-loop", "list-comprehension"]
difficulty: "medium"
prerequisites: ["for-loops", "nested-loops", "list-comprehension"]
learning_outcomes:
  - "Initialisere 2D lister med nestede løkker"
  - "Fylle matrise med verdier"
  - "Bruke list comprehension for 2D initialisering"
author: "Frode Næsje & Copilot"
visibility: "student"
---

# 2D Liste-Initialisering – Løkker og Comprehension

Demonstrasjon av to måter å initialisere en 2D liste (matrise):

## Metode 1: Nestede Løkker
```python
NUM_ROWS = 3
NUM_COLS = 3
matrix = []
for i in range(NUM_ROWS):
    row = []
    for j in range(NUM_COLS):
        value = i * NUM_COLS + j + 1
        row.append(value)
    matrix.append(row)
```

## Metode 2: List Comprehension
```python
matrix = [[i * NUM_COLS + j + 1 for j in range(NUM_COLS)] 
          for i in range(NUM_ROWS)]
```

Begge produserer: `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]`

## Viktig

Method 1 er lettere å forstå for nybegynnere.
Method 2 er mer elegant og pythonisk.

Se `sc_05_11_twodim_init.py`.

