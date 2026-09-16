# file: snippet_list_iteration.py
# Reassigning the iteration variable does not modify the list.
# Assigning through an index changes the element stored in the list.

numbers = [3, 7, 2, 8, 4]
for number in numbers:
    print(number)

numbers = [3, 7, 2, 8, 4]
for number in numbers:
    number = number * 2
    print(number, end=" ")
print()
print(numbers)

numbers = [3, 7, 2, 8, 4]
for index in range(len(numbers)):
    numbers[index] *= 2
print(numbers)

numbers = [3, 7, 2, 8, 4]
for index, value in enumerate(numbers):
    numbers[index] = value + 1
print(numbers)

numbers = [3, 7, 2, 8, 4]
for index, value in enumerate(numbers, start=1):
    print(f"Element {index}: {value}")
