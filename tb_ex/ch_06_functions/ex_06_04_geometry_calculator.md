---
title: "Geometry Calculator"
id: "ex_06_04_geometry_calculator"
tags: ["function", "multiple return values", "math", "tuple", "type hint"]
difficulty: "easy"
prerequisites: ["def", "return", "tuple", "math", "float", "type hint"]
learning_outcomes:
  - "Write functions that return multiple values as a tuple"
  - "Unpack a tuple returned from a function"
  - "Use the math module inside a function"
  - "Organize related functions in one module"
---

# Geometry Calculator

## Exercise

Write three functions that each calculate the area and perimeter
of a geometric shape, returning both values as a tuple.

1. `rectangle(width: float, height: float) -> tuple` -
   area = width * height, perimeter = 2 * (width + height)

2. `circle(radius: float) -> tuple` -
   area = pi * r^2, perimeter = 2 * pi * r

3. `right_triangle(a: float, b: float) -> tuple` -
   area = 0.5 * a * b, perimeter = a + b + hypotenuse
   (use Pythagoras for the hypotenuse)

Write a main program that lets the user choose a shape, reads the
required dimensions, and displays area and perimeter.

## Example run

```
Choose a shape:
1. Rectangle
2. Circle
3. Right triangle
Your choice: 2
Enter radius: 5
Circle with radius 5.0:
  Area:      78.54
  Perimeter: 31.42
```

## Topics

- Functions returning a tuple
- Tuple unpacking
- `import math`
- Simple menu with `match-case`

---
## Instructor notes

**Learning objectives covered:** multiple return values, tuple unpacking,
math module, menu

**Tuple unpacking pattern:**
```python
area, perimeter = circle(radius)
```

**Extension:** Ask students to add a fourth shape - equilateral triangle
or regular hexagon. This reinforces the pattern.
