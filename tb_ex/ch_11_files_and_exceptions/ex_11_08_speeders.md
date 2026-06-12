---
title: "Speed Camera Analysis"
id: "ex_11_06_speeders"
tags: ["datetime", "strptime", "timedelta", "csv", "DictReader", "dict"]
difficulty: "medium"
prerequisites: ["datetime", "strptime", "timedelta", "csv", "DictReader", "dict"]
learning_outcomes:
  - "Parse datetime strings from a CSV file using strptime"
  - "Compute travel time using timedelta subtraction"
  - "Convert timedelta to speed using total_seconds()"
  - "Build a dict[str, list[datetime]] from file data"
---

# Speed Camera Analysis

## Exercise

Two speed cameras A and B are placed 5 km apart on a road with a
speed limit of 60 km/h. A vehicle travelling at exactly 60 km/h takes
exactly 5 minutes to travel between them. Any shorter travel time means
the vehicle was speeding.

The file `camera_data.csv` contains all camera readings for one day:

```
reg_no,camera,timestamp
NB72826,A,2022-01-03 07:11:41
NB72826,B,2022-01-03 07:20:06
FY99401,A,2022-01-03 07:22:33
FY99401,B,2022-01-03 07:26:42
...
```

Note that a vehicle may pass the cameras more than once in the same day.
`ZZ94355` appears only in camera A - it turned off before reaching B.

Write these functions:

### load_camera_data(filename: str) -> dict[str, dict[str, list]]

Read the CSV and return a nested dict:

```python
# Structure: {reg_no: {"A": [datetime, ...], "B": [datetime, ...]}}
{
    "NB72826": {
        "A": [datetime(2022, 1, 3, 7, 11, 41)],
        "B": [datetime(2022, 1, 3, 7, 20,  6)],
    },
    "FY99401": {
        "A": [datetime(2022, 1, 3, 7, 22, 33),
              datetime(2022, 1, 3, 8, 17, 33)],
        "B": [datetime(2022, 1, 3, 7, 26, 42),
              datetime(2022, 1, 3, 8, 19,  3)],
    },
    ...
}
```

### find_speeders(data, distance_km, speed_limit)

For each vehicle that passed both cameras, match each A-time to the
nearest B-time that is later, compute the speed, and collect all
violations. Return a list of tuples:
`(reg_no, time_a, time_b, speed_kmh)`

### Main program

Load the data, find speeders, and print a report.

## Example run

```
Speed camera report - 5 km, limit 60 km/h
-------------------------------------------
FY99401  07:22:33 -> 07:26:42  72.3 km/h  SPEEDING
DA49644  07:27:14 -> 07:31:37  68.4 km/h  SPEEDING
ZH73969  07:32:36 -> 07:37:35  60.2 km/h  SPEEDING
EL67820  07:40:40 -> 07:45:39  60.2 km/h  SPEEDING
SY60306  08:03:11 -> 08:07:01  78.3 km/h  SPEEDING
FY99401  08:17:33 -> 08:19:03  200.0 km/h  SPEEDING

Vehicles checked: 7
Violations found: 6
```

## Hint

To compute speed from two datetime objects:

```python
travel_time = time_b - time_a          # gives a timedelta
seconds     = travel_time.total_seconds()
hours       = seconds / 3600
speed_kmh   = distance_km / hours
```

To match A- and B-times for a vehicle that passes multiple times:
for each A-time, find the first B-time that is greater than the A-time.

## Topics

- `datetime.strptime()` to parse timestamps
- `timedelta` subtraction and `total_seconds()`
- `csv.DictReader` to read structured data
- Nested dict as the data model

---
## Instructor notes

**Learning objectives covered:** strptime, timedelta, total_seconds,
DictReader, nested dict

**Connection to book:** This is the exact example from section 11.11
of the chapter, extended into a full exercise with file I/O. Students
recognise the problem from the text and implement it properly.

**The matching logic:** For each A-time, find the first B-time > A-time.
This handles multiple passes correctly. ZZ94355 has no B-times and
is silently skipped.

**timedelta arithmetic:**
```python
MIN_TIME = timedelta(hours=distance_km / speed_limit_kmh)
if travel_time < MIN_TIME:
    # speeding
```
