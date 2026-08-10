# file: ex_08_05_playlist_start.py
import random

class Playlist:
    def __init__(self, name):
        # TODO: store _name and initialise _songs as empty list
        pass

    @property
    def name(self):
        # TODO: return _name
        pass

    @name.setter
    def name(self, value):
        # TODO: set _name, raise ValueError if empty string
        pass

    def add(self, song):
        # TODO: append song to _songs
        pass

    def remove(self, song):
        # TODO: remove song from _songs
        # Print a message if the song is not found
        pass

    def shuffle(self):
        # TODO: shuffle _songs in place using random.shuffle
        pass

    def __len__(self):
        # TODO: return number of songs
        pass

    def __contains__(self, song):
        # TODO: return True if song is in _songs
        pass

    def __str__(self):
        # TODO: return formatted string with name, count, and numbered song list
        pass


if __name__ == "__main__":
    p = Playlist("Road Trip")
    p.add("Bohemian Rhapsody")
    p.add("Hotel California")
    p.add("Stairway to Heaven")
    p.add("Sweet Child O' Mine")

    print(p)
    print(f"'Hotel California' in playlist: {'Hotel California' in p}")
    print(f"'Yesterday' in playlist: {'Yesterday' in p}")
    print(f"Length: {len(p)}")

    p.remove("Hotel California")
    print(f"\nAfter removing 'Hotel California':")
    print(p)
