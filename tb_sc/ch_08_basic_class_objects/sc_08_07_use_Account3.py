# file: sc_08_07_use_Account3.py
from sc_08_06_Account3 import Account

account1 = Account(123, 456, 1000, 2.5)
account1.deposit(500)
account1.deposit(1500)
account1.withdraw(200)
account1.withdraw(2000)
account1.add_monthly_interest()
account1.print_transactions()

# Using properties
print(f"\nBalance after: {account1.balance:.2f}")
print(f"Interest rate: {account1.interest}%")

# Change balance and interest via properties
account1.balance = 2000
account1.interest = 3.0
print(f"\nNew balance: {account1.balance:.2f}")