---
title: "Employees and Payroll"
id: "ex_10_02_employees"
tags: ["inheritance", "polymorphism", "super", "ABC", "abstractmethod"]
difficulty: "easy"
prerequisites: ["class", "inheritance", "super()", "ABC", "abstractmethod"]
learning_outcomes:
  - "Build a class hierarchy with a shared abstract method"
  - "Use super().__init__() at each level"
  - "Demonstrate polymorphism: iterate a mixed list and call the same method"
  - "Accumulate results across months"
---

# Employees and Payroll

## Exercise

Build a small payroll system. Create an abstract base class `Employee`
and three concrete subclasses.

### Employee (ABC)

**Attributes:** `_name`, `_employee_id`, `_salary_history` (list)

**Methods:**
- `add_salary(amount)` - append to salary history
- `print_salaries()` - print name, ID and each monthly entry
- `@abstractmethod calculate_payroll()` - returns this month's pay
  and calls `add_salary()` to record it

### SalaryEmployee(Employee)
Fixed monthly salary.
```python
SalaryEmployee(name, employee_id, monthly_salary)
```

### HourlyEmployee(Employee)
Pay = hourly rate * hours worked.
```python
HourlyEmployee(name, employee_id, hourly_rate)
```
Add a method `set_hours(hours)` to set hours for the month.

### CommissionEmployee(Employee)
Fixed base salary plus a commission amount.
```python
CommissionEmployee(name, employee_id, base_salary, commission)
```

### Simulation

Simulate payroll for 3 months. For `HourlyEmployee` use 160, 150 and
170 hours in the three months. After the simulation print salary
history for all employees.

## Example run

```
Month 1:
  Alice (ID: 1): 3000.00
  Bob   (ID: 2): 3200.00
  Clara (ID: 3): 3200.00

Month 2:
  Alice (ID: 1): 3000.00
  Bob   (ID: 2): 3000.00
  Clara (ID: 3): 3200.00

Month 3:
  Alice (ID: 1): 3000.00
  Bob   (ID: 2): 3400.00
  Clara (ID: 3): 3200.00

Salary history - Alice (ID: 1): 3000.00  3000.00  3000.00
Salary history - Bob   (ID: 2): 3200.00  3000.00  3400.00
Salary history - Clara (ID: 3): 3200.00  3200.00  3200.00
```

## Topics

- Abstract base class with `@abstractmethod`
- `super().__init__()` in each subclass
- Polymorphism: one loop calls `calculate_payroll()` on all types

---
## Instructor notes

**Learning objectives covered:** ABC, abstractmethod, super, polymorphism

**Key insight:** The simulation loop is identical for all three employee
types - it just calls `calculate_payroll()`. This is polymorphism in
action: same interface, different behaviour.

**Connection to ch 8:** Students already built an `Employee` class in
ch 8 ex_08_02. This is a fresh design - the payroll abstraction is new.
