# file: sc_13_02b_closure_mechanics.py
# How Python implements closures behind the scenes

"""
CLOSURE MECHANICS: Stack vs Heap

The problem:
------------
When a function returns, its stack frame is normally removed.
That also removes its local variables.
But a closure must remember variables from the outer scope
even after the outer function has returned.

Python's solution:
------------------
Python moves closed-over variables from the stack to the heap
by wrapping them in special 'cell' objects. This lets the
variables outlive the stack frame where they were created.
"""

print("=" * 70)
print("PART 1: Basic closure example")
print("=" * 70)

def make_multiplier(factor):
    """
    Make a function that multiplies by 'factor'.
    'factor' must survive after make_multiplier returns.
    """
    def multiplier(x):
        # multiplier closes over factor from the outer scope.
        return x * factor
    
    return multiplier

# Create two different closures.
times_2 = make_multiplier(2)
times_3 = make_multiplier(3)

print(f"\ntimes_2(5) = {times_2(5)}")  # 10
print(f"times_3(5) = {times_3(5)}")    # 15

# make_multiplier has returned, but 'factor' lives on.
print("\nmake_multiplier's stack frame is gone,")
print("but 'factor' still exists on the heap.")

print("\n" + "=" * 70)
print("PART 2: Inspecting the closure mechanism")
print("=" * 70)

# Python stores closed-over variables in __closure__.
print(f"\ntimes_2.__closure__ = {times_2.__closure__}")
print(f"Type: {type(times_2.__closure__)}")

if times_2.__closure__:
    closed_count = len(times_2.__closure__)
    print(f"\nNumber of closed variables: {closed_count}")
    
    for i, cell in enumerate(times_2.__closure__):
        print(f"  Cell {i}: {cell}")
        print(f"    Type: {type(cell)}")
        print(f"    Value: {cell.cell_contents}")

print("\n" + "=" * 70)
print("PART 3: Comparing two closures")
print("=" * 70)

print("\ntimes_2 closes over factor=2:")
times_2_value = times_2.__closure__[0].cell_contents
print(f"  times_2 cell contents = {times_2_value}")

print("\ntimes_3 closes over factor=3:")
times_3_value = times_3.__closure__[0].cell_contents
print(f"  times_3 cell contents = {times_3_value}")

print("\nEach closure has its own cell object on the heap!")

print("\n" + "=" * 70)
print("PART 4: Several closed-over variables")
print("=" * 70)

def make_calculator(a, b):
    """Closure with several closed-over variables."""
    operation = "add"  # A third variable
    
    def calculate():
        if operation == "add":
            return a + b
        return 0
    
    return calculate

calc = make_calculator(10, 5)
print(f"\ncalc() = {calc()}")

print(f"\nNumber of closed variables: {len(calc.__closure__)}")
for i, cell in enumerate(calc.__closure__):
    print(f"  Cell {i}: {cell.cell_contents}")

print("\n" + "=" * 70)
print("PART 5: Closure with mutable state (nonlocal)")
print("=" * 70)

def make_counter(start=0):
    """
    Make a counter that can be incremented.
    Show that the heap cell object can be modified.
    """
    count = start  # Stored in a heap cell object
    
    def increment():
        nonlocal count  # Needed to modify count
        count += 1
        return count
    
    return increment

counter1 = make_counter(0)
counter2 = make_counter(100)

print("\nCounter 1:")
print(f"  {counter1()}")  # 1
print(f"  {counter1()}")  # 2
print(f"  {counter1()}")  # 3

print("\nCounter 2:")
print(f"  {counter2()}")  # 101
print(f"  {counter2()}")  # 102

# Inspect the cell objects.
print("\nCounter 1's cell:")
counter1_value = counter1.__closure__[0].cell_contents
print(f"  Current value: {counter1_value}")

print("\nCounter 2's cell:")
counter2_value = counter2.__closure__[0].cell_contents
print(f"  Current value: {counter2_value}")

print("\n" + "=" * 70)
print("PART 6: Function without closure, for comparison")
print("=" * 70)

def regular_function(x):
    """Regular function without a closure."""
    return x * 2

closure_attr = regular_function.__closure__
print(f"\nregular_function.__closure__ = {closure_attr}")
print("None means no closed-over variables: no cells!")

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print("""
The closure mechanism in Python:

1. Stack problem: Local variables disappear when a
   function returns.

2. Heap solution: Python moves closed-over variables
   to the heap by wrapping them in 'cell' objects.

3. __closure__: Each closure has a __closure__ attribute.
   It is a tuple of cell objects.

4. cell_contents: Each cell has a cell_contents
   attribute holding the actual value.

5. Lifetime: Heap cell objects survive as long as the
   closure exists, regardless of stack frames.

6. Mutable state: With 'nonlocal', closures can modify
   cell values and give functions private state.

This is why closures can remember their environment!
""")
