---
title: "Salary Table"
id: "ex_02_06_salary_table"
tags: ["f-string", "field width", "alignment", "input", "formatting"]
difficulty: "medium"
prerequisites: ["print", "input", "f-string", "variables"]
learning_outcomes:
  - "Use f-string field width to align text and number columns"
  - "Understand default alignment: text left, numbers right"
  - "Use variables as format specifiers in f-strings"
---

# Salary Table

## Exercise

### Part 1

Write a program that reads name, age and monthly salary for three people,
then prints a formatted table with aligned columns.

Example run:

```
Enter name 1: Alice
Enter age 1: 32
Enter monthly salary 1: 52000
Enter name 2: Bob
Enter age 2: 28
Enter monthly salary 2: 47500
Enter name 3: Clara
Enter age 3: 41
Enter monthly salary 3: 61000

Name                 Age    Monthly salary
Alice                 32         52,000.00
Bob                   28         47,500.00
Clara                 41         61,000.00
```

Use hardcoded field widths in the f-string format specifiers.

### Part 2

Extend your solution: store the field widths in variables and use them
in the format specifiers instead of hardcoded numbers.

```python
name_width = 20
age_width = 6
salary_width = 18

# then use them like this:
print(f"{name:{name_width}}{age:{age_width}}{salary:{salary_width},.2f}")
```

Run the program and verify the output is identical to Part 1.
Then try changing `name_width = 25` - the whole table adjusts automatically.

## Topics

- f-string field width and alignment
- Comma separator for large numbers (`{value:,.2f}`)
- Variables as format specifiers (`{value:{width}}`)

---
## Instructor notes

**Learning objectives covered:** f-string field width, column alignment, dynamic format specifiers

**Part 1 hint:** Default alignment is text-left, numbers-right. Use `{name:20}` for a 20-char left-aligned text column and `{salary:18,.2f}` for a right-aligned number with comma separator.

**Part 2 insight:** The format spec inside `{}` can itself contain variable references. `f"{value:{width}.{precision}f}"` is fully valid Python - this is the "advanced" pattern from the chapter. Changing one variable updates the entire table layout.
