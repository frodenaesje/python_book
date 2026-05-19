# File: sc_14_02_sum.py
"""
Recursion: Sum of numbers
Demonstrates returning values from recursive functions
"""

print("=" * 60)
print("SUM OF NUMBERS - Returning values from recursion")
print("=" * 60)

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

print("\n" + "-" * 60)
print("Visualizing the call stack for sum_recursive(4):")
print("-" * 60)
print("""
  sum_recursive(4)
  → 4 + sum_recursive(3)
      → 3 + sum_recursive(2)
          → 2 + sum_recursive(1)
              → 1 + sum_recursive(0)
                  → 0  [BASE CASE - returns 0]
              → 1 + 0 = 1
          → 2 + 1 = 3
      → 3 + 3 = 6
  → 4 + 6 = 10
""")

print("\nKey insight:")
print("  - Each recursive call returns a value")
print("  - These values are combined as the stack unwinds")
print("  - Base case provides the starting point for unwinding")
