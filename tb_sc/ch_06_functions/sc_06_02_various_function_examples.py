# file: sc_06_02_various_function_examples.py
# Focused examples of *args, **kwargs, and unpacking techniques

# ========== *args: Packing and unpacking of varargs ==========

# Function that takes a variable number of positional arguments
def sum_all(*numbers):
    """Sums all given arguments."""
    return sum(numbers)

# Packing: Arguments are packed into a tuple
print("=== *args - Packing ===")
result = sum_all(1, 2, 3, 4, 5)
print(f"sum_all(1, 2, 3, 4, 5) = {result}")

# Unpacking: Use * to unpack a sequence when calling a function
numbers_list = [10, 20, 30]
print(f"\nnumbers_list = {numbers_list}")
result = sum_all(*numbers_list)  # Unpacks the list into arguments
print(f"sum_all(*numbers_list) = {result}")

# ========== **kwargs: Packing and unpacking of keyword arguments ==========

# Function that takes a variable number of keyword arguments
def create_profile(**attributes):
    """Creates a profile description from keyword arguments."""
    profile = []
    for key, value in attributes.items():
        profile.append(f"{key}: {value}")
    return " | ".join(profile)

print("\n=== **kwargs - Packing ===")
profile = create_profile(name="Anna", age=30, city="Oslo")
print(profile)

# Unpacking: Use ** to unpack a dictionary when calling a function
person_dict = {"name": "John", "age": 25, "hobby": "climbing"}
print(f"\nperson_dict = {person_dict}")
profile = create_profile(**person_dict)  # Unpacks the dictionary into keyword arguments
print(profile)

# ========== Combined use of *args and **kwargs ==========

def print_data(*args, **kwargs):
    """Takes both positional arguments and keyword arguments."""
    print("Posisional arguments  (*args):", args)
    print("Keyword arguments (**kwargs):", kwargs)

print("\n=== Combined *args and **kwargs ===")
print_data(1, 2, 3, name="John", age=29)

# Unpacking both parts simultaneously
data = [100, 200, 300]
config = {"type": "test", "debug": True}
print("\nUnpacking both list and dictionary:")
print_data(*data, **config)

# ========== Mutable Default Arguments - Pitfall ==========

# WRONG: Mutable object as default value is evaluated only once
def append_wrong(element, lst=[]):
    lst.append(element)
    return lst

print("\n=== Mutable Default (WRONG) ===")
print(append_wrong(1))  # [1]
print(append_wrong(2))  # [1, 2] - Same list is reused!

# CORRECT: Use None as default value
def append_correct(element, lst=None):
    if lst is None:
        lst = []
    lst.append(element)
    return lst

print("\n=== Mutable Default (CORRECT) ===")
print(append_correct(1))  # [1]
print(append_correct(2))  # [2] - New list each time
