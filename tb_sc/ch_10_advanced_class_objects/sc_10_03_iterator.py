# file: sc_10_03_iterator.py
class MyCollection:
    def __init__(self, data):
        self._data = data

    def __iter__(self):
        return iter(self._data)   # Reuses the list's built-in iterator

collection = MyCollection([1, 2, 3])
for item in collection:
    print(item, end=" ")   # 1 2 3

for item in collection:   # Works again - new iterator each time
    print(item, end=" ")   # 1 2 3

class MyIterator:
    def __init__(self, data):
        self._data = data
        self._index = 0

    def __iter__(self):
        return self   # Iterator is itself - exhausted after one pass

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
