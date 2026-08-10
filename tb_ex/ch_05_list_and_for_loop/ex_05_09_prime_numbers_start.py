# file: ex_05_09_prime_numbers_start.py
import math

# --- Part 1: check a single number ---

n = int(input("Enter a number: "))

# TODO: Check if n is prime using trial division
#       - Numbers <= 1 are not prime
#       - Check all divisors from 2 up to int(n**0.5) + 1
#       - If any divisor divides n evenly: not prime, break early
#       - Use a flag variable: is_prime = True, set to False if a divisor is found

# TODO: Print the result
#       Example: "17 is prime."  or  "42 is not prime."


# --- Part 2: all primes up to 100 ---

print("\nPrime numbers up to 100:")

# TODO: Loop through all numbers from 2 to 100
#       For each number, check if it is prime (same algorithm as Part 1)
#       Print primes on one line separated by spaces
#       Hint: use print(n, end=" ") to print without newline
