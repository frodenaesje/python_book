# File: sc_11_01_basic_file_handling.py
"""
Basic file operations: open, close, read (various methods), write (various methods)
This demonstrates the fundamental file operations using open() and close()
"""

print("=== WRITING FILES - DIFFERENT METHODS ===")

# 1. Write a new file (overwrites existing)
file = open('sample.txt', 'w')
file.write("Hello World!\n")
file.write("This is line 2.\n") 
file.write("This is line 3.")
file.close()
print("✓ Created sample.txt with write() method")

# Read back to verify
file = open('sample.txt', 'r')
content = file.read()
file.close()
print("Content of sample.txt after writing:")
print(content)
print(repr(content))

# 2. Write multiple lines at once
lines = ["First line\n", "Second line\n", "Third line\n"]
file = open('multi_lines.txt', 'w')
file.writelines(lines)
file.close()
print("✓ Created multi_lines.txt with writelines() method")

# Read back to verify
file = open('multi_lines.txt', 'r')
content = file.read()
file.close()
print("Content of multi_lines.txt after writing:")
print(content)
print(repr(content))

# 3. Append to existing file
file = open('sample.txt', 'a')
file.write("\nAppended line 4")
file.write("\nAppended line 5")
file.close()
print("✓ Appended to sample.txt")

print("\n=== READING FILES - DIFFERENT METHODS ===")

# 1. Read entire file at once
file = open('sample.txt', 'r')
content = file.read()
file.close()
print("1. Read entire file with read():")
print(content)
print(repr(content))


# 2. Read file line by line
print("\n2. Read line by line with readline():")
file = open('sample.txt', 'r')
line_number = 1
while True:
    line = file.readline()
    if not line:  # Empty string means end of file
        break
    print(f"Line {line_number}: {repr(line)}")
    line_number += 1
file.close()

# 3. Read all lines into a list
print("\n3. Read all lines with readlines():")
file = open('sample.txt', 'r')
lines = file.readlines()
file.close()
for i, line in enumerate(lines, 1):
    print(f"Line {i}: {repr(line)}")

# 4. Read specific number of characters
print("\n4. Read specific characters with read(n):")
file = open('sample.txt', 'r')
first_10_chars = file.read(10)
next_5_chars = file.read(5)
file.close()
print(f"First 10 characters: {repr(first_10_chars)}")
print(f"Next 5 characters: {repr(next_5_chars)}")

# 5. Iterate over file object (most Pythonic)
print("\n5. Iterate over file object (recommended):")
file = open('sample.txt', 'r')
for line_num, line in enumerate(file, 1):
    print(f"Line {line_num}: {line.rstrip()}")  # rstrip() removes newline
file.close()

print("\n=== READING AND WRITING DIFFERENT FILE MODES ===")

# Text mode vs Binary mode
print("6. Text mode (default):")
file = open('sample.txt', 'r')  # 'r' is text mode
content = file.read()
file.close()
print(f"Type: {type(content)}, Length: {len(content)} characters")

print("\n7. Binary mode:")
file = open('sample.txt', 'rb')  # 'rb' is binary mode
content = file.read()
file.close()
print(f"Type: {type(content)}, Length: {len(content)} bytes")
print(f"First 20 bytes: {content[:20]}")

# Reading with encoding specification
print("\n8. Specify encoding explicitly:")
file = open('sample.txt', 'r', encoding='utf-8')
content = file.read()
file.close()
print(f"Read with UTF-8 encoding: {len(content)} characters")

print("\n=== FILES CREATED FOR DEMONSTRATION ===")
print("Files created: sample.txt, multi_lines.txt")
print("Use sc_11_02_examining_file_object.py to examine file object properties.")
