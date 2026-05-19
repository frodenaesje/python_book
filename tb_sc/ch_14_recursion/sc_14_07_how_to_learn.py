# File: sc_14_07_how_to_learn.py
"""
How to get good at recursion: Step-by-step guide
"""

print("=" * 60)
print("HOW TO GET GOOD AT RECURSION")
print("=" * 60)

print("\n" + "=" * 60)
print("STEP 1: Start Simple")
print("=" * 60)
print("""
Begin with the simplest recursive problems:
  • Countdown
  • Sum of numbers
  • Factorial
  
These teach you the fundamental pattern:
  1. Identify the base case
  2. Make a recursive call with a simpler problem
  3. Return or use the result
  
Practice writing these from scratch until it becomes natural.
""")

# Simple example to practice
print("\nPractice Example: Print numbers from n down to 1")
print("-" * 40)

def print_numbers(n):
    """Print numbers from n down to 1"""
    if n == 0:  # Base case
        return
    print(n)
    print_numbers(n - 1)  # Recursive case

print("print_numbers(5):")
print_numbers(5)

print("\n" + "=" * 60)
print("STEP 2: Think in Subproblems")
print("=" * 60)
print("""
Ask yourself: "How can I solve a smaller version of this problem?"

Example: Sum of a list
  sum([1, 2, 3, 4, 5])
  = 1 + sum([2, 3, 4, 5])    ← Smaller problem!
  = 1 + (2 + sum([3, 4, 5]))
  = 1 + (2 + (3 + sum([4, 5])))
  ...
  
The key insight:
  "If I can solve it for n-1, I can solve it for n"
  
Don't try to trace all the recursive calls in your head!
Just focus on:
  1. Base case (simplest version)
  2. One recursive step (how to reduce the problem)
""")

# Example to demonstrate thinking in subproblems
print("\nExample: Length of a list")
print("-" * 40)

def length(lst):
    """Calculate length of list recursively"""
    if not lst:  # Base case: empty list has length 0
        return 0
    # Recursive case: 1 + length of rest
    return 1 + length(lst[1:])

test_list = [10, 20, 30, 40]
print(f"length({test_list}) = {length(test_list)}")
print("\nThought process:")
print("  length([10, 20, 30, 40]) = 1 + length([20, 30, 40])")
print("  length([20, 30, 40])     = 1 + length([30, 40])")
print("  length([30, 40])         = 1 + length([40])")
print("  length([40])             = 1 + length([])")
print("  length([])               = 0  [BASE CASE]")

print("\n" + "=" * 60)
print("STEP 3: Write the Base Case First")
print("=" * 60)
print("""
The base case is your "safety net" - it stops infinite recursion.

Strategy:
  1. Think: "What's the simplest input?"
  2. Write the base case first
  3. Test with that simple input
  4. Only then write the recursive case
  
Common base cases:
  • n == 0 or n == 1  (for numbers)
  • lst == []         (for lists)
  • str == ""         (for strings)
  • node == None      (for trees)
  
Always test with base case inputs first!
""")

# Example: Reverse a string
print("\nExample: Reverse a string")
print("-" * 40)

def reverse_string(s):
    """Reverse a string recursively"""
    # Base case: empty string or single character
    if len(s) <= 1:
        return s
    # Recursive case: last char + reverse of rest
    return s[-1] + reverse_string(s[:-1])

test_string = "hello"
print(f"reverse_string('{test_string}') = '{reverse_string(test_string)}'")
print("\nBase case testing:")
print(f"  reverse_string('') = '{reverse_string('')}'")
print(f"  reverse_string('a') = '{reverse_string('a')}'")

print("\n" + "=" * 60)
print("STEP 4: Visualize the Call Stack")
print("=" * 60)
print("""
Draw or write out how the function calls itself.

Example for factorial(4):

  factorial(4)
  ├─ 4 * factorial(3)
  │      ├─ 3 * factorial(2)
  │      │      ├─ 2 * factorial(1)
  │      │      │      └─ returns 1  [BASE CASE]
  │      │      └─ returns 2 * 1 = 2
  │      └─ returns 3 * 2 = 6
  └─ returns 4 * 6 = 24
  
This visualization helps you understand:
  • How the stack grows (going down)
  • When the base case is hit
  • How values return (going back up)
""")

