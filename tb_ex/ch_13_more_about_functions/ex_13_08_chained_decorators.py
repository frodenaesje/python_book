# file: ex_13_08_chained_decorators.py
from ex_13_04_timing_decorator import timer
from ex_13_05_logging_decorator import log_call

# Order 1: timer is outermost
# Equivalent: compute = timer(log_call(compute))
# timer's wrapper runs first -> log_call's wrapper (named "wrapper") is what gets timed
@timer
@log_call
def compute(n):
    return sum(range(n))

# Order 2: log_call is outermost
# Equivalent: compute2 = log_call(timer(compute2))
# log_call's wrapper runs first -> timer's wrapper (named "wrapper") is what gets logged
@log_call
@timer
def compute2(n):
    return sum(range(n))


if __name__ == "__main__":
    print("--- Order 1: @timer above @log_call ---")
    compute(1_000_000)

    print()
    print("--- Order 2: @log_call above @timer ---")
    compute2(1_000_000)
