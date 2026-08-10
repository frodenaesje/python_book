# file: sc_04_05_alternative_ways_choices.py
# description: Alternative ways to make choices in Python
# finding the name of a weekday

# with if-elif-else statements
day = 3
if day == 1:   name = "Monday" # single-line if statement here & below
elif day == 2: name = "Tuesday"
elif day == 3: name = "Wednesday"
# ... etc.
else:          name = "Invalid day"
print(name)

# with a list (indexing):
day      = 3
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"]

if 1 <= day <= 7:
    print(weekdays[day - 1])    # day 1 -> index 0
else:
    print("Invalid day")

# with a dictionary (key-value pairs):
day      = 3
weekdays = {1: "Monday", 2: "Tuesday", 3: "Wednesday",
            4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}

print(weekdays.get(day, "Invalid day"))
