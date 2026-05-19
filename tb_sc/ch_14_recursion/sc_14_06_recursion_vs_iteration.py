# File: sc_14_06_recursion_vs_iteration.py
"""
Recursion vs Iteration: When to use which approach
"""

print("=" * 60)
print("RECURSION VS ITERATION: Making the Right Choice")
print("=" * 60)

print("\n" + "=" * 60)
print("WHEN TO USE RECURSION")
print("=" * 60)
print("""
✓ Problem naturally divides into smaller versions of itself
  Examples: Tree traversal, divide-and-conquer algorithms
  
✓ Code is cleaner and more elegant with recursion
  Examples: Tower of Hanoi, directory traversal
  
✓ Problem depth is reasonable (< 1000 levels in Python)
  Examples: Parsing expressions, backtracking algorithms
  
✓ Working with recursive data structures
  Examples: Trees, graphs, nested lists

Good use cases:
  • Tree/graph traversal
  • Divide and conquer (merge sort, quick sort)
  • Tower of Hanoi
  • Generating permutations/combinations
  • Parsing nested structures
  • Backtracking problems (sudoku, maze solving)
""")

print("\n" + "=" * 60)
print("WHEN TO USE ITERATION (loops)")
print("=" * 60)
print("""
✓ Simple, straightforward loops
  Examples: Counting, summing, searching arrays
  
✓ Performance is critical
  Iteration has less overhead than recursion
  
✓ Problem depth could be very large
  No risk of stack overflow with iteration
  
✓ No natural recursive structure
  Examples: Processing a list sequentially

Good use cases:
  • Simple counting or accumulation
  • Array/list processing
  • Fibonacci sequence
  • Most mathematical sequences
  • File reading line by line
  • User input loops
""")

print("\n" + "=" * 60)
print("SIDE-BY-SIDE COMPARISON")
print("=" * 60)

# Example 1: Countdown
print("\n1. COUNTDOWN - Both work well")
print("-" * 40)

def countdown_recursive(n):
    if n == 0:
        print("Done!")
    else:
        print(n)
        countdown_recursive(n - 1)

def countdown_iterative(n):
    while n > 0:
        print(n)
        n -= 1
    print("Done!")

print("Recursive:")
countdown_recursive(3)
print("\nIterative:")
countdown_iterative(3)

print("\nVerdict: Both are fine, but iterative is simpler for this")

# Example 2: Sum of list
print("\n" + "=" * 60)
print("2. SUM OF LIST - Iteration is better")
print("-" * 40)

def sum_recursive(lst):
    if not lst:
        return 0
    return lst[0] + sum_recursive(lst[1:])

def sum_iterative(lst):
    total = 0
    for num in lst:
        total += num
    return total

numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")
print(f"Recursive sum: {sum_recursive(numbers)}")
print(f"Iterative sum: {sum_iterative(numbers)}")
print(f"Built-in sum:  {sum(numbers)}")

print("\nVerdict: Iteration is clearer and faster")

# Example 3: Finding maximum
print("\n" + "=" * 60)
print("3. FINDING MAXIMUM - Iteration is better")
print("-" * 40)

def max_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    return max(lst[0], max_recursive(lst[1:]))

def max_iterative(lst):
    max_val = lst[0]
    for num in lst[1:]:
        if num > max_val:
            max_val = num
    return max_val

numbers = [3, 7, 2, 9, 1, 5]
print(f"Numbers: {numbers}")
print(f"Recursive max: {max_recursive(numbers)}")
print(f"Iterative max: {max_iterative(numbers)}")
print(f"Built-in max:  {max(numbers)}")

print("\nVerdict: Iteration is clearer and more efficient")

print("\n" + "=" * 60)
print("RECURSION PITFALLS")
print("=" * 60)
print("""
✗ Forgetting the base case
  → Infinite recursion → Stack overflow
  
✗ Stack overflow with deep recursion
  → Python limit: ~1000 recursive calls
  → Solution: Use iteration or increase recursion limit (risky!)
  
✗ Inefficiency without memoization
  → Fibonacci is classic example: O(2^n) without memoization
  → Solution: Use iteration or memoization
  
✗ Harder to debug
  → Stack traces can be long and confusing
  → Solution: Print statements, or convert to iteration
  
✗ More memory overhead
  → Each recursive call uses stack space
  → Solution: Use iteration for large problems
""")

print("\n" + "=" * 60)
print("PERFORMANCE COMPARISON")
print("=" * 60)

import time

def time_function(func, *args, iterations=100000):
    """Time how long a function takes"""
    start = time.time()
    for _ in range(iterations):
        func(*args)
    end = time.time()
    return end - start

# Compare recursive vs iterative factorial
def factorial_recursive(n):
    return 1 if n <= 1 else n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

n = 10
iterations = 100000

print(f"\nCalculating factorial({n}) {iterations} times:")
print("-" * 40)

time_rec = time_function(factorial_recursive, n, iterations=iterations)
time_iter = time_function(factorial_iterative, n, iterations=iterations)

print(f"Recursive:  {time_rec:.4f} seconds")
print(f"Iterative:  {time_iter:.4f} seconds")
print(f"Speedup:    {time_rec/time_iter:.2f}x faster with iteration")

print("\n" + "=" * 60)
print("SUMMARY: Decision Guide")
print("=" * 60)
print("""
Choose RECURSION when:
  • Problem is naturally recursive (trees, divide-and-conquer)
  • Code is much cleaner with recursion
  • Depth is small (< 1000 in Python)
  • Performance is not critical
  
Choose ITERATION when:
  • Simple sequential processing
  • Performance matters
  • Depth could be large
  • No natural recursive structure
  
When in doubt:
  1. Start with the clearest solution (often iteration)
  2. Only use recursion if it makes code significantly cleaner
  3. Profile if performance matters
  4. Remember: Readability counts!
""")
