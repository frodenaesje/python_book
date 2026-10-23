# file: sc_11_18_path_examples.py
from pathlib import Path

# __file__ contains the path to this Python script.
print(f"The module's __file__ variable printed as it is :\n{__file__}")

# Path creates a path object; resolve() returns an absolute path,
# following symbolic links to the files or directories they point to.
# A symbolic link provides another path to a file or directory without copying it.
p = Path(__file__).resolve()
cwd = Path.cwd().resolve()

# The current working directory (CWD) is used to interpret relative paths.
# It depends on how the program is started and may differ from the
# directory containing this script.

print("CWD:", cwd)

# The absolute path to this script, including its filename.
print("Absolute:", p)

# The relative path to this script
print("Relative:", p.relative_to(cwd))

# The filename without its extension, for example sc_11_18_path_examples.
print("Stem:", p.stem)

# The file extension, including the dot: .py.
print("Suffix:", p.suffix)

# The directory containing this script.
print("Parent:", p.parent)

# Path objects have their own methods for simple read and write operations
p = Path("example.txt")
p.touch() # Create an empty file
          # preserve its contents if it already exists.
# Write
p.write_text("This is a test.\n", encoding="utf-8")
# Read
content = p.read_text(encoding="utf-8")
print(content)

# Append using the Path object's open() method.
with p.open("a", encoding="utf-8") as f:
    f.write("Appended using p.open().\n")

# The built-in open() also accepts a Path object.
with open(p, "a", encoding="utf-8") as f:
    f.write("Appended using open(p).\n")

print(p.read_text(encoding="utf-8"))
