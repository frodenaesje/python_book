---
title: "Contact Book GUI"
id: "ex_12_04_contact_book_gui"
tags: ["tkinter", "ttk", "Listbox", "filedialog", "messagebox", "StringVar", "json"]
difficulty: "medium"
prerequisites: ["tkinter", "ttk", "Listbox", "filedialog", "messagebox", "json"]
learning_outcomes:
  - "Connect a GUI to file I/O from chapter 11"
  - "Use filedialog to let the user choose a file"
  - "Use Listbox to display a collection of items"
  - "Use messagebox for confirmations and errors"
  - "Use StringVar for a status bar"
---

# Contact Book GUI

## Exercise

Build a GUI for the JSON contact book from exercise 11.05. The backend
functions (`load_contacts`, `save_contacts`, `add_contact`,
`remove_contact`, `search`) are already written - this exercise adds
a graphical front end.

Copy `ex_11_05_json_contacts.py` to this folder and import from it.

### Interface

- **Listbox** showing all contacts (name only)
- **Entry fields** for name, phone, email, city
- **Buttons:** Add, Remove, Clear fields
- **Menu or buttons:** Open file, Save file (using `filedialog`)
- **Search Entry** that filters the Listbox as the user types
- **Status bar** at the bottom using `StringVar`

### filedialog

Use `filedialog.askopenfilename()` to let the user choose which JSON
file to open. Use `filedialog.asksaveasfilename()` to choose where to
save. Filter for `*.json` files.

### messagebox

Use `messagebox.showerror()` for errors (duplicate name, not found).
Use `messagebox.askyesno()` to confirm before removing a contact.

## Example run

![Contact Book GUI](images/ex_12_04_contact_book_gui_01.png)

## Topics

- `filedialog.askopenfilename()` and `asksaveasfilename()`
- `messagebox.showerror()` and `askyesno()`
- `Listbox` with `insert()`, `delete()`, `curselection()`
- `StringVar` for status bar
- Connecting GUI to existing backend functions

---
## Instructor notes

**Learning objectives covered:** filedialog, messagebox, Listbox, StringVar
status bar, GUI/backend separation

**Architecture note:** The GUI is a thin layer on top of the backend.
The contacts dict lives in memory; the GUI just displays and modifies it.
This separation is the key design principle worth emphasising.

**Listbox selection pattern:**
```python
selection = lb_contacts.curselection()
if selection:
    name = lb_contacts.get(selection[0])
```

**filedialog filetypes:**
```python
filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
```
