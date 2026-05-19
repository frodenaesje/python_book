# file: sc_13_04_decorator.py
# Decorators: functions that wrap other functions
# This builds on sc_13_03b_closure_as_wrapper.py.

# Step 1: Simple decorator with @ syntax
def simple_decorator(func):
    """Wrap a function with extra functionality."""
    def wrapper():
        print("--- Before the function is called ---")
        func()  # Closure: wrapper remembers func.
        print("--- After the function is called ---")
    return wrapper

# @simple_decorator means: greet = simple_decorator(greet)
@simple_decorator
def greet():
    print("Hi!")

greet()

print("\n" + "="*50 + "\n")

@simple_decorator
def say_goodbye():
    print("Goodbye!")

say_goodbye()

print("\n" + "="*50 + "\n")

# Step 2: Decorator with arguments and return values
def smart_decorator(func):
    """Decorate functions with arguments and return values."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        print(f"  args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@smart_decorator
def add(a, b):
    return a + b

@smart_decorator
def greet_person(name, greeting="Hi"):
    return f"{greeting}, {name}!"

result1 = add(5, 3)
print(f"Result: {result1}")

print()

result2 = greet_person("Anna", greeting="Hallo")
print(f"Result: {result2}")

print("\n" + "="*50 + "\n")

# Step 3: Practical logging decorator with state
def log_calls(func):
    """Log every call to the function."""
    call_count = 0
    
    def wrapper(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        print(f"[LOG] Call #{call_count} to {func.__name__}")
        return func(*args, **kwargs)
    
    return wrapper

@log_calls
def calculate(x, y):
    return x * y + x

print(calculate(3, 4))
print(calculate(5, 2))
print(calculate(1, 1))
