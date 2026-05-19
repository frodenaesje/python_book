# file: sc_08_09_circle_with_op_overload1.py
class Circle:
    def __init__(self, radius=1):
        self._radius = radius

    def __str__(self) -> str:
        return f'Radius = {self._radius}'

    def __eq__(self, other) -> bool:
        return self._radius == other._radius

    def __lt__(self, other) -> bool:
        return self._radius < other._radius

    def __gt__(self, other) -> bool:
        return self._radius > other._radius


def main():
    circle1 = Circle()
    circle2 = Circle(25)

    print(circle1)  # __str__()
    print(circle2)

    print(f"Are equal? {circle1 == circle2}")  # __eq__()
    print(f"c1 > c2? {circle1 > circle2}")  # __gt__()
    print(f"c1 < c2? {circle1 < circle2}")    # __lt__()

if __name__ == "__main__":
    main()
