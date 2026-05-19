# file: sc_06_03_parameter_scope.py

# parameter names can be anything
# parameter names have local scope and have nothing
# to do with variables outside the function

def add_two_numbers(a, b):
    return a + b

x = 1
y = 2
svar1 = add_two_numbers(x, y)
print(svar1)  # 3
svar2 = add_two_numbers(x, y)
print(svar2)  # 3