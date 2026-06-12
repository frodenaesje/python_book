# file: ex_05_06_isbn10_start.py

# TODO: Read the first 9 digits as a string (not int - to preserve leading zeros)

# TODO: Calculate the checksum using enumerate()
#       Hint: for i, char in enumerate(digits):
#                 total += int(char) * (i + 1)
#       The weight for the first digit is 1, second is 2, ..., ninth is 9

# TODO: Determine the check character
#       If checksum == 10: check character is 'X'
#       Otherwise: check character is str(checksum)

# TODO: Print the complete ISBN-10 code
#       Example: "ISBN-10: 0201616220"
