---
title: "Fartsovertredelser med Vehicle Klasse"
id: "ch_07_tuple_set_dict_ex_07_06_speeding"
tags: ["dict", "klasse", "datetime", "pickle", "løsning"]
difficulty: "hard"
prerequisites: ["klasser", "dict", "datetime", "pickle"]
learning_outcomes:
  - "Designe Vehicle-klasse for kjøretøydata"
  - "Lagre SpeedTicket-objekter i kjøretøy"
  - "Implementere __eq__ for objektsammenlikning"
  - "Persistere data med pickle"
  - "Integrere komplekse systemer"
author: "Frode Næsje & Copilot"
visibility: "student"
has_solution: true
---

# Fartsovertredelser med Vehicle Klasse

Komplett løsning for fartsovertredelsessystem med klasse-basert design, persistens og rapporter.

## Klasser

### SpeedTicket
- **Attributter**: `_timestamp_A`, `_timestamp_B`, `_speed`
- **Metode**: `as_line()` – Formaterer overtredelse for utskrift
- **Metode**: `__eq__()` – Tillater å sjekke `ticket in list` for deduplisering

### Vehicle
- **Attributter**: Regnr, merke, modell, årsmodell, kjørelengde, pris
- **Attributt**: `_speed_tickets` – Liste av SpeedTicket-objekter
- **Metode**: `add_speed_ticket()` – Legger til uten dubletter
- **Metode**: `report()` – Skriver ut alle overtredelser

## Persistens

Kjøretøy og overtredelser lagres via `pickle` i `vehicles.dat`:
```python
with open("vehicles.dat", "wb") as f:
    pickle.dump(vehicles_dict, f)
```

## Workflow

1. Les boksfiler (box_a.txt, box_b.txt)
2. Beregn fart for hver kjøretøy-kombinasjon
3. Opprett SpeedTicket for over­tredelser
4. Lagre i Vehicle-objekter
5. Persisterer til fil

## Nøkkelfunksjoner

- `read_log()` – Les boksfil til dictionary
- `pair_first_after()` – Match tider fra A og B
- `avg_speed_kmt()` – Beregn gjennomsnittsfart
- `find_speeding_vehicles()` – Returner {reg: [tickets]}

## Datastruktur

```python
vehicles_dict = {
    'AB12345': Vehicle(...),
    'CD67890': Vehicle(...),
}
```

Hver Vehicle har liste med alle overtredelser knyttet til det kjøretøyet.

Se startkode i [ex_07_06_speeding_start.py](ex_07_06_speeding_start.py).

