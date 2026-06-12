# file: ex_14_04_recursive_power.py

calls = [0]  # shared call counter

def power(base, exp):
    """Compute base**exp recursively. O(exp) calls."""
    calls[0] += 1
    # TODO: base case: power(base, 0) = 1
    # TODO: recursive step: base * power(base, exp - 1)
    pass


def fast_power(base, exp):
    """Compute base**exp using fast exponentiation. O(log exp) calls."""
    calls[0] += 1
    # TODO: base case: fast_power(base, 0) = 1
    # TODO: if exp is even:
    #         half = fast_power(base, exp // 2)
    #         return half * half   (compute once, use twice!)
    # TODO: if exp is odd:
    #         return base * fast_power(base, exp - 1)
    pass


if __name__ == "__main__":
    for exp in [10, 20, 100]:
        calls[0] = 0
        result = power(2, exp)
        print(f"power(2, {exp:3}) = {result}  calls: {calls[0]}")

        calls[0] = 0
        result = fast_power(2, exp)
        print(f"fast_power(2, {exp:3}) = {result}  calls: {calls[0]}")
        print()
