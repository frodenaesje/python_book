# file: ex_06_02_magic_dates.py

def is_magic_date(day: int, month: int, year: int) -> bool:
    """Return True if day * month equals the last two digits of year."""
    return day * month == year % 100


if __name__ == "__main__":
    print("Magic dates in the 20th century:")
    for year in range(1900, 2000):
        for month in range(1, 13):
            for day in range(1, 32):
                if is_magic_date(day, month, year):
                    print(f"{day:02d}/{month:02d}/{year}")
