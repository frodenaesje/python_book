# file: ex_10_02_employees.py
from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, employee_id):
        self._name           = name
        self._employee_id    = employee_id
        self._salary_history = []

    def add_salary(self, amount):
        self._salary_history.append(amount)

    def print_salaries(self):
        history = "  ".join(f"{s:.2f}" for s in self._salary_history)
        print(f"Salary history - {self._name:<6}(ID: {self._employee_id}): {history}")

    @abstractmethod
    def calculate_payroll(self):
        pass


class SalaryEmployee(Employee):
    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)
        self._monthly_salary = monthly_salary

    def calculate_payroll(self):
        self.add_salary(self._monthly_salary)
        return self._monthly_salary


class HourlyEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate):
        super().__init__(name, employee_id)
        self._hourly_rate = hourly_rate
        self._hours = 0

    def set_hours(self, hours):
        self._hours = hours

    def calculate_payroll(self):
        pay = self._hourly_rate * self._hours
        self.add_salary(pay)
        return pay


class CommissionEmployee(Employee):
    def __init__(self, name, employee_id, base_salary, commission):
        super().__init__(name, employee_id)
        self._base_salary = base_salary
        self._commission  = commission

    def calculate_payroll(self):
        pay = self._base_salary + self._commission
        self.add_salary(pay)
        return pay


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
            print(f"  {emp._name:<6}(ID: {emp._employee_id}): {pay:.2f}")
        print()

    for emp in employees:
        emp.print_salaries()
