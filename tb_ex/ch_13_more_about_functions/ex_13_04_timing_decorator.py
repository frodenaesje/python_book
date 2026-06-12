# file: ex_13_04_timing_decorator.py
import time


def timer(func):
    """Decorator that prints the execution time of func in milliseconds."""
    def wrapper(*args, **kwargs):
        start  = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_ms = (time.perf_counter() - start) * 1000
        print(f"{func.__name__}() took {elapsed_ms:.2f} ms")
        return result
    return wrapper


@timer
def find_primes():
    """Find all primes below 100 000 using trial division."""
    primes = []
    for n in range(2, 100_000):
        is_prime = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
    return primes


@timer
def fibonacci(n):
    """Return the nth Fibonacci number recursively."""
    if n <= 1:
        return n
    return fibonacci.__wrapped__(n - 1) + fibonacci.__wrapped__(n - 2) \
        if hasattr(fibonacci, '__wrapped__') \
        else _fib(n)


def _fib(n):
    if n <= 1:
        return n
    return _fib(n - 1) + _fib(n - 2)


@timer
def sort_words(text, reverse=False):
    """Split text into words, sort them, and return as a string."""
    words = text.split()
    return " ".join(sorted(words, reverse=reverse))


if __name__ == "__main__":
    primes = find_primes()
    print(f"Found {len(primes)} primes\n")

    result = sort_words("banana apple cherry kiwi mango")
    print(f"Sorted: {result}\n")

    result2 = sort_words("banana apple cherry", reverse=True)
    print(f"Sorted desc: {result2}")
