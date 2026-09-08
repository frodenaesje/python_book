# sc_05_13_while_demo.py

# while: check condition before each iteration
count = 0
while count < 5:
    print(f'count is {count}')
    count += 1      # IMPORTANT: must update count!

# Reading input - beginner (duplicated input call)
text = input('> ')
while text != 'quit':
    print(f'You typed: {text}')
    text = input('> ')

# Pythonic: while True with break
while True:
    text = input('> ')
    if text == 'quit':
        break
    print(f'You typed: {text}')

# Unknown number of iterations
total = 0
number = 1
while total <= 100:
    total += number
    number += 1
print(f'Exceeded 100 after {number-1} numbers, sum={total}')