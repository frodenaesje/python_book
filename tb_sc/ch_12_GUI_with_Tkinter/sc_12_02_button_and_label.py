# file: sc_12_02_button_and_label.py
import tkinter as tk

# Main window
root = tk.Tk()
root.title("Callback + Reset")
root.geometry("300x200")
# Default text for label
INSTRUCTION = "Click the button to get a message here."

# A Label where we display messages to the user.
lb_demo = tk.Label(root, text=INSTRUCTION)
lb_demo.pack(padx=10, pady=10)

def show_message():
    lb_demo.config(text="The button was clicked!")

def reset_message():
    lb_demo.config(text=INSTRUCTION)

# Button to show the message
bt_show = tk.Button(root, text="Show message", command=show_message)
bt_show.pack(padx=5, pady=5)

# Button to reset the message
bt_reset = tk.Button(root, text="Reset", command=reset_message)
bt_reset.pack(padx=5, pady=(0, 10))

root.mainloop()