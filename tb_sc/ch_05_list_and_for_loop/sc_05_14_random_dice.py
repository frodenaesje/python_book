# file: sc_05_14_random_dice.py
import random

NUM_ROLLS = 10000
NUM_SIDES = 6

# Indices 0 and 1 are unused - sum can be 2 to 12
frequency = [0] * 13

for _ in range(NUM_ROLLS):
    d1 = random.randint(1, NUM_SIDES)
    d2 = random.randint(1, NUM_SIDES)
    frequency[d1 + d2] += 1

print(f"{'Sum':>5}  {'Count':>7}  {'Share':>7}  {'Expected':>10}")
print("-" * 35)
for dot_sum in range(2, 13):
    count    = frequency[dot_sum]
    share    = count / NUM_ROLLS
    expected = (6 - abs(dot_sum - 7)) / 36
    print(f"{dot_sum:>5}  {count:>7}  {share:>7.1%}  {expected:>10.1%}")
