# file: ex_12_06_dot_bounding_box.py
import tkinter as tk
from tkinter import ttk

CANVAS_W = 500
CANVAS_H = 400

root = tk.Tk()
root.title("Dots and Bounding Box")

canvas = tk.Canvas(root, width=CANVAS_W, height=CANVAS_H, bg="white")
canvas.pack(pady=8)

dots   = []
iv_size = tk.IntVar(value=8)
sv_info = tk.StringVar(value="Click to place dots.")

def on_click(event):
    x, y = event.x, event.y
    dots.append((x, y))
    r = iv_size.get()
    canvas.create_oval(x - r, y - r, x + r, y + r,
                       fill="steelblue", outline="navy")
    redraw_bbox()
    if len(dots) >= 2:
        min_x = min(p[0] for p in dots)
        max_x = max(p[0] for p in dots)
        min_y = min(p[1] for p in dots)
        max_y = max(p[1] for p in dots)
        sv_info.set(f"Dots: {len(dots)}   Box: {max_x-min_x} x {max_y-min_y} pixels")
    else:
        sv_info.set(f"Dots: {len(dots)}")

def redraw_bbox():
    if len(dots) < 2:
        return
    min_x = min(p[0] for p in dots)
    max_x = max(p[0] for p in dots)
    min_y = min(p[1] for p in dots)
    max_y = max(p[1] for p in dots)
    canvas.delete("bbox")
    canvas.create_rectangle(min_x, min_y, max_x, max_y,
                             outline="red", width=2, tags="bbox")

def clear():
    dots.clear()
    canvas.delete("all")
    sv_info.set("Click to place dots.")

canvas.bind("<Button-1>", on_click)

fr = ttk.Frame(root)
fr.pack(pady=4)
ttk.Button(fr, text="Clear", command=clear).pack(side="left", padx=6)
ttk.Label(fr, text="Dot size:").pack(side="left")
ttk.Spinbox(fr, from_=2, to=30, textvariable=iv_size, width=4).pack(side="left", padx=4)
ttk.Label(root, textvariable=sv_info).pack(pady=4)

root.mainloop()
