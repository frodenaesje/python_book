# file: ex_05_07_rolling_two_dice_start.py
import random

NUM_RUNS = 1000

# TODO: Create a list of 13 zeros for counting sums (indices 0 and 1 unused)

# TODO: Simulate NUM_RUNS rolls of two dice
#       Hint: use random.randint(1, 6) for each die
#       Add the two dice values and increment the corresponding counter

# TODO: Create a list of expected probabilities for sums 2-12
#       expected = [0, 0, 1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]

# TODO: Print the header
#       Example:
#       "  Total   Simulated   Expected"
#       "           Percent    Percent"

# TODO: Print one row per sum (2 to 12)
#       Show: sum, simulated percent, expected percent
#       Hint: simulated percent = counts[i] / NUM_RUNS * 100
#             expected percent  = expected[i] * 100
