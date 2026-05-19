import tkinter as tk

def show_label_properties():
    properties = label.configure()
    text_field.delete("1.0", tk.END)
    for name, value in properties.items():
        current_value = value[-1]  # Last element is the current value
        text_field.insert(tk.END, f"{name}: {current_value}
")

root = tk.Tk()
root.title("Label properties with configure()")

label = tk.Label(root, text="Sample text", fg="blue", bg="white", font=("Arial", 12))
label.pack(pady=10)

button = tk.Button(root, text="Show properties", command=show_label_properties)
button.pack(pady=5)

text_field = tk.Text(root, width=50, height=15)
text_field.pack(padx=10, pady=10)

root.mainloop()