# file: sc_13_00_simple_decorator_example.py
import time

def measure(other_func):
    def wrapper():
        start_time = time.time()
        other_func()
        stop_time = time.time()
        print(f"Elapsed time : {stop_time - start_time:.6f} seconds")
    return wrapper

@measure
def turtle_step():
    print("Turtle about to do a step")
    time.sleep(3)
    print("Turtle finished a step")

@measure
def rabbit_step():
    print("Rabbit about to do a step")
    time.sleep(0.5)
    print("Rabbit finished a step")

turtle_step()
rabbit_step()
