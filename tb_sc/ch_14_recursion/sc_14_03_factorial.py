# File: sc_14_03_factorial.py
def factorial(n):
    """Calculate n! (n factorial)"""
    if n == 0 or n == 1:  # BASE CASE
        return 1
    else:                 # RECURSIVE CASE: n * (n-1)!
        return n * factorial(n - 1)

print("\nStandard recursive factorial:")
print("factorial(5) =", factorial(5))
print("Explanation: 5! = 5 x 4 x 3 x 2 x 1 = 120")
