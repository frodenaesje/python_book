# file: sc_10_17_abc_iterator.py
from collections.abc import Iterator

class CountUp(Iterator):
    def __init__(self, start, stop):
        self._current = start
        self._stop    = stop

    def __next__(self):
        if self._current >= self._stop:
            raise StopIteration
        value = self._current
        self._current += 1
        return value

for number in CountUp(1, 5):
    print(number, end=" ")   # 1 2 3 4
