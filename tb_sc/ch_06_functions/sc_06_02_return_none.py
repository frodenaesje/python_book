# file sc_06_02_return_none.py
# Functions without return automatically return None
def say_hello(name):
    print(f'Hello, {name}!')

result = say_hello('Anna')   # Hello, Anna!
print(result)                # None


# Classic pitfall: sort() returns None!
numbers = [3, 1, 4, 1, 5]

# Wrong:
sorted_numbers = numbers.sort()
print(sorted_numbers)        # None  <- bug!

# Correct:
numbers.sort()               # sort in place
print(numbers)               # [1, 1, 3, 4, 5]

# Or use sorted() which returns a new list:
sorted_numbers = sorted(numbers)