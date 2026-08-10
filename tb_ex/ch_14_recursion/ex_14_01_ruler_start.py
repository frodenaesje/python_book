# file: ex_14_01_ruler.py

def ruler(left, right, height, rul=None):
    """Draw a recursive ruler and return the tick-height list."""
    if rul is None:
        rul = [" "] * int(right)

    # TODO: base case - when height <= 0, return rul

    # TODO: find midpoint: mid = (left + right) // 2

    # TODO: recursively draw left half with height - 1

    # TODO: record the mark: rul[int(mid)] = height
    #       and print the mark: print("-" * height)

    # TODO: recursively draw right half with height - 1

    # TODO: return rul
    pass


def draw_ruler(rul):
    """Print a visual representation of the ruler. (Not part of the main exercise.)"""
    max_height = max(h for h in rul if isinstance(h, int))
    for level in range(max_height, 0, -1):
        line = ""
        for val in rul:
            if isinstance(val, int) and val >= level:
                line += "|"
            else:
                line += " "
        print(line)
    print("".join(str(i % 10) for i in range(len(rul))))


if __name__ == "__main__":
    rul = ruler(0, 8, 3)
    print(rul)
    print()
    draw_ruler(rul)
