# file: ex_14_08_decimal_to_binary.py

def to_binary(n: int) -> str:
    """Return the binary string representation of n (recursive)."""
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return to_binary(n // 2) + str(n % 2)


DIGITS = "0123456789ABCDEF"

def to_base(n: int, base: int) -> str:
    """Return n in the given base (2-16) as a string."""
    if n < base:
        return DIGITS[n]
    return to_base(n // base, base) + DIGITS[n % base]


if __name__ == "__main__":
    for n in [0, 1, 10, 42, 255]:
        result = to_binary(n)
        print(f"to_binary({n:3}) = {result:>8}  verify: {int(result, 2)}")

    print()
    print(f"to_base(42, 2)   = {to_base(42, 2)}")
    print(f"to_base(42, 8)   = {to_base(42, 8)}")
    print(f"to_base(42, 16)  = {to_base(42, 16)}")
    print(f"to_base(255, 16) = {to_base(255, 16)}")
