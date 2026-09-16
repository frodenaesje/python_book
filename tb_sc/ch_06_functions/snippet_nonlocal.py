# file: snippet_nonlocal.py
# nonlocal lets an inner function modify a variable
# in the enclosing function's scope.

def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
    inner()
    print(count)  # 1

outer()
