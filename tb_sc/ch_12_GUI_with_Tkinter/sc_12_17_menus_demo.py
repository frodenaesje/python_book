# file: sc_12_17_menus_demo.py

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def create_gui():
    root = tk.Tk()
    root.title("Menus - Demo")
    
    # Text widget for demonstrating menu actions
    fr_main = ttk.Frame(root, padding=10)
    fr_main.pack(fill="both", expand=True)
    
    lb_info = ttk.Label(fr_main, text="Try the menu bar above, or right-click the text area below:", 
                        font=("Arial", 10))
    lb_info.pack(pady=(0, 5))
    
    tx_text = tk.Text(fr_main, width=50, height=15, wrap="word")
    tx_text.pack(fill="both", expand=True)
    tx_text.insert("1.0", "This is a text editor demo.\n\n"
                          "Use the File menu to create new documents or exit.\n"
                          "Use the Edit menu to cut, copy, paste, or select all.\n"
                          "Right-click anywhere in this text to see a popup menu.\n\n"
                          "Try keyboard shortcuts:\n"
                          "- Ctrl+N for New\n"
                          "- Ctrl+X for Cut\n"
                          "- Ctrl+C for Copy\n"
                          "- Ctrl+V for Paste\n"
                          "- Ctrl+A for Select All")
    
    # --- Menu Bar ---
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    
    # File menu
    menu_file = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=menu_file)
    
    def new_file():
        if messagebox.askyesno("New File", "Clear the current text?"):
            tx_text.delete("1.0", tk.END)
            tx_text.insert("1.0", "New document...")
    
    def open_file():
        messagebox.showinfo("Open", "Open file dialog would appear here.")
    
    def save_file():
        content = tx_text.get("1.0", tk.END)
        messagebox.showinfo("Save", f"Would save {len(content)} characters.")
    
    def exit_app():
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            root.quit()
    
    menu_file.add_command(label="New", command=new_file, accelerator="Ctrl+N")
    menu_file.add_command(label="Open...", command=open_file, accelerator="Ctrl+O")
    menu_file.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
    menu_file.add_separator()
    menu_file.add_command(label="Exit", command=exit_app, accelerator="Ctrl+Q")
    
    # Edit menu
    menu_edit = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Edit", menu=menu_edit)
    
    def cut_text():
        try:
            tx_text.event_generate("<<Cut>>")
        except:
            pass
    
    def copy_text():
        try:
            tx_text.event_generate("<<Copy>>")
        except:
            pass
    
    def paste_text():
        try:
            tx_text.event_generate("<<Paste>>")
        except:
            pass
    
    def select_all():
        tx_text.tag_add("sel", "1.0", "end-1c")
        tx_text.mark_set("insert", "1.0")
        tx_text.see("insert")
        return "break"
    
    menu_edit.add_command(label="Cut", command=cut_text, accelerator="Ctrl+X")
    menu_edit.add_command(label="Copy", command=copy_text, accelerator="Ctrl+C")
    menu_edit.add_command(label="Paste", command=paste_text, accelerator="Ctrl+V")
    menu_edit.add_separator()
    menu_edit.add_command(label="Select All", command=select_all, accelerator="Ctrl+A")
    
    # Help menu
    menu_help = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=menu_help)
    
    def show_about():
        messagebox.showinfo("About", "Menu Demo Application\n\nDemonstrates menu bars and popup menus in Tkinter.")
    
    menu_help.add_command(label="About", command=show_about)
    
    # --- Keyboard shortcuts (bindings) ---
    root.bind("<Control-n>", lambda e: new_file())
    root.bind("<Control-o>", lambda e: open_file())
    root.bind("<Control-s>", lambda e: save_file())
    root.bind("<Control-q>", lambda e: exit_app())
    root.bind("<Control-a>", lambda e: select_all())
    
    # --- Popup/Context Menu ---
    popup_menu = tk.Menu(root, tearoff=0)
    popup_menu.add_command(label="Cut", command=cut_text)
    popup_menu.add_command(label="Copy", command=copy_text)
    popup_menu.add_command(label="Paste", command=paste_text)
    popup_menu.add_separator()
    popup_menu.add_command(label="Select All", command=select_all)
    
    def show_popup(event):
        try:
            popup_menu.tk_popup(event.x_root, event.y_root)
        finally:
            popup_menu.grab_release()
    
    tx_text.bind("<Button-3>", show_popup)  # Right-click (Windows/Linux)
    tx_text.bind("<Button-2>", show_popup)  # Middle-click (some systems)
    
    return root


if __name__ == "__main__":
    app = create_gui()
    app.mainloop()
