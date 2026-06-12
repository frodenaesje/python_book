---
title: "Multiplication Table"
id: "ex_05_08_multiplication_table"
tags: ["for", "range", "nested loops", "f-string", "list comprehension"]
difficulty: "medium"
prerequisites: ["for", "range", "nested loops", "f-string field width"]
learning_outcomes:
  - "Use nested for loops to generate a 2D table"
  - "Align columns in tabular output"
  - "Understand how the outer and inner loop variables combine"
---

# Multiplication Table

## Exercise

Write a program that displays a multiplication table for integers
from 1 to 10. Include row and column labels.

## Example run

```
     1    2    3    4    5    6    7    8    9   10
 1   1    2    3    4    5    6    7    8    9   10
 2   2    4    6    8   10   12   14   16   18   20
 3   3    6    9   12   15   18   21   24   27   30
 4   4    8   12   16   20   24   28   32   36   40
 5   5   10   15   20   25   30   35   40   45   50
 6   6   12   18   24   30   36   42   48   54   60
 7   7   14   21   28   35   42   49   56   63   70
 8   8   16   24   32   40   48   56   64   72   80
 9   9   18   27   36   45   54   63   72   81   90
10  10   20   30   40   50   60   70   80   90  100
```

## Topics

- Nested `for` loops
- `end=""` to print without newline
- Column alignment with f-string field widths

---
## Instructor notes

**Learning objectives covered:** nested loops, print with end, column alignment

**The print trick:** `print(f"{value:5}", end="")` prints without a newline,
allowing multiple values on the same line. `print()` at the end of the inner
loop moves to the next row.

**Extension:** Ask students to make the table size configurable by reading N
from the user, and display an N x N table.
