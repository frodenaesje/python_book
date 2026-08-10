# file: ex_11_07_librarylibrary_start.py

# TODO: Define the exception hierarchy
# class LibraryError(Exception): pass
# class BookNotFoundError(LibraryError): pass
# class AlreadyBorrowedError(LibraryError): pass
# class BorrowLimitError(LibraryError): pass

MAX_LOANS = 3


class Book:
    def __init__(self, title: str, author: str):
        self._title       = title
        self._author      = author
        self._is_borrowed = False
        self._borrowed_by = None

    def __str__(self):
        status = f"(borrowed by {self._borrowed_by})" if self._is_borrowed else "(available)"
        return f"{self._title} by {self._author} {status}"

class Library:
    def __init__(self):
        self._books      = {}   # title -> Book
        self._user_loans = {}   # user  -> list of titles

    def add_book(self, title: str, author: str) -> None:
        self._books[title] = Book(title, author)

    def borrow(self, title: str, user: str) -> None:
        # TODO: raise BookNotFoundError if title not in _books
        # TODO: raise AlreadyBorrowedError if book is already borrowed
        # TODO: raise BorrowLimitError if user already has MAX_LOANS books
        # TODO: mark book as borrowed, update _user_loans
        pass

    def return_book(self, title: str, user: str) -> None:
        # TODO: raise BookNotFoundError if title not in _books
        # TODO: raise LibraryError if book is not currently borrowed by user
        # TODO: mark book as available, update _user_loans
        pass

    def available_books(self) -> list[str]:
        return [t for t, b in self._books.items() if not b._is_borrowed]

    def user_loans(self, user: str) -> list[str]:
        return self._user_loans.get(user, [])


if __name__ == "__main__":
    lib = Library()
    for title, author in [
        ("The Hobbit",  "J.R.R. Tolkien"),
        ("Dune",        "Frank Herbert"),
        ("Python 101",  "Mike Driscoll"),
        ("Clean Code",  "Robert C. Martin"),
    ]:
        lib.add_book(title, author)

    print(f"Available: {', '.join(lib.available_books())}\n")

    # TODO: borrow books for Alice and Bob with try-except

    # TODO: demonstrate BookNotFoundError

    # TODO: demonstrate AlreadyBorrowedError

    print(f"\nAvailable: {', '.join(lib.available_books())}")
    print(f"Alice's loans: {', '.join(lib.user_loans('Alice'))}")
