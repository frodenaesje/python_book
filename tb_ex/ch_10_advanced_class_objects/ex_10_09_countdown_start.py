# file: ex_10_09_countdown_start.py

class Countdown:
    def __init__(self, start):
        # TODO: initialise the countdown state.
        pass

    def __iter__(self):
        # TODO: return this iterator without resetting it.
        pass

    def __next__(self):
        # TODO: produce the next number or signal exhaustion.
        pass


def countdown(start):
    # TODO: produce the same numbers using yield.
    pass


if __name__ == "__main__":
    iterator = Countdown(3)
    print("Iterator first:", next(iterator))
    # list() consumes all remaining values, leaving this iterator exhausted.
    print("Iterator remaining:", list(iterator))
    print("Iterator exhausted:", list(iterator))
    generator = countdown(3)
    print("Generator first:", next(generator))
    # list() also consumes the generator, so the following list() call is empty.
    print("Generator remaining:", list(generator))
    print("Generator exhausted:", list(generator))
    print("Fresh iterator:", end="")
    for number in Countdown(3):
        print(f" {number}", end="")
    print()
    print("Fresh generator:", end="")
    for number in countdown(3):
        print(f" {number}", end="")
    print()
    print("Zero:", list(Countdown(0)), list(countdown(0)))
    print("Negative:", list(Countdown(-2)), list(countdown(-2)))
