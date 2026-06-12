# file: ex_08_02_employee_start.py

class Employee:
    _employee_count = 0  # class variable

    def __init__(self, name, employee_id, department, salary):
        # TODO: store all attributes with leading underscore
        # TODO: increment _employee_count
        pass

    def give_raise(self, amount):
        # TODO: increase salary by amount
        # Reject negative or zero amounts with a message
        pass

    def annual_salary(self):
        # TODO: return monthly salary * 12
        pass

    @classmethod
    def get_employee_count(cls):
        # TODO: return total number of employees created
        pass

    def __str__(self):
        # TODO: return formatted string with all attributes
        pass

    def __eq__(self, other):
        # TODO: equal if same employee_id
        pass

    def __lt__(self, other):
        # TODO: compare by salary
        pass

    def __gt__(self, other):
        # TODO: compare by salary
        pass


if __name__ == "__main__":
    e1 = Employee("Alice Johnson", 1001, "Engineering", 65000)
    e2 = Employee("Bob Smith",     1002, "Marketing",   55000)
    e3 = Employee("Clara Lee",     1003, "Engineering", 72000)

    print(e1)
    print(f"Annual salary: {e1.annual_salary()}")
    e1.give_raise(5000)
    print(f"After raise:   {e1.annual_salary()}")
    e1.give_raise(-1000)

    print(f"\nEmployees created: {Employee.get_employee_count()}")
    print(f"\ne1 == e2? {e1 == e2}")
    best = max(e1, e2, e3)
    print(f"Highest salary: {best._name} ({best._salary}/month)")
