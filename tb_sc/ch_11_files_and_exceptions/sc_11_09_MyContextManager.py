# file sc_11_09_MyContextManager.py
from pathlib import Path
from contextlib import AbstractContextManager

class MyContextManager(AbstractContextManager):
    def __init__(self, filename, mode):
        self._filename = filename
        self._mode = mode
        self._file = None
    
    def __enter__(self):
        self._file = open(self._filename, self._mode)
        print(f"Hello from __enter__, opening file {self._filename} in mode {self._mode}")
        return self._file
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self._file:
            self._file.close()
            print(f"Goodbye from __exit__, closing file {self._filename}")
        return False

# Usage:
Path('test.txt').touch()  # Creates the file if it does not exist
with MyContextManager('test.txt', 'w') as f:
    f.write('Hello from context manager')
