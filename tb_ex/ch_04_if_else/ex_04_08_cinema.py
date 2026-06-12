# file: ex_04_08_cinema.py

age     = int(input("Age: "))
tickets = int(input("Number of tickets: "))
evening = input("Evening screening? (yes/no): ").strip().lower() == "yes"

if age < 12:
    category = "Child"
    price = 8
elif age <= 25:
    category = "Student"
    price = 12
elif age <= 66:
    category = "Adult"
    price = 16
else:
    category = "Senior"
    price = 12

if evening and category == "Adult":
    price += 3
    category_label = "Adult (evening)"
else:
    category_label = category

subtotal = price * tickets
discount = subtotal * 0.10 if tickets >= 3 else 0
total = subtotal - discount

print("---")
print(f"Category: {category_label}")
print(f"Price per ticket: ${price}")
print(f"Number of tickets: {tickets}")
print(f"Subtotal: ${subtotal:.2f}")
if discount > 0:
    print(f"Group discount (10%): -${discount:.2f}")
print(f"Total: ${total:.2f}")
