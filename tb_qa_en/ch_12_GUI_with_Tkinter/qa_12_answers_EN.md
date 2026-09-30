# Chapter 12 – Answer Key: Review Questions

## Understanding

**1. Event-driven programming**
In event-driven programming, events such as mouse clicks, key presses, timer events and other events determine which callbacks run. The program responds by calling the registered callbacks. Each callback executes ordinary Python statements; event-driven programming does not inherently mean parallel threads. In a regular sequential program, the written sequence of instructions determines the main flow.

**2. `mainloop()` and what happens without it**
`mainloop()` processes Tk events and dispatches callbacks. Without `mainloop()` or another mechanism that processes Tk events, a normal standalone Tkinter GUI cannot update and respond normally. Omitting `mainloop()` does not skip the remaining Python statements: they still execute, and the script ends when its remaining code finishes.

**3. `command` without parentheses**
`command=on_button_click` passes a function reference, a callable that Tkinter can invoke later when the button is activated. `command=on_button_click()` calls the function when that expression is evaluated and supplies its return value as the `command` option.

**4. `command` vs. `bind()`**
Use `command` for a widget's built-in action, such as activating a Button. Use `bind()` for a specified event, such as a key press or mouse movement, especially when the callback needs details from the event object. Examples include `<Button-1>`, `<KeyPress>` and `<Enter>`. A Button command receives no event argument, but the arguments supplied to command callbacks depend on the widget; not all command callbacks take no arguments.

**5. The event object**
The event object is passed automatically by Tkinter to callback functions registered with `bind()`. It contains details about the event — `event.x`/`event.y` for mouse coordinates, `event.widget` for the widget that triggered the event, `event.keysym` for the symbolic key name, and so on.

**6. Lambda and `command`/`bind()`**
A lambda is a small anonymous function. For a Button, `command=lambda: on_click("Hello", lista)` defers the call until the button is activated and forwards the chosen arguments. With `bind()`, `lambda event: on_click("Hello", lista, event)` receives the Event from Tkinter and forwards it with our arguments. The event is placed last here because that is what this `on_click` signature requires; it need not always be forwarded last.

**7. What is a closure, and how does it help the lambda?**
A closure retains access to bindings from an enclosing function's scope. An inner function can use those bindings later, even after the enclosing function has returned. It does not automatically copy or freeze their values. A lambda can form a closure in the same way as a function defined with `def`. However, a module-level lambda referring to a global list does not capture that name as a closure variable, and the literal `"Hello"` is not a captured variable.

**8. `pack()` vs. `grid()`**
`pack()` places widgets in sequence vertically or horizontally — simple and intuitive. `grid()` places widgets in rows and columns — better suited for forms and tables. The two cannot be mixed in the same container.

**9. `StringVar`, `IntVar` and `DoubleVar`**
`StringVar`, `IntVar` and `DoubleVar` provide observable Tk variables with string, integer and floating-point access. They connect application state to supported widget options such as `textvariable=`, `variable=` or `listvariable=`. An Entry is a two-way example: editing the Entry updates the variable, and writing the variable updates the displayed Entry value through Tk event processing. A Label can display a linked variable but is not an editable input. Ordinary Python variables have no automatic widget link.

**10. `trace_add("write", callback)`**
`trace_add("write", callback)` registers a callback for writes to the Tk variable, including writing the same value again. Writes may come from code or a linked widget. Tkinter passes three arguments: the variable name, an index (empty for a scalar variable), and the operation or mode (`"write"`). We can use `*args` or `*_` to accept these arguments without using them.

**11. `config()` vs. `itemconfig()` on Canvas**
`config()` changes properties of the Canvas widget itself (background colour, size, etc.). `itemconfig()` changes properties of one specific graphical object inside the canvas, identified by the ID returned when the object was created.

**12. Why we avoid `time.sleep()` in an animation callback on the GUI thread**
When `time.sleep()` runs in a Tkinter animation callback on the GUI thread, it blocks that thread while sleeping and prevents its event loop from processing events during the pause. `canvas.after(ms, callback)` schedules the callback for later without blocking the GUI thread. The callback runs when the delay has elapsed and the event loop can process it, so this is not an exact timing guarantee.

**13. Ball as a class vs. function-based**
With a class the Ball object owns its own state (`dx`, `dy`, `id`) as instance variables — no `global` needed. The `move()` method contains all the logic for movement and collision. It is easy to add more balls by creating more instances. The function-based variant is simpler for a single ball but scales poorly.

**14. Modal dialog boxes**
Modal dialog boxes block interaction with the main window until the user has closed them. We cannot click on or use the main window while the dialog is open.

**15. Always check the return value from dialog boxes**
Different dialog APIs represent cancellation or negative choices differently. Depending on the API, the result may be `None`, an empty string or `False`. Check the documented return value before using it. Ignoring the result may cause an error or unintended behavior, but does not necessarily raise an exception. For example, with `simpledialog.askstring`, `if result is not None:` excludes cancellation, while `if result:` also excludes an accepted empty string. For numeric input, zero can be a valid result and should not be confused with cancellation.

---

## Practical exercises

GUI programming differs from most other topics in this book on one important point: even the simplest meaningful program requires a window, widgets, callbacks and an event loop. It is difficult to create short, isolated tasks that can be solved in the REPL or in a few lines.

Practical tasks for this chapter can therefore be found among the exercises — they are deliberately chosen and sized to train the most important mechanisms from the chapter without becoming too extensive.
