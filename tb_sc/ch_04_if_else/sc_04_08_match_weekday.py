# file: sc_04_08_match_weekday.py

day = 3

match day:
    case 1: print('Monday')
    case 2: print('Tuesday')
    case 3: print('Wednesday')
    case 4: print('Thursday')
    case 5: print('Friday')
    case 6: print('Saturday')
    case 7: print('Sunday')
    case _: print('Invalid day')   # wildcard


# Structural pattern matching - a taste
point = [3, 0]
match point:
    case [0, 0]: print('Origin')
    case [x, 0]: print(f'On the x-axis: x={x}')
    case [0, y]: print(f'On the y-axis: y={y}')
    case [x, y]: print(f"Point ({x}, {y})")
