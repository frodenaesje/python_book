# file: sc_11_17_csv_dict.py
import csv
from pathlib import Path

FILENAME = Path(__file__).resolve().parent / "vehicles.csv"

# Write with DictWriter
fieldnames = ["reg_no", "brand", "model", "year"]
rows = [
    {
        "reg_no": "EL67820",
        "brand": "Tesla",
        "model": "Model 3",
        "year": 2021,
    },
    {
        "reg_no": "NB72826",
        "brand": "Toyota",
        "model": "Yaris",
        "year": 2019,
    },
    {
        "reg_no": "AB12345",
        "brand": "Volvo",
        "model": "XC60",
        "year": 2022,
    },
]

with open(FILENAME, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    # Writes header row automatically.
    writer.writeheader()
    writer.writerows(rows)

# Read with DictReader
with open(FILENAME, "r", newline="", encoding="utf-8") as f:
    # Uses the first line as column names automatically.
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['reg_no']}: "
              f"{row['brand']} {row['model']} "
              f"({row['year']})")
