# file: sc_18_01_performance_libear.py
# Demonstrates linear time complexity O(N) by measuring execution time
# for increasing input sizes.
# The time taken should increase linearly with input size.

import time

def getTime(n):
    # Note: time.time() cannot be used here because it has insufficient resolution
    # for measuring very fast operations.
    # time.perf_counter() provides higher precision
    # and is not affected by system clock adjustments.
    # perf_counter() measure the time im micrrosecons,
    # and is 1000 times more precise than time.time()
    startTime = time.perf_counter()
    m = 0
    for _ in range(n):
        m = m + 1 # do something that takes constant time
    endTime = time.perf_counter()
    return(endTime - startTime)

def main():
    duration = [0] * 4
    size = [10000, 100000, 1000000, 10000000]
    duration[0] = getTime(size[0])
    duration[1] = getTime(size[1])
    duration[2] = getTime(size[2])
    duration[3] = getTime(size[3])
    for i in range(len(size)):
        print(f"Size: {size[i]:>10} | Runtime: {duration[i]:.6f}s")
    
    print("\nRatios (should be ~10 for O(N) complexity):")
    for i in range(1, len(size)):
        ratio = duration[i] / duration[i-1] if duration[i-1] > 0 else 0
        size_ratio = size[i] / size[i-1]
        print(f"  N ratio: {size_ratio:.1f}x → Time ratio: {ratio:.2f}x")

main()