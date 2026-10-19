# An Iterable Media Library

## Exercise

Extend exercise 10.6, Media Library. Keep its existing classes and methods unchanged.
The supplied files import them from `ex_10_06_media_library.py` in the same
directory and add an `IterableLibrary(Library)` subclass. If you have your own
completed solution, you may use that implementation instead.

1. Write a separate `LibraryIterator` class. Its constructor receives the
   library's item list. Implement `__iter__()` and `__next__()` yourself.
2. Implement `IterableLibrary.__iter__()` so each call returns a new
   `LibraryIterator`. Traverse the media objects in insertion order.
3. Raise `StopIteration` after the final item. Further calls must also raise
   `StopIteration`; do not restart an exhausted iterator.
4. Run two complete traversals of the same library. Then create two iterators,
   advance the first twice and the second once, and show that their positions
   are independent.
5. Show that an empty library produces no items. Explain briefly why the current
   index belongs to the iterator rather than the library.

Do not use `yield` or delegate traversal to `iter(self._items)` in this
exercise: the purpose is to implement the protocol. Do not add or remove media
while a traversal is in progress. Use `media_type()` in the demonstration so
the output is independent of the existing star-rating display.

## Example run

```text
First traversal: ['Movie', 'Book', 'Podcast']
Second traversal: ['Movie', 'Book', 'Podcast']
First iterator: Movie
First iterator: Book
Second iterator: Movie
First iterator remaining: ['Podcast']
First iterator exhausted: []
Empty library: []
```

## Hints

- Each iterator needs its own current position.
- Returning a new iterator allows nested loops over the same collection too.

## Topics

- Iterable versus iterator
- Separate traversal state and persistent exhaustion
- Reusable collections

## Assessment criteria

| Criterion | Description | Weight (%) |
|---|---|---:|
| Library iteration | Makes the library iterable in insertion order using a separate iterator class. | 40 |
| Iterator behaviour | Returns the iterator itself from __iter__, advances correctly, and remains exhausted after StopIteration. | 35 |
| Demonstration and explanation | Shows repeated traversal, independent iterators, and an empty library, and explains where traversal state belongs. | 25 |
| **Total** | | **100%** |
