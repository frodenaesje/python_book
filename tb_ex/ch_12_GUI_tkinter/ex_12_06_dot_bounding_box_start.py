# file: ex_12_06_dot_bounding_box_start.py
import tkinter as tk
from tkinter import ttk

CANVAS_W = 500
CANVAS_H = 400

root = tk.Tk()
root.title("Dots and Bounding Box")

canvas = tk.Canvas(root, width=CANVAS_W, height=CANVAS_H, bg="white")
canvas.pack(pady=8)

dots = []   # list of (x, y) tuples

iv_size = tk.IntVar(value=8)   # dot radius
sv_info = tk.StringVar(value="Click to place dots.")

def on_click(event):
    # TODO: append (event.x, event.y) to dots
    # TODO: draw a filled circle at the click position (use iv_size for radius)
    # TODO: call redraw_bbox()
    # TODO: update sv_info label
    pass

def redraw_bbox():
    # TODO: if fewer than 2 dots, return
    # TODO: compute min_x, max_x, min_y, max_y from dots
    # TODO: canvas.delete("bbox") to remove previous rectangle
    # TODO: canvas.create_rectangle(min_x, min_y, max_x, max_y,
    #           outline="red", width=2, tags="bbox")
    pass

def clear():
    # TODO: clear dots list, canvas.delete("all"), reset sv_info
    pass

# TODO: canvas.bind("<Button-1>", on_click)

# Controls
fr = ttk.Frame(root)
fr.pack(pady=4)
ttk.Button(fr, text="Clear", command=clear).pack(side="left", padx=6)
ttk.Label(fr, text="Dot size:").pack(side="left")
ttk.Spinbox(fr, from_=2, to=30, textvariable=iv_size, width=4).pack(side="left", padx=4)
ttk.Label(root, textvariable=sv_info).pack(pady=4)

root.mainloop()
