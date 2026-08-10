# file: ex_10_05_duck_typing_start.py
from datetime import datetime


class ConsoleLogger:
    def log(self, message):
        # TODO: print message with timestamp prefix
        # e.g. "[2024-01-15 14:30:00] Loading data"
        # Hint: datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        pass


class FileLogger:
    def __init__(self, filename):
        # TODO: store filename
        pass

    def log(self, message):
        # TODO: append message to file (open in append mode "a")
        pass


class MemoryLogger:
    def __init__(self):
        # TODO: initialise _messages as empty list
        pass

    def log(self, message):
        # TODO: append message to _messages
        pass

    def get_messages(self):
        # TODO: return _messages
        pass


def run_pipeline(loggers, steps):
    # TODO: for each step, call log(step) on every logger
    # Note: no isinstance() needed - just call log() on whatever is passed
    pass


if __name__ == "__main__":
    console = ConsoleLogger()
    memory  = MemoryLogger()
    file_log = FileLogger("pipeline.log")

    loggers = [console, memory, file_log]
    steps   = ["Loading data", "Cleaning data", "Training model", "Done"]

    run_pipeline(loggers, steps)

    print("\nMemory log:")
    for msg in memory.get_messages():
        print(f"  {msg}")
