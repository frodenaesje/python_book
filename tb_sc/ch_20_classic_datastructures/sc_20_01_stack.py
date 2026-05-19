# file: sc_20_01stack.py
class Stack:
    def __init__(self):
        self._elements = []  # Use a list to store stack elements

    def push(self, item):
        """Add an item to the top of the stack."""
        self._elements.append(item)

    def pop(self):
        """Remove and return the item at the top of the stack.
           Raises IndexError if stack is empty."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._elements.pop()

    def peek(self):
        """Return the item at the top of the stack
           without removing it.
           Raises IndexError if stack is empty."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._elements[-1]

    def is_empty(self):
        """Return True if the stack is empty, False otherwise."""
        return len(self._elements) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self._elements)
    
# Use the Stack class
if __name__ == "__main__":  
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    print("Top of stack:", stack.peek())  # Should print 3
    print("Stack size:", stack.size())     # Should print 3
    
    print("Popped item:", stack.pop())     # Should print 3
    print("Top of stack after pop:", stack.peek())  # Should print 2
    print("Stack size after pop:", stack.size())    # Should print 2   