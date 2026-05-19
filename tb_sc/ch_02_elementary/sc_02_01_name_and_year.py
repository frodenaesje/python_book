# file name: sc_02_01_name_and_year.py
CURRENT_YEAR = 2025

# Ask the user for name and age
first_name = input("What is your name: ")
age = int(input("What is your age: "))

# Calculate the birth year
birth_year = CURRENT_YEAR - age

# Print greeting and birth year
print("Hello,", first_name, "you were born in", birth_year)
