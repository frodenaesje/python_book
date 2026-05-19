# Chapter 12 – Answer Key: Review Questions

## Understanding

**1. Event-driven programming**
In event-driven programming it is the user who controls the flow — the program waits for events such as mouse clicks and key presses and responds accordingly. This differs from sequential programming where the program itself controls what happens and in what order.

**2. `mainloop()` and what happens without it**
`mainloop()` starts Tkinter's event loop, which continuously monitors the event queue and calls registered callback functions. Without `mainloop()` the window is never shown and the program exits immediately.

**3. `command` without parentheses**
`command=on_button_click` sends the reference (address) of the function — Tkinter can call it later when the button is pressed. `command=on_button_click()` calls the function immediately at startup and sets `command` to the return value, not the function itself.

**4. `command` vs. `bind()`**
`command` is a simple parameter for widgets like Button, Checkbutton and Scale — it connects one specific action to the widget. `bind()` can be used on all widgets, gives access to the event object with details about the event (mouse coordinates, which key was pressed, etc.), and can handle many different event types such as `<Button-1>`, `<KeyPress>`, `<Enter>`.

**5. The event object**
The event object is passed automatically by Tkinter to callback functions registered with `bind()`. It contains details about the event — `event.x`/`event.y` for mouse coordinates, `event.widget` for the widget that triggered the event, `event.keysym` for the symbolic key name, and so on.

**6. Lambda and `command`/`bind()`**
Lambda lets us pass parameters to callback functions. `command=on_click` sends no parameters. `command=lambda: on_click("Hello", lista)` lets us pass our own values. With `bind()` we use `lambda event: on_click("Hello", lista, event)` to receive the event object and pass our own parameters alongside it.

**7. What is a closure, and how does it help the lambda?**
A closure arises when an inner function refers to variables from an outer function's scope and lives on after the outer function has finished. The inner function "remembers" those values. A lambda is a perfectly ordinary function and becomes a closure in exactly the same way — when it references names from the surrounding scope it captures them. In Tkinter, `lambda: on_click("Hello", lista)` remembers `"Hello"` and `lista` from the outer scope so they are available when the button is eventually pressed.

**8. `pack()` vs. `grid()`**
`pack()` places widgets in sequence vertically or horizontally — simple and intuitive. `grid()` places widgets in rows and columns — better suited for forms and tables. The two cannot be mixed in the same container.

**9. `StringVar`, `IntVar` and `DoubleVar`**
Tkinter variables are observable objects that can be connected directly to widgets via `textvariable=`, `variable=` or `listvariable=`. The connection is two-way: what the user types is automatically synchronised into the variable, and changes to the variable from code are immediately shown in the widget. Regular Python variables have no such connection to the GUI.

**10. `trace_add("write", callback)`**
`trace_add("write", callback)` registers a callback that is called automatically every time the variable changes — regardless of whether the change comes from code or from the user via a widget. Tkinter always passes three arguments: internal variable name, index and mode. We use `*args` or `*_` to accept them without using them.

**11. `config()` vs. `itemconfig()` on Canvas**
`config()` changes properties of the Canvas widget itself (background colour, size, etc.). `itemconfig()` changes properties of one specific graphical object inside the canvas, identified by the ID returned when the object was created.

**12. Why we must never use `time.sleep()` in a Tkinter animation**
`time.sleep()` blocks the entire Python thread including Tkinter's event loop — the window freezes and does not respond to user interaction. `canvas.after(ms, func)` schedules a call to `func` after `ms` milliseconds without blocking the event loop.

**13. Ball as a class vs. function-based**
With a class the Ball object owns its own state (`dx`, `dy`, `id`) as instance variables — no `global` needed. The `move()` method contains all the logic for movement and collision. It is easy to add more balls by creating more instances. The function-based variant is simpler for a single ball but scales poorly.

**14. Modal dialog boxes**
Modal dialog boxes block interaction with the main window until the user has closed them. We cannot click on or use the main window while the dialog is open.

**15. Always check the return value from dialog boxes**
The user can cancel a dialog by pressing Cancel or closing the window. In that case `None` or an empty string is returned. Without checking, the code that uses the return value will crash with `TypeError` or `AttributeError`.

---

## Practical exercises

GUI programming differs from most other topics in this book on one important point: even the simplest meaningful program requires a window, widgets, callbacks and an event loop. It is difficult to create short, isolated tasks that can be solved in the REPL or in a few lines.

Practical tasks for this chapter can therefore be found among the exercises — they are deliberately chosen and sized to train the most important mechanisms from the chapter without becoming too extensive.
