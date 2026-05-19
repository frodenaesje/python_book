# file: ch_18_06_closest_point_implementations.py
import math
import random
import time
from typing import List, Tuple

# Point er en tuple (x, y)
Point = Tuple[float, float]

def distance(p1: Point, p2: Point) -> float:
    """Euklidsk avstand mellom to punkter."""
    x1, y1 = p1
    x2, y2 = p2
    dx, dy = x1 - x2, y1 - y2
    return math.sqrt(dx**2 + dy**2)

def generate_random_points(n: int, width: float = 100,
                           height: float = 100) -> List[Point]:
    """Genererer n tilfeldige punkter i en width x height rektangel."""
    pts = []
    for _ in range(n):
        x = random.uniform(0, width)
        y = random.uniform(0, height)
        pts.append((x, y))
    return pts

# ============================================================
# Brute Force: O(n²)
# ============================================================
def closest_pair_brute_force(points: List[Point]) -> Tuple[Point, Point, float]:
    """
    Finner det nærmeste punktparet ved å sjekke alle par.
    Tidskompleksitet: O(n²)
    """
    n = len(points)
    if n < 2:
        raise ValueError("Trenger minst 2 punkter")
    
    min_dist = float('inf')
    p1_closest = points[0]
    p2_closest = points[1]
    
    for i in range(n):
        for j in range(i + 1, n):
            d = distance(points[i], points[j])
            if d < min_dist:
                min_dist = d
                p1_closest = points[i]
                p2_closest = points[j]
    
    return p1_closest, p2_closest, min_dist

# ============================================================
# Divide-and-Conquer: O(n log n)
# ============================================================
def _closest_pair_strip(strip: List[Point], delta: float) -> float:
    
    min_dist = delta
    n = len(strip)
    
    for i in range(n):
        # Sjekk maksimalt de neste 6 punktene
        j = i + 1
        while j < n and (strip[j][1] - strip[i][1]) < min_dist:
            d = distance(strip[i], strip[j])
            if d < min_dist:
                min_dist = d
            j += 1
            # Praktisk: bryt etter 6 sjekker
            if j - i > 6:
                break
    
    return min_dist

def _closest_pair_recursive(px: List[Point], py: List[Point]) -> float:
    
    n = len(px)
    
    # Base case: bruk brute force for små n
    if n <= 3:
        min_dist = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                d = distance(px[i], px[j])
                if d < min_dist:
                    min_dist = d
        return min_dist
    
    # Del i to halvdeler
    mid = n // 2
    midpoint = px[mid]
    
    # Del px
    px_left = px[:mid]
    px_right = px[mid:]
    
    # Del py basert på midtpunktet
    py_left = [p for p in py if p[0] <= midpoint[0]]
    py_right = [p for p in py if p[0] > midpoint[0]]
    
    # Rekursive kall
    delta_left = _closest_pair_recursive(px_left, py_left)
    delta_right = _closest_pair_recursive(px_right, py_right)
    
    # Minste avstand så langt
    delta = min(delta_left, delta_right)
    
    # Bygg strip: punkter innenfor delta fra midtlinjen
    strip = [p for p in py if abs(p[0] - midpoint[0]) < delta]
    
    # Sjekk strip
    delta_strip = _closest_pair_strip(strip, delta)
    
    return min(delta, delta_strip)

def closest_pair_divide_conquer(points: List[Point]) -> float:
    """
    Finner minste avstand mellom punktpar.
    Tidskompleksitet: O(n log n)
    """
    if len(points) < 2:
        raise ValueError("Trenger minst 2 punkter")
    
    # Sorter på x og y
    px = sorted(points, key=lambda p: p[0])
    py = sorted(points, key=lambda p: p[1])
    
    return _closest_pair_recursive(px, py)

# ============================================================
# Sammenligning og testing
# ============================================================
def compare_algorithms(points: List[Point]) -> None:
    """Kjører begge algoritmer og sammenligner resultat og kjøretid."""
    n = len(points)
    sep = "=" * 60
    print(f"\n{sep}")
    print(f"Closest Pair for {n} punkter")
    print(f"{sep}")
    
    # Brute Force
    start = time.perf_counter()
    p1, p2, dist_bf = closest_pair_brute_force(points)
    time_bf = time.perf_counter() - start
    
    print(f"\nBrute Force:")
    print(f"  Minste avstand: {dist_bf:.4f}")
    print(f"  Punkter: ({p1[0]:.2f}, {p1[1]:.2f}) og ({p2[0]:.2f}, {p2[1]:.2f})")
    print(f"  Kjøretid: {time_bf * 1000:.4f} ms")
    
    # Divide-and-Conquer
    start = time.perf_counter()
    dist_dc = closest_pair_divide_conquer(points)
    time_dc = time.perf_counter() - start
    
    print(f"\nDivide-and-Conquer:")
    print(f"  Minste avstand: {dist_dc:.4f}")
    print(f"  Kjøretid: {time_dc * 1000:.4f} ms")
    
    # Sammenligning
    print(f"\n{sep}")
    if abs(dist_bf - dist_dc) < 0.0001:
        print("✓ Begge algoritmer fant samme avstand")
    else:
        print(f"⚠ Ulik avstand: BF={dist_bf:.4f} vs DC={dist_dc:.4f}")
    
    if time_bf > 0:
        speedup = time_bf / time_dc
        print(f"Divide-and-Conquer er {speedup:.2f}x raskere")

if __name__ == "__main__":
    # Test 1: Liten datamengde
    print("\nTest 1: 10 tilfeldige punkter")
    points_10 = generate_random_points(10)
    compare_algorithms(points_10)
    
    # Test 2: Middels datamengde
    print("\n\nTest 2: 100 tilfeldige punkter")
    points_100 = generate_random_points(100)
    compare_algorithms(points_100)
    
    # Test 3: Større datamengde
    print("\n\nTest 3: 1000 tilfeldige punkter")
    points_1000 = generate_random_points(1000)
    compare_algorithms(points_1000)
    
    # Test 4: Stort datasett (kun divide-and-conquer)
    print("\n\nTest 4: 10000 tilfeldige punkter (kun divide-and-conquer)")
    points_10000 = generate_random_points(10000)
    start = time.perf_counter()
    dist = closest_pair_divide_conquer(points_10000)
    elapsed = time.perf_counter() - start
    print(f"  Minste avstand: {dist:.4f}")
    print(f"  Kjøretid: {elapsed * 1000:.4f} ms")
