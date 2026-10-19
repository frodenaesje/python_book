# file: ex_10_08_university_generators.py
from ex_10_04_university import University, Student, GraduateStudent, Staff


class SearchableUniversity(University):
    def students_with_min_gpa(self, min_gpa):
        for member in self._members:
            if isinstance(member, Student) and member._gpa >= min_gpa:
                yield member

    def matching_members(self, query):
        for member in self._members:
            if query.lower() in member._name.lower():
                yield member


if __name__ == "__main__":
    university = SearchableUniversity("Python University")
    university.add(Student("Alice Johnson", 20, 1001, 3.8))
    university.add(Student("Bob Smith", 22, 1002, 3.2))
    university.add(GraduateStudent("Clara Lee", 26, 1003, 3.9,
                                   "Learning Python", "Dr. Park"))
    university.add(Staff("David Park", 45, 2001, "Computer Science"))

    matches = university.students_with_min_gpa(3.5)
    print("First match:", next(matches)._name)
    print("Remaining matches:", [member._name for member in matches])
    print("Exhausted:", list(matches))
    print("Fresh search:", [member._name for member in
                            university.students_with_min_gpa(3.5)])
    print("Name matches:", [member._name for member in
                            university.matching_members("LEE")])
    print("No matches:", list(university.matching_members("Nobody")))
    total = sum(member._gpa for member in
                university.students_with_min_gpa(3.5))
    print(f"GPA total: {total:.1f}")
