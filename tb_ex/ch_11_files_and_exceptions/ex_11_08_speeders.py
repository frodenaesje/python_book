# file: ex_11_08_speedersspeeders.py
import csv
from datetime import datetime, timedelta

TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"
DISTANCE_KM      = 5
SPEED_LIMIT      = 60


def load_camera_data(filename: str) -> dict[str, dict[str, list]]:
    """Load camera readings from CSV. Returns {reg_no: {"A": [...], "B": [...]}}."""
    data = {}
    with open(filename, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            reg_no = row["reg_no"]
            camera = row["camera"]
            ts     = datetime.strptime(row["timestamp"], TIMESTAMP_FORMAT)
            data.setdefault(reg_no, {"A": [], "B": []})
            data[reg_no][camera].append(ts)
    return data


def find_speeders(data: dict[str, dict[str, list]],
                  distance_km: float,
                  speed_limit: float) -> list[tuple]:
    """Find speeding violations. Returns list of (reg_no, time_a, time_b, speed_kmh)."""
    min_time   = timedelta(hours=distance_km / speed_limit)
    violations = []

    for reg_no, cameras in data.items():
        b_times = cameras["B"]
        if not b_times:
            continue
        for time_a in cameras["A"]:
            later_b = [t for t in b_times if t > time_a]
            if not later_b:
                continue
            time_b      = min(later_b)
            travel_time = time_b - time_a
            if travel_time < min_time:
                hours     = travel_time.total_seconds() / 3600
                speed_kmh = distance_km / hours
                violations.append((reg_no, time_a, time_b, speed_kmh))

    return violations


if __name__ == "__main__":
    data       = load_camera_data("camera_data.csv")
    violations = find_speeders(data, DISTANCE_KM, SPEED_LIMIT)

    print(f"Speed camera report - {DISTANCE_KM} km, limit {SPEED_LIMIT} km/h")
    print("-" * 43)

    for reg_no, time_a, time_b, speed in violations:
        ta = time_a.strftime("%H:%M:%S")
        tb = time_b.strftime("%H:%M:%S")
        print(f"{reg_no}  {ta} -> {tb}  {speed:.1f} km/h  SPEEDING")

    print(f"\nVehicles checked: {len(data)}")
    print(f"Violations found: {len(violations)}")
