---
title: "Grade Statistics"
id: "ex_07_02_grade_statistics"
tags: ["tuple", "dict", "tuple unpacking", "setdefault", "grouping"]
difficulty: "easy"
prerequisites: ["tuple", "dict", "for", "tuple unpacking", "list"]
learning_outcomes:
  - "Use tuples to represent records"
  - "Build a dict from a list of tuples"
  - "Group values by key using setdefault() or get()"
  - "Use dict to count occurrences"
---

# Grade Statistics

## Exercise

A teacher has collected grades from three subjects. The data is stored
as a list of tuples where each tuple contains student name, subject
and grade. Tuples are a natural choice since each row is a fixed
combination of three related values.

Use this data:

```python
grades = [
    ("Alice",   "Math",    "B"),
    ("Bob",     "Math",    "C"),
    ("Alice",   "Python",  "A"),
    ("Charlie", "Math",    "A"),
    ("Bob",     "Python",  "B"),
    ("Alice",   "Physics", "C"),
    ("Charlie", "Python",  "A"),
    ("Bob",     "Physics", "A"),
    ("Charlie", "Physics", "B"),
]
```

Write a program that:
1. Prints all grades neatly formatted - one line per tuple
2. Counts the number of grades per subject and prints the result
3. Builds a dict `{student: [grade, grade, ...]}` and prints all
   grades per student

## Example run

```
All grades:
  Alice    Math      B
  Bob      Math      C
  Alice    Python    A
  Charlie  Math      A
  Bob      Python    B
  Alice    Physics   C
  Charlie  Python    A
  Bob      Physics   A
  Charlie  Physics   B

Grades per subject:
  Math:    3
  Physics: 3
  Python:  3

Grades per student:
  Alice:    B, A, C
  Bob:      C, B, A
  Charlie:  A, A, B
```

## Hint

Use tuple unpacking in the for loop: `for name, subject, grade in grades`

To count per subject: build a dict with `get()`:
`counts[subject] = counts.get(subject, 0) + 1`

To group per student: use `setdefault()`:
`by_student.setdefault(name, []).append(grade)`

## Topics

- Tuples as records
- Dict as counter
- Dict as grouping structure
- `get()` and `setdefault()`

---
## Instructor notes

**Learning objectives covered:** tuple unpacking, dict as counter, dict
as grouper, get/setdefault

**Key contrast:** Two dict-building patterns side by side - counting
(values are ints) vs grouping (values are lists). Students see both
use cases in one exercise.
