# file: sc_03_03_to_decimal.py

# Convert from binary to decimal
# Starting point: a string representing a bit pattern
# Technique: extract digit by digit and multiply by the base
# raised to the power of the digit's position

binary_string = "1010101101101"
result = 0

pos = len(binary_string) - 1 # The exponent for the current digit
for ch in binary_string:
    result = result + int(ch) * 2** pos
    pos -= 1

print(result) # 5485

# Convert from hex to decimal
# Starting point: a string representing a hex number
# Technique: extract digit by digit and multiply by the base
# raised to the power of the digit's position

hex_string = "156D"
result = 0

pos = len(hex_string) - 1 # The exponent for the current digit
for ch in hex_string:
    if (ch >= 'A' and ch <= 'F'):
        digit = (ord(ch) - ord('A') + 10)
    else:
        digit = int(ch)

    result = result + digit * 16 ** pos
    pos -= 1

print(result) # 5485