# File: sc_14_02_sum.py
def sum_recursive(n):
    """Calculate sum of 1 + 2 + 3 + ... + n"""
    if n == 0:  # BASE CASE
        return 0
    else:       # RECURSIVE CASE: Add n to sum of (n-1)
        return n + sum_recursive(n - 1)

def sum_iter(n):
    """Iterative version for comparison"""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print("\nRecursive sum:")
print("sum_recursive(5) =", sum_recursive(5))
print("Explanation: 5 + 4 + 3 + 2 + 1 = 15")

print("\nIterative sum:")
print("sum_iter(5) =", sum_iter(5))