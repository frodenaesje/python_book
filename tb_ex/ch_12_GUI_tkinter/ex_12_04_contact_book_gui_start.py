# file: ex_12_04_contact_book_gui_start.py
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from ex_11_05_json_contacts import load_contacts, save_contacts, add_contact, \
                                   remove_contact, search

root = tk.Tk()
root.title("Contact Book")
root.minsize(600, 400)

contacts = {}           # the in-memory contact dict
current_file = None     # path of the currently open file

sv_status  = tk.StringVar(value="No file loaded.")
sv_search  = tk.StringVar()
sv_name    = tk.StringVar()
sv_phone   = tk.StringVar()
sv_email   = tk.StringVar()
sv_city    = tk.StringVar()

# TODO: Write refresh_list() - clears and repopulates the Listbox
#       If sv_search is not empty, show only matching contacts

# TODO: Write on_open() - use filedialog.askopenfilename() to pick a .json file
#       Load with load_contacts(), refresh the list, update sv_status

# TODO: Write on_save() - use filedialog.asksaveasfilename() if no current_file
#       Save with save_contacts(), update sv_status

# TODO: Write on_add() - read the four StringVars, call add_contact()
#       Show messagebox.showerror on ValueError, refresh list

# TODO: Write on_remove() - get selected name from Listbox
#       Confirm with messagebox.askyesno(), call remove_contact(), refresh list

# TODO: Write on_select(event) - when user clicks Listbox, populate the fields
#       with the selected contact's data

# TODO: Write on_search(*args) - trace sv_search to filter in real time

sv_search.trace_add("write", lambda *a: None)  # TODO: connect to on_search

# --- Layout ---
# TODO: Left side: Listbox + search entry
# TODO: Right side: form fields (name, phone, email, city) + buttons
# TODO: Bottom: status bar label

root.mainloop()
