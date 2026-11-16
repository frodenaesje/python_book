# file: sc_04_14_point_side.py
x0 = int(input("p0, x-coordinate: "))
y0 = int(input("p0, y-coordinate: "))
x1 = int(input("p1, x-coordinate: "))
y1 = int(input("p1, y-coordinate: "))
x2 = int(input("p2, x-coordinate: "))
y2 = int(input("p2, y-coordinate: "))

if x0 == x2 and y0 == y2:
    print("p0 and p2 must be different points.")
else:
    side = (x2 - x0) * (y1 - y0) - (y2 - y0) * (x1 - x0)

    if side > 0:
        print("p1 is to the left of the line from p0 to p2.")
    elif side == 0:
        print("p1 is on the line through p0 and p2.")
    else:
        print("p1 is to the right of the line from p0 to p2.")
