# file: sc_12_13_entry_list_demo_v3.py

# This version demonstrates another way to structure the same GUI as
# sc_12_13_entry_list_demo.py, which uses nested callback functions.
# A class keeps the widgets and callback methods together in one object.

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class CountryListApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Listbox + Entry Demo")

        # Instruction text at the top
        lb_intro = tk.Label(
            self.root,
            text="Add a country by typing in the field "
                 "and pressing 'Add'.")
        lb_intro.pack(padx=10, pady=(10, 0))

        # Frame for listbox + scrollbar
        fr_listbox = ttk.Frame(self.root)
        fr_listbox.pack(padx=10, pady=10, fill="both", expand=False)

        sb_scroll = ttk.Scrollbar(
            fr_listbox, orient=tk.VERTICAL)
        # The Listbox requests a default width of 20 characters.
        # fill=tk.BOTH lets it stretch to fill the available width in fr_listbox.
        self.lbx_countries = tk.Listbox(
            fr_listbox, height=8,
            yscrollcommand=sb_scroll.set,
            selectmode=tk.SINGLE)
        sb_scroll.config(command=self.lbx_countries.yview)
        sb_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lbx_countries.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

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
            self.lbx_countries.insert(tk.END, c)

        # Status field showing number of elements
        self.status_var = tk.StringVar()

        self.update_status()

        lb_status = ttk.Label(
            self.root, textvariable=self.status_var, anchor="w")
        lb_status.pack(fill="x", padx=10)

        # Frame for entry + button for adding new countries
        fr_entry = ttk.Frame(self.root)
        fr_entry.pack(padx=10, pady=(6, 10), fill="x")

        self.en_entry = ttk.Entry(fr_entry)
        self.en_entry.pack(side=tk.LEFT, fill="x", expand=True)

        bt_add = ttk.Button(
            fr_entry, text="Add", command=self.add_country)
        bt_add.pack(side=tk.RIGHT, padx=(6, 0))

        # Optional: button to remove selected item

        bt_remove = ttk.Button(
            self.root, text="Remove selected",
            command=self.remove_selected)
        bt_remove.pack(padx=10, pady=(0, 10), anchor="e")

        # Keyboard bindings: Enter adds, Del removes
        self.en_entry.bind("<Return>", self.add_country)
        self.lbx_countries.bind("<Delete>", self.remove_selected)

    def update_status(self):
        self.status_var.set(
            f"Number of countries in the list: "
            f"{self.lbx_countries.size()}")

    def add_country(self, event=None):
        """Add a valid, non-duplicate country from the entry."""
        text = self.en_entry.get().strip()
        if not text:
            # Empty string: do nothing (or show a small warning)
            messagebox.showinfo(
                "Info",
                "Enter a country name before adding.")
            return

        # Check for duplicate (case-insensitive)
        existing = [
            self.lbx_countries.get(i)
            for i in range(self.lbx_countries.size())
        ]
        if any(text.lower() == e.lower() for e in existing):
            messagebox.showinfo(
                "Info",
                f"'{text}' already exists in the list.")
            self.en_entry.delete(0, tk.END)
            return

        self.lbx_countries.insert(tk.END, text)
        self.en_entry.delete(0, tk.END)
        self.update_status()

    def remove_selected(self, event=None):
        sel = self.lbx_countries.curselection()
        if not sel:
            messagebox.showinfo(
                "Info",
                "Select an item in the list to remove it.")
            return
        idx = sel[0]
        self.lbx_countries.delete(idx)
        self.update_status()


if __name__ == "__main__":
    app = CountryListApp()
    app.root.mainloop()
