# file: heap_sort.py
class MinHeap:
    def __init__(self):
        self._heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def insert(self, key):
        self._heap.append(key)
        self.heapify_up(len(self._heap) - 1)

    def heapify_up(self, index):
        while (
            index != 0
            and self._heap[self.parent(index)] > self._heap[index]
        ):
            parent_idx = self.parent(index)
            self._heap[parent_idx], self._heap[index] = (
                self._heap[index],
                self._heap[parent_idx],
            )
            index = self.parent(index)

    def extract_min(self):
        if len(self._heap) == 0:
            return None
        root = self._heap[0]
        last_element = self._heap.pop()
        if len(self._heap) > 0:
            self._heap[0] = last_element
            self.heapify_down(0)
        return root

    def heapify_down(self, index):
        while True:
            smallest = index
            left = self.left(index)
            right = self.right(index)

            if (
                left < len(self._heap)
                and self._heap[left] < self._heap[smallest]
            ):
                smallest = left
            if (
                right < len(self._heap)
                and self._heap[right] < self._heap[smallest]
            ):
                smallest = right
            if smallest == index:
                break

            self._heap[index], self._heap[smallest] = (
                self._heap[smallest],
                self._heap[index],
            )
            index = smallest

    def get_min(self):
        if len(self._heap) == 0:
            return None
        return self._heap[0]

    def size(self):
        return len(self._heap)

def heap_sort(arr):
    min_heap = MinHeap()
    for item in arr:
        min_heap.insert(item)

    sorted_arr = []
    while min_heap.size() > 0:
        sorted_arr.append(min_heap.extract_min())
    return sorted_arr