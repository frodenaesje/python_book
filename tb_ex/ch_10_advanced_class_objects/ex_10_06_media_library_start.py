# file: ex_10_06_media_library_start.py
from abc import ABC, abstractmethod


class MediaItem(ABC):
    def __init__(self, title, year):
        # TODO: store _title, _year and initialise _rating to 0
        pass

    @abstractmethod
    def media_type(self) -> str:
        # TODO: return e.g. "Movie", "Book", "Podcast"
        pass

    def rate(self, score):
        # TODO: set _rating, validate 1-5, raise ValueError otherwise
        pass

    def __str__(self):
        # TODO: e.g. "[Movie] Inception (2010) ★★★★☆"
        # Hint: stars = "★" * self._rating + "☆" * (5 - self._rating)
        pass

    def __lt__(self, other):
        # TODO: compare by rating
        pass


class Movie(MediaItem):
    def __init__(self, title, year, director, duration_min):
        # TODO: call super().__init__() and store _director, _duration_min
        pass

    def media_type(self):
        return "Movie"


class Book(MediaItem):
    def __init__(self, title, year, author, pages):
        # TODO: call super().__init__() and store _author, _pages
        pass

    def media_type(self):
        return "Book"


class Podcast(MediaItem):
    def __init__(self, title, year, host, num_episodes):
        # TODO: call super().__init__() and store _host, _num_episodes
        pass

    def media_type(self):
        return "Podcast"


class Library:
    def __init__(self, name):
        self._name  = name
        self._items = []

    def add(self, item):
        # TODO: add item to _items
        pass

    def top_rated(self, n):
        # TODO: return n items with highest rating (sorted descending)
        pass

    def by_type(self, media_type_str):
        # TODO: return items where item.media_type() == media_type_str
        pass

    def search(self, query):
        # TODO: return items where query (case-insensitive) is in title
        pass

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return f"Library: {len(self)} items"


if __name__ == "__main__":
    lib = Library("My Library")

    m1 = Movie("Inception", 2010, "Christopher Nolan", 148)
    m1.rate(4)
    m2 = Movie("The Matrix", 1999, "The Wachowskis", 136)
    m2.rate(5)
    b1 = Book("The Pragmatic Programmer", 1999, "Hunt & Thomas", 352)
    b1.rate(5)
    p1 = Podcast("Lex Fridman Podcast", 2018, "Lex Fridman", 400)
    p1.rate(4)
    p2 = Podcast("Software Engineering Daily", 2015, "Jeff Meyerson", 1500)
    p2.rate(3)

    for item in [m1, m2, b1, p1, p2]:
        lib.add(item)

    print(lib)

    print("\nTop 3:")
    for item in lib.top_rated(3):
        print(f"  {item}")

    print("\nMovies:")
    for item in lib.by_type("Movie"):
        print(f"  {item}")

    print("\nSearch 'prag':")
    for item in lib.search("prag"):
        print(f"  {item}")