# Demonstrate with trace output
print("\nFactorial with trace:")
print("-" * 40)

def factorial_trace(n, indent=0):
    """Factorial with visualization of recursion"""
    prefix = "  " * indent
    print(f"{prefix}factorial({n}) called")
    
    if n <= 1:
        print(f"{prefix}→ Base case! Returning 1")
        return 1
    
    result = n * factorial_trace(n - 1, indent + 1)
    print(f"{prefix}→ Returning {n} * {result // n} = {result}")
    return result

print("\nfactorial_trace(4):")
result = factorial_trace(4)
print(f"\nFinal result: {result}")

print("\n" + "=" * 60)
print("STEP 5: Compare with Iteration")
print("=" * 60)
print("""
For each recursive function, try writing an iterative version.

This helps you:
  • Understand what the recursion is really doing
  • See when recursion is clearer
  • See when iteration is better
  • Build intuition for both approaches
  
Exercise: Write both versions for:
  • Sum of list
  • Finding maximum
  • Reversing a string
  • Computing powers (x^n)
""")

# Example: Power function
print("\nExample: Computing x^n")
print("-" * 40)

def power_recursive(x, n):
    """Calculate x^n recursively"""
    if n == 0:
        return 1
    return x * power_recursive(x, n - 1)

def power_iterative(x, n):
    """Calculate x^n iteratively"""
    result = 1
    for _ in range(n):
        result *= x
    return result

x, n = 2, 5
print(f"power_recursive({x}, {n}) = {power_recursive(x, n)}")
print(f"power_iterative({x}, {n}) = {power_iterative(x, n)}")

print("\n" + "=" * 60)
print("STEP 6: Practice, Practice, Practice")
print("=" * 60)
print("""
The only way to truly understand recursion is through practice.

Beginner exercises:
  ☐ Count occurrences of a character in a string
  ☐ Check if a string is a palindrome
  ☐ Calculate GCD (greatest common divisor)
  ☐ Generate all subsets of a set
  
Intermediate exercises:
  ☐ Binary search in a sorted list
  ☐ Flatten a nested list
  ☐ Generate all permutations
  ☐ Solve Tower of Hanoi
  
Advanced exercises:
  ☐ Traverse a binary tree
  ☐ Solve N-Queens problem
  ☐ Implement merge sort
  ☐ Solve Sudoku with backtracking
  
Start with the beginner exercises and work your way up!
""")

# Beginner exercise example
print("\nBeginner Exercise: Count occurrences")
print("-" * 40)

def count_char(s, char):
    """Count occurrences of char in string s"""
    if not s:  # Base case: empty string
        return 0
    # Check first character, then add count from rest
    count_first = 1 if s[0] == char else 0
    return count_first + count_char(s[1:], char)

test_string = "hello world"
test_char = "l"
print(f"count_char('{test_string}', '{test_char}') = {count_char(test_string, test_char)}")

print("\n" + "=" * 60)
print("SUMMARY: Your Learning Path")
print("=" * 60)
print("""
Week 1: Master the basics
  • Countdown, sum, factorial
  • Understand base case and recursive case
  • Practice visualizing the stack
  
Week 2: Build confidence
  • String manipulation (reverse, palindrome)
  • List operations (length, sum, max)
  • Compare recursive and iterative solutions
  
Week 3: Tackle harder problems
  • Tower of Hanoi
  • Generate permutations
  • Binary search
  
Week 4+: Real-world applications
  • Tree traversal
  • Backtracking problems
  • Divide-and-conquer algorithms
  
Remember:
  • Start simple and build up gradually
  • Visualize the recursion
  • Practice both writing and reading recursive code
  • Don't get discouraged - recursion takes time to "click"!
  
The moment of understanding will come, and when it does,
recursion will become one of your most powerful tools!
""")
