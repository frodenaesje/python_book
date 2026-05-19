# file: sc_04_03_parking.py
"""Parking fee examples for chapter 4.3.

The examples show how if, if-else, nested if-else, elif, chained comparisons,
and combined conditions can be used to decide an hourly rate and a final fee.

The first part of the file contains loose example code that is meant to be
read and understood step by step. Each snippet uses fixed values and prints
its result immediately. These examples are not a complete calculator by
themselves; they are concrete demonstrations of the language features that
make the final implementation easier to understand.

The later part of the file collects the same parking rules into a reusable
function, parking_fee(), and then verifies that function with example cases.
That final section is the real model: it applies the rule set consistently
and shows how the earlier if/else patterns appear in a complete calculation.
"""

from math import ceil

# 4.3.1 One-way if
# The simplest form: do something only if the condition is true.
# Nothing happens otherwise.
duration_min = 12  # minutes

if duration_min <= 15:
    print("Free - under 15 minutes.")

print()

# 4.3.2 Two-way if-else
# With else we ensure that something always happens.
is_weekend = True

if is_weekend:
    hourly_rate = 30 * 0.5    # 50% discount on weekends
else:
    hourly_rate = 30          # full price on weekdays

print(f"Hourly rate: {hourly_rate} NOK")
print()

# 4.3.3 Nested if-else
# Determine the base hourly rate based on the start time.
start_time = 19    # integer hours, 0-23

if start_time < 8:
    hourly_rate = 0
else:
    if start_time < 18:
        hourly_rate = 30
    else:
        if start_time < 22:
            hourly_rate = 15
        else:
            hourly_rate = 0

print(f"Nested if-else rate: {hourly_rate} NOK")
print()

# 4.3.4 elif - flatter and more readable
start_time = 19

if start_time < 8:
    hourly_rate = 0
elif start_time < 18:
    hourly_rate = 30
elif start_time < 22:
    hourly_rate = 15
else:
    hourly_rate = 0

print(f"Elif rate: {hourly_rate} NOK")
print()

# 4.3.5 Chained comparisons
# Python allows a readable interval test like 8 <= start_time < 18.
start_time = 14

if 8 <= start_time < 18:
    hourly_rate = 30
elif 18 <= start_time < 22:
    hourly_rate = 15
else:
    hourly_rate = 0

print(f"Chained comparison rate: {hourly_rate} NOK")
print()

# 4.3.6 if-else with combined conditions
is_weekend = False
is_ev = True

# Base rate by time of day
if 8 <= start_time < 18:
    hourly_rate = 30
elif 18 <= start_time < 22:
    hourly_rate = 15
else:
    hourly_rate = 0

# Discounts only apply if there is actually a rate
if hourly_rate > 0 and is_weekend:
    hourly_rate *= 0.5

if hourly_rate > 0 and is_ev:
    hourly_rate *= 0.5    # can be combined with weekend discount

print(f"Combined conditions rate: {hourly_rate} NOK")
print()


def parking_fee(duration_min: int,
                start_time: int,
                is_weekend: bool = False,
                is_ev: bool = False,
                has_disability: bool = False) -> int:
    """Compute a parking fee according to the chapter 4.3 model."""
    # First 15 minutes are always free.
    if duration_min <= 15:
        return 0

    # Disability permit gives free parking up to 6 hours.
    if has_disability and duration_min <= 360:
        return 0

    # Determine the base hourly rate by time of day.
    if 8 <= start_time < 18:
        hourly_rate = 30
    elif 18 <= start_time < 22:
        hourly_rate = 15
    else:
        hourly_rate = 0

    # Discounts only apply when a rate is positive.
    if hourly_rate > 0 and is_weekend:
        hourly_rate *= 0.5

    if hourly_rate > 0 and is_ev:
        hourly_rate *= 0.5

    # Calculate chargeable hours after the free 15 minutes.
    chargeable_minutes = max(duration_min - 15, 0)
    hours = ceil(chargeable_minutes / 60)
    fee = int(hourly_rate * hours)

    # Maximum daily price cap.
    if fee > 250:
        fee = 250

    return fee


# Example cases for manual verification
# These are not automated unit tests, but they demonstrate how the full
# parking_fee() function behaves for a few representative situations.
examples = [
    (12, 10, False, False, False),   # free under 15 minutes
    (45, 10, False, False, False),   # daytime, 1 hour charge
    (90, 19, False, False, False),   # evening, 2 hours charge
    (120, 23, False, False, False),  # night, free
    (90, 10, True, False, False),    # weekend discount
    (90, 10, True, True, False),     # weekend + EV
    (300, 10, False, False, True),   # disability permit under 6 hours free
    (480, 10, False, False, False),  # full day, capped at 250 NOK
]

for duration, start, weekend, ev, disability in examples:
    fee = parking_fee(duration, start, weekend, ev, disability)
    print(
        f"duration={duration} min, start={start}, weekend={weekend}, "
        f"ev={ev}, disability={disability} -> fee={fee} NOK"
    )
