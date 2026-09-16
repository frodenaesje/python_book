# file: snippet_collection_comprehensions.py
# Comprehensions can build sets and dictionaries; parentheses create a generator.
# Pass the generator expression to tuple() to build a tuple.

# Set comprehension
# Curly braces without a key:value pair create a set.
# Duplicate results are automatically collapsed into one value.
words = ["apple", "kiwi", "banana", "fig", "cherry"]

lengths = {len(word) for word in words}
print(lengths)
# The set contains 3, 4, 5 and 6, but its display order is not guaranteed.


# Dict comprehension
# A colon separates the key expression from the value expression.
words = ["apple", "kiwi", "banana"]

lengths = {word: len(word) for word in words}
print(lengths)
# {"apple": 5, "kiwi": 4, "banana": 6}


# Build a dictionary from two parallel sequences.
# zip() supplies one name and one age for each iteration.
names = ["Anna", "Bjorn", "Celina"]
ages = [25, 34, 29]

people = {name: age for name, age in zip(names, ages)}
print(people)
# {"Anna": 25, "Bjorn": 34, "Celina": 29}


# Invert a dictionary by exchanging its keys and values.
prices = {"apple": 10, "kiwi": 8}

by_price = {price: fruit for fruit, price in prices.items()}
print(by_price)
# {10: "apple", 8: "kiwi"}

# Dictionary keys must be unique. If an inversion produces the same
# key more than once, the later value silently replaces the earlier one.


# There is no tuple comprehension.
# Parentheses around a comprehension expression create a generator expression.
squares = (x * x for x in range(5))
print(squares)
# The output identifies a generator object; its memory address will vary.


# To create a tuple, pass the generator expression to tuple().
# No extra pair of parentheses is needed.
squares = tuple(x * x for x in range(5))
print(squares)
# (0, 1, 4, 9, 16)
