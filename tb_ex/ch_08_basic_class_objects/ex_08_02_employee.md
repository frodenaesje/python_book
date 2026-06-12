---
title: "Employee"
id: "ex_08_02_employee"
tags: ["class", "class variable", "classmethod", "__str__", "__eq__", "__lt__"]
difficulty: "easy"
prerequisites: ["class", "__init__", "class variable", "@classmethod"]
learning_outcomes:
  - "Use a class variable to count instances"
  - "Implement a @classmethod"
  - "Sort objects using __lt__ and __gt__"
  - "Distinguish between class variables and instance attributes"
---

# Employee

## Exercise

Create a class `Employee` with the following:

**Instance attributes** (leading underscore):
- `_name`, `_employee_id`, `_department`, `_salary`

**Class variable:**
- `_employee_count` - incremented each time an employee is created

**Methods:**
- `give_raise(amount)` - increase salary by `amount`. Reject negative amounts.
- `annual_salary()` - returns monthly salary * 12
- `@classmethod get_employee_count()` - returns total employees created
- `__str__()` - formatted output of all attributes
- `__eq__()` - two employees are equal if they have the same `_employee_id`
- `__lt__()` - sort by salary
- `__gt__()` - sort by salary

## Example run

```
Employee ID: 1001
Name:        Alice Johnson
Department:  Engineering
Monthly:     65000
Annual salary: 780000
After raise:   840000
Invalid raise - amount must be positive.

Employees created: 3

e1 == e2? False
Highest salary: Clara Lee (72000/month)
```

## Topics

- Class variable
- `@classmethod`
- Comparison dunder methods
- `max()` with objects

---
## Instructor notes

**Learning objectives covered:** class variable, classmethod, dunder methods,
max() with objects

**Class variable pattern:**
```python
class Employee:
    _employee_count = 0
    def __init__(self, ...):
        Employee._employee_count += 1
```

**max() demo:** `max(e1, e2, e3)` uses `__gt__` automatically.
