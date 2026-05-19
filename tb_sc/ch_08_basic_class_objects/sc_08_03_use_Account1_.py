# file: sc_08_03_use_Account1_.py
from sc_08_02_Account1 import Account

account1 = Account(1, 1000, 50000, 7)
account2 = Account(2, 1001, 10000, 5)
print(account1)
print(account2)
Account.deposit(account1, 500)
print(f'New balance after deposit: {account1.get_balance()}')
account1.withdraw(1000)
print(f'New balance after withdr.: {account1.get_balance()}')
account1.add_monthly_interest()
print(f'New balance after monthly interest: {account1._balance}')