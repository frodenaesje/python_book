# file: sc_05_16_birthday_cards.py
print("Think of your day of birth, a number from 1 to 31.")
weights = [1, 2, 4, 8, 16]
day = 0

for weight in weights:
    card = []
    for number in range(1, 32):
        if (number & weight) != 0:
            card.append(number)

    print(f"\nCard value: {weight}")
    for start in range(0, len(card), 4):
        row = card[start:start + 4]
        print(" ".join([f"{number:2}" for number in row]))

    answer = input("Is your day on this card? (y/n): ").strip().lower()
    while answer != "y" and answer != "n":
        answer = input("Please enter y or n: ").strip().lower()

    if answer == "y":
        day += weight

if day == 0:
    print("No day from 1 to 31 matches five no answers.")
else:
    print(f"Your day of birth is {day}.")
