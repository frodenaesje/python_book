# file: sc_12_10_canvas_bind.py
import tkinter as tk

def on_canvas_click(event):
    # Find the ID of the nearest object to the event coordinates
    clicked_items = canvas.find_closest(event.x, event.y)
    if clicked_items:
        item_id = clicked_items[0]
        print(f"Selected nearest object with ID: {item_id}")
        # Change color of the nearest object
        canvas.itemconfig(item_id, fill="green")

root = tk.Tk()
root.title("Canvas with bind")
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Draw some shapes
rect_id = canvas.create_rectangle(50, 50, 150, 150, fill="red")
oval_id = canvas.create_oval(200, 50, 300, 150, fill="blue")

# Bind mouse click to canvas
canvas.bind("<Button-1>", on_canvas_click)

root.mainloop()