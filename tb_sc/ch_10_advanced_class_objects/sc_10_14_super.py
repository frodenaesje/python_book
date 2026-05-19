# file: sc_10_14_super.py
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age  = age

    def __str__(self):
        return f"Name: {self._name}, Age: {self._age}"

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self._student_id = student_id

    def __str__(self):
        return (super().__str__()
                + f", Student-ID: {self._student_id}")

p = Person("Alice", 45)
s = Student("Bob", 22, "s12345")
print(p)  # Name: Alice, Age: 45
print(s)  # Name: Bob, Age: 22, Student-ID: s12345
