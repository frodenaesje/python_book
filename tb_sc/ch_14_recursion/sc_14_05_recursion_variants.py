# File: sc_14_05_recursion_variants.py
"""
Advanced Recursion: Variants, Common Mistakes, and Debugging
A comprehensive guide to different types of recursion
"""

print("=" * 70)
print("RECURSION VARIANTS - Deep dive into recursive techniques")
print("=" * 70)

# ============================================================================
# PART 1: Types of Recursion
# ============================================================================

print("\n" + "=" * 70)
print("PART 1: TYPES OF RECURSION")
print("=" * 70)

# 1.1 Linear Recursion (one recursive call)
print("\n1. Linear Recursion - One recursive call per function")
print("-" * 70)

def factorial(n):
    """Linear recursion: only one recursive call"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("factorial(5) =", factorial(5))
print("Call chain: factorial(5) → factorial(4) → factorial(3) → ...")

# 1.2 Tree Recursion (multiple recursive calls)
print("\n2. Tree Recursion - Multiple recursive calls")
print("-" * 70)

def fibonacci_tree(n):
    """Tree recursion: two recursive calls - forms a tree structure"""
    if n <= 1:
        return n
    return fibonacci_tree(n - 1) + fibonacci_tree(n - 2)

print("fibonacci_tree(6) =", fibonacci_tree(6))
print("Forms a tree: each call spawns two more calls")

# 1.3 Tail Recursion (recursive call is the last operation)
print("\n3. Tail Recursion - Recursive call is the LAST operation")
print("-" * 70)

def factorial_tail(n, accumulator=1):
    """
    Tail recursion: recursive call is the last thing that happens
    No work is done after the recursive call returns
    """
    if n <= 1:
        return accumulator
    return factorial_tail(n - 1, n * accumulator)  # Last operation!

print("factorial_tail(5) =", factorial_tail(5))
print("Key: Nothing happens AFTER the recursive call")
print("     (Some languages optimize this to avoid stack growth)")

# Compare with NON-tail recursion
def factorial_not_tail(n):
    """NOT tail recursion: multiplication happens AFTER the call"""
    if n <= 1:
        return 1
    result = factorial_not_tail(n - 1)  # Recursive call
    return n * result                    # Work AFTER the call!

print("factorial_not_tail(5) =", factorial_not_tail(5))
print("Not tail: multiplication happens after recursive call returns")

# 1.4 Mutual Recursion (functions call each other)
print("\n4. Mutual Recursion - Functions call each other")
print("-" * 70)

def is_even(n):
    """Checks if n is even by calling is_odd"""
    if n == 0:
        return True
    return is_odd(n - 1)

def is_odd(n):
    """Checks if n is odd by calling is_even"""
    if n == 0:
        return False
    return is_even(n - 1)

print("is_even(4) =", is_even(4))
print("is_odd(4) =", is_odd(4))
print("Call chain: is_even(4) → is_odd(3) → is_even(2) → is_odd(1) → ...")

# ============================================================================
# PART 2: Optimization Techniques
# ============================================================================

print("\n" + "=" * 70)
print("PART 2: OPTIMIZATION TECHNIQUES")
print("=" * 70)

# 2.1 Memoization with Dictionary
print("\n1. Memoization with Dictionary - Flexible caching")
print("-" * 70)

def fib_memo_dict(n, memo=None):
    """Dictionary-based memoization - flexible, dynamic"""
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fib_memo_dict(n - 1, memo) + fib_memo_dict(n - 2, memo)
    return memo[n]

print("fib_memo_dict(50) =", fib_memo_dict(50))
print("✓ Pros: Flexible, works with any key type")
print("✗ Cons: Slightly slower lookup than list")

# 2.2 Memoization with List
print("\n2. Memoization with List - Fast, preallocated")
print("-" * 70)

def fib_memo_list(n):
    """List-based memoization - requires knowing max n"""
    if n <= 1:
        return n
    
    memo = [-1] * (n + 1)
    memo[0], memo[1] = 0, 1
    
    def helper(k):
        if memo[k] != -1:
            return memo[k]
        memo[k] = helper(k - 1) + helper(k - 2)
        return memo[k]
    
    return helper(n)

print("fib_memo_list(50) =", fib_memo_list(50))
print("✓ Pros: Faster lookup, predictable memory")
print("✗ Cons: Must know max n in advance")

# 2.3 Using Python's @lru_cache decorator
print("\n3. Python's @lru_cache - Built-in memoization")
print("-" * 70)

from functools import lru_cache

@lru_cache(maxsize=None)
def fib_cached(n):
    """Using Python's built-in caching decorator"""
    if n <= 1:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)

