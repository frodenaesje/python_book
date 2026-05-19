# file: sc_04_01_ternary_demo.py
# Ternary operator: condition ? value_if_true : value_if_false

# Example 1: Plural ending
num_apples = int(input("How many apples do you have? "))
print(f"You have {num_apples} apple{'s' if num_apples != 1 else ''}.")

# Example 2: Using word instead of number
print(f"You have {'one' if num_apples == 1 else num_apples} apple{'s' if num_apples != 1 else ''}.")

# Example 3: Discount calculation
price = float(input("Enter purchase price: "))
discount = price * 0.1 if price > 100 else 0
final_price = price - discount
print(f"Final price: ${final_price:.2f} {'(10% discount applied)' if discount > 0 else ''}")

# Example 4: Grade based on score
score = int(input("Enter test score (0-100): "))
grade = "Pass" if score >= 60 else "Fail"
print(f"Result: {grade}")

