---
title: "University Hierarchy"
id: "ex_10_04_university"
tags: ["inheritance", "super", "composition", "isinstance", "polymorphism", "classmethod"]
difficulty: "medium"
prerequisites: ["class", "inheritance", "super()", "isinstance", "classmethod", "list"]
learning_outcomes:
  - "Build on existing classes from chapter 8"
  - "Extend a class hierarchy across three levels"
  - "Combine inheritance with composition"
  - "Use isinstance() to process mixed collections"
---

# University Hierarchy

## Exercise

Extend the `Student` class from chapter 8 into a small university
hierarchy. Copy `ex_08_07_student_register.py` to this folder and
import from it.

### Person (new base class)

**Attributes:** `_name`, `_age`

**Methods:**
- `__str__()` - e.g. `Alice Johnson (age 32)`

### Student(Person) - extends ch 8 Student

Modify `Student` to inherit from `Person` instead of standing alone.

**Additional attributes:** `_student_id`, `_gpa`

**Override:** `__str__()` - extends Person's with student ID and GPA

### GraduateStudent(Student)

**Additional attributes:** `_thesis_title`, `_supervisor`

**Override:** `__str__()` - extends Student's with thesis info

### Staff(Person)

**Attributes:** `_staff_id`, `_department`

**Override:** `__str__()` - extends Person's with department

### Professor(Staff)

**Additional attributes:** `_title` (e.g. "Prof.", "Dr."), `_research_area`

**Override:** `__str__()` - extends Staff's with title and research area

### University

**Composition:** holds a list of `Person` objects (students and staff)

**Methods:**
- `add(person)` - add any Person
- `list_students()` - print all Student instances (including GraduateStudents)
- `list_staff()` - print all Staff instances
- `find_by_name(name)` - case-insensitive partial match across all persons
- `__len__()` - total number of persons

## Example run

```
University has 5 members.

Students:
  Alice Johnson (age 20) | ID: 1001 | GPA: 3.8
  Bob Smith (age 22) | ID: 1002 | GPA: 3.2
  Clara Lee (age 26) | ID: 1003 | GPA: 3.9 | Thesis: ML in healthcare | Supervisor: Prof. Wang

Staff:
  David Park (age 45) | Dept: Computer Science
  Prof. Emma Wang (age 52) | Dept: Computer Science | Research: Machine Learning

Search 'lee':
  Clara Lee (age 26) | ID: 1003 | GPA: 3.9 | Thesis: ML in healthcare | Supervisor: Prof. Wang
```

## Topics

- Three-level hierarchy building on ch 8
- `super().__str__()` at each level
- Composition: University contains Persons
- `isinstance()` to filter a mixed list

---
## Instructor notes

**Learning objectives covered:** multi-level hierarchy, super, composition,
isinstance, connection to ch 8

**Connection to ch 8:** Students see their own `Student` class from
ex_08_07 becoming part of a larger design. This reinforces that classes
are building blocks - not isolated exercises.

**isinstance and subclasses:** `isinstance(p, Student)` returns True for
both `Student` and `GraduateStudent` objects - so `list_students()` picks
up both without any extra logic.
