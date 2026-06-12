# file: ex_14_04_recursive_power.py

calls = [0]

def power(base, exp):
    """Compute base**exp recursively. O(exp) calls."""
    calls[0] += 1
    if exp == 0:
        return 1
    return base * power(base, exp - 1)


def fast_power(base, exp):
    """Compute base**exp using fast exponentiation. O(log exp) calls."""
    calls[0] += 1
    if exp == 0:
        return 1
    if exp % 2 == 0:
        half = fast_power(base, exp // 2)
        return half * half
    return base * fast_power(base, exp - 1)


if __name__ == "__main__":
    for exp in [10, 20, 100]:
        calls[0] = 0
        result = power(2, exp)
        p_calls = calls[0]

        calls[0] = 0
        result2 = fast_power(2, exp)
        fp_calls = calls[0]

        print(f"power(2, {exp:3})      = {result}  calls: {p_calls}")
        print(f"fast_power(2, {exp:3}) = {result2}  calls: {fp_calls}")
        print()
