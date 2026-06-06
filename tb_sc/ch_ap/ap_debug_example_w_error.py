# file: sc_debug_example_w_error.py
def find_largest(numbers):
    """Returns the largest number in the list."""
    largest = 0
    for n in numbers:
        if n > largest:
            largest = n
    return largest

def find_largest_c(numbers):
    """Returns the largest number in the list."""
    largest = numbers[0]
    for n in numbers:
        if n > largest:
            largest = n
    return largest

data = [-5, -2, -8, -1]
print(find_largest(data))   # Expected: -1, actual: 0
print(find_largest_c(data))   # -1
