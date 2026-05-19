# file: sc_12_09_canvas_demo.py
import tkinter as tk
from tkinter import ttk
import random

class CanvasDemo:
    def __init__(self, root):
        self.root = root
        self.canvas_width = 500
        self.canvas_height = 350
        self.root.title("Canvas demo")
        self.root.resizable(False, False)
    
        # Size selection
        self.size_var = tk.StringVar(value="Medium")
        size_frame = ttk.LabelFrame(root, text="Size")
        size_frame.pack(padx=10, pady=5, fill="x")
        rb_small = ttk.Radiobutton(
            size_frame, text="Small",
            variable=self.size_var, value="Small")
        rb_medium = ttk.Radiobutton(
            size_frame, text="Medium",
            variable=self.size_var, value="Medium")
        rb_large = ttk.Radiobutton(
            size_frame, text="Large",
            variable=self.size_var, value="Large")
        rb_small.pack(side="left", padx=5)
        rb_medium.pack(side="left", padx=5)
        rb_large.pack(side="left", padx=5)

        # Button frame
        button_frame = ttk.Frame(root)
        button_frame.pack(padx=10, pady=5, fill="x")
        bt_rectangle = ttk.Button(
            button_frame, text="Rectangle",
            command=self.draw_rectangle)
        bt_oval = ttk.Button(
            button_frame, text="Oval",
            command=self.draw_oval)
        bt_triangle = ttk.Button(
            button_frame, text="Triangle",
            command=self.draw_triangle)
        bt_rectangle.pack(side="left", padx=5)
        bt_oval.pack(side="left", padx=5)
        bt_triangle.pack(side="left", padx=5)

        # Canvas
        self.canvas = tk.Canvas(
            root, width=self.canvas_width,
            height=self.canvas_height, bg="white")
        self.canvas.pack(padx=10, pady=10)

        # For selection and deletion
        self._select_rect = None
        self._start_x = None
        self._start_y = None

        self.canvas.bind("<Button-1>", self._on_canvas_click)
        self.canvas.bind("<B1-Motion>", self._on_canvas_drag)
        self.canvas.bind(
            "<ButtonRelease-1>", self._on_canvas_release)
    
    def _on_canvas_click(self, event):
        # Always start selection rectangle on click
        self._start_x = event.x
        self._start_y = event.y
        self._select_rect = self.canvas.create_rectangle(
            event.x, event.y, event.x, event.y,
            outline="red", dash=(2, 2))

    def _on_canvas_drag(self, event):
        # Update selection rectangle during drag
        if self._select_rect is not None:
            self.canvas.coords(
                self._select_rect,
                self._start_x, self._start_y,
                event.x, event.y)

    def _on_canvas_release(self, event):
        # Delete all shapes within the selection rectangle
        if self._select_rect is not None:
            x0, y0, x1, y1 = self.canvas.coords(
                self._select_rect)
            x_min, x_max = min(x0, x1), max(x0, x1)
            y_min, y_max = min(y0, y1), max(y0, y1)
            items = self.canvas.find_enclosed(
                x_min, y_min, x_max, y_max)
            for item in items:
                self.canvas.delete(item)
            self.canvas.delete(self._select_rect)
            self._select_rect = None
            self._start_x = None
            self._start_y = None

    def get_size(self):
        size = self.size_var.get()
        if size == "Small":
            return 40, 40
        elif size == "Medium":
            return 80, 80
        else:
            return 120, 120

    def draw_rectangle(self):
        w, h = self.get_size()
        x0 = random.randint(0, self.canvas_width - w)
        y0 = random.randint(0, self.canvas_height - h)
        x1, y1 = x0 + w, y0 + h
        self.canvas.create_rectangle(
            x0, y0, x1, y1,
            fill="lightblue", outline="black")

    def draw_oval(self):
        w, h = self.get_size()
        x0 = random.randint(0, self.canvas_width - w)
        y0 = random.randint(0, self.canvas_height - h)
        x1, y1 = x0 + w, y0 + h
        self.canvas.create_oval(
            x0, y0, x1, y1,
            fill="lightgreen", outline="black")

    def draw_triangle(self):
        w, h = self.get_size()
        # Ensure the entire triangle is within the canvas
        x0 = random.randint(0, self.canvas_width - w)
        # y0 is the bottom of the triangle.
        y0 = random.randint(h, self.canvas_height)
        points = [x0, y0, x0 + w, y0, x0 + w/2, y0 - h]
        self.canvas.create_polygon(
            points, fill="lightcoral", outline="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = CanvasDemo(root)
    root.mainloop()
