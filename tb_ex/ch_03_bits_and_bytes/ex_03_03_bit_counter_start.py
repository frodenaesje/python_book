# file: ex_03_03_bit_counter_start.py

number = int(input("Enter a positive integer: "))

# TODO: Use bin() to get the binary representation and print it
#       Example: "Binary:        0b101010"

# TODO: Count the number of 1-bits using .count('1')
#       Hint: bin() returns a string like '0b101010' - count only in the
#             part after '0b', or count in the full string (0 never appears
#             as a bit in '0b', so counting the full string also works)
#       Example: "Number of 1-bits: 3"

# TODO: Check if number fits in one byte (0-255)
#       If yes: print the binary representation padded to 8 bits
#               Hint: strip '0b' from bin(), then use .zfill(8)
#               Example: "Padded to 8 bits: 00101010"
#       If no:  print a message saying it does not fit
#               Example: "300 does not fit in one byte (max 255)."
