# file: snippet_global.py
# global lets an assignment inside a function change a global variable.
# Without it, the assignment here creates a separate local variable.

# Without global:
x = 10
def change_x():
    x = 5  # local variable - the global x is unchanged
    print("Inside:", x)

change_x()
print("Outside:", x)  # 10

# With global:
x = 10
def change_x():
    global x
    x = 5  # now the global x is changed
    print("Inside:", x)

change_x()
print("Outside:", x)  # 5

# A local variable shadows a global variable with the same name.
# Changing the local variable leaves the global variable unchanged.

x = 10

def func():
    x = 20  # local variable - does not change global x

func()
print(x)  # 10
