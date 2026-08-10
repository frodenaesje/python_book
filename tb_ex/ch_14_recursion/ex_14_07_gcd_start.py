# file: ex_14_07_gcd.py

def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of a and b using Euclid's algorithm."""
    # TODO: base case: if b == 0, return a
    # TODO: recursive step: gcd(b, a % b)
    pass


def lcm(a: int, b: int) -> int:
    """Return the lowest common multiple of a and b."""
    # TODO: a * b // gcd(a, b)
    pass


def simplify(numerator: int, denominator: int) -> tuple:
    """Return the fraction in lowest terms as a tuple (num, den)."""
    # TODO: find gcd of numerator and denominator
    # TODO: divide both by gcd and return as tuple
    pass


if __name__ == "__main__":
    print(gcd(48, 18))    # 6
    print(gcd(100, 75))   # 25
    print(gcd(17, 5))     # 1
    print(gcd(0, 7))      # 7
    print()
    print(lcm(4, 6))      # 12
    print(lcm(12, 18))    # 36
    print()
    print(simplify(6, 8))     # (3, 4)
    print(simplify(100, 75))  # (4, 3)
