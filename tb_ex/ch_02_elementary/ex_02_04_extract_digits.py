# file: ex_02_04_extract_digits.py

number = int(input("Enter a four-digit integer: "))

digit4 = number % 10
number //= 10
digit3 = number % 10
number //= 10
digit2 = number % 10
number //= 10
digit1 = number % 10

print(f"The number in reverse order is: {digit4}{digit3}{digit2}{digit1}")
