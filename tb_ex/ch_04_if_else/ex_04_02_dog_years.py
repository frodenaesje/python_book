# file: ex_04_02_dog_years.py

human_years = float(input("Enter the dog's age in human years: "))

if human_years <= 0:
    print("Please enter a positive age.")
elif human_years <= 1:
    dog_years = human_years * 10.5
elif human_years <= 2:
    dog_years = 21.0
else:
    dog_years = 21.0 + (human_years - 2) * 4

print(f"The dog's age in dog years is {dog_years}.")
