# file: sc_11_06_pathlib-examples.py
from pathlib import Path

# The __file__ variable contains the path to the current
# script
print(f"The name of the python script being executed:\n"
      f"as Path object: {Path(__file__)}\n"
      f"as a string: {__file__}")

# A text file created from this script will be created
# in the current working directory. The current working
# directory can be found with Path.cwd()
print("The current working directory is:")
print(Path.cwd())

# create a text file and write some content to it
with open("example.txt", "w") as f:
    f.write("Hello, World!\nThis is a test file.\n"
            "Pathlib is great for file handling.")

# If we open the file without specifying a path, it
# will be opened in the current working directory
with open("example.txt", "r") as f:
    print("The absolute path to the file just created "
          "is:")
    print(Path(f.name).resolve())

# What if we want to create the file in the same
# directory as the script?
script_dir = Path(__file__).resolve()
script_dir = Path(__file__).resolve().parent
file_in_script_dir = script_dir / "example.txt"
with open(file_in_script_dir, "w") as f:
    f.write("This file is created in the script's "
            "directory:")
    print("The absolute path to the file just created "
          "is:")
    print(Path(file_in_script_dir).resolve())
    print(Path(file_in_script_dir)) # same as above

# An other way to concatenate paths is to use the
# joinpath() method
another_file_in_script_dir = script_dir.joinpath(
    "another_example.txt")
with open(another_file_in_script_dir, "w") as f:
    f.write("This is another file created in the "
            "script's directory using joinpath().")


# pathlib does not have methods for
# copying or moving files. We can use the shutil
# module for that
import shutil
copied_file_path = script_dir / "copied_example.txt"
shutil.copy(file_in_script_dir, copied_file_path)