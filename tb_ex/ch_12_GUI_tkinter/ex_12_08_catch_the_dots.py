# file: ex_12_08_catch_the_dots.py
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

bx = CANVAS_W // 2
basket = canvas.create_rectangle(
    bx - BASKET_W//2, CANVAS_H - 40,
    bx + BASKET_W//2, CANVAS_H - 40 + BASKET_H,
    fill="#e9c46a", outline="white")

dot = None

def move_basket(dx):
    x1, y1, x2, y2 = canvas.coords(basket)
    if x1 + dx < 0:           dx = -x1
    if x2 + dx > CANVAS_W:    dx = CANVAS_W - x2
    canvas.move(basket, dx, 0)

def get_fall_speed():
    return 2 + state["score"] // 5

def new_dot():
    global dot
    if dot:
        canvas.delete(dot)
    x = random.randint(DOT_R + 5, CANVAS_W - DOT_R - 5)
    dot = canvas.create_oval(x - DOT_R, -DOT_R,
                              x + DOT_R,  DOT_R,
                              fill="#e63946", outline="white")

def check_collision():
    global dot
    if not dot: return
    bx1, by1, bx2, by2 = canvas.coords(basket)
    dx1, dy1, dx2, dy2 = canvas.coords(dot)

    if dx2 >= bx1 and dx1 <= bx2 and dy2 >= by1 - DOT_R:
        state["score"] += 1
        sv_score.set(f"Score: {state['score']}")
        new_dot()
    elif dy1 >= CANVAS_H:
        state["lives"] -= 1
        sv_lives.set("Lives: " + "o" * state["lives"])
        if state["lives"] <= 0:
            game_over()
        else:
            new_dot()

def game_loop():
    if not state["running"]: return
    if dot:
        canvas.move(dot, 0, get_fall_speed())
    check_collision()
    root.after(DELAY, game_loop)

def start_game():
    state["score"] = 0
    state["lives"] = 3
    state["running"] = True
    sv_score.set("Score: 0")
    sv_lives.set("Lives: ooo")
    canvas.delete("gameover")
    new_dot()
    game_loop()

def game_over():
    state["running"] = False
    canvas.create_text(CANVAS_W//2, CANVAS_H//2,
                       text=f"Game Over!\nScore: {state['score']}",
                       fill="white", font=("Calibri", 24, "bold"),
                       justify="center", tags="gameover")

root.bind("<Left>",  lambda e: move_basket(-BASKET_STEP))
root.bind("<Right>", lambda e: move_basket( BASKET_STEP))

fr = ttk.Frame(root)
fr.pack(pady=4)
ttk.Label(fr, textvariable=sv_score).pack(side="left", padx=10)
ttk.Label(fr, textvariable=sv_lives).pack(side="left", padx=10)
ttk.Button(fr, text="Start / Restart", command=start_game).pack(side="left", padx=10)

root.mainloop()
