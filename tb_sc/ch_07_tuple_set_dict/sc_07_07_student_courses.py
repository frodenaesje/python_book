# file: sc_07_07_student_courses.py

# A nested dictionary models data with several levels.
# Student ID -> student information -> courses and grades.
grades = {
    1001: {
        "name": "Paul Barnes",
        "courses": {
            "math": 8,
            "physics": 7,
            "c++": 3
        }
    },
    1031: {
        "name": "Bill Shankley",
        "courses": {
            "math": 6,
            "c++": 6
        }
    },
    1011: {
        "name": "Jane Jillingham",
        "courses": {
            "physics": 2,
            "math": 5
        }
    },
    1012: {
        "name": "Bill Gates",
        "courses": {
            "java": 10,
            "c++": 7
        }
    },
    1019: {
        "name": "Jack The Ripper",
        "courses": {
            "math": 8,
            "physics": 7
        }
    },
    1090: {
        "name": "Don Henley",
        "courses": {
            "physics": 10,
            "c++": 8
        }
    }
}

# Follow the keys level by level to retrieve nested values.
student_id = 1001
print(grades[student_id]["name"])
print(grades[student_id]["courses"])
print(grades[student_id]["courses"]["math"])


# Sort by the sum of physics and c++ grades.
# item is a (student_id, student_info) tuple from grades.items().
def get_grades(item):
    courses = item[1]["courses"]
    # A missing course contributes zero to the sum.
    return courses.get("physics", 0) + courses.get("c++", 0)


# key=get_grades makes sorted() compare the calculated sums.
sorted_list = sorted(grades.items(), key=get_grades, reverse=True)
sorted_dict = dict(sorted_list)

for student_id, info in sorted_dict.items():
    print(f"{student_id}: {info['name']}, Courses: {info['courses']}")
