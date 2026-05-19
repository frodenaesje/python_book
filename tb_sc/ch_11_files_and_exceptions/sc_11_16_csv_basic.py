# file: sc_11_16_csv_basic.py
import csv
from pathlib import Path

FILENAME = Path(__file__).resolve().parent / "vehicles.csv"

# These CSV test data are written to a file, then read back
rows = [
    ["reg_no", "brand", "model", "year"],   # header
    ["EL67820", "Tesla", "Model 3", 2021],
    ["NB72826", "Toyota", "Yaris", 2019],
    ["AB12345", "Volvo", "XC60", 2022],
]

with open(FILENAME, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

# Read
with open(FILENAME, "r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)  # read the header row separately
    print("Columns:", header)
    for row in reader:
        print(row)
