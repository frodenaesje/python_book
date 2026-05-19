# file: sc_12_16_dialogboxes_demo.py

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog

def create_gui():
    root = tk.Tk()
    root.title("Dialog Boxes - Demo")

    # Main frame
    fr_main = ttk.Frame(root, padding=10)
    fr_main.pack(fill="both", expand=True)

    # Title
    lb_title = ttk.Label(fr_main, text="Dialog Boxes in Tkinter", font=("Arial", 14, "bold"))
    lb_title.pack(pady=(0, 10))

    # Left and right frames
    fr_left = ttk.Frame(fr_main)
    fr_left.pack(side="left", fill="both", expand=True, padx=(0, 8))
    fr_right = ttk.Frame(fr_main)
    fr_right.pack(side="left", fill="both", expand=True)

    # --- Message boxes (left) ---
    lb_messages = ttk.Label(fr_left, text="Message boxes:", font=("Arial", 10, "bold"))
    lb_messages.pack(anchor="w", pady=(10, 5))


    def show_info():
        messagebox.showinfo("Information", "This is an information message.")

    bt_info = ttk.Button(fr_left, text="showinfo - Show info", command=show_info)
    bt_info.pack(fill="x", pady=2)

    def show_warning():
        messagebox.showwarning("Warning", "This is a warning!")

    bt_warning = ttk.Button(fr_left, text="showwarning - Show warning", command=show_warning)
    bt_warning.pack(fill="x", pady=2)

    def show_error():
        messagebox.showerror("Error", "This is an error message!")

    bt_error = ttk.Button(fr_left, text="showerror - Show error", command=show_error)
    bt_error.pack(fill="x", pady=2)


    # --- Question dialogs (left) ---
    lb_questions = ttk.Label(fr_left, text="Question dialogs:", font=("Arial", 10, "bold"))
    lb_questions.pack(anchor="w", pady=(10, 5))

    def ask_yes_no():
        result = messagebox.askyesno("Question", "Are you sure you want to continue?")
        if result:
            messagebox.showinfo("Result", "You chose: Yes")
        else:
            messagebox.showinfo("Result", "You chose: No")

    bt_yesno = ttk.Button(fr_left, text="askyesno - Yes/No question", command=ask_yes_no)
    bt_yesno.pack(fill="x", pady=2)

    def ask_yes_no_cancel():
        result = messagebox.askyesnocancel("Save?", "Do you want to save changes?")
        if result is True:
            messagebox.showinfo("Result", "You chose: Yes")
        elif result is False:
            messagebox.showinfo("Result", "You chose: No")
        else:
            messagebox.showinfo("Result", "You chose: Cancel")

    bt_yesnocancel = ttk.Button(fr_left, text="askyesnocancel - Yes/No/Cancel", command=ask_yes_no_cancel)
    bt_yesnocancel.pack(fill="x", pady=2)

    def ask_ok_cancel():
        result = messagebox.askokcancel("Confirm", "Do you want to delete this file?")
        if result:
            messagebox.showinfo("Result", "You chose: OK")
        else:
            messagebox.showinfo("Result", "You chose: Cancel")

    bt_okcancel = ttk.Button(fr_left, text="askokcancel - OK/Cancel", command=ask_ok_cancel)
    bt_okcancel.pack(fill="x", pady=2)


    # --- File dialogs (right) ---
    lb_files = ttk.Label(fr_right, text="File dialogs:", font=("Arial", 10, "bold"))
    lb_files.pack(anchor="w", pady=(10, 5))

    def open_file():
        filename = filedialog.askopenfilename(
            title="Select a file",
            filetypes=(("Text files", "*.txt"), ("Python files", "*.py"), ("All files", "*.*"))
        )
        if filename:
            messagebox.showinfo("File selected", f"You selected:\n{filename}")

    bt_open = ttk.Button(fr_right, text="askopenfilename - Open file", command=open_file)
    bt_open.pack(fill="x", pady=2)

    def save_file():
        filename = filedialog.asksaveasfilename(
            title="Save file as",
            defaultextension=".txt",
            filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
        )
        if filename:
            messagebox.showinfo("File saved", f"File saved as:\n{filename}")

    bt_save = ttk.Button(fr_right, text="asksaveasfilename - Save file", command=save_file)
    bt_save.pack(fill="x", pady=2)

    def select_directory():
        dirname = filedialog.askdirectory(title="Select a folder")
        if dirname:
            messagebox.showinfo("Folder selected", f"You selected:\n{dirname}")

    bt_directory = ttk.Button(fr_right, text="askdirectory - Select folder", command=select_directory)
    bt_directory.pack(fill="x", pady=2)

    # --- Simple input dialog (right) ---
    lb_input = ttk.Label(fr_right, text="Simple input:", font=("Arial", 10, "bold"))
    lb_input.pack(anchor="w", pady=(10, 5))

    def ask_string():
        result = simpledialog.askstring("Input", "What is your name?")
        if result:
            messagebox.showinfo("Result", f"Hello, {result}!")

    bt_string = ttk.Button(fr_right, text="askstring - Ask for text", command=ask_string)
    bt_string.pack(fill="x", pady=2)

    def ask_integer():
        result = simpledialog.askinteger("Input", "How old are you?", minvalue=0, maxvalue=120)
        if result is not None:
            messagebox.showinfo("Result", f"You are {result} years old.")

    bt_integer = ttk.Button(fr_right, text="askinteger - Ask for integer", command=ask_integer)
    bt_integer.pack(fill="x", pady=2)

    def ask_float():
        result = simpledialog.askfloat("Input", "How tall are you (in meters)?", minvalue=0.0, maxvalue=3.0)
        if result is not None:
            messagebox.showinfo("Result", f"You are {result} meters tall.")

    bt_float = ttk.Button(fr_right, text="askfloat - Ask for float", command=ask_float)
    bt_float.pack(fill="x", pady=2)

    return root

if __name__ == "__main__":
    app = create_gui()
    app.mainloop()
