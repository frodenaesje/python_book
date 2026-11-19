# File: sc_14_01_countdown.py

def countdown(n):
    """Count down from n to 1, then print 'Finished!'"""
    if n == 0:  # BASE CASE: Stop when n reaches 0
        print("Finished!")
    else:       # RECURSIVE CASE: Print n, then call with n-1
        print(n)
        countdown(n - 1)  # Function calls itself!

print("\nRecursive countdown(5):")
countdown(5)


def countdown_iter(n):
    """Same result using a loop instead of recursion"""
    while n > 0:
        print(n)
        n -= 1
    print("Finished!")

print("\n\nIterative countdown_iter(5):")
countdown_iter(5)