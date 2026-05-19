# file: sc_12_14_itemconfig_demo.py
import tkinter as tk

def change_rectangle():
    canvas.itemconfig(
        rectangle_id, fill="orange", outline="black")

def change_background():
    canvas.config(bg="lightgray")

root = tk.Tk()
root.title("itemconfig() vs config()")
root.geometry("350x250")
canvas = tk.Canvas(root, width=300, height=150, bg="white")
canvas.pack(padx=10, pady=10)
canvas.update()

canvas_w = canvas.winfo_width()
canvas_h = canvas.winfo_height()
rect_w   = 100
rect_h   = 50

x0 = (canvas_w - rect_w) // 2
y0 = (canvas_h - rect_h) // 2

rectangle_id = canvas.create_rectangle(
    x0, y0, x0 + rect_w, y0 + rect_h,
    fill="blue", outline="black")

bt_object = tk.Button(
    root, text="Change rectangle (itemconfig)",
    command=change_rectangle)
bt_background = tk.Button(
    root, text="Change background (config)",
    command=change_background)
bt_object.pack(pady=(0, 5))
bt_background.pack(pady=(0, 10))

root.mainloop()

