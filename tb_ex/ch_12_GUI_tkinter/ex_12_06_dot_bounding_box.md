---
title: "Dots and Bounding Box"
id: "ex_12_06_dot_bounding_box"
tags: ["tkinter", "Canvas", "mouse events", "bind", "Entry", "IntVar", "bounding box"]
difficulty: "medium"
prerequisites: ["tkinter", "Canvas", "bind()", "mouse events", "Entry"]
learning_outcomes:
  - "Handle mouse click events on a Canvas"
  - "Store and redraw a collection of points"
  - "Compute a bounding rectangle from min/max coordinates"
  - "Understand the difference between a bounding box and a convex hull"
---

# Dots and Bounding Box

## Exercise

Click on a Canvas to place dots. After each click, draw an axis-aligned
bounding rectangle around all the dots - the smallest rectangle with
sides parallel to the axes that contains every dot.

### Requirements

- Click to place a dot (filled circle, configurable size)
- After each click, redraw the bounding rectangle around all dots
- An Entry or Spinbox for dot size (default 8 pixels)
- A button to clear all dots
- A label showing the number of dots and the bounding box dimensions

### Computing the bounding box

The bounding box is simply:
- Left edge:   `min(x for x, y in dots)`
- Right edge:  `max(x for x, y in dots)`
- Top edge:    `min(y for x, y in dots)`
- Bottom edge: `max(y for x, y in dots)`

## Extension - The Convex Hull

The bounding rectangle always has its sides parallel to the axes. But
the tightest possible boundary around the dots is the **convex hull** -
the smallest convex polygon that contains all the points. Imagine
stretching a rubber band around all the dots and letting it snap tight.

Finding the convex hull is a classic computational geometry problem.
One approach is the **gift wrapping algorithm** (also called Jarvis march):

1. Start at the leftmost point (guaranteed to be on the hull)
2. From the current point, find the point that is most
   counter-clockwise relative to all other points
3. Add that point to the hull and repeat until back at the start

The gift wrapping algorithm runs in O(n*h) time where h is the number
of hull vertices. The more efficient **Graham scan** sorts the points
by angle and runs in O(n log n).

This is the kind of problem covered in depth in Part 2 of this book.
For now, understanding that the bounding box is a rough approximation
and the convex hull is the exact solution is enough.

## Example run

![Dot bounding box](images/ex_12_06_dot_bounding_box_01.png)

## Topics

- `canvas.bind("<Button-1>", on_click)` for mouse clicks
- `event.x, event.y` for click coordinates
- `min()` and `max()` over a list of tuples
- Redrawing with `canvas.delete("bbox")` and `canvas.create_rectangle()`
- Bounding box vs convex hull

---
## Instructor notes

**Learning objectives covered:** mouse events, min/max over points,
bounding box, convex hull concept

**Why this exercise:** It introduces computational geometry naturally,
through something visual and interactive. The bounding box is simple
enough to implement in one line, but the convex hull extension gives
students something to think about without requiring them to implement it.

**Redraw pattern:**
```python
canvas.delete("bbox")  # delete previous rectangle (tagged "bbox")
canvas.create_rectangle(min_x, min_y, max_x, max_y,
                        outline="red", width=2, tags="bbox")
```

**Convex hull discussion:** Ask students: if you have 100 random dots,
roughly how many will be on the convex hull? (Usually around 10-20,
the rest are inside.) This makes the O(n*h) complexity intuitive.
