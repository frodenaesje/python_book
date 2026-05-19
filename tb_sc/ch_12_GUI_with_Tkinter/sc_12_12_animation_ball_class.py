# file: sc_12_12_animation_ball_class.py
import tkinter as tk
import random

class Ball:
    def __init__(self, canvas, color, size, dx, dy):
        self.canvas = canvas
        self.size = size
        self.dx = dx
        self.dy = dy
        self.id = canvas.create_oval(
            10, 90, 10+size, 90+size,
            fill=color)
    
    def move(self):
        self.canvas.move(self.id, self.dx, self.dy)
        x0, y0, x1, y1 = self.canvas.coords(self.id)
        # Bounce in x direction
        if x0 <= 0 or x1 >= int(self.canvas['width']):
            self.dx = -self.dx
        # Bounce in y direction
        if y0 <= 0 or y1 >= int(self.canvas['height']):
            self.dy = -self.dy

class BallAnimation:
    def __init__(self, root):
        self.canvas = tk.Canvas(
            root, width=400, height=200, bg="white")
        self.canvas.pack(padx=10, pady=10)
        # Example: random color, size and direction
        color = random.choice([
            "blue", "red", "green", "orange"
        ])
        size = random.randint(20, 50)
        dx = random.choice([-4, 4])
        dy = random.choice([-3, 3])
        self.ball = Ball(self.canvas, color, size, dx, dy)
        self.animate()

    def animate(self):
        self.ball.move()
        self.canvas.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Ball class with bounce in all directions")
    BallAnimation(root)
    root.mainloop()
