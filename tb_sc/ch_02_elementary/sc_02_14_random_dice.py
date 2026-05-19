# file: sc_02_14_random_dice.py
import random

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
total_dots = die1 + die2

print(f"Die 1: {die1}")
print(f"Die 2: {die2}")
print(f"Sum:       {total_dots}")
