# file: ch_13_code_snippets.py
# useful function attributes
def greet(name="Susan"):
    """Says hello."""
    return f"Hello, {name}!"


print(greet.__name__)      # greet
print(greet.__doc__)       # Says hello.
print(greet.__defaults__)  # Default values
print(greet.__closure__)   # Used with closures

def comp(f, g, x):
    """Returner f(g(x))."""
    return f(g(x))

comp(print, len, "Hello") # Først len("Hello") -> 5, så print(5) -> 5

# using simple lambdas
names = ["John", "Mary", "Andrew"]
print(sorted(names, key=lambda name: len(name)))  # Sort by name length

numbers = [1, 2, 3, 4]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # Keep even numbers
print(even_numbers)  # [2, 4]


# 1) closure example without parameter
def make_greeting_without_parameter():
    greeting = "Hi"

    def say(name):
        return f"{greeting}, {name}"

    return say

hi = make_greeting_without_parameter()
print(hi("John"))  # "Hi, John"


# closure example with parameter
def make_greeting_with_parameter(greeting):
    def say(name):
        return f"{greeting}, {name}"

    return say

greeting = make_greeting_with_parameter("Hi")
print(greeting("John"))  # "Hi, John"


# 3) From closure to decorator: what if we pass a function instead of data?
# In the closure above, we passed "Hello" (data).
# Now let's pass a function and have the inner function call it.

# This is a basic decorator -
# it takes a function and returns a wrapper
def add_enthusiasm(func):
    
    def wrapper(name):
        result = func(name)  # Call the original function
        return result + "!"  # Add something extra
    return wrapper

# Original function
def say(name):
    return f"Hi, {name}"

# Apply decorator manually (without @ syntax)
say = add_enthusiasm(say)
print(say("John"))  # "Hi, John!"


# Same thing with @ syntax sugar
@add_enthusiasm
def say(name):
    return f"Hi, {name}"

print(say("John"))  # "Hi, John!"


# ======================================================================
# Step 1: A practical decorator with a fixed signature
# wrapper(data) works as long as all decorated functions take one argument
# ======================================================================
import time
import random
import numpy as np

def timed(func):
    def wrapper(data): # Fixed: we know func takes one argument
        t0 = time.perf_counter()
        result = func(data)
        print(f"{func.__name__}: {time.perf_counter() - t0:.4f} s")
        return result
    return wrapper

@timed
def python_sort(data):
    return sorted(data)

@timed
def numpy_quicksort(data):
    return np.sort(np.array(data), kind="quicksort")

data = [random.randint(0, 1_000_000) for _ in range(200_000)]
python_sort(data.copy())
numpy_quicksort(data.copy())

# ======================================================================
# Step 2: Problem — what if we want to pass extra arguments?
# numpy_sort(data.copy(), kind="mergesort")  # ERROR: wrapper(data) only takes one argument!
# Solution: use *args/**kwargs to support any function signature
# ======================================================================

def timed(func):
    def wrapper(*args, **kwargs): # Now works for any signature
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__}: {time.perf_counter() - t0:.4f} s")
        return result
    return wrapper

@timed
def numpy_sort(data, kind="quicksort"):
    return np.sort(np.array(data), kind=kind)

numpy_sort(data.copy(), kind="quicksort")
numpy_sort(data.copy(), kind="mergesort")
numpy_sort(data.copy(), kind="heapsort")