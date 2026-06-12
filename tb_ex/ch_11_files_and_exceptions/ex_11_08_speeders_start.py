# file: ex_11_08_speedersspeeders_start.py
import csv
from datetime import datetime, timedelta

TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"
DISTANCE_KM      = 5
SPEED_LIMIT      = 60


def load_camera_data(filename: str) -> dict[str, dict[str, list]]:
    """Load camera readings from CSV into a nested dict.

    Returns:
        {reg_no: {"A": [datetime, ...], "B": [datetime, ...]}}
    """
    # TODO: open with csv.DictReader - columns: reg_no, camera, timestamp
    # TODO: for each row, parse timestamp with datetime.strptime()
    # TODO: build and return the nested dict
    #       Hint: use data.setdefault(reg_no, {"A": [], "B": []})
    pass


def find_speeders(data: dict[str, dict[str, list]],
                  distance_km: float,
                  speed_limit: float) -> list[tuple]:
    """Find speeding violations.

    For each vehicle with both A and B times:
      - match each A-time to the first B-time that is later
      - compute speed = distance_km / travel_hours
      - collect if speed > speed_limit

    Returns:
        list of (reg_no, time_a, time_b, speed_kmh)
    """
    # TODO: compute MIN_TIME as timedelta(hours=distance_km / speed_limit)
    # TODO: for each vehicle in data:
    #         skip if no B-times
    #         for each A-time, find first B-time > A-time
    #         compute travel_time = time_b - time_a
    #         if travel_time < MIN_TIME: compute speed and add to violations
    pass


if __name__ == "__main__":
    data = load_camera_data("camera_data.csv")
    violations = find_speeders(data, DISTANCE_KM, SPEED_LIMIT)

    print(f"Speed camera report - {DISTANCE_KM} km, limit {SPEED_LIMIT} km/h")
    print("-" * 43)

    for reg_no, time_a, time_b, speed in violations:
        ta = time_a.strftime("%H:%M:%S")
        tb = time_b.strftime("%H:%M:%S")
        print(f"{reg_no}  {ta} -> {tb}  {speed:.1f} km/h  SPEEDING")

    print(f"\nVehicles checked: {len(data)}")
    print(f"Violations found: {len(violations)}")
