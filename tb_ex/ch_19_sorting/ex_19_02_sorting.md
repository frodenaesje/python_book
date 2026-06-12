---
title: "Benchmarking av klassiske sorteringsalgoritmer"
tags: ["sortering", "benchmark", "big-o", "timeit", "importlib"]
difficulty: "medium"
prerequisites: ["funksjoner", "lister", "moduler", "dictionary"]
learning_outcomes:
  - "Forstå hvordan dynamisk import med importlib fungerer"
  - "Måle kjøretid med timeit.repeat"
  - "Sammenligne målt kjøretid med teoretisk vekst (Big-O)"
  - "Implementere teoretisk modell i kode"
author: "Frode Naesje & Copilot"
visibility: "student"
has_solution: true
---

# Benchmarking av klassiske sorteringsalgoritmer

Merk: Det er lite koding i denne oppgaven. Hovedpoenget er å forstå hvordan programmet fungerer, hvordan innebygde moduler brukes, og hvordan målte kjøretider kan sammenlignes med teoretiske modeller (Big-O).

## Beskrivelse av utlevert startkode

Startfilen [sorting_start.py](sorting_start.py) måler eksekveringstid for ulike sorteringsalgoritmer med tre inputstørrelser:
- `N = 1000`
- `N = 5000`
- `N = 10000`

Algoritmene benchmarkes gjennom lista `ALGORITHMS`, for eksempel:

```python
ALGORITHMS = [
    "insertion_sort",
    "selection_sort",
    "merge_sort",
    "tim_sort",
    "quick_sort",
    "heap_sort",
]
```

Forutsetninger for at programmet skal kjøre:
- Alle algoritmefiler ligger i samme katalog som `sorting_start.py`.
- Modulnavn og funksjonsnavn matcher (f.eks. `merge_sort.py` med funksjon `merge_sort(...)`).
- Hver funksjon tar en liste som input.

Programmet setter importsti med:

```python
sys.path.insert(0, os.path.dirname(__file__))
```

Dette gjør at Python finner modulene i samme mappe.

## Kort gjennomgang av programflyten

1. `run_sorting_algorithm(algorithm, array)`
- Importerer modul dynamisk med `importlib.import_module(algorithm)`.
- Henter funksjonen med `getattr(module, algorithm)`.
- Måler tid med `repeat(lambda: func(list(array)), repeat=1, number=3)`.
- Returnerer beste tid (`min(times)`).

2. `benchmark(algorithms, sizes)`
- Lager tilfeldig basisliste for hver størrelse.
- Kjører alle algoritmer på kopi av samme basisliste.
- Lagrer resultat i dictionary med nøkkel `(algoritme, størrelse)`.

3. `theoretical_time(algorithm, n)`
- Skal returnere teoretisk kostnad (vekstform), ikke sekunder.

4. `compare_with_big_o(...)`
- Sammenligner målt tid med teoretisk tid etter skalering.
- Skalering brukes fordi Big-O gir vekstform, ikke absolutt tid i sekunder.

## Oppgave

Implementer funksjonen:

```python
def theoretical_time(algorithm, n):
```

Krav:
- `algorithm` er et navn som streng (f.eks. `"insertion_sort"`).
- `n` er antall elementer i input.
- Returner:
  - `n * n` for kvadratiske algoritmer
  - `n * math.log(n)` for `n log n`-algoritmer
  - `n` dersom algoritmen ikke gjenkjennes

Kjør deretter programmet og vurder om målt verdi følger teoretisk verdi.

Observer spesielt forskjellen mellom:
- `n^2`-algoritmer
- `n log n`-algoritmer

## Leveranse

Lever følgende:
1. Modifisert `sorting_start.py`
2. Snapshot/skjermbilde av utskrift fra kjøring

## Praktisk merknad

Du kan bruke egne implementasjoner av sorteringsalgoritmer, eller de vedlagte, men de må ligge i samme katalog som `sorting_start.py` for at dynamisk import skal virke.

Startkoden er fullt fungerende og bør ikke endres, bortsett fra koden du skriver i `theoretical_time()`. Begynn gjerne med en av algoritmene, dvs at ALGORITHMS kun har ett innslag, eksempelvis:

```python
ALGORITHMS = [
    "insertion_sort"
]
```
Da vil utskriften se slik ut:

Running algorithms: ['insertion_sort']
Running measurements…

=== array length 1000 ===
Algorithm: insertion_sort. Minimum execution time: 0.046008599922060966

=== array length 5000 ===
Algorithm: insertion_sort. Minimum execution time: 1.3214455000124872

=== array length 10000 ===
Algorithm: insertion_sort. Minimum execution time: 4.802041499991901

Measured vs expected (scaled) times:  
insertion_sort n=  1000 measured=0.046009s expected~0.046009s  
insertion_sort n=  5000 measured=1.321446s expected~1.150215s  
insertion_sort n= 10000 measured=4.802041s expected~4.600860s
