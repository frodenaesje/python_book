# file: sc_08_06_Account3.py
from datetime import datetime

class Transaction:
    def __init__(self, amount, trans_type):
        self._amount = amount
        self._trans_type = trans_type  # "deposit", "withdraw", "interest"
        self._timestamp = datetime.now()

    def __str__(self):
        return f"{self._timestamp:%Y-%m-%d %H:%M:%S} | {self._trans_type.capitalize():8} | {self._amount:8.2f}"


class Account:
    def __init__(self, cust_id, account_no, start_balance, interest):
        self._cust_id = cust_id
        self._account_no = account_no
        self._balance = start_balance
        self._interest = interest
        self._transactions = []

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:
            print("Balance cannot be negative!")
        else:
            self._balance = new_balance

    @property
    def interest(self):
        return self._interest

    @interest.setter
    def interest(self, new_interest):
        if new_interest < 0:
            print("Interest rate cannot be negative!")
        else:
            self._interest = new_interest

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._transactions.append(Transaction(amount, "deposit"))
        else:
            print("Deposit amount must be positive!")
        return self._balance

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            self._transactions.append(Transaction(amount, "withdraw"))
        else:
            print("Insufficient balance for withdrawal!")
        return self._balance

    def add_monthly_interest(self):
        monthly_interest = self.calculate_monthly_interest()
        self._balance += monthly_interest
        self._transactions.append(Transaction(monthly_interest, "interest"))

    def calculate_monthly_interest(self):
        return self._balance * self._interest / 100 / 12

    def get_transactions(self):
        return self._transactions
    
    def print_transactions(self):
        print("Date and time         | Type     |   Amount")
        print("-" * 42)
        for trans in self._transactions:
            print(trans)

    def __str__(self):
        return f'''
Customer id  = {self._cust_id}
Account no   = {self._account_no}
Balance      = {self._balance:.2f}
Interest     = {self._interest}%
'''
