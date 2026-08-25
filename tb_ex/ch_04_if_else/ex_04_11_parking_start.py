"""
Exercise 04.11 - Parking fee  --  START

The input code is written for you. Add your if-else logic below it: work
out the fee and print it. Watch the mixed conditions - above all a car
that is BOTH weekend and electric (it must get both discounts).
"""

# ---- input (ready-made, do not change) ----
start_hour = int(input("Start hour (0-23): "))
duration_min = int(input("Duration in minutes: "))
weekend = input("Weekend? (y/n): ").strip().lower().startswith("y")
electric = input("Electric vehicle? (y/n): ").strip().lower().startswith("y")
disability = input("Disability permit? (y/n): ").strip().lower().startswith("y")

# ---- your logic below ----
# 1) hourly rate from start_hour:   08-18 is 30,   18-22 is 15,   else 0
# 2) free_minutes:                  360 if disability else 15
# 3) billable = duration_min - free_minutes     (not below 0)
# 4) cost = rate * billable / 60
# 5) discounts: halve for weekend, halve for electric - BOTH can apply,
#               so use two separate 'if's, not an if/elif chain
# 6) cap the cost at 250
# 7) print:  f"Parking fee: {cost:.2f}"
