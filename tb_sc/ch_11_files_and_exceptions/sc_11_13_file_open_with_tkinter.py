# File: sc_11_13_file_open_with_tkinter.py
"""
Simple file copy using tkinter file dialogs
- Open a file using askopenfilename()
- Save to another file using asksaveasfilename()
- Tkinter window is hidden and destroyed after use
"""

import tkinter as tk
from tkinter import filedialog

# Create root window and hide it
root = tk.Tk()
root.withdraw()  # Hide the main window

# Open file dialog to select source file
print("Select a file to open...")
source_file = filedialog.askopenfilename(
    title="Select file to open",
    filetypes=(("Text files", "*.txt"), ("Python files", "*.py"), ("All files", "*.*"))
)

if not source_file:
    print("No file selected for opening. Exiting.")
    root.destroy()
    exit()

print(f"Selected source file: {source_file}")

# Read content from source file
try:
    with open(source_file, 'r', encoding='utf-8') as file:
        content = file.read()
    print(f"Successfully read {len(content)} characters from source file.")
except Exception as e:
    print(f"Error reading file: {e}")
    root.destroy()
    exit()

# Save file dialog to select destination file
print("\nSelect where to save the file...")
dest_file = filedialog.asksaveasfilename(
    title="Save file as",
    defaultextension=".txt",
    filetypes=(("Text files", "*.txt"), ("Python files", "*.py"), ("All files", "*.*"))
)

if not dest_file:
    print("No destination file selected. Exiting.")
    root.destroy()
    exit()

print(f"Selected destination file: {dest_file}")

# Write content to destination file
try:
    with open(dest_file, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Successfully wrote {len(content)} characters to destination file.")
except Exception as e:
    print(f"Error writing file: {e}")
    root.destroy()
    exit()

# Clean up - destroy tkinter root window
root.destroy()

print("\n✓ File copy completed successfully!")
print(f"Copied from: {source_file}")
print(f"Copied to:   {dest_file}")
