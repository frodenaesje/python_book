---
title: "Postfix Notasjon"
id: "ch_20_classic_datastructures_ch_20_02_postfix_notation"
tags: ["deque", "stack", "algoritmer", "operatorer"]
difficulty: "medium"
prerequisites: ["lister", "deque", "operatorer"]
learning_outcomes:
  - "Bruke deque som stack-datastruktur"
  - "Implementere postfix evaluering med stack"
  - "Forstå algoritmer for uttrykk-evaluering"
author: "Frode Næsje & Copilot"
visibility: "student"
has_solution: true
---

# Postfix Notasjon

Postfix notasjon er en måte å skrive aritmetiske uttrykk på uten parenteser.

## Oppgave

Postfix notasjon er også kjent som Reverse Polish Notation (RPN). I postfix-notasjon plasseres operatorer etter operandene i stedet for foran eller mellom dem.

**Eksempel:** $(4 + 5) \times 3$ blir i postfix `4 5 + 3 *`

Skriv en funksjon **`eval_postfix(postfix_expression)`** som evaluerer et postfix uttrykk ved å følge denne algoritmen:

1. Opprett en tom stack kalt `evaluation_stack`
2. For hvert tegn i `postfix_expression`:
   - Hvis token er et tall, legg det til `evaluation_stack`
   - Hvis token er en operator, pop de nødvendige antall operander fra `evaluation_stack`, utfør operasjonen, og legg resultatet tilbake på `evaluation_stack`
3. Når alle tokens er behandlet, skal `evaluation_stack` inneholde ett element, som er resultatet

## Krav

- Du skal **kun** behandle de binære operatorene: `+`, `-`, `*`, `/`, `%`, `^`
- Uttrykkene skal **kun** inneholde heltall
- `/` er **heltallsdivisjon** (integer division)
- Bruk `deque` fra `collections` for stack-implementasjonen

## Eksempler

| Postfix-uttrykk | Infix-ekvivalent | Resultat |
|---|---|---|
| `4 5 +` | $4 + 5$ | 9 |
| `4 5 + 3 *` | $(4 + 5) \times 3$ | 27 |
| `10 2 /` | $10 \div 2$ | 5 |
| `15 7 %` | $15 \bmod 7$ | 1 |
| `2 3 ^` | $2^3$ | 8 |
| `3 4 + 5 * 2 -` | $((3 + 4) \times 5) - 2$ | 33 |

## Temaer

- `collections.deque` som stack-datastruktur
- Algoritmer for evaluering av uttrykk
- Håndtering av operatorer
- Stack-basert beregning
