# sc_05_12_break_continue.py
numbers = [4, 7, -2, 8, -5, 3, 9]

for number in numbers:
    if number < 0:
        print(f'{number} is negative - stopping')
        break              # exit loop entirely
    if number % 2 == 0:
        continue           # skip to next iteration
    print(number)

# Output:
# 7
# -2 is negative - stopping
# 4 skipped by continue, 8 never reached (break)

# for-else: else runs only if no break occurred
number = 29
for divisor in range(2, number):
    if number % divisor == 0:
        print(f"{number} is not a prime number")
        break
else:           # runs only if loop completed without break
    print(f'{number} is a prime number')

number = 29
is_prime = True

for divisor in range(2, number):
    if number % divisor == 0:
        is_prime = False
        break

if is_prime:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
