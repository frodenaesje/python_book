# file: ex_07_02_grade_statistics.py

grades = [
    ("Alice",   "Math",    "B"),
    ("Bob",     "Math",    "C"),
    ("Alice",   "Python",  "A"),
    ("Charlie", "Math",    "A"),
    ("Bob",     "Python",  "B"),
    ("Alice",   "Physics", "C"),
    ("Charlie", "Python",  "A"),
    ("Bob",     "Physics", "A"),
    ("Charlie", "Physics", "B"),
]

print("All grades:")
for name, subject, grade in grades:
    print(f"  {name:<9}{subject:<10}{grade}")

counts = {}
by_student = {}
for name, subject, grade in grades:
    counts[subject] = counts.get(subject, 0) + 1
    by_student.setdefault(name, []).append(grade)

print("\nGrades per subject:")
for subject in sorted(counts):
    print(f"  {subject:<10}{counts[subject]}")

print("\nGrades per student:")
for student in sorted(by_student):
    print(f"  {student:<10}{', '.join(by_student[student])}")
