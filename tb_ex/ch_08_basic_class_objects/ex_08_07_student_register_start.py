# file: ex_08_07_student_register_start.py

class Student:
    _student_count = 0

    def __init__(self, name, student_id, gpa):
        # TODO: initialize the required attributes with a validated GPA.
        # Keep the shared count of successfully created students up to date.
        pass

    @classmethod
    def get_count(cls):
        # TODO: return the total number of students created.
        pass

    @property
    def gpa(self):
        # TODO: return this student's GPA.
        pass

    @gpa.setter
    def gpa(self, value):
        # TODO: accept values from 0.0 through 4.0.
        # Otherwise raise ValueError.
        pass

    def __str__(self):
        # TODO: return a readable string containing name, ID and GPA.
        pass

    def __lt__(self, other):
        # TODO: compare this student's GPA with the other student's GPA.
        pass


class StudentRegister:
    def __init__(self):
        # TODO: initialize an independent, empty list of Student objects.
        pass

    def add(self, student):
        # TODO: add the supplied Student object to this register.
        pass

    def remove_by_id(self, student_id):
        # TODO: remove the student with this ID.
        # If not found, leave the register unchanged and print a message.
        pass

    def find_by_name(self, name):
        # TODO: return all case-insensitive partial name matches as a list.
        pass

    def top_students(self, n):
        # TODO: return up to n students in descending GPA order.
        # Use Student comparison.
        pass

    def __len__(self):
        # TODO: return the number of students in this register.
        pass

    def __str__(self):
        # TODO: return all students, one per line.
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
