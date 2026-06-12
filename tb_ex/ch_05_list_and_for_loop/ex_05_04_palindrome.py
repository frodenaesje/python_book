# file: ex_05_04_palindrome.py

text = input("Enter a string: ")

# Part 1
if text == text[::-1]:
    print(f'"{text}" is a palindrome.')
else:
    print(f'"{text}" is not a palindrome.')

# Part 2
cleaned = text.replace(" ", "").lower()
if cleaned == cleaned[::-1]:
    print(f'"{text}" is a palindrome (ignoring spaces).')
else:
    print(f'"{text}" is not a palindrome (ignoring spaces).')
