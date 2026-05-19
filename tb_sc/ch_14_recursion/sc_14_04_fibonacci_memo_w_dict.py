# File: sc_14_04_fibonacci_memo_w_dict.py
def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:  # Already computed?
        return memo[n]
    
    if n <= 1:  # BASE CASE
        return n
    
    # Recursive case: Store result before returning
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

print("fibonacci_memo n = 10: ", fibonacci_memo(10))
print("fibonacci_memo n = 50: ", fibonacci_memo(50))
print("fibonacci_memo n = 100: ", fibonacci_memo(100))