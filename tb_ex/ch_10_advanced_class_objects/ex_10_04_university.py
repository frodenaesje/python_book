# file: ex_10_04_university.py


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age  = age

    def __str__(self):
        return f"{self._name} (age {self._age})"


class Student(Person):
    def __init__(self, name, age, student_id, gpa):
        super().__init__(name, age)
        self._student_id = student_id
        self._gpa        = gpa

    def __str__(self):
        return super().__str__() + f" | ID: {self._student_id} | GPA: {self._gpa}"

    def __lt__(self, other):
        return self._gpa < other._gpa


class GraduateStudent(Student):
    def __init__(self, name, age, student_id, gpa, thesis_title, supervisor):
        super().__init__(name, age, student_id, gpa)
        self._thesis_title = thesis_title
        self._supervisor   = supervisor

    def __str__(self):
        return (super().__str__() +
                f" | Thesis: {self._thesis_title} | Supervisor: {self._supervisor}")


class Staff(Person):
    def __init__(self, name, age, staff_id, department):
        super().__init__(name, age)
        self._staff_id   = staff_id
        self._department = department

    def __str__(self):
        return super().__str__() + f" | Dept: {self._department}"


class Professor(Staff):
    def __init__(self, name, age, staff_id, department, title, research_area):
        super().__init__(name, age, staff_id, department)
        self._title         = title
        self._research_area = research_area

    def __str__(self):
        base = f"{self._title} {self._name} (age {self._age}) | Dept: {self._department}"
        return base + f" | Research: {self._research_area}"


class University:
    def __init__(self, name):
        self._name    = name
        self._members = []

    def add(self, person):
        self._members.append(person)

    def list_students(self):
        for p in self._members:
            if isinstance(p, Student):
                print(f"  {p}")

    def list_staff(self):
        for p in self._members:
            if isinstance(p, Staff):
                print(f"  {p}")

    def find_by_name(self, name):
        return [p for p in self._members if name.lower() in p._name.lower()]

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
