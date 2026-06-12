# file: ex_06_08_random_password.py
import random
from ex_06_07_password_checker import is_good_password

def random_password() -> str:
    """Generate a random password of 7-10 printable ASCII characters."""
    length = random.randint(7, 10)
    chars = [chr(random.randint(33, 126)) for _ in range(length)]
    return ''.join(chars)


if __name__ == "__main__":
    attempts = 0
    password = random_password()
    attempts += 1

    while not is_good_password(password):
        password = random_password()
        attempts += 1

    print(f"Generated password: {password}")
    print(f"Attempts needed: {attempts}")
