# file: sc_10_08_composition_alternative.py
class A:
    def __init__(self):
        self.a_value = "A's value"

class B:
    def __init__(self):
        self.b_value = "B's value"

class C:
    def __init__(self):
        self.a = A()
        self.b = B()

    def show(self):
        print(self.a.a_value)
        print(self.b.b_value)

C().show()
