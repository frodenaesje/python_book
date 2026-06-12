# file: ex_12_02_unit_converter_start.py
import tkinter as tk
from tkinter import ttk

KM_PER_MILE = 1.60934

root = tk.Tk()
root.title("Unit Converter")
root.resizable(False, False)

# TODO: Create StringVar for km and miles fields
# sv_km    = tk.StringVar()
# sv_miles = tk.StringVar()

# TODO: Create StringVar for decimal places (default "2")
# sv_decimals = tk.StringVar(value="2")

updating = False  # prevents recursive updates

def km_changed(*args):
    # TODO: if updating, return
    # TODO: set updating = True
    # TODO: try to read sv_km as float, compute miles, set sv_miles
    # TODO: on ValueError: clear sv_miles
    # TODO: set updating = False
    pass

def miles_changed(*args):
    # TODO: same pattern, opposite direction
    pass

# TODO: attach km_changed to sv_km with trace_add("write", km_changed)
# TODO: attach miles_changed to sv_miles

# --- Layout ---
# TODO: Label "km", Entry for km, Label "miles", Entry for miles
#       Use grid() with row=0, columns 0-3

# TODO: Label "Decimals (1-5):", Entry connected to sv_decimals, on row=1
#       When sv_decimals changes, retrigger km_changed via trace_add

root.mainloop()
