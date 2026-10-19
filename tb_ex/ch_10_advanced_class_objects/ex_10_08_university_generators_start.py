# file: ex_10_08_university_generators_start.py
from ex_10_04_university import University, Student, GraduateStudent, Staff


class SearchableUniversity(University):
    def students_with_min_gpa(self, min_gpa):
        # TODO: yield qualifying students, including graduate students.
        pass

    def matching_members(self, query):
        # TODO: yield members with a case-insensitive partial name match.
        pass


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
    # TASK: replace None with sum() applied to a generator expression.
    total = None
    print(f"GPA total: {total:.1f}")
