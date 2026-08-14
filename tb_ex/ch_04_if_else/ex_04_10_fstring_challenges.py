# file: ex_04_10_fstring_challenges.py

# --- 1. Basic interpolation ---
name = "John"
age = 30
print(f"{name} is {age} years old.")

# --- 2. Two decimals ---
amount = 837.5
print(f"Amount: {amount:.2f}")

# --- 3. Right alignment (width 8) ---
a = 5
b = 42
c = 1370
print(f"{a:>8}")
print(f"{b:>8}")
print(f"{c:>8}")

# --- 4. Percent (one decimal) ---
correct = 27
total = 40
print(f"Score: {correct / total:.1%}")

# --- 5. Sign and thousands separator ---
balance = 2500.0
print(f"{balance:+,.2f}")

# --- 6. A different thousands separator ---
population = 5391369
print(f"{population:,}".replace(",", " "))

# --- 7. Method calls inside the field ---
first = "john"
last = "english"
print(f"{first.capitalize()} {last.upper()}")

# --- 8. Ternary: even or odd ---
number = 7
print(f"{number} is {'even' if number % 2 == 0 else 'odd'}")

# --- 9. Ternary: plural ending ---
count = 1
print(f"You have {count} message{'s' if count != 1 else ''}")

# --- 10. Put it together ---
quantity = 3
price = 49.9
print(f"{quantity} item{'s' if quantity != 1 else ''} cost {quantity * price:.2f} in total")
