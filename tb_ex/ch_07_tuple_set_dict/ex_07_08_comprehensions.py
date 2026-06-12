# file: ex_07_08_comprehensions.py

# --- Tuple comprehensions ---

result = tuple(i**2 for i in range(6))
print("Tuple 1:", result)

result = tuple((i, i**2) for i in range(0, 11, 2))
print("Tuple 2:", result)

# --- Set comprehensions ---

word = "hello"
result = {char for char in word}
print("Set 3:", result)

words = ["apple", "apricot", "banana", "cat", "blueberry", "dog"]
result = {len(word) for word in words if word[0] in ('a', 'b')}
print("Set 4:", result)

# --- Dict comprehensions ---

result = {i: i**2 for i in range(5)}
print("Dict 5:", result)

words = ["apple", "cat", "banana", "dog", "elephant", "ox"]
result = {word: len(word) for word in words if len(word) > 3}
print("Dict 6:", result)
