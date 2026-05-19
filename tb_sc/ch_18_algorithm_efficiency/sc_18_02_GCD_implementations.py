# file: sc_18_02_GCD_implementations.py
# ------------------------------------------------------------
# 1. Brute force from 1 to min(a, b)
#    - Checks ALL possible divisors.
#    - Complexity: O(n)
# ------------------------------------------------------------
def gcd_bruteforce(a, b):
    gcd = 1
    limit = min(a, b)
    for d in range(1, limit + 1):
        if a % d == 0 and b % d == 0:
            gcd = d
    return gcd


# ------------------------------------------------------------
# 2. Search DOWNWARD from min(a, b)
#    - Improvement: Stops when we find the first valid divisor.
#    - Finds GCD faster in practice, but still O(n).
# ------------------------------------------------------------
def gcd_downward(a, b):
    limit = min(a, b)
    for d in range(limit, 0, -1):
        if a % d == 0 and b % d == 0:
            return d
    return 1  # actually never necessary


# ------------------------------------------------------------
# 3. Search downward BUT start at min(a, b) // 2
#    - Insight: GCD cannot be greater than half of
#      the smallest number (unless the numbers are equal).
#    - Improvement: The search space is halved in the worst case.
#    - Still linear, but fewer tests: O(n/2) = O(n)
# ------------------------------------------------------------
def gcd_half_range(a, b):
    m = min(a, b)

    # If the numbers are equal, return the number
    if a == b:
        return a

    # Start at half (rounded down)
    for d in range(m // 2, 0, -1):
        if a % d == 0 and b % d == 0:
            return d

    return 1


# ------------------------------------------------------------
# 4. Euclid's algorithm (modulus variant)
#    - Major improvement: Uses mathematical relationship:
#          gcd(a, b) = gcd(b, a % b)
#    - Reduces the numbers dramatically per step.
#    - Complexity: O(log n), extremely much faster.
# ------------------------------------------------------------
def gcd_euclid(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# ------------------------------------------------------------
# Example usage when running the file directly
# ------------------------------------------------------------
if __name__ == "__main__":
    a, b = 128, 96

    print("Bruteforce:", gcd_bruteforce(a, b))
    print("Downward search:", gcd_downward(a, b))
    print("Half range search:", gcd_half_range(a, b))
    print("Euclid:", gcd_euclid(a, b))