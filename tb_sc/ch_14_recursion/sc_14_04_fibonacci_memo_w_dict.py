# File: sc_14_04_fibonacci_memo_w_dict.py
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print("fibonacci(10) =", fibonacci(10))


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

def fibonacci_iter(n):
    if n <= 1:
        return n
    a, b = 0, 1   # a = F(0), b = F(1)
    for _ in range(2, n + 1):
        a, b = b, a + b   # move the window forward
    return b


print("iterative N = 10 : ", fibonacci_iter(10))
