# file: sc_07_06_constructor_calls_as_values.py

from datetime import datetime

# Constructor calls can be used directly as dictionary values.
# Python creates the datetime objects when the dictionary is defined.
passages = {
    "NB72826": datetime(2022, 1, 3, 7, 11, 41),
    "FY99401": datetime(2022, 1, 3, 7, 22, 33),
}

# The values are already datetime objects, so their methods can be used directly.
for reg, ts in passages.items():
    print(f"{reg}: {ts.strftime('%Y-%m-%d %H:%M:%S')}")


# strftime() converts a datetime object to a formatted string.
# The format codes specify how the date and time should be displayed.
ts = datetime(2022, 1, 3, 7, 11, 41)

print(ts.strftime("%Y-%m-%d %H:%M:%S"))   # 2022-01-03 07:11:41
print(ts.strftime("%d.%m.%Y kl. %H:%M"))  # 03.01.2022 kl. 07:11
