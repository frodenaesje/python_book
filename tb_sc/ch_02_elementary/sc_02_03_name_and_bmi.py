# file name: sc_02_03_name_and_bmi.py
from datetime import datetime

current_year = datetime.now().year
first_name = input("What is your name: ")
age = int(input("What is your age: "))
body_weight = float(input("What is your weight in kg: "))
body_height = float(input("What is your height in cm: "))

# Calculate BMI
bmi = body_weight / (body_height / 100) ** 2
birth_year = current_year - age

print("Hello,", first_name, "you were born in", birth_year)
print("Your BMI is:", round(bmi,2))
