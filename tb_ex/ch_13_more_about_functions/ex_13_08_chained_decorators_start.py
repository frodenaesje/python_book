# file: ex_13_08_chained_decorators_start.py
from ex_13_04_timing_decorator import timer
from ex_13_05_logging_decorator import log_call

# TODO: Apply @timer (outer) and @log_call (inner) to compute
# Order 1: timer is outermost - it runs first
@timer
@log_call
def compute(n):
    return sum(range(n))

# TODO: Apply @log_call (outer) and @timer (inner) to compute2
# Order 2: log_call is outermost - it runs first
@log_call
@timer
def compute2(n):
    return sum(range(n))

# TODO: Add a comment for each function explaining:
#   - which decorator is the outermost wrapper
#   - what the equivalent non-@ syntax looks like
#     e.g. compute = timer(log_call(compute))

if __name__ == "__main__":
    print("--- Order 1: @timer above @log_call ---")
    compute(1_000_000)

    print()
    print("--- Order 2: @log_call above @timer ---")
    compute2(1_000_000)
