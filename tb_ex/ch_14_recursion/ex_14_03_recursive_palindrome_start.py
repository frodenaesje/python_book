# file: ex_14_03_recursive_palindrome.py

def is_palindrome(s: str) -> bool:
    """Return True if s is a palindrome, using recursion."""
    # TODO: base case: a string of length 0 or 1 is always a palindrome
    # TODO: recursive step: first and last characters must match,
    #       AND the middle part (s[1:-1]) must also be a palindrome
    pass


def is_phrase_palindrome(phrase: str) -> bool:
    """Return True if phrase is a palindrome, ignoring spaces and case."""
    # TODO: remove spaces and convert to lowercase, then call is_palindrome
    pass


if __name__ == "__main__":
    # Part 1
    print(is_palindrome("racecar"))   # True
    print(is_palindrome("hello"))     # False
    print(is_palindrome("a"))         # True
    print(is_palindrome(""))          # True
    print(is_palindrome("level"))     # True
    print()

    # Part 2
    print(is_phrase_palindrome("never odd or even"))             # True
    print(is_phrase_palindrome("A man a plan a canal Panama"))   # True
    print(is_phrase_palindrome("race a car"))                    # False
