# file: ex_05_06_isbn10.py

digits = input("Enter the first 9 digits of the ISBN-10: ")

total = 0
for i, char in enumerate(digits):
    total += int(char) * (i + 1)

checksum = total % 11
check_char = 'X' if checksum == 10 else str(checksum)

print(f"ISBN-10: {digits}{check_char}")
