# file: sc_08_02_Account1.py
class Account:
    def __init__(self, cust_id, account_no, start_balance, interest):
        self._cust_id = cust_id
        self._account_no = account_no
        self._balance = start_balance
        self._interest = interest

    def get_balance(self):
        return self._balance
    
    def set_balance(self, new_balance):
        self._balance = new_balance
        
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        return self._balance

    def add_monthly_interest(self):
        monthly_interest = self.calculate_monthly_interest()
        self._balance += monthly_interest

    def calculate_monthly_interest(self):
        return self._balance * self._interest / 100 / 12

    def __str__(self):
        return f'''
Customer id  = {self._cust_id}
Account no = {self._account_no}
Balance = {self._balance}
Interest = {self._interest}
'''
