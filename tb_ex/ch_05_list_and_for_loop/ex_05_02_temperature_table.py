# file: ex_05_02_temperature_table.py

print(f"{'Celsius':>10}{'Fahrenheit':>12}")
for c in range(0, 101, 10):
    f = c * 9 / 5 + 32
    print(f"{c:>10}{f:>12.1f}")
