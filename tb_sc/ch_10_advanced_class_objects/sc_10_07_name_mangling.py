# file: sc_10_07_name_mangling.py
class A:
    def __init__(self):
        self.__value = "A's value"
        super().__init__()

    def show_a(self):
        print(self.__value)

class B:
    def __init__(self):
        self.__value = "B's value"
        super().__init__()

    def show_b(self):
        print(self.__value)

class C(A, B):
    def __init__(self):
        super().__init__()  # Follows MRO: C -> A -> B -> object.
        

c = C()
c.show_a()  # Output: A's value
c.show_b()  # Output: B's value
