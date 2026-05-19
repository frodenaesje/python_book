# file: sc_05_15_lotto.py
import random
import math

NUM_NUMBERS = 34
DRAW_SIZE = 7

def simulate(num_draws: int) -> list[int]:
    # random.sample() draws unique numbers without manually
    # handling removal
    frequency = [0] * (NUM_NUMBERS + 1)
    for _ in range(num_draws):
        for num in random.sample(
            range(1, NUM_NUMBERS + 1),
            DRAW_SIZE
        ):
            frequency[num] += 1
    return frequency

def print_results(frequency: list[int], num_draws: int) -> None:
    expected = num_draws * DRAW_SIZE / NUM_NUMBERS
    print(
        f"\n--- {num_draws} draws "
        f"(expected per number: {expected:.1f}) ---"
    )
    # enumerate(frequency[1:], start=1) gives (number, count)
    # directly - no manual index handling
    for num, count in enumerate(frequency[1:], start=1):
        deviation_pct = (count - expected) / expected * 100
        print(
            f"  Number {num:2}: {count:6}  "
            f"deviation: {deviation_pct:+.1f}%"
        )

for n in [10, 100, 1000, 1_000_000]:
    print_results(simulate(n), n)

combinations = math.comb(NUM_NUMBERS, DRAW_SIZE)
probability  = 1 / combinations
print(f"\n--- All combinations are equally likely ---")
print(f"Number of possible combinations: {combinations:,}")
print(f"  [1, 2, 3, 4, 5, 6, 7]:       {probability:.10f}")
print(f"  [3, 9, 14, 21, 27, 31, 34]:  {probability:.10f}")
print("Exactly the same - order and pattern make no difference.")