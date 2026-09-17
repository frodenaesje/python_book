# sc_04_09_walrus.py
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]   # 12 elements

# Without walrus - len() called twice
if len(data) > 10:
    print(f'Large list with {len(data)} elements')

# With walrus - computed once, used in test and after
if (n := len(data)) > 10:
    print(f'Large list with {n} elements')


while (line := input("Type something: ").strip()):
    print(f"You typed: {line}")
# Stops when user presses Enter without typing
