# file: sc_10_03_iterator.py
# Delegate to the list's built-in iterator.
# Each traversal gets a new iterator.
class MyCollection:
    def __init__(self, data):
        self._data = data

    def __iter__(self):
        # Reuses the list's built-in iterator.
        return iter(self._data)

collection = MyCollection([1, 2, 3])
for item in collection:
    print(item, end=" ")   # 1 2 3

for item in collection:   # Works again - new iterator each time
    print(item, end=" ")   # 1 2 3

# Return self as the iterator and track the position in __next__().
# This iterator is exhausted after one traversal.
class MyIterator:
    def __init__(self, data):
        self._data = data
        self._index = 0

    def __iter__(self):
        # Iterator is itself - exhausted after one pass.
        return self

    def __next__(self):
        if self._index < len(self._data):
            item = self._data[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

it = MyIterator([1, 2, 3])
for item in it:
    print(item, end=" ")   # 1 2 3
for item in it:
    print(item, end=" ")   # Nothing - iterator is exhausted

# Create a separate iterator object for each traversal.
# Each iterator tracks its own position.
# The collection can therefore be reused.
class MyCollection:
    def __init__(self, data):
        self._data = data

    def __iter__(self):
        return MyCollectionIterator(self._data)

class MyCollectionIterator:
    def __init__(self, data):
        self._data = data
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._data):
            item = self._data[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

collection = MyCollection([1, 2, 3])
for item in collection:
    print(item, end=" ")   # 1 2 3

# Can be used again.
for item in collection:
    print(item, end=" ")

# Iterators become exhausted after one traversal in all three examples.
# In examples 1 and 3, each loop calls iter(collection), creating a fresh iterator.
# In example 2, iter(it) returns the same iterator; create a new MyIterator
# before the second loop to traverse the data again.

# Inherit __iter__() from Iterator; it returns self.
# The collection still creates a separate iterator for each traversal.
from collections.abc import Iterator

class MyCollection:
    def __init__(self, data):
        self._data = data

    def __iter__(self):
        return MyCollectionIterator(self._data)

class MyCollectionIterator(Iterator):
    def __init__(self, data):
        self._data = data
        self._index = 0

    def __next__(self):
        if self._index < len(self._data):
            item = self._data[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

collection = MyCollection([1, 2, 3])
print()
for item in collection:
    print(item, end=" ")   # 1 2 3
print()

for item in collection:   # Works again - new iterator each time
    print(item, end=" ")   # 1 2 3

# Use yield in __iter__() to create a generator for each traversal.
# Python tracks the position; no separate iterator class is needed.
class MyCollection:
    def __init__(self, data):
        self._data = data

    def __iter__(self):
        for item in self._data:
            yield item

collection = MyCollection([1, 2, 3])
print()
for item in collection:
    print(item, end=" ")   # 1 2 3
print()

for item in collection:   # Works again - new generator each time
    print(item, end=" ")   # 1 2 3
