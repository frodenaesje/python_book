# file: sc_08_14_object.py
"""
Demonstrates important dunder methods (magic methods) that can be overridden.
These methods allow objects to integrate with Python's built-in functions and operators.
"""

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def __str__(self):
        """String representation for end users (print, str())"""
        return f"{self._name} ({self._age} years old)"
    
    def __repr__(self):
        """Developer representation (repr(), debugging)"""
        return f"Person('{self._name}', {self._age})"
    
    def __eq__(self, other):
        """Equality comparison (==)"""
        if not isinstance(other, Person):
            return False
        return self._name == other._name and self._age == other._age
    
    def __lt__(self, other):
        """Less than comparison (<) - enables sorting"""
        if not isinstance(other, Person):
            return NotImplemented
        return self._age < other._age
    
    def __le__(self, other):
        """Less than or equal (<=)"""
        return self < other or self == other
    
    def __hash__(self):
        """Hash for use in sets/dict keys"""
        return hash((self._name, self._age))


class NumberCollection:
    def __init__(self, numbers):
        self._numbers = list(numbers)
    
    def __len__(self):
        """Length for len() function"""
        return len(self._numbers)
    
    def __getitem__(self, index):
        """Index access with [] operator"""
        return self._numbers[index]
    
    def __setitem__(self, index, value):
        """Index assignment with [] operator"""
        self._numbers[index] = value
    
    def __contains__(self, item):
        """Membership testing with 'in' operator"""
        return item in self._numbers
    
    def __iter__(self):
        """Iterator for for-loops and unpacking"""
        return iter(self._numbers)
    
    def __bool__(self):
        """Truthiness for if statements"""
        return len(self._numbers) > 0
    
    def __add__(self, other):
        """Addition with + operator"""
        if isinstance(other, NumberCollection):
            return NumberCollection(self._numbers + other._numbers)
        return NotImplemented
    
    def __str__(self):
        return f"NumberCollection({self._numbers})"


class Counter:
    def __init__(self, start=0):
        self._value = start
    
    def __call__(self, increment=1):
        """Makes object callable like a function"""
        self._value += increment
        return self._value
    
    def __enter__(self):
        """Context manager entry"""
        print(f"Entering context with counter at {self._value}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        print(f"Exiting context with counter at {self._value}")
        return False  # Don't suppress exceptions
    
    def __str__(self):
        return f"Counter({self._value})"


if __name__ == "__main__":
    print("=== DEMONSTRATION OF DUNDER METHODS ===")
    
    # Person class demonstrations
    print("\n--- Person Class ---")
    alice = Person("Alice", 30)
    bob = Person("Bob", 25)
    alice2 = Person("Alice", 30)
    
    print(f"str(alice): {alice}")        # __str__
    print(f"repr(alice): {repr(alice)}")  # __repr__
    print(f"alice == alice2: {alice == alice2}")  # __eq__
    print(f"alice == bob: {alice == bob}")
    print(f"bob < alice: {bob < alice}")  # __lt__
    
    # Sorting uses comparison methods
    people = [alice, bob, Person("Charlie", 35)]
    people.sort()
    print(f"Sorted by age: {[str(p) for p in people]}")
    
    # Hash enables use in sets
    person_set = {alice, bob, alice2}  # alice and alice2 are same
    print(f"Unique people in set: {len(person_set)}")
    
    # NumberCollection class demonstrations
    print("\n--- NumberCollection Class ---")
    numbers = NumberCollection([1, 2, 3, 4, 5])
    
    print(f"Collection: {numbers}")      # __str__
    print(f"Length: {len(numbers)}")    # __len__
    print(f"First item: {numbers[0]}")  # __getitem__
    print(f"3 in numbers: {3 in numbers}")  # __contains__
    print(f"10 in numbers: {10 in numbers}")
    
    # Modify collection
    numbers[0] = 10  # __setitem__
    print(f"After numbers[0] = 10: {numbers}")
    
    # Iteration
    print("Iterating:", end=" ")  # __iter__
    for num in numbers:
        print(num, end=" ")
    print()
    
    # Truthiness
    empty = NumberCollection([])
    print(f"bool(numbers): {bool(numbers)}")  # __bool__
    print(f"bool(empty): {bool(empty)}")
    
    # Addition
    more_numbers = NumberCollection([6, 7, 8])
    combined = numbers + more_numbers  # __add__
    print(f"Combined: {combined}")
    
    # Counter class demonstrations
    print("\n--- Counter Class ---")
    counter = Counter(10)
    print(f"Initial: {counter}")
    
    # Callable object
    print(f"counter(): {counter()}")     # __call__
    print(f"counter(5): {counter(5)}")   # __call__ with argument
    
    # Context manager
    print("\nUsing as context manager:")
    with counter as c:  # __enter__ and __exit__
        print(f"Inside context: {c()}")
        print(f"Inside context: {c(3)}")
    
    print("\n=== SUMMARY OF IMPORTANT DUNDER METHODS ===")
    print("__init__     - Object initialization")
    print("__str__      - User-friendly string (print, str)")
    print("__repr__     - Developer string (repr, debugging)")
    print("__eq__       - Equality comparison (==)")
    print("__lt__       - Less than (<) - enables sorting")
    print("__hash__     - Hash for sets/dict keys")
    print("__len__      - Length (len() function)")
    print("__getitem__  - Index access (obj[key])")
    print("__setitem__  - Index assignment (obj[key] = value)")
    print("__contains__ - Membership (item in obj)")
    print("__iter__     - Iteration (for loops)")
    print("__bool__     - Truthiness (if obj)")
    print("__add__      - Addition (+)")
    print("__call__     - Make object callable (obj())")
    print("__enter__    - Context manager entry (with)")
    print("__exit__     - Context manager exit (with)")