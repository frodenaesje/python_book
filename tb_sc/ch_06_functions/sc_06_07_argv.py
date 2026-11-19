# file: sc_06_07_argv.py
import sys

print(sys.argv)

# sys.argv[0] is the script name or path used to launch the program.
# The Run button in VS Code typically launches it with its full path.
# Example output: ['C:/.../sc_06_07_argv.py']

# For the command below, first change to the script's folder in the terminal:
# python sc_06_07_argv.py Alice 30
# Output: ['sc_06_07_argv.py', 'Alice', '30']
# From another folder, supply the script's relative or full path instead.
# That path will then appear in sys.argv[0].
