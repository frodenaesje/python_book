---
title: "Playlist with Custom Exceptions"
id: "ex_11_04_playlist_exceptions"
tags: ["custom exception", "exception hierarchy", "raise", "try-except", "class"]
difficulty: "easy"
prerequisites: ["custom exception", "raise", "try-except", "class", "Playlist from ch 8"]
learning_outcomes:
  - "Design a small exception hierarchy"
  - "Raise custom exceptions instead of printing errors"
  - "Catch specific exceptions in client code"
  - "Understand why exceptions are better than return values for errors"
---

# Playlist with Custom Exceptions

## Exercise

In chapter 8 you built a `Playlist` class. It printed error messages
directly when something went wrong. Now we improve it using custom
exceptions.

### Exception hierarchy

```
PlaylistError (base)
├── DuplicateSongError  - song already in playlist
└── PlaylistFullError   - playlist has reached max size
```

### Updated Playlist

Copy your `Playlist` class from chapter 8 and make these changes:

1. Add a `max_size` parameter to `__init__` (default 50)
2. In `add(song)`: raise `DuplicateSongError` if the song is already
   in the playlist, raise `PlaylistFullError` if the playlist is full
3. In `remove(song)`: raise `PlaylistError` if the song is not found
   (instead of printing a message)

Each exception should carry a meaningful message.

### Main program

Demonstrate all three exceptions with `try-except` blocks. Show that
the playlist continues to work normally after an exception is caught.

## Example run

```
Added: Bohemian Rhapsody
Added: Hotel California
Added: Stairway to Heaven

DuplicateSongError: 'Bohemian Rhapsody' is already in playlist 'Road Trip'.
PlaylistError: 'Yesterday' is not in playlist 'Road Trip'.

Playlist: Road Trip (3 songs)
  1. Bohemian Rhapsody
  2. Hotel California
  3. Stairway to Heaven
```

## Topics

- Custom exception hierarchy
- `raise` with a message
- `try-except` for specific exception types
- Exceptions vs. print-based error handling

---
## Instructor notes

**Learning objectives covered:** exception hierarchy, raise, try-except,
exceptions vs return values

**Why build on Playlist:** Students already know the class. Refactoring
familiar code to use exceptions makes the improvement concrete - they
can see exactly what changed and why it is better.

**Key comparison to make explicit:**
```python
# Before (ch 8):
def remove(self, song):
    if song in self._songs:
        self._songs.remove(song)
    else:
        print(f"'{song}' not found in playlist.")

# After (ch 11):
def remove(self, song):
    if song not in self._songs:
        raise PlaylistError(f"'{song}' is not in playlist '{self._name}'.")
    self._songs.remove(song)
```
The caller now decides how to handle the error - not the class.
