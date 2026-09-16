# file: snippet_function_local_scope.py
# Variables defined inside a function are local to that function.
# Accessing the local variable z outside it raises NameError.

def func():
    z = 42  # local variable

func()
print(z)  # NameError: z is not defined
