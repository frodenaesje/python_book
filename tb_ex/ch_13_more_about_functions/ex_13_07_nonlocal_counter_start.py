# file: ex_13_07_nonlocal_counter_start.py

def make_counter(start=0, step=1):
    """Return three closures (increment, decrement, reset) sharing one counter."""
    count = start

    def increment():
        # TODO: declare nonlocal count
        # TODO: count += step
        # TODO: return count
        pass

    def decrement():
        # TODO: declare nonlocal count
        # TODO: count -= step
        # TODO: return count
        pass

    def reset():
        # TODO: declare nonlocal count
        # TODO: count = start
        # TODO: return count
        pass

    return increment, decrement, reset


# Without nonlocal - this will raise UnboundLocalError:
# def bad_increment():
#     count += step   # Python sees assignment -> treats count as local
#                     # but count has no local value -> UnboundLocalError


if __name__ == "__main__":
    inc, dec, reset = make_counter(start=10, step=2)
    print(inc())    # 12
    print(inc())    # 14
    print(dec())    # 12
    print(reset())  # 10
    print(inc())    # 12

    print()
    # Default counter
    up, down, back = make_counter()
    print(up())   # 1
    print(up())   # 2
    print(down()) # 1
    print(back()) # 0
