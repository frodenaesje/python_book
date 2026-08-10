# file: ex_08_07_student_register_start.py

class Student:
    _student_count = 0

    def __init__(self, name, student_id, gpa):
        # TODO: store _name, _student_id
        # TODO: use the gpa property setter to store and validate gpa
        # TODO: increment _student_count
        pass

    @classmethod
    def get_count(cls):
        # TODO: return total students created
        pass

    @property
    def gpa(self):
        # TODO: return _gpa
        pass

    @gpa.setter
    def gpa(self, value):
        # TODO: validate 0.0 <= value <= 4.0, raise ValueError otherwise
        # TODO: store as _gpa
        pass

    def __str__(self):
        # TODO: return e.g. "Alice Johnson  (ID: 1001, GPA: 3.9)"
        pass

    def __lt__(self, other):
        # TODO: compare by GPA
        pass


class StudentRegister:
    def __init__(self):
        # TODO: initialise _students as empty list
        pass

    def add(self, student):
        # TODO: add student to _students
        pass

    def remove_by_id(self, student_id):
        # TODO: remove student with matching _student_id
        # Print a message if not found
        pass

    def find_by_name(self, name):
        # TODO: return list of students where name (case-insensitive) is in _name
        pass

    def top_students(self, n):
        # TODO: return n students with highest GPA
        # Hint: sorted(..., reverse=True)[:n]
        pass

    def __len__(self):
        # TODO: return number of students
        pass

    def __str__(self):
        # TODO: return all students, one per line
        pass


if __name__ == "__main__":
    reg = StudentRegister()
    reg.add(Student("Alice Johnson", 1001, 3.9))
    reg.add(Student("Bob Olsen",     1002, 2.8))
    reg.add(Student("Clara Lee",     1003, 3.7))
    reg.add(Student("David Park",    1004, 3.2))

    print(f"Register has {len(reg)} students.\n")

    print("Top 2 students:")
    for s in reg.top_students(2):
        print(f"  {s}")

    print(f"\nSearch for 'o':")
    for s in reg.find_by_name("o"):
        print(f"  {s}")

    print(f"\nTotal students created: {Student.get_count()}")
