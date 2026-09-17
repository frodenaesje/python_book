# file: sc_02_12_input_patterns.py

name = input("What is your name? ")
age = int(input("What is your age? "))
weight = float(input("What is your weight in kg? "))

age_text = input("What is your age? ")
age = int(age_text)

city = input("Which city do you live in? ").strip()
print(city)

answer = input("Do you want to continue? ").strip().lower()
print(answer)

first_name, last_name = input("Enter first and last name: ").split()
print(first_name, last_name)
