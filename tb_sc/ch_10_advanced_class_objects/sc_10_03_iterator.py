# file: sc_10_03_iterator.py
from collections.abc import Iterator

class MyIterator(Iterator):
    def __init__(self):
        self.data = [1, 2, 3]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            item = self.data[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

class MyCollectionV1:
    def __init__(self, data):
        self._data = data

    def __iter__(self):
        # Uses the list's built-in iterator.
        return iter(self._data)

class MyCollectionV2:
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

my_iterator = MyIterator()
print("MyIterator")
for item in my_iterator:
    print(item, end=" ")

collection = MyCollectionV1([1, 2, 3])
print("\nMyCollectionV1")
for item in collection:
    print(item, end=" ")

# Can be used again.
for item in collection:
    print(item, end=" ")

collection = MyCollectionV2([1, 2, 3])
print("\nMyCollectionV2")
for item in collection:
    print(item, end=" ")

# Can be used again.
for item in collection:
    print(item, end=" ")
