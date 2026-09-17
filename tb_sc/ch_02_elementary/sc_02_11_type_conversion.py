# file: sc_02_11_type_conversion.py
# Type conversion between different data types (int, float, str)

# String to int
age = int("25")
print(f"String '25' converted to int: {age}, type: {type(age)}")

# String to float
price = float("19.99")
print(f"String '19.99' converted to float: {price}, type: {type(price)}")

# int("hello")  # Uncomment to see ValueError: the text is not an integer.

# Int to string
text1 = str(42)
print(f"Int 42 converted to string: '{text1}', type: {type(text1)}")

# Float to string
text2 = str(3.14)
print(f"Float 3.14 converted to string: '{text2}', type: {type(text2)}")

# Useful when concatenating numbers with text
name = "Anna"
age = 12
print(name + " is " + str(age) + " years old.")

print("\n=== Converting between Int and Float ===")

# Int to float
x = float(5)
print(f"Int 5 converted to float: {x}, type: {type(x)}")

# Float to int - TRUNCATES (doesn't round!)
y = int(5.9)
print(f"Float 5.9 converted to int: {y}, type: {type(y)} - Note: truncated, not rounded")

print(int(True))    # 1
print(int(False))   # 0
print(float(True))  # 1.0
print(bool(0))      # False
print(bool(42))     # True
print(bool(""))     # False
print(bool("hi"))   # True
