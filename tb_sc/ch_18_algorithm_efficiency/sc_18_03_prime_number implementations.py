# file: sc_18_03_prime_number implementations.py
from math import sqrt

def prime_half(n):
    """
    Test divisorer bare opp til number/2.
       
    Logikk: En divisor kan aldri være større enn number/2
    (bortsett fra number selv).
    
    Kompleksitet: O(n²/2) → O(n²)
    """
    primes = []
    for number in range(2, n + 1):
        is_prime = True
        # Tester opp til number/2 i stedet for number-1
        for divisor in range(2, number // 2 + 1):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    return primes


def prime_brute_force(n):
    primes = []
    for number in range(2, n + 1):
        is_prime = True
        for divisor in range(2, int(sqrt(number)) + 1):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    return primes


def prims(n):
    # Klassisk implementasjon: Sieve of Eratosthenes
    # Initialiserer en boolean-array hvor True = "mulig primtall"
    # Markerer deretter alle multipler som False (ikke primtall)
    
    if n < 2:
        return []
    
    # Initialiserer: is_prime[i] = True for alle tall fra 0 til n
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 og 1 er ikke primtall
    
    # For hvert primtall p opp til sqrt(n):
    for p in range(2, int(sqrt(n)) + 1):
        if is_prime[p]:
            # Markerer alle multipler av p som ikke-primtall
            # Start fra p² (mindre multipler er allerede markert av mindre primtall)
            start = p * p
            for multiple in range(start, n + 1, p):
                is_prime[multiple] = False
    
    # Samler alle tall som er markert som primtall
    primes = [num for num in range(2, n + 1) if is_prime[num]]
    return primes


def print_primes(label, primes, number_per_line):
    print(f"{label}:")
    for index, prime in enumerate(primes, start=1):
        end_char = "\n" if index % number_per_line == 0 else ""
        print(f" {prime}", end=end_char)
    print(f"\n{len(primes)} prime(s) less than or equal to {primes[-1] if primes else 1}")

def main():
    n = int(input("Find all prime numbers <= n, enter n: "))
    number_per_line = 10
    print_primes("Half (opp til n/2)", prime_half(n), number_per_line)
    print()
    print_primes("Brute force (opp til √n)", prime_brute_force(n), number_per_line)
    print()
    print_primes("Sieve (Eratosthenes)", prims(n), number_per_line)


main()
