---
title: "Vector2D"
id: "ex_08_04_vector2d"
tags: ["class", "__add__", "__mul__", "__abs__", "__str__", "__repr__", "__neg__"]
difficulty: "medium"
prerequisites: ["class", "__init__", "dunder methods", "math"]
learning_outcomes:
  - "Implement vector arithmetic with dunder methods"
  - "Use __abs__ for vector magnitude"
  - "Implement scalar multiplication with __mul__"
  - "Implement __neg__ for vector negation"
---

# Vector2D

## Exercise

Create a class `Vector2D` representing a 2D mathematical vector.

**Attributes:**
- `_x`, `_y` - the x and y components

**Methods:**
- `__str__()` - e.g. `Vector2D(3, 4)`
- `__repr__()` - same as `__str__`
- `__add__()` - vector addition: (x1+x2, y1+y2)
- `__sub__()` - vector subtraction
- `__mul__(scalar)` - scalar multiplication: (x*s, y*s)
- `__neg__()` - negate the vector: (-x, -y)
- `__abs__()` - magnitude: sqrt(x^2 + y^2)
- `__eq__()` - equal if both components are equal
- `dot(other)` - dot product: x1*x2 + y1*y2

## Example run

```
v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

v1:          Vector2D(3, 4)
v2:          Vector2D(1, 2)
v1 + v2:     Vector2D(4, 6)
v1 - v2:     Vector2D(2, 2)
v1 * 3:      Vector2D(9, 12)
-v1:         Vector2D(-3, -4)
|v1|:        5.0
v1.dot(v2):  11
v1 == v2:    False
```

## Topics

- Arithmetic dunder methods
- `__abs__` for magnitude
- `__neg__` for negation
- `dot()` as a regular method

---
## Instructor notes

**Learning objectives covered:** arithmetic dunders, __abs__, __neg__, dot product

**Why Vector2D:** Vectors have natural arithmetic that maps directly to dunder
methods. The result is always a new Vector2D which reinforces immutability
patterns. `__abs__` is particularly elegant - `abs(v)` for magnitude.

**Extension:** Add `normalize()` that returns a unit vector (divide each
component by the magnitude).
