# file sc_10_09_mixin.py
class LoggerMixin:
    def log(self, message):
        print(f"Log: {message}")

class Processor:
    def process(self):
        print("Processing...")

class LoggedProcessor(Processor, LoggerMixin):
    pass

lp = LoggedProcessor()
lp.process()
lp.log("Done")