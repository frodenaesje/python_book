# file: ex_12_07_ball_animation_start.py
import tkinter as tk
from tkinter import ttk
import random

CANVAS_W = 500
CANVAS_H = 400
RADIUS   = 20
DELAY    = 16   # ms between frames (~60 fps)

root = tk.Tk()
root.title("Ball Animation")

canvas = tk.Canvas(root, width=CANVAS_W, height=CANVAS_H, bg="#1a1a2e")
canvas.pack()

balls  = []   # list of dicts: {"id": canvas_id, "vx": float, "vy": float}
paused = False

def add_ball():
    # TODO: pick random position (inside canvas, clear of edges)
    # TODO: pick random velocity (e.g. between -4 and 4, not zero)
    # TODO: create oval on canvas with random fill colour
    # TODO: append {"id": item_id, "vx": vx, "vy": vy} to balls
    pass

def update_ball(ball):
    # TODO: canvas.move(ball["id"], ball["vx"], ball["vy"])
    # TODO: get new position with canvas.coords()
    # TODO: if hitting left or right wall: reverse vx
    # TODO: if hitting top or bottom wall: reverse vy
    pass

def animate():
    # TODO: if not paused: update all balls, then root.after(DELAY, animate)
    pass

def toggle_pause():
    global paused
    # TODO: toggle paused, if resuming call animate()
    pass

# Controls
fr = ttk.Frame(root)
fr.pack(pady=6)

# TODO: Pause button connected to toggle_pause
# TODO: Speed Scale (affects velocity multiplier)
# TODO: Add ball button connected to add_ball
# TODO: Label showing number of balls

# Start with one ball
add_ball()
animate()

root.mainloop()
