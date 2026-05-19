# file: sc_20_03_deque_as stack_and_queue.py
# Demonstates how to use collections.deque as both stack and queue
# data structures
from collections import deque

# Using deque as a stack (LIFO)
stack = deque()
stack.append(1)  # Push 1
stack.append(2)  # Push 2
stack.append(3)  # Push 3
print("Stack top:", stack[-1])  # 3
print("Popped from stack:", stack.pop())  # 3
print("Stack after pop:", list(stack))  # [1, 2]


# Using deque as a queue (FIFO)
queue = deque()
queue.append(1)  # Enqueue 1
queue.append(2)  # Enqueue 2
queue.append(3)  # Enqueue 3
print("Queue front:", queue[0])  # 1
print("Dequeued from queue:", queue.popleft())  # 1
print("Queue after dequeue:", list(queue))  # [2, 3]


# Same deque instance behaving as stack and queue
deque_structure = deque()
deque_structure.append("A")
deque_structure.append("B")
deque_structure.append("C")

result = list(deque_structure)
print("Same deque start:", result)  # ['A', 'B', 'C']
print("As stack (pop):", deque_structure.pop())
# 'C'
result = list(deque_structure)
print("After stack pop:", result)  # ['A', 'B']

deque_structure.append("D")
result = list(deque_structure)
print("Before queue dequeue:", result)  # ['A', 'B', 'D']
print("As queue (popleft):", deque_structure.popleft())  # 'A'
print("After queue dequeue:", list(deque_structure))  # ['B', 'D']