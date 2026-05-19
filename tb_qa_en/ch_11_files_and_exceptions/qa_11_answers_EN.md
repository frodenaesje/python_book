# Chapter 11 – Answer Key: Review Questions

## Understanding

**1. Text files vs. binary files**
Text files contain readable text and are handled as strings in Python — character encoding happens automatically. Binary files contain raw bytes that are not directly human-readable — images, PDFs, pickle files. Python handles them without automatic conversion.

**2. File modes `"w"` and `"a"`**
`"w"` opens for writing and overwrites all existing content — the file always starts empty. `"a"` (append) adds content to the end of existing content without deleting anything. Both create the file if it does not exist.

**3. `read()`, `readline()` and `readlines()`**
`read()` reads the entire file as one string. `readline()` reads one line at a time including the newline. `readlines()` reads the entire file and returns a list where each element is one line.

**4. Why direct iteration is more memory-efficient**
`readlines()` loads the entire file into memory. Direct iteration reads one line at a time — Python fetches the next line from disk only when we request it. For large files this is critical.

**5. `repr()` and file reading**
`repr()` gives a technical representation where escape sequences are shown as they are — `\n` is shown as `\n` instead of an actual newline. Useful for seeing exactly what the file contains.

**6. Text encoding and UTF-8**
Text encoding determines which numbers represent which characters. Python does not always use UTF-8 by default — on Windows the default is often `cp1252`. Solution: always use `encoding="utf-8"`.

**7. Broad vs. specific exception handling**
`except:` without a type catches absolutely all exceptions — including ones we had not thought of. We risk hiding bugs. Specific types such as `except FileNotFoundError:` catch only what we actually expect.

**8. The `else` block**
Runs only if no exception occurred in the `try` block. Gives a clear separation between risky code and follow-up code that should only run on success.

**9. The `finally` block**
`finally` always runs — whether or not an exception occurred. Ideal for cleanup that must always happen, such as closing a file or database connection.

**10. Custom exception classes**
A descriptive type like `InvalidPasswordError` is clearer than `ValueError`, makes it easier to catch precisely in client code, and makes the error cause clear to both developer and user.

**11. What `with` guarantees — and what it does not**
`with` guarantees that the resource is cleaned up — the file is closed — regardless of what happens in the block. `with` does not guarantee that exceptions are handled — they propagate normally.

**12. CWD vs. script directory**
CWD is the directory the program is run from. The script directory is the directory where the Python file is located. Relative paths are interpreted relative to the CWD, not the script directory. For predictable file placement: use `Path(__file__).resolve().parent`.

**13. Serialisation and deserialisation**
Serialisation converts a data structure into a linear representation that can be stored on disk or sent over a network. Deserialisation is the reverse process.

**14. The most important difference between `pickle` and `json`**
`pickle` is binary, Python-only, and handles all Python objects directly. `json` is text-based, human-readable and language-independent, but only supports simple data types — custom classes require manual conversion.

**15. `pickle` and security**
A pickle file can contain code that is executed automatically when `pickle.load()` is called. A malicious actor can create a pickle file that runs arbitrary code. pickle is intended for internal use where we control the files ourselves.

**16. `datetime.date`, `datetime.time` and `datetime.datetime`**
`datetime.date` represents only a date. `datetime.time` represents only a time of day. `datetime.datetime` combines both and is the most commonly used.

**17. Subtracting two `datetime` objects**
Returns a `timedelta` object representing the duration between the two points in time.

**18. `strptime()` vs. `strftime()`**
`strptime()` parses text into a datetime (str → datetime). `strftime()` formats a datetime into text (datetime → str). Both use the same format codes.

**19. `total_seconds()` vs. the `seconds` attribute**
`timedelta.seconds` gives only the seconds component — not the days. `total_seconds()` gives the entire duration in seconds including the days. Always use `total_seconds()` for the complete duration.

**20. CSV and the `csv` module**
CSV (Comma-Separated Values) is a text-based table format where the values on each row are separated by a delimiter. We use the `csv` module instead of `split(",")` because the module handles edge cases correctly — values with commas inside quotes, newlines in fields, and different delimiters.

**21. `csv.reader` vs. `csv.DictReader`**
`csv.reader` returns each row as a list — we refer by index (`row[1]`). `csv.DictReader` returns each row as a dictionary with column names as keys — we refer by name (`row["brand"]`). `DictReader` is more readable and robust.

**22. `newline=""` with CSV files**
Without `newline=""` Python may add extra blank lines between rows on Windows. `newline=""` leaves all newline handling to the `csv` module.

**23. `next(reader)`**
`next(reader)` reads one row and advances the iterator. Useful for reading the header row separately so it is not treated as a data row in the loop.

