# file: sc_02_08_print_parameters.py

# Default output - space between arguments
print("Hello", 42, 3.14, True)
# Output: Hello 42 3.14 True

# Change separator with sep
print("Hello", 42, 3.14, True, sep=", ")
# Output: Hello, 42, 3.14, True

# Change line ending with end
print("Hello", 42, 3.14, True, sep=", ", end=".")
print("next line")
# Output: Hello, 42, 3.14, True.next line

# String concatenation with +
print("Hello" + ", " + str(42) + ", " + str(3.14) + ", " + str(True))
# Output: Hello, 42, 3.14, True

# Arithmetic inside print()
print("The sum of 2 and 3 is", 2 + 3)
# Output: The sum of 2 and 3 is 5
