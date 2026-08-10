# file: ex_14_05_tower_of_hanoi.py

def hanoi(n, source, target, auxiliary, counter):
    """Solve Tower of Hanoi and increment counter[0] for each move."""
    if n == 0:
        return
    hanoi(n - 1, source, auxiliary, target, counter)
    counter[0] += 1
    hanoi(n - 1, auxiliary, target, source, counter)


def format_time(seconds):
    """Convert a number of seconds to a human-readable string."""
    # TODO: convert seconds to minutes, hours, days, years
    # divmod(seconds, 60) gives (minutes, remaining_seconds)
    # continue up through hours, days, years (365 days)
    # return the largest non-zero unit as a string
    pass


if __name__ == "__main__":
    # TODO: for n in range(1, 16):
    #         count moves using hanoi() with a counter = [0]
    #         print n, moves, and verify against 2**n - 1

    print()
    # TODO: for n in [10, 20, 30, 64]:
    #         compute 2**n - 1 seconds and print format_time()
