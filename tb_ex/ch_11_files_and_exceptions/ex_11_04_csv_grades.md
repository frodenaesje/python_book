---
title: "CSV Grade Report"
id: "ex_11_02_csv_grades"
tags: ["csv", "DictReader", "DictWriter", "dict", "type hint", "float"]
difficulty: "easy"
prerequisites: ["csv", "DictReader", "dict", "list", "float", "type hint"]
learning_outcomes:
  - "Read a CSV file using csv.DictReader"
  - "Build a dict[str, list[float]] from CSV data"
  - "Compute averages and find top/bottom students"
  - "Write results to a new CSV using csv.DictWriter"
---

# CSV Grade Report

## Exercise

The file `grades.csv` contains grades for five students across four subjects.

```
name,math,english,science,history
Alice,5.5,6.0,4.5,5.0
Bob,3.0,4.5,3.5,4.0
...
```

Write two functions:

### load_grades(filename: str) -> dict[str, list[float]]

Read the CSV and return a dict where each key is a student name and
the value is a list of their grades (as floats).

```python
# Result:
{
    "Alice": [5.5, 6.0, 4.5, 5.0],
    "Bob":   [3.0, 4.5, 3.5, 4.0],
    ...
}
```

### write_report(grades: dict[str, list[float]], filename: str) -> None

Compute the average for each student and write a summary CSV with columns
`name` and `average`, sorted from highest to lowest average.

### Main program

Load `grades.csv`, print the averages, and write the report to
`grade_report.csv`.

## Example run

```
Grade averages:
  Clara:  5.75
  Emma:   5.38
  Alice:  5.25
  Bob:    3.75
  David:  3.75

Report written to grade_report.csv
```

## Topics

- `csv.DictReader` and `csv.DictWriter`
- `dict[str, list[float]]` as the data model
- Computing averages
- Sorting by value

---
## Instructor notes

**Learning objectives covered:** DictReader, DictWriter, typed dict, averages

**Why dict[str, list[float]]:** The type hint tells the student exactly
what the function returns before they start writing it. The CSV maps
directly to this structure - each row is one key-value pair.

**DictReader skips the header automatically** - worth pointing out.

**sorted with key:**
```python
sorted(averages.items(), key=lambda x: x[1], reverse=True)
```
