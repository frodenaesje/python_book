# file: sc_12_03_config_vs_index.py
import tkinter as tk

root = tk.Tk()
root.title("Two ways to change widgets")
root.geometry("300x100")
# Label 1 – changed with config()
label_config = tk.Label(root, text="Label with config", fg="black")
label_config.pack(pady=5)

# Label 2 – changed with index
label_index = tk.Label(root, text="Label with index", fg="black")
label_index.pack(pady=5)

# Change Label 1 with config()
label_config.config(text="Changed with config()", fg="blue")

# Change Label 2 with option dictionary (index)
label_index["text"] = "Changed with index"
label_index["fg"] = "green"

root.mainloop()
