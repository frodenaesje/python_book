# file: ex_12_05_move_circle_start.py
import tkinter as tk
from tkinter import ttk

CANVAS_W = 400
CANVAS_H = 400
RADIUS   = 30

root = tk.Tk()
root.title("Move a Circle")

# TODO: Create Canvas, draw a circle in the centre with create_oval()
#       Store the item id: circle = canvas.create_oval(...)

# TODO: Entry for step size (default 10)
#       Label showing current position

def get_step():
    # TODO: read Entry value, return int (default 10 if invalid)
    return 10

def move(dx, dy):
    # TODO: get current bounding box with canvas.coords(circle)
    # TODO: clamp dx/dy so circle stays inside canvas
    # TODO: canvas.move(circle, dx, dy)
    # TODO: update position label
    pass

# TODO: Bind arrow keys to move()
#       root.bind("<Left>",  lambda e: move(-get_step(), 0))  etc.

# --- Part 2: RGB colour sliders ---
# TODO: Three Scale widgets for R, G, B (0-255)
# TODO: When any slider changes, compute hex colour and call
#       canvas.itemconfig(circle, fill=color)

root.mainloop()
