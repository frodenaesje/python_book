# file: ex_07_02_grade_statistics_start.py

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

# TODO: Print all grades using tuple unpacking
#       for name, subject, grade in grades:
#       Format: "  Alice    Math      B"

# TODO: Count grades per subject using get()
#       counts[subject] = counts.get(subject, 0) + 1
#       Print sorted by subject name

# TODO: Group grades per student using setdefault()
#       by_student.setdefault(name, []).append(grade)
#       Print each student with their grades joined by ", "
