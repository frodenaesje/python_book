# file: snippet_shadowing.py
# A local variable shadows a global variable with the same name.
# Changing the local variable leaves the global variable unchanged.

x = 10

def func():
    x = 20  # local variable - does not change global x

func()
print(x)  # 10
