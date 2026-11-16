# file: sc_06_17_route_length.py
import math


def distance(x0: float, y0: float, x1: float, y1: float) -> float:
    """Return the straight-line distance between two points."""
    dx = x1 - x0
    dy = y1 - y0
    return math.sqrt(dx * dx + dy * dy)


def route_length(points: list) -> float:
    """Return the length along consecutive points, in their given order."""
    total = 0.0
    for index in range(1, len(points)):
        x0, y0 = points[index - 1]
        x1, y1 = points[index]
        total += distance(x0, y0, x1, y1)
    return total


if __name__ == "__main__":
    stops = [(0, 0), (120, 50), (200, 200), (380, 160)]
    for index in range(1, len(stops)):
        x0, y0 = stops[index - 1]
        x1, y1 = stops[index]
        length = distance(x0, y0, x1, y1)
        print(f"Leg {index}: {length:.2f} m")
    print(f"Total route: {route_length(stops):.2f} m")
