# file: sc_10_06_multilpe_inheritance2.py
class A:
    def __init__(self):
        self.value = "A's value"
        super().__init__()  # Calls the next class in the MRO.

class B:
    def __init__(self):
        self.value = "B's value"
        super().__init__()  # Calls the next class in the MRO.

class C(A, B):
    def __init__(self):
        super().__init__()  # Follows MRO: C -> A -> B -> object.
        # Old code without super():
        # A.__init__(self)
        # B.__init__(self)

    def show(self):
        print(self.value)

c = C()
c.show()  # Output: B's value
print(f"MRO: {C.__mro__}")  # Shows: C -> A -> B -> object.
