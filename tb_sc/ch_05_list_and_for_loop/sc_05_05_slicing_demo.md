---
title: "Slicing – Stringer og Lister"
id: "ch_05_list_and_for_loop_sc_05_05_slicing_demo"
tags: ["slicing", "string", "list", "index", "step"]
difficulty: "easy"
prerequisites: []
learning_outcomes:
  - "Bruke slicing på strenger og lister"
  - "Forstå start, stop og step i slicing"
  - "Reversere strenger/lister med slicing"
author: "Frode Næsje & Copilot"
visibility: "student"
---

# Slicing – Stringer og Lister

Demonstrasjon av slicing med syntax `s[start:stop:step]`.

## Grunnleggende Slicing

- `s[0:5]` – fra indeks 0 til 4 (stop er eksklusiv)
- `s[:]` eller `s[::]` – hele strengen/listen
- `s[::2]` – annethvert tegn/element

## Reversering

- `s[::-1]` – reversert streng/liste
- `s[5:0:-1]` – baklengs fra indeks 5 til 1

## Spesialverdier

- `None` som start/stop/step bruker standardverdier
- Fungerer på både strenger og lister

Se `sc_05_05_slicing_demo.py` for aktuelle eksempler.

