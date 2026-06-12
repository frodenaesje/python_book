---
title: "Catch the Dots"
id: "ex_12_08_catch_the_dots"
tags: ["tkinter", "Canvas", "after", "keyboard", "collision", "game", "StringVar"]
difficulty: "medium"
prerequisites: ["tkinter", "Canvas", "after()", "keyboard events", "collision detection"]
learning_outcomes:
  - "Combine animation, keyboard input and collision detection"
  - "Implement a simple game loop with a score and lives system"
  - "Use after() with a game state to implement game over"
  - "Reset and restart a game without restarting the program"
---

# Catch the Dots

## Exercise

Build a simple game. A basket (rectangle) moves left and right at the
bottom of the screen. Dots fall from the top. The player catches dots
by moving the basket under them.

### Rules

- Dots fall from random horizontal positions at the top
- The player moves the basket left/right with arrow keys
- Catching a dot: +1 score
- Missing a dot (reaches the bottom): -1 life
- Start with 3 lives. Game over at 0 lives.
- Dots speed up as score increases
- New dot appears every second (or when the previous one is caught/missed)

### Interface

- Canvas for the game area
- Score and lives displayed with StringVar labels
- A Start/Restart button
- Game over message displayed on the canvas

## Example run

![Catch the dots](images/ex_12_08_catch_the_dots_01.png)

## Topics

- Game loop with `after()`
- Overlap/collision detection with `canvas.coords()`
- Game state: score, lives, running
- Keyboard movement with bounds checking
- Reset and restart

---
## Instructor notes

**Learning objectives covered:** game loop, collision detection, game state,
keyboard input, after()

**Collision detection:**
```python
bx1, by1, bx2, by2 = canvas.coords(basket)
dx1, dy1, dx2, dy2 = canvas.coords(dot)
if dx2 >= bx1 and dx1 <= bx2 and dy2 >= by1:
    # caught!
```

**Game state pattern:** Use a dict or module-level variables:
```python
state = {"score": 0, "lives": 3, "running": False}
```

**Speed progression:**
```python
fall_speed = 2 + state["score"] // 5
```

**Why this exercise:** Brings together almost everything from the chapter -
Canvas, after(), keyboard events, labels, buttons, StringVar - in a context
that is genuinely fun. Students also see how the concepts from the ball
animation (after() loop, movement, bounds) apply directly to a game.
