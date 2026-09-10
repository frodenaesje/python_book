# file: sc_06_03_parameter_names.py
# parameter names can be anything - they are local names
# that exist only inside the function, and do not conflict
# with variables outside it

def add_two_numbers(a, b):
    return a + b

x = 1
y = 2
result = add_two_numbers(x, y)
print(result)  # 3

# The same function, now with the parameters named x and y.
# These are NOT the x and y above - they are separate, local names.
def add_two_numbers(x, y):
    return x + y

result = add_two_numbers(x, y)
print(result)  # 3  - works exactly the same