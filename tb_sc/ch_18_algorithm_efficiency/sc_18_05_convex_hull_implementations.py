# file: sc_18_05_convex_hull_implementations.py
import math
import random
import time
from typing import List, Tuple

# Point er en tuple (x, y)
Point = Tuple[float, float] # Point er en type-alias for en tuple av to flyttall

def orientation(p0: Point, p1: Point, p2: Point) -> float:
    """
    Returnerer orienteringen til p2 relativt til linjen
    p0→p1. >0: venstre, <0: høyre, 0: kolineær.
    """
    # Pakke ut koordinater
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    return (x1 - x0)*(y2 - y0) - (x2 - x0)*(y1 - y0)

def distance(p1: Point, p2: Point) -> float:
    """Euklidsk avstand mellom to punkter."""
    x1, y1 = p1
    x2, y2 = p2
    dx, dy = x1 - x2, y1 - y2
    return math.sqrt(dx**2 + dy**2)

def generate_random_points(n: int, width: float = 100,
                            height: float = 100
                            ) -> List[Point]:
    """Genererer n tilfeldige punkter i
    en width x height rektangel."""
    pts = []
    for _ in range(n):
        x = random.uniform(0, width)
        y = random.uniform(0, height)
        pts.append((x, y))
    return pts

def print_hull(name: str, hull: List[Point]) -> None:
    """Printer convex hull."""
    count = len(hull)
    print(f"\n{name} - {count} punkter på hull:")
    for i, (x, y) in enumerate(hull):
        print(f"  {i+1}. ({x:.2f}, {y:.2f})")

def _start_point_key(p: Point) -> Tuple[float, float]:
    """Returner et tuple med lavest y-verdi, så høyest x-verdi.
    For å få effekten av høyest x ved lik y, returnerer vi -p[0]."""
    return (p[1], -p[0])

# Spesifikk for Graham Scan
def _polar_sort_key(p: Point, p0: Point) -> Tuple[float, float]:
    """Nøkkel: polarvinkel og avstand."""
    dy = p[1] - p0[1]
    dx = p[0] - p0[0]
    angle = math.atan2(dy, dx)
    # Negativ avstand for descending order
    dist = -distance(p0, p)
    return (angle, dist)

def graham_scan(points: List[Point]) -> List[Point]:
    # 1. Finn p0: lavest y, deretter høyest x
    p0 = min(points, key=_start_point_key)

    # 2. Sorter etter polarvinkel fra p0
    # Theta = vinkel fra positiv x-akse til
    # linjen OP, målt mot klokken
    def sort_by_polar(p: Point) -> Tuple[float, float]:
        return _polar_sort_key(p, p0)

    other_pts = [p for p in points if p != p0]
    sorted_pts = sorted(other_pts, key=sort_by_polar)

    # 3. Start stakken
    stack: List[Point] = [p0, sorted_pts[0],
                          sorted_pts[1]]

    # 4. Sjekk konkavitet
    for p in sorted_pts[2:]:
        # Høyresving eller kolineært?
        while (len(stack) >= 2 and
               orientation(stack[-2],
                           stack[-1], p) <= 0):
            stack.pop()
        stack.append(p)

    return stack

# Gift wrapping (Jarvis March)
def jarvis_march(points: List[Point]) -> List[Point]:
    # 1. Finn startpunktet h0
    h0 = min(points, key=_start_point_key)
    hull = [h0]
    current = h0

    while True:
        # Initialiser kandidat
        if points[0] != current:
            candidate = points[0]
        else:
            candidate = points[1]

        for p in points:
            if p == current:
                continue

            # Hvis p ligger mer til venstre
            ori = orientation(current, candidate, p)
            if ori > 0:
                candidate = p
            # Hvis kolineært, velg lengst
            elif ori == 0:
                d_p = distance(current, p)
                d_cand = distance(current, candidate)
                if d_p > d_cand:
                    candidate = p

        current = candidate

        # Sjekk om vi er tilbake ved start
        if current == h0:
            break

        hull.append(current)

    return hull


def compare_algorithms(points: List[Point]) -> None:
    """Kjører begge algoritmer og
    sammenligner kjøretid og resultat."""
    sep = "=" * 60
    print(f"\n{sep}")
    print(f"Convex Hull for {len(points)} punkter")
    print(f"{sep}")

    # Graham Scan
    start = time.perf_counter()
    graham_hull = graham_scan(points)
    graham_time = time.perf_counter() - start

    print_hull("Graham Scan", graham_hull)
    ms = graham_time * 1000
    print(f"Kjøretid: {ms:.4f} ms")

    # Jarvis March
    start = time.perf_counter()
    jarvis_hull = jarvis_march(points)
    jarvis_time = time.perf_counter() - start

    print_hull("Jarvis March", jarvis_hull)
    ms = jarvis_time * 1000
    print(f"Kjøretid: {ms:.4f} ms")

    # Sammenligning
    print(f"\n{sep}")
    speedup = jarvis_time / graham_time
    print(f"Graham Scan er {speedup:.2f}x raskere")
    g_len = len(graham_hull)
    j_len = len(jarvis_hull)
    if g_len == j_len:
        print("✓ Begge fant samme hull-størrelse")
    else:
        print(f"⚠ Ulik størrelse: "
              f"Graham {g_len} vs Jarvis {j_len}")


if __name__ == "__main__":
    # Test 1: Liten datamengde
    print("\nTest 1: 10 tilfeldige punkter")
    points_10 = generate_random_points(10)
    compare_algorithms(points_10)

    # Test 2: Større datamengde
    print("\n\nTest 2: 1000 tilfeldige punkter")
    points_1000 = generate_random_points(1000)
    compare_algorithms(points_1000)

    # Test 3: Stort datasett
    print("\n\nTest 3: 10000 tilfeldige punkter")
    points_10000 = generate_random_points(10000)
    compare_algorithms(points_10000)
