# file: ex_13_05_logging_decorator_start.py

def log_call(func):
    """Decorator that logs each call and return value."""
    def wrapper(*args, **kwargs):
        # TODO: build a list of argument strings
        #       positional: [repr(a) for a in args]
        #       keyword:    [f"{k}={repr(v)}" for k, v in kwargs.items()]
        # TODO: print "CALL  funcname(arg1, arg2, key=val)"
        # TODO: call func(*args, **kwargs) and store result
        # TODO: print "RETURN result"
        # TODO: return result
        pass
    return wrapper


# TODO: Apply @log_call to the two functions below

def add(a, b):
    return a + b


def greet(name, greeting="Hi"):
    return f"{greeting}, {name}!"


if __name__ == "__main__":
    print(add(3, 5))
    print()
    print(greet(name="Alice", greeting="Hello"))
