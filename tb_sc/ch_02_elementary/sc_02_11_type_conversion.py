# file: sc_02_11_type_conversion.py
# Type conversion between different data types (int, float, str)


# String to int
age = int("25")
print(f"String '25' converted to int: {age}, type: {type(age)}")

# String to float
price = float("19.99")
print(f"String '19.99' converted to float: {price}, type: {type(price)}")

# Note: The string must contain a valid number, otherwise ValueError is raised
try:
    invalid = int("hello")  # This will raise ValueError
except ValueError as e:
    print(f"Error: Cannot convert 'hello' to int - {e}")


# Int to string
text1 = str(42)
print(f"Int 42 converted to string: '{text1}', type: {type(text1)}")

# Float to string
text2 = str(3.14)
print(f"Float 3.14 converted to string: '{text2}', type: {type(text2)}")

# Useful when concatenating numbers with text
name = "Alice"
age = 25
message = name + " is " + str(age) + " years old."
print(f"Concatenation: {message}")

print("\n=== Converting between Int and Float ===")

# Int to float
x = float(5)
print(f"Int 5 converted to float: {x}, type: {type(x)}")

# Float to int - TRUNCATES (doesn't round!)
y = int(5.9)
print(f"Float 5.9 converted to int: {y}, type: {type(y)} - Note: truncated, not rounded")

z = int(5.1)
print(f"Float 5.1 converted to int: {z}, type: {type(z)} - Also truncated")

# If you need rounding instead of truncation, use round()
rounded = round(5.9)
print(f"Float 5.9 rounded: {rounded}")

print("\n=== Practical Example: User Input ===")
# input() always returns a string, so you need to convert it
# (This is a demonstration - normally you'd use input())
user_input = "42"
converted_number = int(user_input)
print(f"User entered: '{user_input}' (string)")
print(f"Converted to: {converted_number} (int)")


