# file: ex_08_02_employee.py

class Employee:
    _employee_count = 0

    def __init__(self, name, employee_id, department, salary):
        self._name        = name
        self._employee_id = employee_id
        self._department  = department
        self._salary      = salary
        Employee._employee_count += 1

    def give_raise(self, amount):
        if amount <= 0:
            print("Invalid raise - amount must be positive.")
        else:
            self._salary += amount

    def annual_salary(self):
        return self._salary * 12

    @classmethod
    def get_employee_count(cls):
        return cls._employee_count

    def __str__(self):
        return (f"Employee ID: {self._employee_id}\n"
                f"Name:        {self._name}\n"
                f"Department:  {self._department}\n"
                f"Monthly:     {self._salary}")

    def __eq__(self, other):
        return self._employee_id == other._employee_id

    def __lt__(self, other):
        return self._salary < other._salary

    def __gt__(self, other):
        return self._salary > other._salary


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
