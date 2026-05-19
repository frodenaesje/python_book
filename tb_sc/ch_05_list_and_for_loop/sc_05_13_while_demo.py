# file: sc_05_13_while_demo.py

# Example 1: simple counter
count = 0
while count < 5:
    print(f"count is {count}")
    count += 1

# Example 2a: read input - duplicated prompt (beginner)
print("\nType something (quit to exit):")
text = input("> ")
while text != "quit":
    print(f"You typed: {text}")
    text = input("> ")

# Example 2b: read input - while True with break (pythonic)
print("\nType something (quit to exit):")
while True:
    text = input("> ")
    if text == "quit":
        break
    print(f"You typed: {text}")

# Example 3: sum numbers until the total exceeds 100
total = 0
number = 1
while total <= 100:
    total += number
    number += 1
print(f"\nThe sum exceeded 100 after {number - 1} numbers, sum = {total}")
