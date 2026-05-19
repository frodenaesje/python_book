# file: sc_13_02_inner_outer.py
# Closures: inner functions that remember outer state

# Example 1: Basic closure
def outer(x: int):
    outer_var = x * 2

    def inner():
        # Closure: inner can access outer's variables,
        # even after outer has returned.
        inner_var = outer_var * 2
        print(f"x: {x}")  # From outer's parameter
        print(f"outer_var: {outer_var}")
        print(f"inner_var: {inner_var}")
        print()

    return inner  # Returns a reference to inner

# Each closure remembers its own environment.
print("First closure (x=42):")
closure1 = outer(42)
closure1()  # Prints: 42, 84, 168

print("Second closure (x=10):")
closure2 = outer(10)
closure2()  # Prints: 10, 20, 40

# Both closures exist at the same time with their own values.
print("Calling first closure again:")
closure1()  # Still: 42, 84, 168

print("\n" + "="*50 + "\n")

# Example 2: Closure as a function wrapper
def simple_decorator(func):
    # Takes a function and returns a wrapper function.
    def wrapper():
        print("--- Before the function is called ---")
        func()  # Closure: wrapper remembers func.
        print("--- After the function is called ---")
    return wrapper

def greet():
    print("Hi!")

# Manual decoration: replace greet with the wrapper version.
print("Original greet:")
greet()

print("\nNow we decorate greet:")
greet = simple_decorator(greet)
greet()  # Calls wrapper, which calls the original greet.

# This is what the @ syntax does in the next file.
