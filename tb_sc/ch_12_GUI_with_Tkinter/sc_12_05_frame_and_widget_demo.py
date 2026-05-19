# file: sc_12_05_frame_and_widget_demo.py
import tkinter as tk
from tkinter import ttk

# Hovedvindu
root = tk.Tk()
root.title("Tkinter Demo - Structured GUI")

# === Frame: Personal info ===
frm_personinfo = ttk.LabelFrame(root, text="Personal information", padding=10)
frm_personinfo.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# Name
lb_navn = ttk.Label(frm_personinfo, text="Name:")
lb_navn.grid(row=0, column=0, sticky="w")
ent_navn = ttk.Entry(frm_personinfo, width=30)
ent_navn.grid(row=0, column=1, pady=5)

# Address
lb_adresse = ttk.Label(frm_personinfo, text="Address:")
lb_adresse.grid(row=1, column=0, sticky="w")
ent_adresse = ttk.Entry(frm_personinfo, width=30)
ent_adresse.grid(row=1, column=1, pady=5)

# === Frame: Options ===
frm_valg = ttk.LabelFrame(root, text="Options", padding=10)
frm_valg.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

# Radiobuttons
rb_valg = tk.StringVar(value="A")

lb_radio = ttk.Label(frm_valg, text="Select a category:")
lb_radio.grid(row=0, column=0, sticky="w")

rb_a = ttk.Radiobutton(frm_valg, text="Flight + hotel", variable=rb_valg, value="A")
rb_a.grid(row=1, column=0, sticky="w")
rb_b = ttk.Radiobutton(frm_valg, text="Hotel only", variable=rb_valg, value="B")
rb_b.grid(row=2, column=0, sticky="w")
rb_c = ttk.Radiobutton(frm_valg, text="Flight only", variable=rb_valg, value="C")
rb_c.grid(row=3, column=0, sticky="w")
rb_d = ttk.Radiobutton(frm_valg, text="Neither", variable=rb_valg, value="C")
rb_d.grid(row=4, column=0, sticky="w")

# Checkbuttons
var_dag1 = tk.IntVar()
var_dag2 = tk.IntVar()
var_dag3= tk.IntVar()

lb_check = ttk.Label(frm_valg, text="Attending days:")
lb_check.grid(row=4, column=0, sticky="w")

cb_dag1 = ttk.Checkbutton(frm_valg, text="Day 1", variable=var_dag1)
cb_dag1.grid(row=5, column=0, sticky="w")
cb_dag2 = ttk.Checkbutton(frm_valg, text="Day 2", variable=var_dag2)
cb_dag2.grid(row=6, column=0, sticky="w")
cb_dag3 = ttk.Checkbutton(frm_valg, text="Day 3", variable=var_dag3)
cb_dag3.grid(row=7, column=0, sticky="w")

# === Submit button ===
def show_data():
    print("Name:", ent_navn.get())
    print("Address:", ent_adresse.get())
    print("Selected category:", rb_valg.get())
    print("Attending day 1:", var_dag1.get())
    print("Attending day 2:", var_dag2.get())
    print("Attending day 3:", var_dag3.get())

bt_submit = ttk.Button(root, text="Submit", command=show_data)
bt_submit.grid(row=2, column=0, pady=10)

# Start GUI
root.mainloop()
