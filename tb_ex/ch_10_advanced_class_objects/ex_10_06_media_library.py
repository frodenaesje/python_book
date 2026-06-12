# file: ex_10_06_media_library.py
from abc import ABC, abstractmethod
star = "\u2605"
empty_star = "\u2606"

class MediaItem(ABC):
    def __init__(self, title, year):
        self._title  = title
        self._year   = year
        self._rating = 0

    @abstractmethod
    def media_type(self) -> str:
        pass

    def rate(self, score):
        if not (1 <= score <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        self._rating = score

    def __str__(self):
        stars = star * self._rating + empty_star * (5 - self._rating)
        return f"[{self.media_type():<8}] {self._title} ({self._year}) {stars}"

    def __lt__(self, other):
        return self._rating < other._rating


class Movie(MediaItem):
    def __init__(self, title, year, director, duration_min):
        super().__init__(title, year)
        self._director     = director
        self._duration_min = duration_min

    def media_type(self):
        return "Movie"


class Book(MediaItem):
    def __init__(self, title, year, author, pages):
        super().__init__(title, year)
        self._author = author
        self._pages  = pages

    def media_type(self):
        return "Book"


class Podcast(MediaItem):
    def __init__(self, title, year, host, num_episodes):
        super().__init__(title, year)
        self._host         = host
        self._num_episodes = num_episodes

    def media_type(self):
        return "Podcast"


class Library:
    def __init__(self, name):
        self._name  = name
        self._items = []

    def add(self, item):
        self._items.append(item)

    def top_rated(self, n):
        return sorted(self._items, reverse=True)[:n]

    def by_type(self, media_type_str):
        return [i for i in self._items if i.media_type() == media_type_str]

    def search(self, query):
        return [i for i in self._items if query.lower() in i._title.lower()]

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
