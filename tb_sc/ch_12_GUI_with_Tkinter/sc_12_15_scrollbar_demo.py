# file sc_12_15_scrollbar_demo.py
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Scrollbar-demo: Listbox, Text, Canvas")

fr_main = ttk.Frame(root)
fr_main.pack(fill="both", expand=True, padx=10, pady=10)

# --- Listbox med scrollbar ---
fr_listbox = ttk.Frame(fr_main)
fr_listbox.pack(side="left", fill="both", expand=True, padx=5)
lb_label = ttk.Label(fr_listbox, text="Listbox")
lb_label.pack()
sb_listbox = ttk.Scrollbar(fr_listbox, orient="vertical")
lbx_listbox = tk.Listbox(
    fr_listbox,
    yscrollcommand=sb_listbox.set,
    height=10)
sb_listbox.config(command=lbx_listbox.yview)
sb_listbox.pack(side="right", fill="y")
lbx_listbox.pack(side="left", fill="both", expand=True)
for i in range(30):
    lbx_listbox.insert(tk.END, f"Item {i+1}")

# --- Text med scrollbar ---
fr_text = ttk.Frame(fr_main)
fr_text.pack(side="left", fill="both", expand=True, padx=5)
lb_text = ttk.Label(fr_text, text="Text")
lb_text.pack()
sb_text = ttk.Scrollbar(fr_text, orient="vertical")
tx_text = tk.Text(
    fr_text,
    yscrollcommand=sb_text.set,
    width=18,
    height=10)
sb_text.config(command=tx_text.yview)
sb_text.pack(side="right", fill="y")
tx_text.pack(side="left", fill="both", expand=True)
for i in range(30):
    tx_text.insert(tk.END, f"Line {i+1}\n")

# --- Canvas med scrollbar ---
fr_canvas = ttk.Frame(fr_main)
fr_canvas.pack(side="left", fill="both", expand=True, padx=5)
lb_canvas = ttk.Label(fr_canvas, text="Canvas")
lb_canvas.pack()
sb_canvas = ttk.Scrollbar(fr_canvas, orient="vertical")
cv_canvas = tk.Canvas(
    fr_canvas,
    width=120,
    height=160,
    bg="white",
    yscrollcommand=sb_canvas.set)
sb_canvas.config(command=cv_canvas.yview)
sb_canvas.pack(side="right", fill="y")
cv_canvas.pack(side="left", fill="both", expand=True)
cv_canvas.create_rectangle(10, 10, 100, 400, fill="lightblue")
cv_canvas.create_text(
    60, 200,
    text="Scroll me!",
    font=("Arial", 12))
cv_canvas.config(scrollregion=cv_canvas.bbox("all"))

root.mainloop()
