---
title: "Temperature Conversion Table"
id: "ex_05_02_temperature_table"
tags: ["for", "range", "f-string", "arithmetic"]
difficulty: "easy"
prerequisites: ["for", "range", "f-string field width", "arithmetic"]
learning_outcomes:
  - "Use range() with a step value"
  - "Apply a formula inside a loop"
  - "Produce aligned tabular output with f-string field widths"
---

# Temperature Conversion Table

## Exercise

Write a program that displays a temperature conversion table for degrees
Celsius and degrees Fahrenheit. The table should cover temperatures from
0 to 100 degrees Celsius in steps of 10 degrees.

The formula for converting Celsius to Fahrenheit is:
F = C * 9 / 5 + 32

Include a header row and align the columns.

## Example run

```
Celsius    Fahrenheit
      0          32.0
     10          50.0
     20          68.0
     30          86.0
     40         104.0
     50         122.0
     60         140.0
     70         158.0
     80         176.0
     90         194.0
    100         212.0
```

## Topics

- `range()` with a step value
- Formula inside a loop
- f-string column alignment

---
## Instructor notes

**Learning objectives covered:** range with step, formula in loop, tabular output

**range() with step:** `range(0, 101, 10)` - worth pointing out that the
stop value (101) must be greater than the last desired value (100).

**Extension:** Ask students to also show Fahrenheit to Celsius in a third
column, or to extend the table to negative temperatures.
