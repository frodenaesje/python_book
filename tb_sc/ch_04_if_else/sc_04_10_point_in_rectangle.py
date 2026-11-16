# file: sc_04_10_point_in_rectangle.py
WIDTH = 8
HEIGHT = 5

x = float(input("Point, x-coordinate: "))
y = float(input("Point, y-coordinate: "))

if 0 < x < WIDTH and 0 < y < HEIGHT:
    print("The point is inside the rectangle.")
elif 0 <= x <= WIDTH and 0 <= y <= HEIGHT:
    print("The point is on the boundary.")
else:
    print("The point is outside the rectangle.")