**24. The `delimiter` parameter**
Specifies the delimiter in the file. The default is a comma, but files exported from Excel with certain locale settings use a semicolon: `csv.reader(f, delimiter=";")`.

---

## Practical

**25. Write and read a name list**
```python
with open("names.txt", "w", encoding="utf-8") as f:
    f.write("Alice\n")
    f.write("Bob\n")
    f.write("Clara\n")
    f.write("Diana\n")
    f.write("Erik\n")

with open("names.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.rstrip())
```

**26. Add names with append**
```python
with open("names.txt", "a", encoding="utf-8") as f:
    f.write("Frode\n")
    f.write("Grete\n")
```

**27. `try/except` with `finally`**
```python
try:
    with open("does_not_exist.txt", "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    print("The file was not found.")
finally:
    print("The code reached the finally block.")
```

**28. Custom exception**
```python
class TooYoungError(Exception):
    pass

def check_age(age: int) -> None:
    if age < 18:
        raise TooYoungError(f"Age {age} is too low.")

try:
    check_age(15)
except TooYoungError as e:
    print(f"Error: {e}")
```

**29. `pathlib`**
```python
from pathlib import Path

script_dir = Path(__file__).resolve().parent
output_file = script_dir / "test.txt"

with open(output_file, "w", encoding="utf-8") as f:
    f.write("Test")

print(output_file.resolve())   # absolute path
print(output_file.name)        # filename with extension
print(output_file.suffix)      # extension only
```

**30. `pickle` with `Product`**
```python
import pickle
from pathlib import Path

class Product:
    def __init__(self, name: str, price: float) -> None:
        self._name  = name
        self._price = price

    def __str__(self) -> str:
        return f"{self._name}: {self._price:.2f}"

products = [Product("Coffee", 3.99), Product("Tea", 2.49), Product("Milk", 1.79)]
filename = Path(__file__).resolve().parent / "products.pkl"

with open(filename, "wb") as f:
    pickle.dump(products, f)

with open(filename, "rb") as f:
    loaded = pickle.load(f)

for p in loaded:
    print(p)
```

**31. `json` with `Product`**
```python
import json
from pathlib import Path

class Product:
    def __init__(self, name: str, price: float) -> None:
        self._name  = name
        self._price = price

    def __str__(self) -> str:
        return f"{self._name}: {self._price:.2f}"

    def to_dict(self) -> dict:
        return {"name": self._name, "price": self._price}

    @staticmethod
    def from_dict(data: dict) -> "Product":
        return Product(data["name"], data["price"])

products = [Product("Coffee", 3.99), Product("Tea", 2.49), Product("Milk", 1.79)]
filename = Path(__file__).resolve().parent / "products.json"

with open(filename, "w", encoding="utf-8") as f:
    json.dump([p.to_dict() for p in products], f, indent=2, ensure_ascii=False)

with open(filename, "r", encoding="utf-8") as f:
    loaded = [Product.from_dict(d) for d in json.load(f)]

for p in loaded:
    print(p)
```

**32. `datetime` — days since date of birth**
```python
from datetime import datetime

date_of_birth = datetime(1990, 6, 15)
age = datetime.now() - date_of_birth
print(f"You have lived for {age.days} days.")
```

**33. `datetime` — add 30 days**
```python
from datetime import datetime, timedelta

in_30_days = datetime.now() + timedelta(days=30)
print(in_30_days.strftime("%d/%m/%Y"))
```

**34. CSV — read and write with `DictReader`/`DictWriter`**
```python
import csv
from pathlib import Path

FILENAME = Path(__file__).resolve().parent / "people.csv"
fieldnames = ["name", "age", "city"]
rows = [
    {"name": "Alice", "age": 28, "city": "London"},
    {"name": "Bob",   "age": 34, "city": "Edinburgh"},
    {"name": "Clara", "age": 22, "city": "Manchester"},
]

with open(FILENAME, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

with open(FILENAME, "r", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(f"{row['name']} is {row['age']} years old and lives in {row['city']}.")
```

**35. CSV — filter and write to new file**
```python
import csv
from pathlib import Path

INFILE  = Path(__file__).resolve().parent / "people.csv"
OUTFILE = Path(__file__).resolve().parent / "over25.csv"

with open(INFILE,  "r", newline="", encoding="utf-8") as fin, \
     open(OUTFILE, "w", newline="", encoding="utf-8") as fout:
    reader = csv.DictReader(fin)
    writer = csv.DictWriter(fout, fieldnames=reader.fieldnames)
    writer.writeheader()
    for row in reader:
        if int(row["age"]) > 25:
            writer.writerow(row)
```
