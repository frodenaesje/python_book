# file: sorting.py
# Comparing measured execution times of sorting algorithms
# to their theoretical big-O predictions.

# Also given as exercise with missing implementation of theoretical_time()
from random import randint
from timeit import repeat
import importlib
import os
import sys
import math

# algorithms available for benchmarking
ALGORITHMS = [
    "insertion_sort",
    "selection_sort",
    "merge_sort",
    "tim_sort",
    "quick_sort",
    "heap_sort"
]

# default sizes if none provided on command line
DEFAULT_SIZES = [1000, 5000, 10000]

# ensure current directory (where sorting.py lives) is on import path
sys.path.insert(0, os.path.dirname(__file__))

def run_sorting_algorithm(algorithm, array):
    # dynamically import the module and get the sorting function
    try:
        module = importlib.import_module(algorithm)
        func = getattr(module, algorithm)
    except Exception:
        raise

    # run the function multiple times on a fresh copy of the array
    times = repeat(lambda: func(list(array)), repeat=1, number=3)
    elapsed = min(times)
    print(f"Algorithm: {algorithm}. Minimum execution time: {elapsed}")
    return elapsed

def benchmark(algorithms, sizes):
    """Run the benchmark for each algorithm and array size.

    Returns a dict mapping ``(algorithm, size)`` to minimum execution time.
    """
    results = {}
    for length in sizes:
        print(f"\n=== array length {length} ===")
        base = [randint(0, 1000) for _ in range(length)]
        for alg in algorithms:
            arr = list(base)
            try:
                elapsed = run_sorting_algorithm(algorithm=alg, array=arr)
                results[(alg, length)] = elapsed
            except Exception as exc:
                print(f"Could not run {alg}: {exc}")
    return results


def theoretical_time(algorithm, n):
    """Return a theoretical cost for *algorithm* on input size *n*.

    Values are unscaled; they reflect the standard asymptotic growth.
    """
    if algorithm in ("insertion_sort", "selection_sort", "bubble_sort"):
        return n * n
    # n log n sorts
    if algorithm in ("merge_sort", "tim_sort", "quick_sort", "heap_sort"):
        return n * math.log2(n) if n > 0 else 0
    # default fall-back
    return n


def compare_with_big_o(algorithms, sizes):
    """Run benchmarks and display measured vs theoretical predictions."""
    print("Running measurements…")
    measured = benchmark(algorithms, sizes)

    # calculate scaling factors so theoretical numbers are in same ballpark
    scaling = {}
    for alg in algorithms:
        # use first size as reference
        ref_size = sizes[0]
        mt = measured.get((alg, ref_size), None)
        if mt is not None:
            scaling[alg] = mt / theoretical_time(alg, ref_size) if theoretical_time(alg, ref_size) > 0 else 1
        else:
            scaling[alg] = 1

    print("\nMeasured vs expected (scaled) times:")
    for alg in algorithms:
        for n in sizes:
            mt = measured.get((alg, n), None)
            if mt is None:
                continue
            expected = theoretical_time(alg, n) * scaling.get(alg, 1)
            print(f"{alg:12} n={n:6} measured={mt:.6f}s expected~{expected:.6f}s")


if __name__ == "__main__":
   
    sizes = DEFAULT_SIZES

    print(f"Running algorithms: {ALGORITHMS}")
    # always compare measured to theoretical
    compare_with_big_o(ALGORITHMS, sizes)
