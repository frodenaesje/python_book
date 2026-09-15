# file: sc_07_05_tuple_unpacking.py

# --- Tuple unpacking ---
a, b = [1, 2]          # list
x, y = (3, 4)          # tuple
first, second = "AB"   # string

# --- Basic unpacking ---
# traditional way
coordinates = (10, 20)
x = coordinates[0]
y = coordinates[1]

# with unpacking - much cleaner
x, y = coordinates
print(f"x = {x}, y = {y}")  # x = 10, y = 20

# --- Return values from functions ---
def get_name_and_age():
    """Returns name and age as a tuple."""
    return "Anna", 25  # Python packs into a tuple automatically

name, age = get_name_and_age()
print(f"{name} is {age} years old")

# --- Ignoring values with _ ---
person_data = ("Anna", 25, "Engineer", "Oslo")
name, _, profession, _ = person_data  # _ ignores age and city
print(f"{name} works as {profession}")

# --- Starred expression * (extended unpacking with *) ---
numbers = (1, 2, 3, 4, 5)
first, second, *rest = numbers
print(f"First: {first}")       # 1
print(f"Second: {second}")     # 2
print(f"Rest: {rest}")         # [3, 4, 5]

# * can be in the middle or at the end
first, *middle, last = numbers
print(f"Middle: {middle}")   # [2, 3, 4]

# --- Nested unpacking ---
person = ("Anna", (25, "Engineer"))
name, (age, profession) = person
print(f"{name}, {age} years, {profession}")

# --- Unpacking with enumerate() ---
fruit = ["apple", "banana", "orange"]
for index, value in enumerate(fruit):
    print(f"{index}: {value}")
