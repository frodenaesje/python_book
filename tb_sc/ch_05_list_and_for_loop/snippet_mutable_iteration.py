# file: snippet_mutable_iteration.py
# The iteration variable refers to an inner list.
# append() changes that object, so the original list shows the change.

numbers = [[1], [2], [3]]
for number in numbers:
    number.append(99)
print(numbers)
