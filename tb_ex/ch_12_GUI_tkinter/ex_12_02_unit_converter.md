---
title: "Unit Converter"
id: "ex_12_02_unit_converter"
tags: ["tkinter", "ttk", "Entry", "StringVar", "IntVar", "trace_add", "grid"]
difficulty: "easy"
prerequisites: ["tkinter", "ttk", "Entry", "StringVar", "trace_add", "grid"]
learning_outcomes:
  - "Use grid() to arrange widgets in rows and columns"
  - "Use StringVar and IntVar to link widgets to Python variables"
  - "Use trace_add() to react to variable changes without a button"
  - "Validate numeric input and show error messages in the GUI"
---

# Unit Converter

## Exercise

Build a live unit converter. When the user types in one field, the
other field updates immediately - no button needed.

Convert between kilometres and miles:
- 1 km = 0.621371 miles

### Part 1 - Basic converter

Two Entry fields side by side, labelled "km" and "miles".
When the user types in km, miles updates. When the user types in
miles, km updates. Use `StringVar` and `trace_add()`.

### Part 2 - Add a precision selector

Add a `StringVar` connected to a small `Entry` field that lets the
user type how many decimal places to display (1-5).
The result updates immediately as the user types.

## Example run

![Unit Converter](images/ex_12_02_unit_converter_01.png)

## Hint

Use a flag to prevent recursive updates:
```python
updating = False

def km_changed(*args):
    global updating
    if updating: return
    updating = True
    # ... update miles field ...
    updating = False
```

## Topics

- `grid(row=, column=, padx=, pady=)` layout
- `StringVar` with `textvariable=`
- `trace_add("write", callback)` for live updates
- `ttk.Scale` with `IntVar`
- Input validation with try-except

---
## Instructor notes

**Learning objectives covered:** grid, StringVar, trace_add, Scale, IntVar,
input validation

**Why StringVar over direct Entry.get():** StringVar can be traced - any
change to the variable automatically triggers a callback. Direct .get()
requires a button or bind() on each keystroke.

**Three StringVars, three traces:** All three variables - km, miles and
decimals - use trace_add. Changing the decimals field immediately updates
the result. This shows the power of the xxxVar pattern cleanly.

**The recursive update problem:** When km changes we update miles, which
triggers miles_changed, which updates km again - infinite loop. The
updating flag breaks the cycle. This is a genuine GUI programming pattern
worth teaching explicitly.
