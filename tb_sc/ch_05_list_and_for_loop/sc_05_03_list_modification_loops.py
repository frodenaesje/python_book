# file: sc_05_03_list_modification_loops.py
numbers = [3, 7, 2, 8, 4]

# Method 1: Loop variable is a copy - doesn't modify the list
for number in numbers:
    number = number * 2
    print(number, end=' ')
# Output: 6 14 4 16 8
print()
print(numbers)
# Output: [3, 7, 2, 8, 4] (unchanged)

# Method 2: Using index - directly modifies the list
for index in range(len(numbers)):
    numbers[index] = numbers[index] * 2
print(numbers)
# Output: [6, 14, 4, 16, 8]

# Method 3: Using enumerate - also modifies the list
for index, value in enumerate(numbers):
    numbers[index] = value + 1
print(numbers)
# Output: [7, 15, 5, 17, 9]