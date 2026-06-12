# file: ex_04_04_days_in_month.py

month = input("Enter month name: ")
month_normalized = month.strip().lower()

match month_normalized:
    case "february":
        days = "28 or 29 days"
    case "april" | "june" | "september" | "november":
        days = "30 days"
    case "january" | "march" | "may" | "july" | "august" | "october" | "december":
        days = "31 days"
    case _:
        days = None

if days:
    print(f"{month} has {days}.")
else:
    print("Unknown month.")
