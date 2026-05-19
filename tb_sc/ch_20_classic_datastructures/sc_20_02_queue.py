# file: sc_20_02_queue.py
# Implementation of a simple Queue data structure using
# collections.deque for efficient operations
from collections import deque

class Queue:
    def __init__(self):
        self._elements = deque()  # Use deque for efficient queue ops

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self._elements.append(item)

    def dequeue(self):
        """Remove and return the item at the front of the queue.
        Raises IndexError if queue is empty."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._elements.popleft()

    def peek(self):
        """Return the item at the front without removing it.
        Raises IndexError if queue is empty."""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._elements[0]

    def is_empty(self):
        """Return True if the queue is empty, False otherwise."""
        return len(self._elements) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self._elements)
    
# Use the Queue class
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    
    print("Front of queue:", queue.peek())  # Should print 1
    print("Queue size:", queue.size())      # Should print 3
    
    print("Dequeued item:", queue.dequeue())  # Should print 1
    print("Front of queue after dequeue:", queue.peek())
    # Should print 2
    print("Queue size after dequeue:", queue.size()) # print 2