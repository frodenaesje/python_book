# file: sc_12_05_frame_and_widget_demo.py
import tkinter as tk
from tkinter import ttk

# Main window
root = tk.Tk()
root.title("Tkinter Demo - Structured GUI")

# === Frame: Personal info ===
frm_personinfo = ttk.LabelFrame(root, text="Personal information", padding=10)
frm_personinfo.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# Name
lb_name = ttk.Label(frm_personinfo, text="Name:")
lb_name.grid(row=0, column=0, sticky="w")
ent_name = ttk.Entry(frm_personinfo, width=30)
ent_name.grid(row=0, column=1, pady=5)

# Address
lb_address = ttk.Label(frm_personinfo, text="Address:")
lb_address.grid(row=1, column=0, sticky="w")
ent_address = ttk.Entry(frm_personinfo, width=30)
ent_address.grid(row=1, column=1, pady=5)

# === Frame: Options ===
frm_options = ttk.LabelFrame(root, text="Options", padding=10)
frm_options.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

# Radiobuttons
rb_choice = tk.StringVar(value="A")

lb_radio = ttk.Label(frm_options, text="Select a category:")
lb_radio.grid(row=0, column=0, sticky="w")

rb_a = ttk.Radiobutton(frm_options, text="Flight + hotel", variable=rb_choice, value="A")
rb_a.grid(row=1, column=0, sticky="w")
rb_b = ttk.Radiobutton(frm_options, text="Hotel only", variable=rb_choice, value="B")
rb_b.grid(row=2, column=0, sticky="w")
rb_c = ttk.Radiobutton(frm_options, text="Flight only", variable=rb_choice, value="C")
rb_c.grid(row=3, column=0, sticky="w")
rb_d = ttk.Radiobutton(frm_options, text="Neither", variable=rb_choice, value="D")
rb_d.grid(row=4, column=0, sticky="w")

# Checkbuttons
var_day1 = tk.IntVar()
var_day2 = tk.IntVar()
var_day3= tk.IntVar()

lb_check = ttk.Label(frm_options, text="Attending days:")
lb_check.grid(row=5, column=0, sticky="w")

cb_day1 = ttk.Checkbutton(frm_options, text="Day 1", variable=var_day1)
cb_day1.grid(row=6, column=0, sticky="w")
cb_day2 = ttk.Checkbutton(frm_options, text="Day 2", variable=var_day2)
cb_day2.grid(row=7, column=0, sticky="w")
cb_day3 = ttk.Checkbutton(frm_options, text="Day 3", variable=var_day3)
cb_day3.grid(row=8, column=0, sticky="w")

# === Submit button ===
def show_data():
    print("Name:", ent_name.get())
    print("Address:", ent_address.get())
    print("Selected category:", rb_choice.get())
    print("Attending day 1:", var_day1.get())
    print("Attending day 2:", var_day2.get())
    print("Attending day 3:", var_day3.get())

bt_submit = ttk.Button(root, text="Submit", command=show_data)
bt_submit.grid(row=2, column=0, pady=10)

# Start GUI
root.mainloop()
