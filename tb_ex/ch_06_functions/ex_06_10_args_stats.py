# file: ex_06_10_args_stats.py

def total(*numbers: float) -> float:
    """Return the sum of all arguments."""
    result = 0.0
    for n in numbers:
        result += n
    return result


def average(*numbers: float) -> float:
    """Return the mean of all arguments."""
    return total(*numbers) / len(numbers)


def stats(*numbers: float) -> tuple:
    """Return (min, max, mean) for all arguments."""
    low = numbers[0]
    high = numbers[0]
    for n in numbers:
        if n < low:
            low = n
        if n > high:
            high = n
    return low, high, average(*numbers)


if __name__ == "__main__":
    print(f"total(1, 2, 3):          {total(1, 2, 3)}")
    print(f"average(1, 2, 3, 4, 5):  {average(1, 2, 3, 4, 5)}")
    low, high, mean = stats(4, 7, 2, 9, 1)
    print(f"stats(4, 7, 2, 9, 1):    min={low}, max={high}, mean={mean}")
