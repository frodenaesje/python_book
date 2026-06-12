# file: ex_03_02_decimal_to_base_start.py

number = int(input("Enter a positive integer: "))

# --- Part 1: decimal to binary ---

# TODO: Convert number to binary using only % and //
#       Hint: number % 2 gives the rightmost binary digit
#             number //= 2 removes that digit
#             Prepend each digit to build the result string
#             Stop when number becomes 0

# TODO: Print your manual result and verify with bin()
#       Example:
#       "Binary (manual):   1010101101101"
#       "Binary (built-in): 0b1010101101101"


# --- Part 2: decimal to hexadecimal ---

# TODO: Convert the original number to hexadecimal using only % and //
#       Hint: use 16 instead of 2
#             For digits 10-15, use "0123456789ABCDEF"[digit]
#             to get the correct hex character

# TODO: Print your manual result and verify with hex()
#       Example:
#       "Hexadecimal (manual):   156D"
#       "Hexadecimal (built-in): 0x156d"