print("fib_cached(50) =", fib_cached(50))
print("✓ Pros: Clean, professional, handles caching automatically")
print("✗ Cons: Less control over cache behavior")
print(f"Cache info: {fib_cached.cache_info()}")

# ============================================================================
# PART 3: Common Mistakes and How to Avoid Them
# ============================================================================

print("\n" + "=" * 70)
print("PART 3: COMMON RECURSION MISTAKES")
print("=" * 70)

# Mistake 1: Missing or wrong base case
print("\n❌ MISTAKE 1: Missing or Wrong Base Case")
print("-" * 70)

# def countdown_bad(n):
#     print(n)
#     countdown_bad(n - 1)  # CRASH! No base case → infinite recursion

def countdown_good(n):
    """Fixed: Has proper base case"""
    if n <= 0:  # BASE CASE
        print("Done!")
        return
    print(n)
    countdown_good(n - 1)

print("countdown_good(3):")
countdown_good(3)
print("✓ Always write the base case FIRST!")

# Mistake 2: Not making progress toward base case
print("\n❌ MISTAKE 2: Not Making Progress Toward Base Case")
print("-" * 70)

# def factorial_bad(n):
#     if n == 0:
#         return 1
#     return n * factorial_bad(n)  # WRONG! n doesn't change → infinite!

def factorial_good(n):
    """Fixed: n decreases toward base case"""
    if n == 0:
        return 1
    return n * factorial_good(n - 1)  # ✓ n-1 moves toward 0

print("factorial_good(5) =", factorial_good(5))
print("✓ Each recursive call must move closer to base case!")

# Mistake 3: Modifying shared state incorrectly
print("\n❌ MISTAKE 3: Modifying Shared State Incorrectly")
print("-" * 70)

def sum_list_bad(lst, total=[0]):  # DANGER! Default mutable argument
    """BAD: Using mutable default argument"""
    if not lst:
        return total[0]
    total[0] += lst[0]
    return sum_list_bad(lst[1:], total)

# First call works
print("First call:", sum_list_bad([1, 2, 3]))
# Second call WRONG - total persists!
print("Second call:", sum_list_bad([1, 2, 3]), "← WRONG! Should be 6")

def sum_list_good(lst, total=0):  # ✓ Immutable default
    """GOOD: Using immutable accumulator"""
    if not lst:
        return total
    return sum_list_good(lst[1:], total + lst[0])

print("sum_list_good([1, 2, 3]) =", sum_list_good([1, 2, 3]))
print("✓ Never use mutable default arguments in recursion!")

# Mistake 4: Stack overflow with deep recursion
print("\n❌ MISTAKE 4: Stack Overflow with Deep Recursion")
print("-" * 70)

import sys
print(f"Python's default recursion limit: {sys.getrecursionlimit()}")

# def deep_recursion(n):
#     if n <= 0:
#         return 0
#     return deep_recursion(n - 1) + 1

# deep_recursion(10000)  # CRASH! RecursionError

print("Solution 1: Use iteration for deep recursion")
print("Solution 2: Increase recursion limit (use with caution)")
print("Solution 3: Use tail recursion (if language optimizes it)")
print("✓ Python does NOT optimize tail recursion!")

# ============================================================================
# PART 4: Debugging Recursive Functions
# ============================================================================

print("\n" + "=" * 70)
print("PART 4: DEBUGGING RECURSIVE FUNCTIONS")
print("=" * 70)

# Technique 1: Add print statements
print("\n1. Technique: Add Trace Print Statements")
print("-" * 70)

def factorial_debug(n, depth=0):
    """Factorial with debug output showing call depth"""
    indent = "  " * depth
    print(f"{indent}→ factorial_debug({n})")
    
    if n <= 1:
        print(f"{indent}← returning 1 (base case)")
        return 1
    
    result = n * factorial_debug(n - 1, depth + 1)
    print(f"{indent}← returning {result}")
    return result

print("Tracing factorial_debug(4):")
factorial_debug(4)

# Technique 2: Visualize the call stack
print("\n2. Technique: Visualize Call Stack")
print("-" * 70)

