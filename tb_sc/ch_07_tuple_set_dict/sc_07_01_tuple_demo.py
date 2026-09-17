# file: sc_07_01_tuple_demo.py

# creating tuples in different ways
tu1 = (1, 2, 3)           # regular tuple with parentheses
tu2 = 4, 5, 6             # tuple without parentheses - also valid
tu3 = tuple([7, 8, 9])    # from list using the constructor
tu4 = ()                  # empty tuple
tu5 = (42,)               # single-value tuple - note the comma!

print("tu1:", tu1)
print("tu2:", tu2)
print("tu3:", tu3)
print("tu4:", tu4)
print("tu5:", tu5)

# immutable - cannot be changed
a_list  = [1, 2, 3]
a_tuple = (1, 2, 3)
a_list[0]  = 99  # OK
# a_tuple[0] = 99  # Uncomment to see TypeError: tuples are immutable

t = (1, [2, 3], 4)
t[1].append(99)   # OK! Changes the list inside the tuple
print(t)          # (1, [2, 3, 99], 4)

# creating from generator and list
tu = tuple(x for x in range(5)) # from generator
print(tu)

tu = tuple([x * 2 for x in range(5)]) # from list comprehension
print(tu)


tu = tuple(map(str, range(3))) # from map-function


# unpacking
a, b, c = tu1
print("Unpacked tu1:", a, b, c)

# swapping values with unpacking
x, y = 10, 20
x, y = y, x
print("Swapped x and y:", x, y)

# extended unpacking with *
tu6 = (1, 2, 3, 4, 5)
first, *middle, last = tu6
print("First:", first)
print("Middle:", middle)
print("Last:", last)
# Unpacking assigns iterable elements to separate variables.
# A starred expression collects the remaining elements in a list.

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
