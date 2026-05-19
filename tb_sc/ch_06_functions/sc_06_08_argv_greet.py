# file: sc_06_08_argv_greet.py
import sys

if len(sys.argv) < 3:
    print(f"Usage: python {sys.argv[0]} <name> <age>")
    sys.exit(1)

name  = sys.argv[1]
age = int(sys.argv[2])
print(f"Hello, {name}! You are {age} years old.")
# Run as: python sc_06_08_argv_greet.py Alice 30, note: run from the same directory as the file
# Output:  Hello, Alice! You are 30 years old.