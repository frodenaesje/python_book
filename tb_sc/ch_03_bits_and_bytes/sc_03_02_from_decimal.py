# sc_03_02_from_decimal.py

# Convert decimal number to binary
# Starting point: a number (number) that is a regular int
# Technique: done by repeated % 2 and // 2 operations on number,
# build up the bit string character by character

number = 5485
result_str = ""

while number > 0:
    next_binary_digit = number % 2
    result_str = chr(next_binary_digit + ord('0')) + result_str
    number = number // 2
print(result_str) # 1010101101101

# Convert decimal number to hexadecimal
# Technique: done by repeated % 16 and // 16 operations on number
# NOTE: we must handle hex_digit >= 10 specially,
# it should become 'A' to 'F'
# Build up the hex string character by character

number = 5485
result_str = ""

while number > 0:
    next_hex_digit = number % 16
    if next_hex_digit < 10:
        result_str = chr(next_hex_digit + ord('0')) + result_str
    else:
        hex_char = chr((next_hex_digit - 10) + ord('A'))
        result_str = hex_char + result_str
    number = number // 16
print(result_str) # 156D