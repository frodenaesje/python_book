# file: sc_07_10_meeting_time.py

# Hours (24-hour clock) when each person is available
available: dict[str, set[int]] = {
    "Alice":   {9, 10, 11, 14, 15},
    "Bob":     {10, 11, 12, 13, 14},
    "Charlie": {8, 9, 10, 14, 15, 16},
    "Diana":   {10, 12, 13, 14, 16},
}

everyone = set(available)            # the keys: all the names
all_hours: set[int] = set()
common_hours = set(range(24))

for hours in available.values():
    all_hours |= hours               # union: at least one person
    common_hours &= hours            # intersection: every person

print(f"Hours that suit everyone: {sorted(common_hours)}")
print()
print(f"{'Hour':<7}{'Can':>4}  Missing")
for hour in sorted(all_hours):
    can_attend = {name for name, hours in available.items() if hour in hours}
    missing = everyone - can_attend
    print(f"{hour:02}:00  {len(can_attend):>4}  {', '.join(sorted(missing))}")
