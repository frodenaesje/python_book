# file: ex_04_06_season.py

month = input("Enter month: ").strip().lower()
day = int(input("Enter day: "))

if ((month == "march" and day >= 20) or
        month in ("april", "may") or
        (month == "june" and day < 21)):
    season = "Spring"
elif ((month == "june" and day >= 21) or
        month in ("july", "august") or
        (month == "september" and day < 22)):
    season = "Summer"
elif ((month == "september" and day >= 22) or
        month in ("october", "november") or
        (month == "december" and day < 21)):
    season = "Autumn"
elif ((month == "december" and day >= 21) or
        month in ("january", "february") or
        (month == "march" and day < 20)):
    season = "Winter"
else:
    season = "Unknown"

print(f"Season: {season}")
