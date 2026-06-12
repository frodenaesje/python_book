# file: ex_06_06_ordinal_numbers.py

def ordinal(n: int) -> str:
    """Return the ordinal string for a positive integer, e.g. '21st'."""
    if n % 100 in (11, 12, 13):
        suffix = "th"
    elif n % 10 == 1:
        suffix = "st"
    elif n % 10 == 2:
        suffix = "nd"
    elif n % 10 == 3:
        suffix = "rd"
    else:
        suffix = "th"
    return f"{n}{suffix}"


if __name__ == "__main__":
    for i in range(1, 26):
        print(f"{ordinal(i):<6}", end="")
        if i % 10 == 0:
            print()
    print()

    n = int(input("\nEnter a number: "))
    print(ordinal(n))
