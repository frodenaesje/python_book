# file: sc_06_11_default_values.py
# Parameters with default values
def greet(name, greeting='Hello'):
    print(f'{greeting}, {name}!')

greet('Anna')            # Hello, Anna!  (default used)
greet('John', 'Hi')     # Hi, John!     (default overridden)

# Non-default params MUST come before default params
def function(a, b=2, c=3):   # OK
    return a + b + c

# def function(a=1, b): # SyntaxError!


# WARNING: mutable default value - a classic bug!
def add_to(element, lst=[]):
    lst.append(element)
    return lst

print(add_to(1))   # [1]
print(add_to(2))   # [1, 2]  <- not [2]!

# Fix: use None as default
def add_to(element, lst=None):
    if lst is None:
        lst = []
    lst.append(element)
    return lst
print(add_to(1))   # [1]
print(add_to(2))   # [2]  <- a fresh list each time