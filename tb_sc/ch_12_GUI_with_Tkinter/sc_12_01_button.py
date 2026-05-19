# file: sc_12_01_button.py
import tkinter as tk

def on_button_click():
     print("The button was pushed!")

root = tk.Tk()
root.title("Callback-example")
root.geometry("300x200")
bt_simple = tk.Button(root, text="Click me!", command=on_button_click)
bt_simple.pack()

root.mainloop()