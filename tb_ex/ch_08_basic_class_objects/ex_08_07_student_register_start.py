# file: ex_08_07_student_register_start.py

class Student:
    _student_count = 0

    # def __init__(self, name, student_id, gpa):
    # TODO: Create the constructor with parameters name, student_id and gpa.
    #       Store the student data and update the shared student count.

    # @classmethod
    # def get_count(cls):
    # TODO: Create the class method get_count().
    #       A class method uses cls instead of self.
    #       Remember the decorator that marks a method as a class method.
    #       Return the total number of Student objects created.

    # TODO: Create a property named gpa.
    #       First create the getter. Remember that a property getter is an
    #       instance method and uses the @property decorator.


    # The setter is provided because exceptions have not been covered yet.
    # Complete it by storing the valid GPA.
    @gpa.setter
    def gpa(self, value):
        if not 0.0 <= value <= 4.0:
            raise ValueError("GPA must be between 0.0 and 4.0")

    # TODO: Store the valid GPA.

    # TODO: Create __str__() as an instance method.
    #       Return a readable string containing name, ID and GPA.

    # TODO: Create __lt__() as an instance method.
    #       It receives another Student object in addition to self.
    #       Compare the students by GPA.


class StudentRegister:
    pass

    # def __init__(self):
    # TODO: Create the constructor.
    #       Each register should start with its own empty list of Student objects.

    # TODO: Create the instance method add().
    #       It needs self and the Student object to add.

    # TODO: Create the instance method remove_by_id().
    #       It needs self and the student ID to remove.
    #       If the ID is not found, leave the register unchanged and print
    #       a clear message.

    # TODO: Create the instance method find_by_name().
    #       It needs self and the name to search for.
    #       Return all case-insensitive partial name matches as a list.

    # TODO: Create the instance method top_students().
    #       It needs self and n.
    #       Return up to n students in descending GPA order.
    #       Use the Student comparison.

    # TODO: Create __len__() as an instance method.
    #       Return the number of students in this register.

    # TODO: Create __str__() as an instance method.
    #       Return all students, one per line.


# CLIENT CODE
#
# The code below demonstrates how the classes should be used.
# Uncomment it when you have implemented the classes and methods above.
# You can then run the file to test your implementation.

# reg = StudentRegister()
# reg.add(Student("Alice Johnson", 1001, 3.9))
# reg.add(Student("Bob Olsen", 1002, 2.8))
# reg.add(Student("Clara Lee", 1003, 3.7))
# reg.add(Student("David Park", 1004, 3.2))
#
# print(f"Register has {len(reg)} students.\n")
#
# print("Top 2 students:")
# for s in reg.top_students(2):
#     print(f"  {s}")
#
# print("\nSearch for 'o':")
# for s in reg.find_by_name("o"):
#     print(f"  {s}")
#
# print(f"\nTotal students created: {Student.get_count()}")