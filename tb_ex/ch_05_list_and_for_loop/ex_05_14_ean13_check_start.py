# file: ex_05_14_ean13_check_start.py
# Extra exercise: EAN-13 check digit

code = input("Enter a 13-digit barcode: ").strip()

# TODO: Check the length and that every character is a digit from 0 to 9.
#       Report invalid input; calculate only when the input is valid.

# TODO: Use enumerate() and a loop over the first twelve digits.
#       Accumulate each digit multiplied by its position-dependent weight.

# TODO: Determine the check digit, including the case where it is zero.

# TODO: Compare with the supplied last digit and report the result.
#       If they differ, show both the supplied and expected digit.
