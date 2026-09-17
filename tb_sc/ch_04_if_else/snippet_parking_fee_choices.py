# file: snippet_parking_fee_choices.py
# Parking-fee rules illustrate one-way, two-way and multiple choices.
# Separate discount conditions allow both discounts to apply.

# One-way if
duration_min = 12

if duration_min <= 15:
    print("Free - under 15 minutes.")

# Two-way if-else
is_weekend = True

if is_weekend:
    hourly_rate = 30 * 0.5
else:
    hourly_rate = 30

print(f"Hourly rate: {hourly_rate}")

# Nested if-else
start_time = 19

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

print(f"Hourly rate: {hourly_rate}")

# The same choice with elif
start_time = 19

if start_time < 8:
    hourly_rate = 0
elif start_time < 18:
    hourly_rate = 30
elif start_time < 22:
    hourly_rate = 15
else:
    hourly_rate = 0

print(f"Hourly rate: {hourly_rate}")

# Combined conditions
start_time = 14
is_weekend = False
is_ev = True

if 8 <= start_time < 18:
    hourly_rate = 30
elif 18 <= start_time < 22:
    hourly_rate = 15
else:
    hourly_rate = 0

if hourly_rate > 0 and is_weekend:
    hourly_rate *= 0.5

if hourly_rate > 0 and is_ev:
    hourly_rate *= 0.5

print(f"Hourly rate: {hourly_rate}")
