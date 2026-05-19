# Pythonic patterns – Chapter 11: File handling and exceptions

## Opening files — `with` vs. manual closing

| Beginner | Pythonic |
|----------|----------|
| `file = open("data.txt", "r")`<br>`content = file.read()`<br>`file.close()` | `with open("data.txt", "r") as file:`<br>`    content = file.read()` |

`with` guarantees the file is closed even if an error occurs.

## Reading line by line

| Beginner | Pythonic |
|----------|----------|
| `lines = file.readlines()`<br>`for line in lines:`<br>`    print(line.rstrip())` | `for line in file:`<br>`    print(line.rstrip())` |

Direct iteration reads one line at a time and does not load the entire file into memory.

## Exception handling — broad vs. precise

| Beginner | Pythonic |
|----------|----------|
| `try:`<br>`    file = open("data.txt")`<br>`except:`<br>`    print("Something went wrong")` | `try:`<br>`    file = open("data.txt")`<br>`except FileNotFoundError:`<br>`    print("The file does not exist")` |

Catch specific exception types. A bare `except:` hides bugs.

## Writing numbers to a file

| Beginner | Pythonic |
|----------|----------|
| `file.write(str(price) + "\n")` | `file.write(f"{price}\n")` |

f-strings are more readable than string conversion and concatenation.

## File path — relative vs. absolute

| Beginner | Pythonic |
|----------|----------|
| `open("data.txt")` | `from pathlib import Path`<br>`file = Path(__file__).resolve().parent / "data.txt"`<br>`open(file)` |

A relative path is interpreted relative to the CWD — not the script's location.

## Serialising custom classes

| pickle | json |
|--------|------|
| `pickle.dump(obj, f)` | Requires `to_dict()` and `from_dict()` |
| `pickle.load(f)` | `json.dump(obj.to_dict(), f)` |
| No extra code needed | `Product.from_dict(json.load(f))` |

Choose pickle for internal Python use. Choose json for readability and data exchange.

## Exception hierarchy — specific before general

| Beginner | Pythonic |
|----------|----------|
| `except Exception as e:`<br>`    print(e)` | `except FileNotFoundError:`<br>`    print("File not found")`<br>`except PermissionError:`<br>`    print("No access")`<br>`except OSError as e:`<br>`    print(f"OS error: {e}")` |

Catch specific types first — the parent class acts as a safety net.

## Custom exceptions — type matters more than content

| Beginner | Pythonic |
|----------|----------|
| `raise ValueError("Invalid password")` | `class InvalidPasswordError(Exception):`<br>`    pass`<br><br>`raise InvalidPasswordError("Too short")` |

A descriptive type makes client code more readable and allows precise catching.

## `with` and `try/except` combined

| Beginner | Pythonic |
|----------|----------|
| `try:`<br>`    file = open("data.txt")`<br>`    content = file.read()`<br>`    file.close()`<br>`except FileNotFoundError:`<br>`    print("File not found")` | `try:`<br>`    with open("data.txt") as file:`<br>`        content = file.read()`<br>`except FileNotFoundError:`<br>`    print("File not found")` |

`with` handles closing. `try/except` handles errors. They solve different problems.

## `datetime` — calculating a time difference

| Beginner | Pythonic |
|----------|----------|
| `diff_seconds = (tB - tA).seconds` | `diff_seconds = (tB - tA).total_seconds()` |

`seconds` gives only the seconds component — not the days. `total_seconds()` gives the complete duration.

## `datetime` — parsing from text

| Beginner | Pythonic |
|----------|----------|
| `year  = int(text[:4])`<br>`month = int(text[5:7])` | `dt = datetime.strptime(text, "%Y-%m-%d")` |

`strptime()` is robust and readable. Manual slicing is fragile.

## CSV — `reader` vs. `DictReader`

| Beginner | Pythonic |
|----------|----------|
| `for row in csv.reader(f):`<br>`    print(row[0], row[1])` | `for row in csv.DictReader(f):`<br>`    print(row["name"], row["city"])` |

`DictReader` gives named fields — the code does not break if columns are added or moved.

## CSV — `newline` when opening

| Beginner | Pythonic |
|----------|----------|
| `open("data.csv", "w", encoding="utf-8")` | `open("data.csv", "w", newline="", encoding="utf-8")` |

Without `newline=""` Windows may add extra blank lines between CSV rows.

## CSV — reading the header separately

| Beginner | Pythonic |
|----------|----------|
| `rows = list(csv.reader(f))`<br>`header = rows[0]`<br>`data = rows[1:]` | `reader = csv.reader(f)`<br>`header = next(reader)`<br>`for row in reader: ...` |

`next()` reads one row and advances the iterator — avoids loading the entire file into memory.

## CSV vs. json vs. pickle

| Scenario | Choice |
|----------|--------|
| Tabular data to be opened in Excel | CSV |
| Complex Python objects for internal use | pickle |
| Data exchange with other systems | json |
| To be versioned in Git and read by humans | json |
