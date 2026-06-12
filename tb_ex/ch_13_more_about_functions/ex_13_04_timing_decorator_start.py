# file: ex_13_04_timing_decorator_start.py
import time


def timer(func):
    """Decorator that prints the execution time of func in milliseconds."""
    def wrapper(*args, **kwargs):
        # TODO: record start time with time.perf_counter()
        # TODO: call func(*args, **kwargs) and store the result
        # TODO: record end time and compute elapsed milliseconds
        # TODO: print the function name and elapsed time
        #       Example: "find_primes() took 18.43 ms"
        # TODO: return the result
        pass
    return wrapper


# TODO: Apply @timer to three functions:

# 1. A function with no parameters
#    e.g. find all primes below 100 000 using trial division
@timer
def find_primes():
    pass  # TODO: implement

# 2. A function with one parameter
@timer
def fibonacci(n):
    pass  # TODO: implement (recursive is fine for demonstrating timing)

# 3. A function with two parameters
@timer
def sort_words(text, reverse=False):
    pass  # TODO: split text, sort, return joined result


if __name__ == "__main__":
    find_primes()
    fibonacci(35)
    sort_words("banana apple cherry kiwi mango")
