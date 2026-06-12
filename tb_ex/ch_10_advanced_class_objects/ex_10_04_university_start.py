# file: ex_10_04_university_start.py


class Person:
    def __init__(self, name, age):
        # TODO: store _name and _age
        pass

    def __str__(self):
        # TODO: e.g. "Alice Johnson (age 20)"
        pass


class Student(Person):
    def __init__(self, name, age, student_id, gpa):
        # TODO: call super().__init__() and store _student_id, _gpa
        pass

    def __str__(self):
        # TODO: extend Person's __str__ with student ID and GPA
        # e.g. "Alice Johnson (age 20) | ID: 1001 | GPA: 3.8"
        pass

    def __lt__(self, other):
        return self._gpa < other._gpa


class GraduateStudent(Student):
    def __init__(self, name, age, student_id, gpa, thesis_title, supervisor):
        # TODO: call super().__init__() and store _thesis_title, _supervisor
        pass

    def __str__(self):
        # TODO: extend Student's __str__ with thesis and supervisor
        pass


class Staff(Person):
    def __init__(self, name, age, staff_id, department):
        # TODO: call super().__init__() and store _staff_id, _department
        pass

    def __str__(self):
        # TODO: extend Person's __str__ with department
        pass


class Professor(Staff):
    def __init__(self, name, age, staff_id, department, title, research_area):
        # TODO: call super().__init__() and store _title, _research_area
        pass

    def __str__(self):
        # TODO: extend Staff's __str__ with title and research area
        # Hint: prepend title to name in the output
        pass


class University:
    def __init__(self, name):
        self._name    = name
        self._members = []

    def add(self, person):
        # TODO: add person to _members
        pass

    def list_students(self):
        # TODO: print all Student instances (including GraduateStudent)
        # Hint: isinstance(p, Student)
        pass

    def list_staff(self):
        # TODO: print all Staff instances
        pass

    def find_by_name(self, name):
        # TODO: return list of members where name matches (case-insensitive partial)
        pass

    def __len__(self):
        return len(self._members)


if __name__ == "__main__":
    uni = University("Python University")
    uni.add(Student("Alice Johnson", 20, 1001, 3.8))
    uni.add(Student("Bob Smith",     22, 1002, 3.2))
    uni.add(GraduateStudent("Clara Lee", 26, 1003, 3.9,
                            "ML in healthcare", "Prof. Wang"))
    uni.add(Staff("David Park", 45, 2001, "Computer Science"))
    uni.add(Professor("Emma Wang", 52, 2002, "Computer Science",
                      "Prof.", "Machine Learning"))

    print(f"University has {len(uni)} members.\n")

    print("Students:")
    uni.list_students()

    print("\nStaff:")
    uni.list_staff()

    print("\nSearch 'lee':")
    for p in uni.find_by_name("lee"):
        print(f"  {p}")
