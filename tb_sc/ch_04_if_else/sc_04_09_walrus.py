# sc_04_09_walrus.py
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]   # 12 elements

# Without walrus - len() called twice
if len(data) > 10:
    print(f'Large list: {len(data)} elements')

# With walrus - computed once, used in test and after
if (n := len(data)) > 10:
    print(f'Large list: {n} elements')


# Without walrus - the input line is repeated
line = input('Type something v1: ').strip()
while line:
    print(f'You typed: {line}')
    line = input('Type something v1: ').strip()

# With walrus - read and test in one step
while (line := input('Type something v2: ').strip()):
    print(f'You typed: {line}')
# Stops when user presses Enter without typing