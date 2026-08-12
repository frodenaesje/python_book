# file: ex_03_05_rgb_color_start.py

# NOTE: The last part - finding the dominant color - uses if-elif-else,
# which we meet in Chapter 4. Everything above it is Chapter 3 material.
# Do the hex decoding now; return for the dominant-color step after
# Chapter 4, or do the whole exercise then.

color = input("Enter a hex color code: ")

# TODO: Remove the '#' if present
#       Hint: use .lstrip('#')

# TODO: Extract the red, green and blue components as two-character strings
#       using slicing: first two chars = red, next two = green, last two = blue

# TODO: Convert each component from hex string to decimal integer
#       Hint: int(hex_string, 16) converts a hex string to decimal

# TODO: Print the three components
#       Example:
#       "Red:   255"
#       "Green: 140"
#       "Blue:  0"

# TODO: Determine and print the dominant color   (Chapter 4: if-elif-else)
#       (the component with the highest value)
#       Example: "Dominant color: Red"
#       Hint: use if-elif to compare the three values
