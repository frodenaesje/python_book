# Filename: lsc_20_01_linkedlist.py
# Følgende metoder er "left as an exercise" i LinkedList-klassen:
# clear, contains, remove, get, indexOf, lastIndexOf, set
class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    # Return the head element in the list 
    def get_first(self):
        if self._size == 0:
            return None
        else:
            return self._head
    
    # Return the last element in the list 
    def get_last(self):
        if self._size == 0:
            return None
        else:
            return self._tail

    # Add an element to the beginning of the list 
    def add_first(self, e):
        new_node = Node(e)  # Create a new node
        new_node._next = self._head  # link to "what was first"
        self._head = new_node  # head points to the new node
        self._size += 1  # Increase list size

        if self._tail is None:  # the new node is the only node in list
            self._tail = self._head
    
    # add() is same as add_last 
    def add(self, e):
        self.add_last(e)
    
    # Add an element to the end of the list 
    def add_last(self, e):
        new_node = Node(e)  # Create a new node for e
    
        if self._tail is None:
            self._head = self._tail = new_node  # The only node in list
        else:
            self._tail._next = new_node  # Link the new with the last node
            self._tail = new_node  # tail now points to the last node
    
        self._size += 1  # Increase size

    
    # Insert a new element at the specified index in this list
    # The index of the head element is 0 
    def insert(self, index, e):
        if index <= 0:
            self.add_first(e)  # Insert first
        elif index >= self._size:
            self.add_last(e)  # Insert last
        else:  # Insert in the middle
            current = self._head
            for _ in range(index - 1):
                current = current._next
            new_node = Node(e)
            new_node._next = current._next
            current._next = new_node
            self._size += 1

    # Remove the head node and
    #  return the object that is contained in the removed node. 
    def remove_first(self):
        if self._size == 0:
            return None  # Nothing to delete
        else:
            temp = self._head  # Keep the first node temporarily
            self._head = self._head._next  # Move head to point the next node
            self._size -= 1  # Reduce size by 1
            if self._head is None: 
                self._tail = None  # List becomes empty 
            return temp  # Return the deleted element

    # Remove the last node and
    # return the object that is contained in the removed node
    def remove_last(self):
        if self._size == 0:
            return None  # Nothing to remove
        elif self._size == 1:  # Only one element in the list
            temp = self._head
            self._head = self._tail = None  # list becomes empty
            self._size = 0
            return temp
        else:
            current = self._head
            for _ in range(self._size - 2):
                current = current._next
            
            temp = self._tail
            self._tail = current
            self._tail._next = None
            self._size -= 1
            return temp

    # Remove the element at the specified position in this list.
    #  Return the element that was removed from the list. 
    def remove_at(self, index):
        if index < 0 or index >= self._size:
            return None  # Out of range
        elif index == 0:
            return self.remove_first()  # Remove first 
        elif index == self._size - 1:
            return self.remove_last()  # Remove last
        else:
            previous = self._head
            for _ in range(index - 1):
                previous = previous._next
            
            current = previous._next
            previous._next = current._next
            self._size -= 1
            return current

    # Return true if the list is empty
    def is_empty(self):
        return self._size == 0
    
    # Return the size of the list
    def get_size(self):
        return self._size

    def __str__(self):
        return "[" + ", ".join(str(element) for element in self) + "]"
    
    def __repr__(self):
        return f"LinkedList({list(self)})"
    
    def __len__(self):
        return self._size
    
    def __bool__(self):
        return self._size > 0

    # Clear the list
    def clear(self):
        self._head = self._tail = None
        self._size = 0

    # Return true if this list contains the element e 
    def contains(self, e):
        print("Implementation left as an exercise")
        return True

    # Remove the element and return true if the element is in the list 
    def remove(self, e):
        print("Implementation left as an exercise")
        return True

    # Return the element from this list at the specified index 
    def get(self, index):
        print("Implementation left as an exercise")
        return None

    # Return the index of the head matching element in this list.
    # Return -1 if no match.
    def index_of(self, e):
        print("Implementation left as an exercise")
        return 0

    # Return the index of the last matching element in this list
    #  Return -1 if no match. 
    def last_index_of(self, e):
        print("Implementation left as an exercise")
        return 0

    # Replace the element at the specified position in this list
    #  with the specified element.
    def set(self, index, e):
        print("Implementation left as an exercise")
        return None
    
    # Return elements via indexer, can use list[0] to get the first element etc
    def __getitem__(self, index):
        # Support negative indexing
        if isinstance(index, int):
            if index < 0:
                index = self._size + index
            if index < 0 or index >= self._size:
                raise IndexError("LinkedList index out of range")
            return self.get(index)
        else:
            raise TypeError("LinkedList indices must be integers")

    # Return an iterator for a linked list
    def __iter__(self):
        return LinkedListIterator(self._head)
    
# The Node class
class Node:
    def __init__(self, e):
        self._element = e
        self._next = None

class LinkedListIterator: 
    def __init__(self, head):
        self._current = head
    
    def __iter__(self):
        return self
        
    def __next__(self):
        if self._current is None:
            raise StopIteration
        element = self._current._element
        self._current = self._current._next
        return element
        
# Test the LinkedList class

def main():
    # Create a list for strings
    list1 = LinkedList()
    list1.add("America") # Add it to the list
    list1.add("Canada") # Add it to the list
    list1.add("Russia") # Add it to the list
    list1.add("France") # Add it to the list
    list1.add("Germany") # Add it to the list
    list1.add("Norway") # Add it to the list
    
    print("List contents:", list1)
    print("List representation:", repr(list1))
    print("List length:", len(list1))
    print("List is truthy:", bool(list1))
    
    # iterate with a for loop
    print("\nIterating:")
    for element in list1:
        print(element, end=" ")
    
    # iterate with enumerator
    print("\n\nEnumerated:")
    for i, element in enumerate(list1):
        print(i, element)
    
    # Test negative indexing
    print("\nNegative indexing:")
    print("list1[-1]:", list1[-1])
    print("list1[-2]:", list1[-2])

if __name__ == "__main__": 
    main()