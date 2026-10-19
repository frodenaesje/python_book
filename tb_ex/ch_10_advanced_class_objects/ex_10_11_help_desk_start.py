# file: ex_10_11_help_desk_start.py

class HelpDesk:
    def __init__(self, priority, regular):
        self.priority = priority
        self.regular = regular

    def __iter__(self):
        # TODO: return a fresh HelpDeskIterator for these lists.
        pass


class HelpDeskIterator:
    def __init__(self, priority, regular):
        # TODO: store the lists and initialise independent traversal state.
        pass

    def __iter__(self):
        # TODO: return this iterator without resetting it.
        pass

    def __next__(self):
        # TODO: return the next scheduled ticket or raise StopIteration.
        pass


class GeneratorHelpDesk:
    def __init__(self, priority, regular):
        self.priority = priority
        self.regular = regular

    def __iter__(self):
        # TODO: yield tickets in schedule order without changing the lists.
        pass


if __name__ == "__main__":
    priority = ["Cannot log in", "Server unavailable"]
    regular = ["Install a printer", "Update software", "Reset preferences"]
    for desk_class in (HelpDesk, GeneratorHelpDesk):
        print(desk_class.__name__)
        desk = desk_class(priority, regular)
        print("First traversal:", list(desk))
        print("Second traversal:", list(desk))
        first = iter(desk)
        second = iter(desk)
        print("First iterator:", next(first), next(first))
        print("Second iterator:", next(second))
        # list() consumes the remaining tickets in this particular iterator.
        print("First remaining:", list(first))
        print("First exhausted:", list(first))
        print("Second remaining:", list(second))
        print("Priority only:", list(desk_class(priority, [])))
        print("Regular only:", list(desk_class([], regular)))
        print("Both empty:", list(desk_class([], [])))
        print("Original priority:", priority)
        print("Original regular:", regular)
        print()
