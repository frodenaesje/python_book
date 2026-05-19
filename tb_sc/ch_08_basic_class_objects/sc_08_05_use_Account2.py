# file: sc_08_05_use_Account2.py
from sc_08_04_Account2 import Account

account = Account(1, 1000, 50000, 7.0)

account.deposit(2000)
account.withdraw(500)
account.add_monthly_interest()

account.print_transactions()
print(account)