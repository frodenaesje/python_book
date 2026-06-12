# file: ex_10_02_employees_start.py
from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, employee_id):
        # TODO: store _name, _employee_id and initialise _salary_history as []
        pass

    def add_salary(self, amount):
        # TODO: append amount to _salary_history
        pass

    def print_salaries(self):
        # TODO: print name, ID and all monthly entries
        # Example: "Salary history - Alice (ID: 1): 3000.00  3000.00  3000.00"
        pass

    @abstractmethod
    def calculate_payroll(self):
        # Must return this month's pay AND call add_salary() to record it
        pass


class SalaryEmployee(Employee):
    def __init__(self, name, employee_id, monthly_salary):
        # TODO: call super().__init__() and store _monthly_salary
        pass

    def calculate_payroll(self):
        # TODO: return _monthly_salary and record it
        pass


class HourlyEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate):
        # TODO: call super().__init__() and store _hourly_rate
        # TODO: initialise _hours to 0
        pass

    def set_hours(self, hours):
        # TODO: store hours for this month
        pass

    def calculate_payroll(self):
        # TODO: return hourly_rate * hours and record it
        pass


class CommissionEmployee(Employee):
    def __init__(self, name, employee_id, base_salary, commission):
        # TODO: call super().__init__() and store _base_salary, _commission
        pass

    def calculate_payroll(self):
        # TODO: return base_salary + commission and record it
        pass


if __name__ == "__main__":
    alice = SalaryEmployee("Alice", 1, 3000)
    bob   = HourlyEmployee("Bob",   2, 20)
    clara = CommissionEmployee("Clara", 3, 2700, 500)

    employees = [alice, bob, clara]
    hours_per_month = [160, 150, 170]

    for month in range(1, 4):
        print(f"Month {month}:")
        bob.set_hours(hours_per_month[month - 1])
        for emp in employees:
            pay = emp.calculate_payroll()
            print(f"  {emp._name} (ID: {emp._employee_id}): {pay:.2f}")
        print()

    for emp in employees:
        emp.print_salaries()
