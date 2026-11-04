# Registration Form

## Exercise

Build a small registration window with tkinter. It should
have:

- Entry fields for **name**, **email** and **age**, each
  with a label
- A **Register** button
- A list area (a `Listbox`) that shows everyone registered
  so far

When the user clicks **Register**, the program reads the
three fields, adds a line like `Alice (32) - alice@x.no` to
the list, and clears the fields so the next person can be
entered. If any field is empty, do nothing.

## Example

```
Name:  [ Alice        ]
Email: [ alice@x.no   ]
Age:   [ 32           ]
        [ Register ]
+---------------------------+
| Alice (32) - alice@x.no   |
| Bob (28) - bob@x.no       |
+---------------------------+
```

## Topics

- `Label` + `Entry` laid out with `grid`
- Reading `Entry` values via `StringVar` in a callback
- `Listbox.insert(tk.END, ...)` to append a row
- Clearing fields by setting the `StringVar` to `""`

## Assessment criteria

| Criterion | Description | Weight (%) |
|---|---|---:|
| Form layout | Create labelled name, email and age fields, a Register button and a Listbox using the stated Tkinter layout. | 30 |
| Registration callback | Read the fields when clicked and append the formatted registration to the existing Listbox contents. | 45 |
| Empty fields and reset | Do nothing when any field is empty and clear all three fields after a successful registration. | 25 |
| **Total** | | **100%** |
