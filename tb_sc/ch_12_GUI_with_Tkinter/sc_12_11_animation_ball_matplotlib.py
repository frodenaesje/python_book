import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random

class Ball:
    def __init__(self, ax, color, size, dx, dy):
        self.ax = ax
        self.size = size
        self.dx = dx
        self.dy = dy
        self.color = color
        self.x = 10 + size / 2
        self.y = 90 + size / 2
        self.width = ax.get_xlim()[1]
        self.height = ax.get_ylim()[1]
        self.circle = plt.Circle((self.x, self.y), size / 2, color=color)
        ax.add_patch(self.circle)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        # Bounce in x direction
        if self.x - self.size / 2 <= 0 or self.x + self.size / 2 >= self.width:
            self.dx = -self.dx
        # Bounce in y direction
        if self.y - self.size / 2 <= 0 or self.y + self.size / 2 >= self.height:
            self.dy = -self.dy
        self.circle.center = (self.x, self.y)

class BallAnimation:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(0, 400)
        self.ax.set_ylim(0, 200)
        self.ax.set_aspect('equal')
        self.ax.axis('off')
        color = random.choice(["blue", "red", "green", "orange"])
        size = random.randint(20, 50)
        dx = random.choice([-4, 4])
        dy = random.choice([-3, 3])
        self.ball = Ball(self.ax, color, size, dx, dy)

    def animate(self, frame):
        self.ball.move()
        return [self.ball.circle]

    def run(self):
        ani = animation.FuncAnimation(self.fig, self.animate, frames=200, interval=20, blit=True)
        plt.show()

if __name__ == "__main__":
    BallAnimation().run()
