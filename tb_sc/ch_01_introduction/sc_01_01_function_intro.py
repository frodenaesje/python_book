# file: sc_01_01_function_intro.py

def add(x, y):
    return x + y

# test the function
result = add(1, 2)
print(result)  # 3
print(add(result, 2.5))  # 5.5
print(add("Hello, ", "world!"))  # Hello, world!
