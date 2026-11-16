# file: sc_07_11_word_game.py
from collections import Counter


def check_guess(secret: str, guess: str) -> list[tuple[str, str]]:
    """Compare a guess with the secret word.

    Both arguments must contain five lowercase letters.

    Returns a list of (letter, mark) tuples, where mark is
    "G" (right letter, right place), "Y" (right letter, wrong place)
    or "-" (no unmatched occurrence remains).
    """
    remaining = Counter(secret)
    marks = ["-"] * len(guess)

    # First pass: letters in the right place
    for index, (secret_letter, guess_letter) in enumerate(zip(secret, guess)):
        if secret_letter == guess_letter:
            marks[index] = "G"
            remaining[guess_letter] -= 1

    # Second pass: right letters in the wrong place
    for index, letter in enumerate(guess):
        if marks[index] != "G" and remaining[letter] > 0:
            marks[index] = "Y"
            remaining[letter] -= 1

    return list(zip(guess, marks))


SECRET = "cable"

for guess in ["bleak", "eagle", "cable"]:
    result = check_guess(SECRET, guess)
    letters = " ".join([letter.upper() for letter, _ in result])
    marks = " ".join([mark for _, mark in result])
    print(letters)
    print(marks)
    print()
