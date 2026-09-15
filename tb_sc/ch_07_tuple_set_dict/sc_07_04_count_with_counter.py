# file: sc_07_04_count_with_counter.py
# Counting occurrences using collections.Counter

from collections import Counter

# Counter creates a dictionary-like object from an iterable.
# Each distinct element becomes a key; its occurrence count is the value.
numbers = [1, 2, 2, 3, 3, 3]
c = Counter(numbers)
print(c)
# Counter({3: 3, 2: 2, 1: 1})

# Strings are iterable, so Counter can count their characters directly.
text = "banana"
c = Counter(text)
print(c)
# Counter({'a': 3, 'n': 2, 'b': 1})

# most_common(n) returns the n elements with the highest counts.
c = Counter("banana bread")
print(c.most_common(2))
# [('a', 3), ('n', 2)]

# update() adds occurrences to an existing Counter.
c = Counter("hi")
c.update("hihi")
print(c)
# Counter({'h': 3, 'i': 3})

# A practical example - counting words in a text
# split() creates the words; Counter counts them in one operation.
text = "once upon a time there was a little man who had a cat"
words = text.split()
c = Counter(words)
print(c)
# Counter({'a': 3, 'once': 1, 'upon': 1, 'time': 1, ...})

# most_common() makes it easy to retrieve the most frequent words.
print(c.most_common(3))
# [('a', 3), ('once', 1), ('upon', 1)]

c = Counter("banankake")
print(c.most_common(2))

