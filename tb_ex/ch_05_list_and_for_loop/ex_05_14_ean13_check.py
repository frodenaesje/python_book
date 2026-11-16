# file: ex_05_14_ean13_check.py
# Extra exercise: EAN-13 check digit - reference solution
code = input("Enter a 13-digit barcode: ").strip()

if len(code) != 13 or not all(["0" <= char <= "9" for char in code]):
    print("A barcode must have exactly 13 digits.")
else:
    total = 0
    for index, char in enumerate(code[:12]):
        weight = 1 if index % 2 == 0 else 3
        total += int(char) * weight

    check_digit = (10 - total % 10) % 10

    if check_digit == int(code[-1]):
        print(f"Check digit is correct: {check_digit}")
    else:
        print(f"Invalid check digit: {code[-1]}.")
        print(f"Expected: {check_digit}.")
