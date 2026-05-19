# file: sc_12_06_button_and_lambda.py
import tkinter as tk

def on_button_click(text, a_list):
    print(f"Text: {text}, List: {a_list}")
    a_list.append(a_list[-1] + 1)

root = tk.Tk()
root.title("Lambda Callback example")
root.geometry("400x50")

some_list = [1]
bt_simple = tk.Button(root, text="Click Me", command=lambda: on_button_click("Hello", some_list))
bt_simple.pack()

root.mainloop()