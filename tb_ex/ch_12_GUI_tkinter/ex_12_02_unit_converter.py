# file: ex_12_02_unit_converter.py
import tkinter as tk
from tkinter import ttk

KM_PER_MILE = 1.60934

root = tk.Tk()
root.title("Unit Converter")
root.resizable(False, False)

sv_km      = tk.StringVar()
sv_miles   = tk.StringVar()
sv_decimals = tk.StringVar(value="2")

updating = False

def get_decimals() -> int:
    try:
        return max(0, min(10, int(sv_decimals.get())))
    except ValueError:
        return 2

def km_changed(*args):
    global updating
    if updating: return
    updating = True
    try:
        km    = float(sv_km.get())
        miles = km / KM_PER_MILE
        sv_miles.set(f"{miles:.{get_decimals()}f}")
    except ValueError:
        sv_miles.set("")
    updating = False

def miles_changed(*args):
    global updating
    if updating: return
    updating = True
    try:
        miles = float(sv_miles.get())
        km    = miles * KM_PER_MILE
        sv_km.set(f"{km:.{get_decimals()}f}")
    except ValueError:
        sv_km.set("")
    updating = False

sv_km.trace_add("write", km_changed)
sv_miles.trace_add("write", miles_changed)
sv_decimals.trace_add("write", km_changed)

# Layout
fr = ttk.Frame(root, padding=10)
fr.grid()

ttk.Label(fr, text="km").grid(row=0, column=0, padx=5)
en_km = ttk.Entry(fr, textvariable=sv_km, width=12)
en_km.grid(row=0, column=1, padx=5)

ttk.Label(fr, text="miles").grid(row=0, column=2, padx=5)
en_miles = ttk.Entry(fr, textvariable=sv_miles, width=12)
en_miles.grid(row=0, column=3, padx=5)

ttk.Label(fr, text="Decimals (1-5):").grid(row=1, column=0, pady=10)
ttk.Entry(fr, textvariable=sv_decimals, width=4).grid(row=1, column=1, sticky="w")

en_km.focus()
root.mainloop()
