# file: ex_12_03_base_converter_start.py
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Base Converter")

# StringVars for the three fields
sv_dec = tk.StringVar()
sv_bin = tk.StringVar()
sv_hex = tk.StringVar()

updating = False

# TODO: Write is_valid_binary(s) -> bool
# TODO: Write is_valid_hex(s) -> bool

# TODO: Write parse_decimal(s) -> tuple[bool, int|str]
#       returns (True, int) or (False, error_message)

# TODO: Write dec_changed(*args), bin_changed(*args), hex_changed(*args)
#       Each: if updating return; set updating=True; try to parse;
#             update other two fields; log the result or error;
#             set updating=False

# TODO: Attach trace_add("write", ...) to each StringVar

# --- Layout ---
# TODO: Frame with three rows: label + entry for each base
#       Use grid layout

# TODO: Text widget + Scrollbar for the log at the bottom

def log(message):
    # TODO: insert message into Text widget and scroll to end
    pass

root.mainloop()
