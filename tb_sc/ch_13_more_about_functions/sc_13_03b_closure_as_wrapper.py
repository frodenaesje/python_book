# file: sc_13_03b_closure_as_wrapper.py
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
