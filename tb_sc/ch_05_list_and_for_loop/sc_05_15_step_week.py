# file: sc_05_15_step_week.py
DAILY_GOAL = 10000

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
steps = [8200, 11450, 6300, 10020, 4900, 15800, 9100]

print(f"{'Day':<6}{'Steps':>8}")
print("-" * 14)
for day, count in zip(days, steps):
    marker = " *" if count >= DAILY_GOAL else ""
    print(f"{day:<6}{count:>8,}{marker}")
print("-" * 14)

total = sum(steps)
average = total / len(steps)
best_day = days[steps.index(max(steps))]
goal_days = [day for day, count in zip(days, steps) if count >= DAILY_GOAL]

print(f"Total:    {total:,} steps")
print(f"Average:  {average:,.0f} steps per day")
print(f"Best day: {best_day} ({max(steps):,} steps)")
print(f"Goal reached on {len(goal_days)} days: {', '.join(goal_days)}")
