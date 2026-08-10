# file: ex_14_09_roman_numerals.py

VALUES = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"),  (90, "XC"),  (50, "L"),  (40, "XL"),
    (10, "X"),   (9, "IX"),   (5, "V"),   (4, "IV"),   (1, "I"),
]


def to_roman(n: int) -> str:
    """Convert a positive integer (1-3999) to a Roman numeral string."""
    # TODO: base case: n == 0 -> return ""
    # TODO: find the first (largest) value v in VALUES where v <= n
    #       Hint: for value, symbol in VALUES: if value <= n: ...
    # TODO: return symbol + to_roman(n - value)
    pass


def from_roman(s: str) -> int:
    """Convert a Roman numeral string to an integer."""
    # Hint: build a lookup dict for both single and two-character symbols
    # then scan left to right, handling subtractive pairs
    # TODO: implement
    pass


if __name__ == "__main__":
    for n in [1, 4, 9, 14, 42, 1994, 3999]:
        print(f"to_roman({n:4}) = {to_roman(n)}")

    print()
    for s in ["I", "IV", "XIV", "XLII", "MCMXCIV", "MMMCMXCIX"]:
        print(f"from_roman({s:12}) = {from_roman(s)}")
