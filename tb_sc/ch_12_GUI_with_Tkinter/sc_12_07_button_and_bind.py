# file: sc_12_07_button_and_bind.py
import tkinter as tk

def on_button_click(event):
    print(f"Mouse click coordinates: x={event.x}, y={event.y}")

root = tk.Tk()
root.title("Bind example")
root.geometry("300x200")
bt_simple = tk.Button(root, text="Click me!")
bt_simple.pack()

# Uses bind instead of command
bt_simple.bind("<Button-1>", on_button_click)

root.mainloop()