def fibonacci_trace(n, depth=0):
    """Fibonacci with call tree visualization"""
    indent = "│  " * depth
    print(f"{indent}├─ fib({n})")
    
    if n <= 1:
        return n
    
    return fibonacci_trace(n - 1, depth + 1) + fibonacci_trace(n - 2, depth + 1)

print("Call tree for fibonacci_trace(4):")
result = fibonacci_trace(4)
print(f"Result: {result}")

# Technique 3: Use a call counter
print("\n3. Technique: Count Function Calls")
print("-" * 70)

call_count = 0

def fibonacci_count(n):
    """Count how many times function is called"""
    global call_count
    call_count += 1
    
    if n <= 1:
        return n
    return fibonacci_count(n - 1) + fibonacci_count(n - 2)

call_count = 0
result = fibonacci_count(10)
print(f"fibonacci_count(10) = {result}")
print(f"Total function calls: {call_count}")
print("(Shows why memoization is important!)")

# ============================================================================
# PART 5: When to Use (and NOT Use) Recursion
# ============================================================================

print("\n" + "=" * 70)
print("PART 5: WHEN TO USE RECURSION")
print("=" * 70)

print("""
✓ USE RECURSION when:
  • Problem has natural recursive structure (trees, graphs)
  • Divide and conquer algorithms (quicksort, merge sort)
  • Backtracking problems (N-queens, maze solving)
  • Mathematical definitions are naturally recursive
  • Code clarity is more important than absolute performance

✗ AVOID RECURSION when:
  • Simple iteration is clearer (summing a list)
  • Recursion depth could be very large (stack overflow risk)
  • Performance is critical and tail call optimization unavailable
  • Memory is constrained (each call uses stack space)

🎯 RECURSION CHECKLIST:
  1. Start with base case – write it first!
  2. Think "one level down" – assume recursive call works
  3. Ensure progress toward base case
  4. Test with small values (n=0, n=1, n=2)
  5. Consider iterative alternative for comparison
  6. Add memoization if subproblems overlap
  7. Use debugging traces for complex recursion
""")

# ============================================================================
# PART 6: Practical Examples Comparing Approaches
# ============================================================================

print("\n" + "=" * 70)
print("PART 6: PRACTICAL COMPARISON")
print("=" * 70)

print("\nProblem: Sum of list elements")
print("-" * 70)

# Recursive approach
def sum_recursive(lst):
    """Recursive sum - elegant but not practical"""
    if not lst:
        return 0
    return lst[0] + sum_recursive(lst[1:])

# Tail recursive approach
def sum_tail(lst, accumulator=0):
    """Tail recursive - better than regular recursion"""
    if not lst:
        return accumulator
    return sum_tail(lst[1:], accumulator + lst[0])

# Iterative approach
def sum_iterative(lst):
    """Iterative - most practical"""
    total = 0
    for item in lst:
        total += item
    return total

test_list = [1, 2, 3, 4, 5]
print(f"sum_recursive({test_list}) = {sum_recursive(test_list)}")
print(f"sum_tail({test_list}) = {sum_tail(test_list)}")
print(f"sum_iterative({test_list}) = {sum_iterative(test_list)}")
print(f"sum (built-in) = {sum(test_list)}")

print("\nRecommendation: Use built-in sum() or iteration!")
print("Recursion here is elegant but impractical.")

# ============================================================================
# SUMMARY TABLE
# ============================================================================

print("\n" + "=" * 70)
print("SUMMARY: Recursion Variants Comparison")
print("=" * 70)

print("""
Type              | Characteristics               | Use Case
------------------|-------------------------------|---------------------------
Linear            | One recursive call            | Factorial, countdown
Tree              | Multiple recursive calls      | Fibonacci, tree traversal
Tail              | Last operation is call        | Accumulator patterns
Mutual            | Functions call each other     | State machines, grammars
Memoized (dict)   | Cache with dictionary         | Unknown key space
Memoized (list)   | Cache with preallocated list  | Known integer range
@lru_cache        | Python's built-in cache       | Production code

Common Patterns:
• Base case → Recursive case → Return
• Accumulator pattern (tail recursion)
• Divide and conquer (split problem)
• Backtracking (try, fail, try another way)

Debugging Tools:
• Print statements with indentation
• Call tree visualization
• Call counters
• Python debugger (pdb)
• Trace decorators

Remember: Recursion is a tool, not a goal. Use it when it makes
code clearer and more maintainable, not just to be "clever".
""")

print("\n" + "=" * 70)
print("END OF RECURSION VARIANTS GUIDE")
print("=" * 70)
