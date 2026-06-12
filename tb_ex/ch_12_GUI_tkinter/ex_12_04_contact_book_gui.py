# file: ex_12_04_contact_book_gui.py
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from ex_11_05_json_contacts import load_contacts, save_contacts, add_contact, \
                                   remove_contact, search

root = tk.Tk()
root.title("Contact Book")
root.minsize(600, 400)

contacts     = {}
current_file = None

sv_status = tk.StringVar(value="No file loaded.")
sv_search = tk.StringVar()
sv_name   = tk.StringVar()
sv_phone  = tk.StringVar()
sv_email  = tk.StringVar()
sv_city   = tk.StringVar()

def refresh_list():
    lb_contacts.delete(0, "end")
    query = sv_search.get()
    shown = search(contacts, query) if query else contacts
    for name in sorted(shown):
        lb_contacts.insert("end", name)

def clear_fields():
    sv_name.set(""); sv_phone.set(""); sv_email.set(""); sv_city.set("")

def on_open():
    global contacts, current_file
    path = filedialog.askopenfilename(
        filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
    if not path: return
    contacts     = load_contacts(path)
    current_file = path
    refresh_list()
    sv_status.set(f"Loaded {len(contacts)} contacts from {path}")

def on_save():
    global current_file
    if not current_file:
        current_file = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
    if not current_file: return
    save_contacts(contacts, current_file)
    sv_status.set(f"Saved {len(contacts)} contacts to {current_file}")

def on_add():
    name = sv_name.get().strip()
    if not name:
        messagebox.showerror("Error", "Name cannot be empty.")
        return
    try:
        add_contact(contacts, name, sv_phone.get(), sv_email.get(), sv_city.get())
        refresh_list()
        clear_fields()
        sv_status.set(f"Added '{name}'.")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def on_remove():
    sel = lb_contacts.curselection()
    if not sel: return
    name = lb_contacts.get(sel[0])
    if messagebox.askyesno("Confirm", f"Remove '{name}'?"):
        remove_contact(contacts, name)
        refresh_list()
        clear_fields()
        sv_status.set(f"Removed '{name}'.")

def on_select(event):
    sel = lb_contacts.curselection()
    if not sel: return
    name = lb_contacts.get(sel[0])
    if name in contacts:
        info = contacts[name]
        sv_name.set(name)
        sv_phone.set(info.get("phone", ""))
        sv_email.set(info.get("email", ""))
        sv_city.set(info.get("city", ""))

def on_search(*args):
    refresh_list()

sv_search.trace_add("write", on_search)

# --- Layout ---
fr_main = ttk.Frame(root, padding=8)
fr_main.pack(fill="both", expand=True)

# Left: listbox + search
fr_left = ttk.Frame(fr_main)
fr_left.pack(side="left", fill="both", expand=True, padx=(0, 8))

ttk.Label(fr_left, text="Search:").pack(anchor="w")
ttk.Entry(fr_left, textvariable=sv_search).pack(fill="x")

sb = ttk.Scrollbar(fr_left)
sb.pack(side="right", fill="y")
lb_contacts = tk.Listbox(fr_left, yscrollcommand=sb.set)
lb_contacts.pack(fill="both", expand=True)
lb_contacts.bind("<<ListboxSelect>>", on_select)
sb.config(command=lb_contacts.yview)

# Right: form + buttons
fr_right = ttk.Frame(fr_main)
fr_right.pack(side="right", fill="y")

for i, (label, sv) in enumerate([("Name",  sv_name), ("Phone", sv_phone),
                                   ("Email", sv_email), ("City",  sv_city)]):
    ttk.Label(fr_right, text=label).grid(row=i, column=0, sticky="w", pady=3)
    ttk.Entry(fr_right, textvariable=sv, width=25).grid(row=i, column=1, padx=5)

fr_btns = ttk.Frame(fr_right)
fr_btns.grid(row=4, column=0, columnspan=2, pady=8)
ttk.Button(fr_btns, text="Add",    command=on_add).pack(side="left", padx=3)
ttk.Button(fr_btns, text="Remove", command=on_remove).pack(side="left", padx=3)
ttk.Button(fr_btns, text="Clear",  command=clear_fields).pack(side="left", padx=3)

fr_file = ttk.Frame(fr_right)
fr_file.grid(row=5, column=0, columnspan=2)
ttk.Button(fr_file, text="Open", command=on_open).pack(side="left", padx=3)
ttk.Button(fr_file, text="Save", command=on_save).pack(side="left", padx=3)

# Status bar
ttk.Label(root, textvariable=sv_status, relief="sunken", anchor="w"
          ).pack(fill="x", side="bottom", padx=2, pady=2)

root.mainloop()
