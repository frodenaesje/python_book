# file: sc_12_11_ball_simple.py
import tkinter as tk

root = tk.Tk()
root.title("Simple ball animation")
root.geometry("420x220")
canvas = tk.Canvas(root, width=400, height=200, bg="white")
canvas.pack(padx=10, pady=10)

oval = canvas.create_oval(10, 90, 50, 130, fill="blue")
dx = 4

def animate():
    global dx
    canvas.move(oval, dx, 0)
    x0, _, x1, _ = canvas.coords(oval)
    if x0 <= 0 or x1 >= 400:
        dx = -dx
    canvas.after(20, animate)

animate()
root.mainloop()
