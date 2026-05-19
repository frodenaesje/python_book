# File: sc_11_02_examining_file_object.py
"""
File objects are fundamental in Python file handling, even in modern code!
This same file object is used with:
- Context managers: with open('file.txt') as file:
- Pathlib: Path('file.txt').open() 
- All file operations return the same type of file object

Understanding file object properties is essential for all file handling approaches.
"""

import os
from pathlib import Path

print("=== CURRENT WORKING DIRECTORY ===")
# Method 1: Using os module
current_dir_os = os.getcwd()
print(f"Current working directory (os.getcwd()): {current_dir_os}")

# Method 2: Using pathlib (modern approach)
current_dir_pathlib = Path.cwd()
print(f"Current working directory (Path.cwd()): {current_dir_pathlib}")

# Method 3: Using os.path for directory of this script
script_dir = os.path.dirname(os.path.abspath(__file__))
print(f"Directory of this script: {script_dir}")

# Method 4: Using pathlib for directory of this script  
script_dir_pathlib = Path(__file__).parent.absolute()
print(f"Directory of this script (pathlib): {script_dir_pathlib}")

print(f"Are they the same? {current_dir_os == str(current_dir_pathlib)}")

# Open a file for reading
file = open('sample.txt', 'r')

# Examine important file object properties
print("=== FILE OBJECT INFORMATION ===")
print(f"File name: {file.name}")
print(f"File mode: {file.mode}")
print(f"File encoding: {file.encoding}")
print(f"Is file closed: {file.closed}")
print(f"Is file readable: {file.readable()}")
print(f"Is file writable: {file.writable()}")
print(f"Is file seekable: {file.seekable()}")
print(f"Current position: {file.tell()}")

print("\n=== FILE CONTENT ===")
content = file.read()
print(content)

print(f"\n=== AFTER READING ===")
print(f"Current position after read: {file.tell()}")
print(f"Is file closed: {file.closed}")

file.close()
print(f"\n=== AFTER CLOSING ===")
print(f"Is file closed: {file.closed}")
# print(f"Position after close: {file.tell()}")  # This would raise an error

print("\n=== MODERN EQUIVALENTS ===")
print("# Same file object with context manager:")
print("with open('text.txt', 'r') as file:")
print("    print(file.name, file.mode)")
print()
print("# Same file object with pathlib:")
print("from pathlib import Path")
print("with Path('text.txt').open('r') as file:")
print("    print(file.name, file.mode)")

print("\n=== FILE POSITION CONTROL ===")
# Demonstrate file position manipulation
with open('text.txt', 'r') as file:
    print(f"Initial position: {file.tell()}")
    
    # Read first 10 characters
    data = file.read(10)
    print(f"Read: '{data}'")
    print(f"Position after reading 10 chars: {file.tell()}")
    
    # Move to beginning
    file.seek(0)
    print(f"Position after seek(0): {file.tell()}")
    
    # Read line by line
    line1 = file.readline()
    print(f"First line: '{line1.strip()}'")
    print(f"Position after readline: {file.tell()}")
    
    # Move to end
    file.seek(0, 2)  # 2 means from end
    print(f"File size (position at end): {file.tell()}")
