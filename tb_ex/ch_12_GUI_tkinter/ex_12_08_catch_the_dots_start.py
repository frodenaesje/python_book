# file: ex_12_08_catch_the_dots_start.py
import tkinter as tk
from tkinter import ttk
import random

CANVAS_W    = 400
CANVAS_H    = 500
BASKET_W    = 60
BASKET_H    = 15
DOT_R       = 12
BASKET_STEP = 20
DELAY       = 16

root = tk.Tk()
root.title("Catch the Dots")

canvas = tk.Canvas(root, width=CANVAS_W, height=CANVAS_H, bg="#1a1a2e")
canvas.pack()

sv_score = tk.StringVar(value="Score: 0")
sv_lives = tk.StringVar(value="Lives: ooo")

state = {"score": 0, "lives": 3, "running": False}

# TODO: Create basket rectangle near bottom of canvas
# TODO: Create first dot near top of canvas

def move_basket(dx):
    # TODO: move basket left/right, clamp to canvas bounds
    pass

def fall_speed():
    # TODO: return 2 + state["score"] // 5
    pass

def new_dot():
    # TODO: delete existing dot if any
    # TODO: create new dot at random x position, near top
    pass

def check_collision():
    # TODO: get coords of basket and dot
    # TODO: if dot overlaps basket: score += 1, new dot, update sv_score
    # TODO: if dot reaches bottom: lives -= 1, update sv_lives
    #         if lives == 0: game_over()
    #         else: new dot
    pass

def game_loop():
    if not state["running"]: return
    # TODO: move dot down by fall_speed()
    # TODO: check_collision()
    # TODO: root.after(DELAY, game_loop)
    pass

def start_game():
    # TODO: reset score, lives, StringVars
    # TODO: state["running"] = True
    # TODO: new_dot(), game_loop()
    # TODO: canvas.delete any game-over text
    pass

def game_over():
    state["running"] = False
    # TODO: display "Game Over! Score: X" text on canvas
    pass

root.bind("<Left>",  lambda e: move_basket(-BASKET_STEP))
root.bind("<Right>", lambda e: move_basket( BASKET_STEP))

fr = ttk.Frame(root)
fr.pack(pady=4)
ttk.Label(fr, textvariable=sv_score).pack(side="left", padx=10)
ttk.Label(fr, textvariable=sv_lives).pack(side="left", padx=10)
ttk.Button(fr, text="Start / Restart", command=start_game).pack(side="left", padx=10)

root.mainloop()
