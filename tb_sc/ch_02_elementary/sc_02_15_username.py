# file: sc_02_15_username.py
import random

first_name = input("First name: ").strip()
last_name = input("Last name: ").strip()
birth_year = input("Year of birth: ").strip()

first = first_name.lower()
last = last_name.lower()

username = (
    last[:3] + first[:3] + birth_year[-2:]
    + str(random.randint(10, 99))
)
email = f"{first}.{last}@student.example.org"
initials = first_name[0].upper() + last_name[0].upper()

print(
    f"Hello, {first_name.title()} "
    f"{last_name.title()} ({initials})!"
)
print(f"Username: {username}")
print(f"Email:    {email}")
