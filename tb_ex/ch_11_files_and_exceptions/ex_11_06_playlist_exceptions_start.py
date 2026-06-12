# file: ex_11_06_playlist_exceptionsplaylist_exceptions_start.py
import random


# TODO: Define the exception hierarchy
# class PlaylistError(Exception):
#     pass
#
# class DuplicateSongError(PlaylistError):
#     pass
#
# class PlaylistFullError(PlaylistError):
#     pass


class Playlist:
    def __init__(self, name: str, max_size: int = 50):
        self._name     = name
        self._songs    = []
        self._max_size = max_size

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Playlist name cannot be empty.")
        self._name = value

    def add(self, song: str) -> None:
        # TODO: raise DuplicateSongError if song is already in _songs
        # TODO: raise PlaylistFullError if len(_songs) >= _max_size
        self._songs.append(song)

    def remove(self, song: str) -> None:
        # TODO: raise PlaylistError if song is not in _songs
        # (instead of printing a message)
        self._songs.remove(song)

    def shuffle(self):
        random.shuffle(self._songs)

    def __len__(self):
        return len(self._songs)

    def __contains__(self, song):
        return song in self._songs

    def __str__(self):
        lines = [f"Playlist: {self._name} ({len(self)} songs)"]
        for i, song in enumerate(self._songs, 1):
            lines.append(f"  {i}. {song}")
        return "\n".join(lines)


if __name__ == "__main__":
    p = Playlist("Road Trip", max_size=5)

    songs = ["Bohemian Rhapsody", "Hotel California", "Stairway to Heaven"]
    for song in songs:
        p.add(song)
        print(f"Added: {song}")

    print()

    # TODO: try to add a duplicate - catch DuplicateSongError and print message

    # TODO: try to remove a song that does not exist - catch PlaylistError

    print()
    print(p)
