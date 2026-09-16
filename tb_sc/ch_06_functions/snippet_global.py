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
