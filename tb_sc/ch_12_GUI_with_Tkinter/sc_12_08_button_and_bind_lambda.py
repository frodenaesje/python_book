# file: sc_12_08_button_and_bind_lambda.py
import tkinter as tk

def on_button_click(text, a_list, event):
    print(f"Event: {event}")
    print(f"Text: {text}, List: {a_list}")
    print(f"Widget that was clicked: {event.widget}")
    print(f"Mouse click coordinates: x={event.x}, y={event.y}")
    a_list.append(a_list[-1] + 1)
    print("---")

root = tk.Tk()
root.title("Bind + Lambda Callback example")
root.geometry("400x100")
some_list = [1]

# Use bind instead of command
bt_simple = tk.Button(root, text="Click Me")
bt_simple.bind("<Button-1>", lambda event: on_button_click("Hello from bind", some_list, event))
bt_simple.pack(pady=10)

root.mainloop()