# Pythonic patterns – Chapter 12: GUI programming with Tkinter

## Callback without vs. with parentheses

| Beginner | Pythonic |
|----------|----------|
| `bt = tk.Button(root, command=on_click())` | `bt = tk.Button(root, command=on_click)` |

With parentheses the function is called immediately and its return value is used as `command`. Without parentheses the reference is passed — Tkinter calls it when the button is pressed.

## Passing parameters to a callback

| Beginner | Pythonic |
|----------|----------|
| `bt = tk.Button(root, command=on_click)`<br>`# No way to pass parameters` | `bt = tk.Button(root, command=lambda: on_click("Hello", lista))` |

Lambda creates a closure that remembers the parameters and passes them on when the button is pressed.

## `bind()` with and without lambda

| Beginner | Pythonic |
|----------|----------|
| `def on_click(event): ...`<br>`widget.bind("<Button-1>", on_click)` | `def on_click(text, event): ...`<br>`widget.bind("<Button-1>",`<br>`    lambda event: on_click("Hello", event))` |

Lambda receives the event from Tkinter and forwards it along with our own parameters. The event object is always passed last.

## `StringVar` and automatic updating

| Beginner | Pythonic |
|----------|----------|
| `def update():`<br>`    lb.config(text=f"Count: {lista.size()}")`<br>`# Must be called manually after each change` | `var = tk.StringVar()`<br>`lb = ttk.Label(root, textvariable=var)`<br>`var.set(f"Count: {lista.size()}")`<br>`# Label updates automatically` |

`textvariable` connects the label to the variable — `var.set()` updates the label without `config()`.

## `trace_add` for automatic calculation

| Beginner | Pythonic |
|----------|----------|
| `bt_calc = tk.Button(root, text="Calculate",`<br>`    command=calculate)` | `var.trace_add("write", calculate)`<br>`# No button needed` |

`trace_add()` calls `calculate()` automatically every time the variable changes — the user does not need to press anything.

## Animation — `time.sleep()` vs. `after()`

| Beginner | Correct |
|----------|---------|
| `def animate():`<br>`    canvas.move(ball, dx, 0)`<br>`    time.sleep(0.02)  # Freezes the GUI!`<br>`    animate()` | `def animate():`<br>`    canvas.move(ball, dx, 0)`<br>`    canvas.after(20, animate)  # Non-blocking` |

`time.sleep()` blocks the event loop and freezes the entire window. `after()` schedules the next call without blocking.

## Animation — `global` vs. class

| Beginner | Pythonic |
|----------|----------|
| `dx = 4`<br>`def animate():`<br>`    global dx`<br>`    dx = -dx` | `class Ball:`<br>`    def __init__(self, ...):`<br>`        self.dx = 4`<br>`    def move(self):`<br>`        self.dx = -self.dx` |

A class keeps state encapsulated without `global`. Easy to create multiple balls.

## `config()` vs. `itemconfig()` on Canvas

| Beginner | Pythonic |
|----------|----------|
| `canvas.config(fill="orange")`<br>`# Doesn't work — fill belongs to the object` | `canvas.config(bg="lightgray")  # the canvas itself`<br>`canvas.itemconfig(rect_id, fill="orange")  # the object` |

`config()` changes the Canvas widget. `itemconfig()` changes one specific object inside the canvas via the ID it received at creation.

## Scrollbar connection

| Beginner | Pythonic |
|----------|----------|
| `sb = ttk.Scrollbar(fr)`<br>`lbx = tk.Listbox(fr)`<br>`# Not connected — scrollbar doesn't work` | `sb = ttk.Scrollbar(fr, orient=tk.VERTICAL)`<br>`lbx = tk.Listbox(fr, yscrollcommand=sb.set)`<br>`sb.config(command=lbx.yview)` |

The connection requires two steps — both must be in place for Listbox and Scrollbar to be synchronised.

## Dialog box — check return value

| Beginner | Pythonic |
|----------|----------|
| `result = simpledialog.askstring("Input", "Name?")`<br>`label.config(text=f"Hello, {result}!")` | `result = simpledialog.askstring("Input", "Name?")`<br>`if result:`<br>`    label.config(text=f"Hello, {result}!")` |

The user can cancel — then `None` is returned. Without checking, `f"Hello, {result}!"` crashes with `TypeError`.
