# file: sc_12_13_entry_list_demo_v4.py

# This version demonstrates another way to structure the same GUI as
# sc_12_13_entry_list_demo.py, which uses nested callback functions.
# Standalone functions receive the widgets they need as arguments, keeping
# dependencies explicit and avoiding shared global widget variables.
# Each call to create_gui() keeps its own widgets local.
# Repeated argument lists make callback setup longer than in the other versions.

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def update_status(lbx_countries, status_var):
    status_var.set(
        f"Number of countries in the list: "
        f"{lbx_countries.size()}")


def add_country(en_entry, lbx_countries, status_var):
    """Add a valid, non-duplicate country from the entry."""
    text = en_entry.get().strip()
    if not text:
        # Empty string: do nothing (or show a small warning)
        messagebox.showinfo(
            "Info",
            "Enter a country name before adding.")
        return

    # Check for duplicate (case-insensitive)
    existing = [
        lbx_countries.get(i)
        for i in range(lbx_countries.size())
    ]
    if any(text.lower() == e.lower() for e in existing):
        messagebox.showinfo(
            "Info",
            f"'{text}' already exists in the list.")
        en_entry.delete(0, tk.END)
        return

    lbx_countries.insert(tk.END, text)
    en_entry.delete(0, tk.END)
    update_status(lbx_countries, status_var)


def remove_selected(lbx_countries, status_var):
    sel = lbx_countries.curselection()
    if not sel:
        messagebox.showinfo(
            "Info",
            "Select an item in the list to remove it.")
        return
    idx = sel[0]
    lbx_countries.delete(idx)
    update_status(lbx_countries, status_var)


def create_gui():
    root = tk.Tk()
    root.title("Listbox + Entry Demo")

    # Instruction text at the top
    lb_intro = tk.Label(
        root,
        text="Add a country by typing in the field "
             "and pressing 'Add'.")
    lb_intro.pack(padx=10, pady=(10, 0))

    # Frame for listbox + scrollbar
    fr_listbox = ttk.Frame(root)
    fr_listbox.pack(padx=10, pady=10, fill="both", expand=False)

    sb_scroll = ttk.Scrollbar(
        fr_listbox, orient=tk.VERTICAL)
    # The Listbox requests a default width of 20 characters.
    # fill=tk.BOTH lets it stretch to fill the available width in fr_listbox.
    lbx_countries = tk.Listbox(
        fr_listbox, height=8,
        yscrollcommand=sb_scroll.set,
        selectmode=tk.SINGLE)
    sb_scroll.config(command=lbx_countries.yview)
    sb_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    lbx_countries.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Pre-filled countries (partial list)
    initial_countries = [
        "England",
        "Sweden",
        "China",
        "India",
        "Iceland",
        "Germany",
        "France",
    ]
    for c in initial_countries:
        lbx_countries.insert(tk.END, c)

    # Status field showing number of elements
    status_var = tk.StringVar()

    update_status(lbx_countries, status_var)

    lb_status = ttk.Label(
        root, textvariable=status_var, anchor="w")
    lb_status.pack(fill="x", padx=10)

    # Frame for entry + button for adding new countries
    fr_entry = ttk.Frame(root)
    fr_entry.pack(padx=10, pady=(6, 10), fill="x")

    en_entry = ttk.Entry(fr_entry)
    en_entry.pack(side=tk.LEFT, fill="x", expand=True)

    # command calls a function without arguments. lambda creates a small
    # function that passes our widgets when clicked, rather than calling
    # add_country immediately while the button is being created.
    bt_add = ttk.Button(
        fr_entry, text="Add",
        command=lambda: add_country(en_entry, lbx_countries, status_var))
    bt_add.pack(side=tk.RIGHT, padx=(6, 0))

    # Optional: button to remove selected item

    bt_remove = ttk.Button(
        root, text="Remove selected",
        command=lambda: remove_selected(lbx_countries, status_var))
    bt_remove.pack(padx=10, pady=(0, 10), anchor="e")

    # Keyboard bindings: Enter adds, Del removes
    # Unlike command, bind passes an event object. These lambdas accept it,
    # but only forward the widgets needed by our standalone functions.
    en_entry.bind(
        "<Return>",
        lambda event: add_country(en_entry, lbx_countries, status_var))
    lbx_countries.bind(
        "<Delete>",
        lambda event: remove_selected(lbx_countries, status_var))

    return root


if __name__ == "__main__":
    app = create_gui()
    app.mainloop()
