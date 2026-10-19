# file: ex_10_07_iterable_library_start.py
from ex_10_06_media_library import Library, Movie, Book, Podcast


class LibraryIterator:
    def __init__(self, items):
        # TODO: store the items and initialise the traversal position.
        pass

    def __iter__(self):
        # TODO: return this iterator.
        pass

    def __next__(self):
        # TODO: return the next item, or signal exhaustion.
        pass


class IterableLibrary(Library):
    def __iter__(self):
        # TODO: create an independent iterator for this traversal.
        pass


if __name__ == "__main__":
    library = IterableLibrary("Study Library")
    library.add(Movie("Arrival", 2016, "Denis Villeneuve", 116))
    library.add(Book("Python Practice", 2025, "Alex Green", 240))
    library.add(Podcast("Code Stories", 2024, "Sam Lee", 12))

    print("First traversal:", [item.media_type() for item in library])
    print("Second traversal:", [item.media_type() for item in library])
    first = iter(library)
    second = iter(library)
    print("First iterator:", next(first).media_type())
    print("First iterator:", next(first).media_type())
    print("Second iterator:", next(second).media_type())
    print("First iterator remaining:", [item.media_type() for item in first])
    print("First iterator exhausted:", list(first))
    print("Empty library:", list(IterableLibrary("Empty")))
