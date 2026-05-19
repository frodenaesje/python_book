# File: sc_14_01_countdown.py
"""
Recursion: Countdown - The simplest recursive example
Introduction to base case and recursive case
"""

print("=" * 60)
print("COUNTDOWN - The Simplest Recursive Example")
print("=" * 60)

print("\n" + "-" * 60)
print("What is Recursion?")
print("-" * 60)
print("""
RECURSION means a function calls itself to solve a problem.

Think of it as breaking a big problem into smaller pieces,
until the pieces are so small they can be solved directly.

Key components:
  1. BASE CASE - The simplest version that can be solved directly
  2. RECURSIVE CASE - The function calls itself with a simpler problem
""")

print("\n" + "=" * 60)
print("RECURSIVE COUNTDOWN")
print("=" * 60)

def countdown(n):
    """Count down from n to 1, then print 'Ferdig!'"""
    if n == 0:  # BASE CASE: Stop when n reaches 0
        print("Ferdig!")
    else:       # RECURSIVE CASE: Print n, then call with n-1
        print(n)
        countdown(n - 1)  # Function calls itself!

print("\nRecursive countdown(5):")
countdown(5)

print("\n" + "-" * 60)
print("How it works:")
print("-" * 60)
print("""
countdown(5):
  → prints 5
  → calls countdown(4)
      → prints 4
      → calls countdown(3)
          → prints 3
          → calls countdown(2)
              → prints 2
              → calls countdown(1)
                  → prints 1
                  → calls countdown(0)
                      → BASE CASE! prints "Ferdig!"
""")

print("\n" + "=" * 60)
print("ITERATIVE COUNTDOWN (for comparison)")
print("=" * 60)

def countdown_iter(n):
    """Same result using a loop instead of recursion"""
    while n > 0:
        print(n)
        n -= 1
    print("Ferdig!")

print("\nIterative countdown_iter(5):")
countdown_iter(5)

print("\n" + "-" * 60)
print("Recursion vs Iteration:")
print("-" * 60)
print("""
Recursive version:
  • More elegant and self-descriptive
  • Uses the call stack
  • Can hit stack limit for large n
  
Iterative version:
  • More explicit about what's happening
  • Uses a loop variable
  • No stack limit concerns
  
For countdown, iteration is simpler and more efficient.
But recursion teaches the fundamental pattern!
""")

print("\n" + "=" * 60)
print("TRY IT YOURSELF")
print("=" * 60)

print("\nExercise 1: Count up instead of down")
print("-" * 40)
print("Write count_up(n) that prints 1, 2, 3, ..., n")
print("Hint: Base case is when n == 1")

print("\nExercise 2: Print with stars")
print("-" * 40)
print("Write countdown_stars(n) that prints:")
print("  5 *****")
print("  4 ****")
print("  3 ***")
print("  2 **")
print("  1 *")
print("  Ferdig!")

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. Recursion = A function calling itself
2. Always need a BASE CASE to stop
3. Each recursive call should be SIMPLER
4. The call stack keeps track of all layers
5. Countdown is the simplest example to understand the pattern

Next steps:
  • See sc_15_02_sum.py for recursion with return values
  • See sc_15_03_factorial.py for a classic example
  • See sc_15_01_tower_of_hanoi.py for a complex problem
""")