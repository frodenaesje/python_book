# file: ex_06_09_bean_machine_start.py
import random

# TODO: Write drop_ball(num_rows: int) -> int
#       Simulates one ball dropping through num_rows pegs.
#       At each row the ball moves left (0) or right (1) randomly.
#       Hint: start at slot 0, add random.randint(0, 1) for each row.
#       Returns the final slot number (0 to num_rows).

# TODO: Write run_simulation(num_balls: int, num_rows: int) -> list
#       Drops num_balls balls through num_rows rows.
#       Returns a list of length num_rows + 1 with the count for each slot.
#       Hint: create a list of zeros, then for each ball call drop_ball()
#             and increment the corresponding slot counter.

# TODO: Write display_histogram(counts: list)
#       Prints one row per slot showing the count and a bar of asterisks.
#       Example: "Slot 3 (107):  *****..."
#       Hint: use one asterisk per ball for simplicity.

if __name__ == "__main__":
    NUM_BALLS = 500
    NUM_ROWS = 8

    print(f"Bean Machine - {NUM_BALLS} balls, {NUM_ROWS} rows\n")

    # TODO: Call run_simulation() and then display_histogram()
