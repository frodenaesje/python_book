# file: sc_10_11_singleton.py
# A singleton class ensures that only one object is made.
class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):  # cls refers to the class.
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, value):
        self.value = value

# Test the Singleton class
s1 = Singleton(10)
s2 = Singleton(20)

print(s1.value) # Output: 10
print(s2.value) # Output: 10
print(s1 is s2) # Output: True (same instance)
