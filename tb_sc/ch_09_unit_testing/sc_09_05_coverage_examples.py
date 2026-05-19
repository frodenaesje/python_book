# file: sc_09_05_coverage_examples.py
def greet(name):
    return f"Hello, {name}!"

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def is_valid(x):
    return x > 0 and x < 10