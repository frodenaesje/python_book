# file name: sc_02_02_name_and_datetime.py
from datetime import datetime

# Get the current year
current_date = datetime.now()
current_year = current_date.year

# Ask the user for name and age
first_name = input("What is your name: ")
age = int(input("What is your age: "))

# Calculate the birth year
birth_year = current_year - age

# Print greeting and birth year
print("Hello,", first_name, "you were born in", birth_year)
