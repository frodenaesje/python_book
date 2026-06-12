# file: ex_07_08_comprehensions_start.py

# --- Tuple comprehensions ---

# Example 1: squares of 0-5
# Loop version (given):
result = ()
for i in range(6):
    result += (i**2,)
print("Tuple 1 (loop):", result)
# TODO: Write the comprehension version:
# result = tuple(...)
# print("Tuple 1 (comp):", result)

# Example 2: pairs (number, square) for even numbers 0-10
result = ()
for i in range(0, 11, 2):
    result += ((i, i**2),)
print("Tuple 2 (loop):", result)
# TODO: Write the comprehension version

# --- Set comprehensions ---

# Example 3: unique letters in "hello"
word = "hello"
result = set()
for char in word:
    result.add(char)
print("Set 3 (loop):", result)
# TODO: Write the comprehension version

# Example 4: lengths of words starting with 'a' or 'b'
words = ["apple", "apricot", "banana", "cat", "blueberry", "dog"]
result = set()
for word in words:
    if word[0] in ('a', 'b'):
        result.add(len(word))
print("Set 4 (loop):", result)
# TODO: Write the comprehension version

# --- Dict comprehensions ---

# Example 5: numbers 0-4 mapped to their squares
result = {}
for i in range(5):
    result[i] = i**2
print("Dict 5 (loop):", result)
# TODO: Write the comprehension version

# Example 6: words longer than 3 mapped to their lengths
words = ["apple", "cat", "banana", "dog", "elephant", "ox"]
result = {}
for word in words:
    if len(word) > 3:
        result[word] = len(word)
print("Dict 6 (loop):", result)
# TODO: Write the comprehension version
